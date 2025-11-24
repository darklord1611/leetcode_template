#include <cuda_runtime.h>

#include <cuda_runtime.h>

__global__ void reduce_optimized(const float* input, float* output, int N) {
    // 1. Allocate Shared Memory
    // "extern" means the size is determined at runtime in the host launch <<<...>>>
    extern __shared__ float sdata[];

    unsigned int tid = threadIdx.x;
    unsigned int i = blockIdx.x * blockDim.x + threadIdx.x;
    unsigned int gridSize = blockDim.x * gridDim.x;

    // 2. Local Accumulation (Grid-Stride Loop)
    // Each thread sums up multiple elements from the input into a private register.
    // This handles cases where N > total threads.
    float local_sum = 0.0f;
    while (i < N) {
        local_sum += input[i];
        i += gridSize;
    }

    // Store the register value into Shared Memory
    sdata[tid] = local_sum;
    __syncthreads(); // Wait for all threads to fill sdata

    // 3. Tree Reduction in Shared Memory
    // We fold the array in half repeatedly: 256 -> 128 -> 64 -> ... -> 1
    for (unsigned int s = blockDim.x / 2; s > 0; s >>= 1) {
        if (tid < s) {
            sdata[tid] += sdata[tid + s];
        }
        __syncthreads(); // Critical: Wait for this step to finish before next stride
    }

    // 4. Single Global Atomic Add per Block
    // Only Thread 0 holds the total sum for this entire block
    if (tid == 0) {
        // We pass 'output' directly (it's a pointer), NOT '&output'
        atomicAdd(output, sdata[0]);
    }
}

extern "C" void solve(const float* input, float* output, int N) {   
    int threadsPerBlock = 256;
    
    // Calculate Grid Size
    // For reduction, we don't necessarily need a block for every element 
    // because of the Grid-Stride Loop. A fixed number of blocks is often better 
    // to saturate the GPU without overhead.
    // But for simplicity, we'll keep your dynamic calculation:
    int blocksPerGrid = (N + threadsPerBlock - 1) / threadsPerBlock;

    // 1. Calculate Shared Memory Size needed per block
    // We need 1 float for every thread in the block
    size_t sharedMemSize = threadsPerBlock * sizeof(float);

    // 2. Launch with 3rd Argument (Shared Mem Bytes)
    reduce_optimized<<<blocksPerGrid, threadsPerBlock, sharedMemSize>>>(input, output, N);

    cudaDeviceSynchronize();

    // totally vibed code
}
#include <cuda_runtime.h>


__global__ void softmax_kernel(const float* input, float* output, int N) {
    // declare share_mem -> aka cache to access the input faster
    extern __shared__ float s_data[];
    
    int tid = threadIdx.x;
    int idx = blockIdx.x * blockDim.x + threadIdx.x;

    // load data from global mem -> shared mem
    float my_val = (tid < N) ? input[idx] : -INFINITY; 
    s_data[tid] = my_val;
    __syncthreads(); // ensure all input values are loaded into the shared mem, else we doomed

    for (unsigned int s = blockDim.x / 2; s > 0; s >>= 1) {
        if (tid < s) {

            if (s_data[tid] < s_data[tid + s]) {
                s_data[tid] = s_data[tid + s];
            }
        }
        __syncthreads();
    }
    

    // now we need to broadcast the max values to all other threads for further use
    float max_val = s_data[0];

    // the main operation here
    s_data[tid] = expf(my_val - max_val);
    __syncthreads();

    for (unsigned int s = blockDim.x / 2; s > 0; s >>= 1) {
        if (tid < s) {
            s_data[tid] += s_data[tid + s];
        }
        __syncthreads();
    }
    

    float sum = s_data[0];
    if (tid < N) {
        output[idx] = s_data[tid] / sum;
    }

}

// still mismatch due to floating point imprecision, or just bad code?
extern "C" void solve(const float* input, float* output, int N) {
    int threadsPerBlock = 256;
    int blocksPerGrid = (N + threadsPerBlock - 1) / threadsPerBlock;
    size_t shared_mem_size = threadsPerBlock * sizeof(float);

    softmax_kernel<<<blocksPerGrid, threadsPerBlock, shared_mem_size>>>(input, output, N);
    cudaDeviceSynchronize();
}

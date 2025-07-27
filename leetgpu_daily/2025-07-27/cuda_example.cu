#include <cuda_runtime.h>

__global__ void leaky_relu_kernel(const float* input, float* output, int N, float alpha) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;

    if (i < N) {
        output[i] = (input[i] > 0) ? input[i] : (input[i] * alpha);
    }
}

// input, output are device pointers (i.e. pointers to memory on the GPU)
extern "C" void solve(const float* input, float* output, int N) {
    int threadsPerBlock = 256;
    int blocksPerGrid = (N + threadsPerBlock - 1) / threadsPerBlock;

    float alpha = 0.01;
    
    leaky_relu_kernel<<<blocksPerGrid, threadsPerBlock>>>(input, output, N, alpha);
    cudaDeviceSynchronize();
}
#include <cuda_runtime.h>


__global__ void count_histogram(const int* input, int* histogram, int N, int num_bins) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;

    if (idx < N && input[idx] < num_bins && input[idx] >= 0) {
        atomicAdd(&histogram[input[idx]], 1);
    }
}

// input, histogram are device pointers
extern "C" void solve(const int* input, int* histogram, int N, int num_bins) {
    int threadsPerBlock = 256;

    int blocksPerGrid = (N + threadsPerBlock - 1) / threadsPerBlock;

    count_histogram<<<blocksPerGrid, threadsPerBlock>>>(input, histogram, N, num_bins);

    cudaDeviceSynchronize();
}

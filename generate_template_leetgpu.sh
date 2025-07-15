#!/bin/bash

# Get today's date
DATE=$(date +%F)
FOLDER="leetgpu_daily/$DATE"

# Create the folder
mkdir -p "$FOLDER"

# CUDA example
cat << 'EOF' > "$FOLDER/cuda_example.cu"
#include "solve.h"
#include <cuda_runtime.h>

__global__ void matrix_multiplication_kernel(const float* A, const float* B, float* C, int M, int N, int K) {

}

// A, B, C are device pointers (i.e. pointers to memory on the GPU)
void solve(const float* A, const float* B, float* C, int M, int N, int K) {
    dim3 threadsPerBlock(16, 16);
    dim3 blocksPerGrid((K + threadsPerBlock.x - 1) / threadsPerBlock.x,
                       (M + threadsPerBlock.y - 1) / threadsPerBlock.y);

    matrix_multiplication_kernel<<<blocksPerGrid, threadsPerBlock>>>(A, B, C, M, N, K);
    cudaDeviceSynchronize();
}
EOF

# Triton example
cat << 'EOF' > "$FOLDER/triton_example.py"
# The use of PyTorch in Triton programs is not allowed for the purposes of fair benchmarking.
import triton
import triton.language as tl

@triton.jit
def matrix_multiplication_kernel(
    a_ptr, b_ptr, c_ptr, 
    M, N, K,
    stride_am, stride_an, 
    stride_bn, stride_bk, 
    stride_cm, stride_ck
):
    a_ptr = a_ptr.to(tl.pointer_type(tl.float32))
    b_ptr = b_ptr.to(tl.pointer_type(tl.float32))
    c_ptr = c_ptr.to(tl.pointer_type(tl.float32))
   
# a_ptr, b_ptr, c_ptr are raw device pointers
def solve(a_ptr: int, b_ptr: int, c_ptr: int, M: int, N: int, K: int):
    stride_am, stride_an = N, 1 
    stride_bn, stride_bk = K, 1  
    stride_cm, stride_ck = K, 1

    grid = (M, K) 
    matrix_multiplication_kernel[grid](
        a_ptr, b_ptr, c_ptr,
        M, N, K,
        stride_am, stride_an,
        stride_bn, stride_bk,
        stride_cm, stride_ck
    )
EOF

# PyTorch example
cat << 'EOF' > "$FOLDER/pytorch_example.py"
import torch

# A, B, C are tensors on the GPU
def solve(A: torch.Tensor, B: torch.Tensor, C: torch.Tensor, M: int, N: int, K: int):
    pass
EOF

# TinyGrad example
cat << 'EOF' > "$FOLDER/tinygrad_example.py"
import tinygrad

# A, B, C are tensors on the GPU
def solve(A: tinygrad.Tensor, B: tinygrad.Tensor, C: tinygrad.Tensor, M: int, N: int, K: int):
    pass
EOF

echo "✅ Created CUDA, Triton, PyTorch, and TinyGrad templates in $FOLDER"

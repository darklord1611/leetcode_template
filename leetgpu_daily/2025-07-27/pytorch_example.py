import torch


# input, output are tensors on the GPU
def solve(input: torch.Tensor, output: torch.Tensor, N: int):
    alpha = 0.01

    output.copy_(torch.where(input > 0, input, input * alpha))

    return

import torch


# input is a tensor on the GPU
def solve(input: torch.Tensor, N: int):
    input_rev = torch.flip(input, dims=[0])
    input.copy_(input_rev)

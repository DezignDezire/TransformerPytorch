import torch

def test_unsqueeze():
    x = torch.tensor([[1,2,3], [4,3,2]])
    x = x.unsqueeze(2)
    print(x)

def einsum():
    x = torch.rand((4,5,6,8))
    print(x)

einsum()
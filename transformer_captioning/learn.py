import torch
x = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
result = torch.triu(x, diagonal=0)
print(result)

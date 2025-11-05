import torch
from torch import nn

if __name__=="__main__":
    input=torch.ones((32,1024))
    print(f"input:{input.shape}")
    fc=nn.Linear(in_features=1024,out_features=256,bias=True)
    output=fc(input)
    print(f"output:{output.shape}")

    fc1=nn.Linear(in_features=1024,out_features=2048,bias=True)
    output1=fc1(input)
    print(f"output1:{output1.shape}")
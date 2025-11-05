import torch 
from torch import nn 

if __name__=="__main__":
    input=torch.ones((32,1280))
    print(f"input:{input.shape}")

    fc=nn.Linear(in_features=1280,out_features=256,bias=True)
    #全結合層（Fully Connected Layer）を使っている
    #in_featuresは入力の次元数、 out_featuresは出力の次元数、 bias=Trueはバイアス項を含める
    output=fc(input)
    print(f"output:{output.shape}")
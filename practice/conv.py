import torch
from torch import nn

if __name__ == "__main__":
    my_tensor=torch.ones((16,3,256,256))
    #onesは、すべての要素が1のテンソルを作る。上のテンソルは、
    #16枚の画像、3チャネル、256ピクセル＊256ピクセルの意味。
    print(f"original:{my_tensor.shape}")

    conv=nn.Conv2d(in_channels=3,out_channels=64,kernel_size=3)
    #畳み込み層の定義を行っている。
    #in_channelは入力のチャネル数、out_channelは出力のチャネル数。
    #kernel_sizeは、カーネルのサイズが３＊３
    out=conv(my_tensor)
    #ここで、畳み込み層（conv）に、my_tensorを通している。
    print(f"out1:{out.shape}")

    conv2=nn.Conv2d(in_channels=3,out_channels=64,kernel_size=3)
    out2=conv2(my_tensor)
    print(f"out2:{out2.shape}")
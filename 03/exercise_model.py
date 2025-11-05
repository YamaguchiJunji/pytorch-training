import torch 
from torch import nn

class ExerciseModel:
    def __init__(self):
        self.conv=nn.Conv2d(in_channels=3,out_channels=64,kernel_size=3)
        
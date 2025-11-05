import torch
from torch import nn
from exercise_model import ExerciseModel

if __name__=="__main__":
    in_tensor=torch.ones(32,3,128,128)
    model=ExerciseModel()

    out=model(in_tensor)
    
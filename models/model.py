import numpy as np 
import pandas as pd

import torch
import torch.nn as nn

from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import torchvision.transforms as transforms

class CNN(nn.Module):
    def __init__(self):
        super(CNN,self).__init__()

        self.convo_layers = nn.Sequential(
            nn.Conv2d(1,32,kernel_size=3,padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2,2),

            nn.Conv2d( 32,64,kernel_size=3,padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2,2),

            nn.Conv2d( 64,128,kernel_size=3,padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2,2)
        )
        
        self.fc_layer=nn.Sequential(
            nn.Linear(3*3*128,256),
            nn.ReLU(),

            nn.Linear(256,10)
        )
    def forward(self,x):
        x=self.convo_layers(x)
        x=x.view(x.size(0),-1)
        x=self.fc_layer(x)
        return x

model = CNN()
model.load_state_dict(torch.load("cnn.pth",map_location="cpu"))
model.eval()


tranform= transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,),(0.5,))
])

def preprocess(img):
    img = img.convert("L")
    img = ImageOps.invert(img)
    img = img.resize((28, 28))
    img = tranform(img)
    img = img.unsqueeze(0)
    return img

def predict(img):
    x=preprocess(img)
    with torch.no_grad():
        output = model(x)
        
    _, predicted = torch.max(output, 1)

    return predicted.item()





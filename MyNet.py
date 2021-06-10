import torch.nn as nn
import sys

class MyNet(nn.Module):
    def __init__(self, num_classes=5):
        super(MyNet, self).__init__()
        
        self.layers = nn.Sequential(
            
            nn.Conv2d(3, 32, kernel_size=3, padding=1),
            nn.BatchNorm2d(32),
            nn.Dropout(),
            nn.MaxPool2d(kernel_size=2),
            nn.ReLU(),
            
            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.MaxPool2d(kernel_size=2),
            nn.ReLU(),
            
            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.MaxPool2d(kernel_size=2),
            nn.ReLU(),
            
            nn.Conv2d(128, 128, kernel_size=3, padding=1),
            nn.Dropout(),
            nn.MaxPool2d(kernel_size=2),
            nn.ReLU(),

            nn.Conv2d(128, 128, kernel_size=3, padding=1),
            nn.MaxPool2d(kernel_size=2),
            nn.ReLU(),
            
            nn.Conv2d(128, 256, (3,3), padding = 1),
            nn.BatchNorm2d(256),
            nn.ReLU(),
            nn.AdaptiveAvgPool2d((7,7)),
            nn.Flatten()                 
        )
        
        self.classifier = nn.Sequential(
            
            nn.Linear(7*7*256, 2048),
            nn.Dropout(),
            nn.LeakyReLU(),
            nn.Linear(2048, 1024),
            nn.Dropout(),
            nn.LeakyReLU(),
            nn.Linear(1024, num_classes),
        )
        
    def forward(self, x):

        x = self.layers(x)
        x = x.view(x.size(0), -1)
        x = self.classifier(x)
        scores = x
        
        return scores
            
            
            
  


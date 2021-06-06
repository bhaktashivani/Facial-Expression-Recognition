import sys
import torch.nn as nn
import torch.nn.functional as F


class WoodNet(nn.Module):
    def __init__(self, num_classes=5):
        super(WoodNet, self).__init__()
        
        self.conv2d = nn.Conv2d(3, 32, kernel_size=3, padding=1)
        self.maxpool = nn.MaxPool2d(kernel_size=2)
        self.relu = nn.ReLU()
        
        self.layers = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=3, padding=1),
            nn.MaxPool2d(kernel_size=2),
            nn.ReLU(),
            
            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.MaxPool2d(kernel_size=2),
            nn.ReLU(),
            
            nn.Conv2d(64, 64, kernel_size=3, padding=1),
            nn.MaxPool2d(kernel_size=2),
            nn.ReLU(),
            
            nn.Conv2d(64, 64, kernel_size=3, padding=1),
            nn.MaxPool2d(kernel_size=2),
            nn.ReLU(),
            
            nn.Conv2d(64, 64, kernel_size=3, padding=1),
            nn.MaxPool2d(kernel_size=2),
            nn.ReLU(),          
        )
        
        self.classifier = nn.Sequential(
            nn.Linear(7 * 7 * 64, 2048),
            nn.ReLU(),
            nn.Linear(2048, 1024),
            nn.ReLU(),
            nn.Dropout(),
            nn.Linear(1024, num_classes),
        )
        
    def forward(self, x):

#         x = self.conv2d(x)
#         x = self.maxpool(x)
#         x = self.relu(x)
        x = self.layers(x)
        
 
        x = x.view(x.size(0), -1)
        x = self.classifier(x)
        scores = x
        return scores
            
            
            
    
import torch.nn as nn
import sys

# class MyNet(nn.Module):
#     def __init__(self, num_classes=5):
#         super(MyNet, self).__init__()
        
        
#         self.channel_1 = 32
#         self.channel_2 = 64
#         self.channel_3 = 128
#         self.channel_4 = 256
#         self.channel_5 = 512
#         self.channel_6 = 1024
        
        
#         self.layers = nn.Sequential(
#             nn.Conv2d(3, self.channel_1, (3,3), padding = 1),
#             nn.BatchNorm2d(32),
#             nn.LeakyReLU(inplace=True),
            
#             nn.Conv2d(self.channel_1, self.channel_2, (3,3), padding = 1),
#             nn.LeakyReLU(inplace=True),
#             nn.MaxPool2d(kernel_size=2, stride=2),

#             nn.Conv2d(self.channel_2, self.channel_3, (3,3), padding = 1),
#             nn.BatchNorm2d(128),
#             nn.LeakyReLU(inplace=True),

#             nn.Conv2d(self.channel_3, self.channel_4, (3,3), padding = 1),
#             nn.BatchNorm2d(256),
#             nn.LeakyReLU(inplace=True),

#             nn.Conv2d(self.channel_4, self.channel_5, (3,3), padding = 1),
#             nn.BatchNorm2d(512),
#             nn.LeakyReLU(inplace=True),

#             nn.Conv2d(self.channel_5, self.channel_5, (1,1), padding = 0),
#             nn.LeakyReLU(inplace=True),
#             nn.MaxPool2d(kernel_size=2, stride=2),
    
#             nn.Conv2d(self.channel_5, self.channel_6, (3,3), padding = 1),
#             nn.BatchNorm2d(1024),
#             nn.LeakyReLU(inplace=True),
#         )
        
#         self.classifier = nn.Sequential(
            
# #             nn.AdaptiveAvgPool2d((7,7)),
# #             nn.Flatten(),
# #             nn.Dropout(),
# #             nn.Linear(self.channel_6 * 7*7, 512),
# #             nn.Linear(512, 256),
# #             nn.Linear(256, num_classes),
            
#             nn.Linear(7 * 7 * self.channel_6, 2048),
#             nn.ReLU(),
#             nn.Linear(2048, 1024),
#             nn.ReLU(),
#             nn.Dropout(),
#             nn.Linear(1024, num_classes),
#         )
        
#     def forward(self, x):
#         x = self.layers(x)
#         x = x.view(x.size(0), -1)
#         x = self.classifier(x)
#         scores = x
#         return scores

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

            
            nn.Conv2d(64, 64, kernel_size=3, padding=1),
            nn.Dropout(),
            nn.MaxPool2d(kernel_size=2),
            nn.ReLU(),
            
            nn.Conv2d(64, 64, kernel_size=3, padding=1),
#             nn.BatchNorm2d(64),
            nn.MaxPool2d(kernel_size=2),
            nn.ReLU(),

            
#             nn.Conv2d(64, 64, kernel_size=3, padding=1),
#             nn.MaxPool2d(kernel_size=2),
#             nn.ReLU(),
            
            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.MaxPool2d(kernel_size=2),
            nn.ReLU(),

            
            nn.Conv2d(128, 256, (3,3), padding = 1),
            nn.BatchNorm2d(256),
#             nn.MaxPool2d(kernel_size=2),
            nn.ReLU(), #[12, 2304]
            nn.AdaptiveAvgPool2d((7,7)),
            nn.Flatten()
            
#             nn.Conv2d(256,512, (3,3), padding = 1),
#             nn.BatchNorm2d(512), #[12, 512]
#             nn.MaxPool2d(kernel_size=2),
#             nn.ReLU(), #[12, 2304]
            
        )
        
        self.classifier = nn.Sequential(
            
            nn.Linear(7*7*256, 2048), # batch size x 
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
#         print(x.shape)
#         x = x.Flatten()
#         sys.exit()
        x = self.classifier(x)
        scores = x
        
        return scores
            
            
            
  


import torch.nn as nn

class EmotionNet(nn.Module):
    def __init__(self, num_classes=7):
        super().__init__()
        self.net = nn.Sequential(
            nn.Conv2d(1,32,3,1,1), nn.ReLU(),
            nn.Conv2d(32,32,3,1,1), nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(32,64,3,1,1), nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Flatten(),
            nn.Linear(64*12*12, 128), nn.ReLU(),
            nn.Linear(128, num_classes)
        )

    def forward(self, x):
        return self.net(x)

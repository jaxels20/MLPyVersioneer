



from summary import Summary

import torch.nn as nn
import torch.nn.functional as F

class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 20, 5)
        self.conv2 = nn.Conv2d(20, 20, 5)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        return F.relu(self.conv2(x))


def main():

    model = Model()

    summary = Summary(model, hyperparameters={"learning_rate": 0.01}, performance_metrics={"accuracy": 0.95})

    summary.export()
    

    

if __name__ == "__main__":
    main()




from summary import Summary

import torch.nn as nn
import torch.nn.functional as F
import pandas as pd

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

    summary = Summary(model)

    summary.export(save_model=False, replace_latest=True)
    
    evaluation_metrics = pd.DataFrame({'loss': [0.1, 0.2, 0.3], 'accuracy': [0.9, 0.8, 0.7]})
    summary.export_evaluation(evaluation_metrics=evaluation_metrics, write_mode='w')


if __name__ == "__main__":
    main()
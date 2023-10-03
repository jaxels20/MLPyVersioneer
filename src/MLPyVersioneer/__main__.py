from summary import Summary
from training_phase_metric_storage import TrainingPhaseMetricStorage as Tpms

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
    
    data = Tpms.load_from_json("meta_data/gnn_v2.json")

    print(data.storage)


    

    

if __name__ == "__main__":
    main()
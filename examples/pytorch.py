import torch
from MLPyVersioneer.summary import Summary

class SimpleNet(torch.nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc = torch.nn.Linear(28*28, 10)

    def forward(self, x):
        x = x.view(-1, 28*28)
        x = self.fc(x)
        return x

model = SimpleNet()
hyperparameters = {"lr": 0.001}
performance_metrics = {"accuracy": 95.5, "loss": 0.05}

summary = Summary(model, model_name="torch_model", hyperparameters=hyperparameters, performance_metrics=performance_metrics)
summary.save()
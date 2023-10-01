from torch import nn
import os
import re

from exporter import Exporter

SUMMARY_FOLDER = "meta_data"

class Summary:

    def __init__(self, model, model_name: str = "model", hyperparameters: dict = None, performance_metrics: dict = None) -> None:
        self.model = model
        self.model_name = model_name
        self.exporter = Exporter()
        self.version = self.calculate_version()
        self.hyperparameters = hyperparameters
        self.performance_metrics = performance_metrics



    def export(self) -> None:
        
        self.exporter.generate_folders()

        self.exporter.generate_files(self)

    def calculate_version(self) -> int:
        # get all the files in the summaries folder
        try:
            files = os.listdir(SUMMARY_FOLDER)

        except FileNotFoundError:
            return 1
        
        # only look at the models with the same name

        files = [file for file in files if file.split("_")[0] == self.model_name]

        # get all the versions from the files
        versions = [int(re.findall(r'\d+', file)[0]) for file in files]

        # if there are no files, start at version 1
        if len(versions) == 0:
            return 1

        # get the latest version
        version = max(versions)

        # increment the version
        version += 1

        return version
    
    def set_hyperparameters(self, hyperparameters: dict) -> None:
        self.hyperparameters = hyperparameters

    def set_performance_metrics(self, performance_metrics: dict) -> None:
        self.performance_metrics = performance_metrics


    def get_architecture(self) -> dict:
        if isinstance(self.model, nn.Module):
            return {str(name): str(value) for name, value in self.model.named_children()} 
        
        return None
        






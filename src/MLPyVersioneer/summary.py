from torch import nn
from torchinfo import summary
import os
import re
import pandas as pd

from exporter import Exporter

SUMMARY_FOLDER = "summaries"

class Summary:

    def __init__(self, model, ) -> None:
        self.model = model
        self.exporter = Exporter()
        self.version = self.calculate_version()


        if isinstance(model, nn.Module):
            self.meta_data = summary(model, verbose=0)

    def __str__(self) -> str:
        return str(self.meta_data)

    def export(self, save_model=True, replace_latest=False) -> None:
        
        self.exporter.generate_folders()

        self.exporter.generate_files(self, save_model, replace_latest)

    def calculate_version(self) -> int:
        # get all the files in the summaries folder
        try:
            files = os.listdir(SUMMARY_FOLDER)

        except FileNotFoundError:
            return 1

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
    

    def export_evaluation(self, evaluation_metrics: pd.DataFrame, write_mode: str ='w'):
        # save the evaluation metrics to a csv file for later visualizations and comparisons
        # Can maybe be used to store the final results of multiple models in one file or results from multiple runs/iterations of the same model
        # If it should handle both cases, how to handle versions? If exporting training iterations of the same model,
        # the version is the same but rows should be identified with iterations/epochs
        # If it should handle multiple different models in the same file where the metrics are the final results of each model,
        # the version are different and the rows are identified with the version number of the model
        self.exporter.generate_evaluation(self.version, evaluation_metrics, write_mode)

    def load_evaluation(self):
        # load the evaluation metrics from the csv file into a pandas dataframe
        pass

    def export_training_config(self, training_config: dict):
        self.exporter.generate_training_config(self.version, training_config)
        # save the parameters from the training phase e.g. leaning rate, epochs, batch size, etc.
        

    def load_training(self):
        # load the parameters from the training phase so that we can easily reproduce the model and results
        pass
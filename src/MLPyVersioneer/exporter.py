import os
import sys
import torch
import pandas as pd
import json


SUMMARY_FOLDER = "summaries"
MODEL_FOLDER = "models"

ALL_FOLDERS = [SUMMARY_FOLDER, MODEL_FOLDER]

class Exporter:

    def __init__(self) -> None:

        pass
        

    def generate_folders(self) -> None:
        try:
            for folder in ALL_FOLDERS:
                if not os.path.exists(folder):
                    os.makedirs(folder)
        except:
            print("Error: Could not create folders")
            sys.exit(1)


    def generate_files(self, summary, save_model, replace_latest) -> None:

        if replace_latest:
            version = summary.version - 1 if summary.version > 1 else 1
        else:
            version = summary.version
        
        # write the meta data to a file
        with open(f"{SUMMARY_FOLDER}/summary_{version}.txt", "w", encoding='utf-8') as f:
            f.write(str(summary.meta_data))

        # save the model
        if save_model:
            torch.save(summary.model, f"{MODEL_FOLDER}/model_{version}.pt")


    def generate_evaluation(self, version, evaluation_metrics: pd.DataFrame, write_mode: str ='w'):
        # save the evaluation metrics to a csv file for later visualizations and comparisons
        # Can maybe be used to store the final results of multiple models in one file or results from multiple runs/iterations of the same model

        # Create evaluation folder if it does not exist
        if not os.path.exists("evaluation"):
            os.makedirs("evaluation")

        evaluation_metrics.to_csv(f"evaluation/evaluation_{version}.csv", mode=write_mode, index=False)

    def generate_training_config(self, version, training_config: dict):
        # Create training configuration folder if it does not exist
        if not os.path.exists("training_config"):
            os.makedirs("training_config")

        with open(f"training_config/training_{version}.json", "w") as f:
            json.dump(training_config, f, indent=4)
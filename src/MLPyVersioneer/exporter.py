import os
import sys
import torch
import json
from datetime import datetime

SUMMARY_FOLDER = "meta_data"
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


    def generate_files(self, summary) -> None:

        summary_json = {}

        summary_json["timestamp"] = str(datetime.now())

        summary_json["model_name"] = summary.model_name

        architecture = summary.get_architecture()
        if architecture != None:
            summary_json["architecture"] = architecture

        if summary.version != None:
            summary_json["version"] = summary.version

        if summary.hyperparameters != None:
            summary_json["hyperparameters"] = summary.hyperparameters

        if summary.performance_metrics != None:
            summary_json["performance_metrics"] = summary.performance_metrics


        

        # write the meta data to a file
        with open(f"{SUMMARY_FOLDER}/{summary.model_name}_v{summary.version}.json", "w") as f:
            f.write(json.dumps(summary_json, indent=4))

        # save the model
        torch.save(summary.model, f"{MODEL_FOLDER}/{summary.model_name}_v{summary.version}.pt")



        



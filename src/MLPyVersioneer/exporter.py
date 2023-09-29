import os
import sys
import torch
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


    def generate_files(self, summary) -> None:

        summary_json = {}

        summary_json["version"] = summary.version
        summary_json["hyperparameters"] = summary.hyperparameters
        summary_json["performance_metrics"] = summary.performance_metrics
        summary_json["meta_data"] = str(summary.meta_data)




        # write the meta data to a file
        with open(f"{SUMMARY_FOLDER}/summary_{summary.version}.json", "w") as f:
            f.write(json.dumps(summary_json, indent=4))

        # save the model
        torch.save(summary.model, f"{MODEL_FOLDER}/model_{summary.version}.pt")



        



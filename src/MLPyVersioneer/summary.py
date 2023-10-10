import os
import re

from MLPyVersioneer.exporter import Exporter
from MLPyVersioneer.training_phase_metric_storage import TrainingPhaseMetricStorage

SUMMARY_FOLDER = "meta_data"

class Summary:
    """
    Class to summarize the model details including hyperparameters, architecture, and performance metrics.

    Attributes:
    - model: Model to be summarized.
    - model_name (str): A descriptive name for the model.
    - hyperparameters (dict): The model's hyperparameters.
    - performance_metrics (dict): Performance metrics like accuracy, loss, etc.
    - training_phase_metrics_storage (TrainingPhaseMetricStorage): Storage for metrics during training phases.
    - version (int): Model version determined based on existing saved summaries.
    """

    def __init__(self, model, model_name: str = "model", hyperparameters: dict = None, performance_metrics: dict = None) -> None:
        self.model = model
        self.model_name = model_name
        self.hyperparameters = hyperparameters
        self.performance_metrics = performance_metrics
        self.training_phase_metrics_storage = TrainingPhaseMetricStorage()
        self.exporter = Exporter()  # Assumes the Exporter class has methods for generating folders and files.
        self.version = self.determine_next_version()

    def save(self) -> None:
        """
        Save the model summary.
        """
        self.exporter.create_required_folders()
        self.exporter.save_model_summary(self)

    def update_hyperparameters(self, hyperparameters: dict) -> None:
        """
        Update model hyperparameters.

        Args:
        - hyperparameters (dict): Dictionary of hyperparameters.
        """
        self.hyperparameters = hyperparameters

    def update_performance_metrics(self, performance_metrics: dict) -> None:
        """
        Update model performance metrics.

        Args:
        - performance_metrics (dict): Dictionary of performance metrics.
        """
        self.performance_metrics = performance_metrics

    def get_architecture(self) -> dict:
        """
        Retrieve model architecture details.

        Returns:
        - architecture (dict): Dictionary representation of model architecture or None if model is not of type nn.Module.
        """
        # PyTorch
        try:
            from torch import nn
            if isinstance(self.model, nn.Module):  # Assumes PyTorch's nn.Module
                return {str(name): str(value) for name, value in self.model.named_children()}
        except ImportError:
            pass
        
        # Keras
        try:
            import keras
            if isinstance(self.model, keras.models.Model):
                layers = [(layer.name, layer.get_config()) for layer in self.model.layers]
                return dict(layers)
        except ImportError:
            pass
            
        # Scikit-learn
        try:
            from sklearn.base import BaseEstimator
            if isinstance(self.model, BaseEstimator):
                return {"class": str(self.model.__class__), "params": self.model.get_params()}
        except ImportError:
            pass

        raise TypeError("Model type is not supported.")

    def add_training_phase_metrics(self, metrics_dict: dict) -> None:
        """
        Add a TrainingPhaseMetric instance to the storage using a dictionary format.

        Args:
        - metric_dict (dict): Dictionary containing 'name', 'value', and 'epoch' keys.
        """
        self.training_phase_metrics_storage.add_metrics_from_dict(metrics_dict)

    def determine_next_version(self) -> int:
        """
        Determine the next version number for the model based on existing saved summaries.

        Returns:
        - version (int): Next version number for the model.
        """
        try:
            files = os.listdir(SUMMARY_FOLDER)
        except FileNotFoundError:
            return 1

        relevant_files = [file for file in files if "_".join(file.split("_")[:-1]) == self.model_name]


        # Extract versions from the filenames
        versions = [int(re.findall(r'\d+', file)[0]) for file in relevant_files]

        if not versions:  # If there are no relevant files, start at version 1
            print("No relevant files found.")
            return 1

        latest_version = max(versions)
        return latest_version + 1
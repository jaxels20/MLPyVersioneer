# Summary Class

The `Summary` class is designed to aggregate and manage details about a machine learning model, such as its hyperparameters, architecture, and performance metrics.

---

## Attributes:

- `model`: The model that needs to be summarized.
- `model_name` (str): Descriptive name for the model.
- `hyperparameters` (dict): Dictionary containing the hyperparameters of the model.
- `performance_metrics` (dict): Dictionary containing performance metrics such as accuracy, loss, etc.
- `training_phase_metrics_storage` (TrainingPhaseMetricStorage): Storage mechanism to keep track of metrics during different training phases.
- `exporter` (Exporter): An instance of the `Exporter` class for saving model and its summary.
- `version` (int): Version of the model, determined based on previously saved summaries.

---

## Methods:

### 1. `__init__(self, model, model_name: str = "model", hyperparameters: dict = None, performance_metrics: dict = None) -> None`

Initializes the `Summary` class and determines the next version for the model.

#### Parameters:

- `model`: The model to be summarized.
- `model_name` (str): Descriptive name for the model. Defaults to "model".
- `hyperparameters` (dict): The model's hyperparameters. Defaults to None.
- `performance_metrics` (dict): Performance metrics like accuracy, loss, etc. Defaults to None.

---

### 2. `save(self) -> None`

Save the model's summary using the associated `Exporter`.

#### Parameters:
- None

#### Returns:
- None

---

### 3. `update_hyperparameters(self, hyperparameters: dict) -> None`

Updates the hyperparameters for the model.

#### Parameters:
- `hyperparameters` (dict): Dictionary containing the updated hyperparameters.

#### Returns:
- None

---

### 4. `update_performance_metrics(self, performance_metrics: dict) -> None`

Updates the performance metrics for the model.

#### Parameters:
- `performance_metrics` (dict): Dictionary containing the updated performance metrics.

#### Returns:
- None

---

### 5. `get_architecture(self) -> dict`

Retrieve details about the model's architecture.

#### Parameters:
- None

#### Returns:
- `architecture` (dict): A dictionary representation of the model's architecture or raises a TypeError if the model type is unsupported. This method supports PyTorch, Keras, and Scikit-learn model architectures.

---

### 6. `add_training_phase_metrics(self, metrics_dict: dict) -> None`

Add metrics for a specific training phase.

#### Parameters:
- `metric_dict` (dict): Dictionary containing metrics details in the format {'name': metric_name, 'value': metric_value, 'epoch': epoch_number}.

#### Returns:
- None

---

### 7. `determine_next_version(self) -> int`

Determine the next version number for the model, which is based on the summaries already saved.

#### Parameters:
- None

#### Returns:
- `version` (int): The next version number for the model.

---


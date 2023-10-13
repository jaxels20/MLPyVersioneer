# TrainingPhaseMetricStorage Class

The `TrainingPhaseMetricStorage` class provides functionality to store and manage `TrainingPhaseMetric` instances. These metrics are grouped by their names for organized storage and retrieval.

---

## Attributes:

- `storage` (dict): A dictionary that holds metrics grouped by their names.

---

## Methods:

### 1. `__init__(self) -> None`

Initializes an empty storage dictionary.

#### Parameters:
- None

---

### 2. `load_from_json(json_path: str) -> TrainingPhaseMetricStorage`

Loads `TrainingPhaseMetric` instances from a provided JSON file and returns a populated `TrainingPhaseMetricStorage` instance.

#### Parameters:
- `json_path` (str): Path to the source JSON file.

#### Returns:
- A populated instance of `TrainingPhaseMetricStorage`.

---

### 3. `add_metric(self, metric: TrainingPhaseMetric) -> None`

Adds a `TrainingPhaseMetric` instance to the storage.

#### Parameters:
- `metric` (TrainingPhaseMetric): The metric to be stored.

#### Returns:
- None

---

### 4. `add_metrics_from_dict(self, metrics_dict: dict) -> None`

Stores multiple `TrainingPhaseMetric` instances using a dictionary format.

#### Parameters:
- `metrics_dict` (dict): A dictionary with 'epoch' as a key and multiple metric names with their corresponding values.

#### Returns:
- None

---

### 5. `get_metrics(self, metric_name: str = None) -> list`

Retrieve metrics for a specific name or all metrics if no name is provided.

#### Parameters:
- `metric_name` (str, optional): Name of the specific metric.

#### Returns:
- A list of `TrainingPhaseMetric` instances.

---

### 6. `get_metrics_as_dicts(self, metric_name: str = None) -> list`

Retrieve metrics in a dictionary format for a specific name or all metrics if no name is provided.

#### Parameters:
- `metric_name` (str, optional): Name of the specific metric.

#### Returns:
- A list of dictionaries representing `TrainingPhaseMetric` instances.

---

### 7. `__str__(self)`

String representation of the stored metrics.

#### Parameters:
- None

---

### 8. `to_csv(self, csv_path: str) -> None`

Exports the stored metrics to a CSV file.

#### Parameters:
- `csv_path` (str): Destination path for the CSV file.

#### Returns:
- None

---

### 9. `to_json(self, json_path: str) -> None`

Exports the stored metrics to a JSON file.

#### Parameters:
- `json_path` (str): Destination path for the JSON file.

#### Returns:
- None

---

### 10. `to_df(self) -> pd.DataFrame`

Converts the stored metrics to a pandas DataFrame.

#### Parameters:
- None

#### Returns:
- A `pandas.DataFrame` containing the stored metrics.

---

### 11. `plot_metric(self, metric_name: str, show : bool = False)`

Plots a specified metric using Plotly.

#### Parameters:
- `metric_name` (str): Name of the metric to be plotted.
- `show` (bool, optional): If True, the plot is displayed. Defaults to False.

#### Returns:
- A Plotly figure object representing the metric plot.

---

## Note:

The `TrainingPhaseMetricStorage` class assumes the presence of the `TrainingPhaseMetric` class and its associated methods. Make sure any external dependencies (e.g., pandas, Plotly, JSON) are available in the environment where this class is utilized.

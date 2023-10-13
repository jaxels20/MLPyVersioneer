# TrainingPhaseMetric Class

The `TrainingPhaseMetric` class represents a metric obtained during a specific training phase or epoch.

---

## Attributes:

- `epoch` (int): The training epoch or phase at which this metric was recorded.
- `name` (str): The name or identifier of the metric (e.g., 'accuracy', 'loss').
- `value` (float or int): The value of the metric for the specified epoch.

---

## Methods:

### 1. `__init__(self, name, value, epoch) -> None`

Initializes a new instance of the `TrainingPhaseMetric` class with the specified attributes.

#### Parameters:
- `name` (str): The name of the metric.
- `value` (float or int): The value of the metric.
- `epoch` (int): The epoch or training phase at which the metric was recorded.

---

### 2. `__str__(self) -> str`

Returns a string representation of the metric.

#### Parameters:
- None

#### Returns:
- A string detailing the epoch, metric name, and its value.

---

### 3. `__json__(self) -> dict`

Generates a dictionary representation of the `TrainingPhaseMetric` instance. This is useful for serialization and storage purposes.

#### Parameters:
- None

#### Returns:
- A dictionary containing 'epoch', 'name', and 'value' keys mapped to their respective values from the object instance.

---

## Usage Example:

```python
metric = TrainingPhaseMetric(name="accuracy", value=0.95, epoch=1)
print(metric)  # Output: Epoch: 1, Name: accuracy, Value: 0.95

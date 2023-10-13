# PyMLVersioneer - Python Machine Learning Model Versioning Library

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

# MLPyVersioneer

`MLPyVersioneer` is a dedicated Python module designed for ML practitioners, assisting in capturing, storing, and managing critical details of machine learning models throughout their training phase.

## Features

- **Model Summarization**: Quickly gather essential details of ML models, including hyperparameters, architecture, and performance metrics.
- **Automatic Model Versioning**: Determine and manage model versions effortlessly based on previously recorded summaries.
- **Granular Metric Management**: Use structured methods to capture, store, and retrieve training phase metrics.
- **Export Utility**: Simplify the saving process of model checkpoints and their associated metadata.
- **Multiple Export Formats**: Export training metrics in various formats, such as CSV, JSON, and Pandas DataFrame.
- **Visualization**: Visualize training phase metrics using built-in plotting methods.

## Installation

### Prerequisites

Ensure you have Python (3.7 or newer) installed on your system. If not, download and install Python from [python.org](https://www.python.org/downloads/).

### Installing with pip (recommended)

Install `MLPyVersioneer` using pip:

```bash
pip install MLPyVersioneer
```

### Installing from Source

For manual installation from the source:

1. Navigate to the directory containing `setup.py`.
2. Run:
```bash
pip install .
```
## Usage 

```python
import MLPyVersioneer as mv


hyperparameters = # your hyperparameters
model = # your model

summary = mv.Summary(model, model_name="model", hyperparameters=hyperparameters)

for epoch in range(epochs):
    # your training code

    loss = # your loss
    accuracy = # your accuracy

    summary.add_training_phase_metrics({"name": "loss", "value": loss, "epoch": epoch})
    summary.add_training_phase_metrics({"name": "accuracy", "value": accuracy, "epoch": epoch})
    


test_accuracy = # your test accuracy
test_loss = # your test loss

performance_metrics = {"accuracy": test_accuracy, "loss": test_loss}
summary.set_performance_metrics(performance_metrics)

summary.save()
```


## Documentation

For comprehensive documentation on each component of `MLPyVersioneer`, please refer to the [official documentation](https://mlpyversioneer.readthedocs.io/en/latest/).

## Contributing

We welcome contributions! If you find a bug or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

[MIT License](LICENSE.txt)

## Acknowledgments

Thank you to all the contributors and users of `MLPyVersioneer`!

# Exporter Class

The `Exporter` class is responsible for generating required folders and saving model details and checkpoints.

---

## Attributes

- None

---

## Methods

### 1. `create_required_folders() -> None`

Ensure all necessary folders exist or create them.

#### Parameters:
- None

#### Returns:
- None

#### Exceptions:
- May raise a generic Exception if there's an error creating a folder.

---

### 2. `save_model_summary(summary) -> None`

Saves the model's metadata as JSON and its state as a PyTorch checkpoint, Keras model, or Scikit-learn model based on its type.

#### Parameters:

- `summary` (Summary): An instance of the `Summary` class containing model details.

#### Returns:
- None

#### Description:

The function saves the model's metadata which includes:
- Current timestamp
- Model name
- Version
- Architecture (or "Not Available" if not provided)
- Hyperparameters (empty dictionary if not provided)
- Performance metrics (empty dictionary if not provided)
- Training phase metrics (empty dictionary if not provided)

This metadata is saved as a JSON file.

The state of the model itself is saved depending on its type:
- If it's a PyTorch model, its state dictionary is saved.
- If it's a Keras model, the entire model is saved.
- If it's a Scikit-learn model, the model is serialized using joblib.

#### Exceptions:
- May raise `ImportError` if necessary libraries (PyTorch, Keras, Scikit-learn) are not available.

---


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from MLPyVersioneer import Summary

model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

hyperparameters = {"lr": 0.001, "optimizer": "adam", "batch_size": 32}
performance_metrics = {"accuracy": 96.0, "loss": 0.04}

summary = Summary(model, model_name="keras_model", hyperparameters=hyperparameters, performance_metrics=performance_metrics)
summary.save()
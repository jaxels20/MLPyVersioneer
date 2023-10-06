from sklearn.ensemble import RandomForestClassifier
from MLPyVersioneer import Summary

model = RandomForestClassifier()

hyperparameters = {"n_estimators": 100, "max_depth": 2}
performance_metrics = {"accuracy": 96.5}  # You'd typically calculate this using cross-validation or other methods

summary = Summary(model, model_name="sklearn_model", hyperparameters=hyperparameters, performance_metrics=performance_metrics)

summary.save()
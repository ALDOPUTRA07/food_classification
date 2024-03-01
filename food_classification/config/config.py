from pathlib import Path

import torch

# Number of epoch for training model
epochs = int(5)

# Define target device
device = "cuda" if torch.cuda.is_available() else "cpu"

# Define project name
PROJECT_NAME = "Food Classification"

# Setuo for saving model
MODEL_PATH = Path("food_classification/train_model/")
MODEL_NAME = "transfer_learning_efficient_bo.pth"
MODEL_SAVE_PATH = MODEL_PATH / MODEL_NAME

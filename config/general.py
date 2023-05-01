import os

import torch


IS_MODEL_SAVED = False

COLORS = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (255, 255, 255)]

MY_DATASET = r'.\!Dataset\small_dataset'

x_train_dir = os.path.join(MY_DATASET, 'Train\\Images')
y_train_dir = os.path.join(MY_DATASET, 'Train\\Masks')

x_valid_dir = os.path.join(MY_DATASET, 'Valid\\Images')
y_valid_dir = os.path.join(MY_DATASET, 'Valid\\Masks')

x_test_dir = os.path.join(MY_DATASET, 'Test\\Images')
y_test_dir = os.path.join(MY_DATASET, 'Test\\Masks')

DEVICE = 'cuda'


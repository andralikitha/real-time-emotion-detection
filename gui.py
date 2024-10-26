import tkinter as tk
from tkinter import messagebox
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

def run_data_collection():
    os.system("python data_collection.py")

def run_data_training():
    os.system("python data_training.py")

def run_inference():
    os.system("python inference.py")

root = tk.Tk()
root.title("Emotion Detection System")

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

data_collection_button = tk.Button(button_frame, text="Collect Data", command=run_data_collection)
data_collection_button.pack(side=tk.LEFT, padx=10)

data_training_button = tk.Button(button_frame, text="Train Model", command=run_data_training)
data_training_button.pack(side=tk.LEFT, padx=10)

inference_button = tk.Button(button_frame, text="Run Inference", command=run_inference)
inference_button.pack(side=tk.LEFT, padx=10)

root.mainloop()
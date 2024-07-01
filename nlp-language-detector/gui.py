import tkinter as tk
from tkinter import messagebox
import joblib

# Load the trained model
model = joblib.load('language_detector_model.pkl')

# Function to predict language
def predict_language():
    sentence = entry.get()
    if not sentence:
        messagebox.showwarning("Input Error", "Please enter a sentence.")
        return

    prediction = model.predict([sentence])[0]
    result_label.config(text=f"Detected Language: {prediction}")

# Create the main window
root = tk.Tk()
root.title("Language Detector")

# Create and place the widgets
entry_label = tk.Label(root, text="Enter a sentence:")
entry_label.pack()

entry = tk.Entry(root, width=50)
entry.pack()

predict_button = tk.Button(root, text="Detect Language", command=predict_language)
predict_button.pack()

result_label = tk.Label(root, text="Detected Language:")
result_label.pack()

# Run the Tkinter event loop
root.mainloop()

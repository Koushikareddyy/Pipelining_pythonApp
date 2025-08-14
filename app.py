import numpy as np
from flask import Flask, request, render_template

# We'll create a simple dummy model here since we don't have your 'model.py'
# In a real-world scenario, you would have your own 'model.py' file with a 'train_model' function
def train_model():
    """
    Creates and returns a simple dummy model for demonstration.
    """
    # This dummy model will always predict the sum of the two inputs.
    class DummyModel:
        def predict(self, input_data, verbose=0):
            # The input_data is expected to be a numpy array like [[num1, num2]]
            # This model returns the sum of the two numbers.
            sums = np.sum(input_data, axis=1, keepdims=True)
            return sums

    return DummyModel()

app = Flask(__name__)
model = train_model()

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            input_data = np.array([[num1, num2]])
            prediction = model.predict(input_data, verbose=0)
            result = f"Predicted Sum: {prediction[0][0]:.2f}"
        except Exception:
            result = "Invalid input. Please enter valid numbers."
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

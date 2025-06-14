# main.py
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# This is the route for your home page
@app.route('/')
def index():
    # It should be rendering the HTML template, NOT returning a string
    return render_template('index.html')

# This is the route that handles the form submission
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'excel_file' not in request.files:
        return "No file part in the request!"
    
    file = request.files['excel_file']
    question = request.form['user_question']

    if file.filename == '' or not question:
        return "Please select a file and provide a question."

    if file:
        try:
            df = pd.read_excel(file)
            html_table = df.head().to_html(classes='data', header="true")
            return render_template('result.html', 
                                   question=question, 
                                   filename=file.filename, 
                                   table=html_table)
        except Exception as e:
            return f"An error occurred while processing the file: {e}"
    
    return "An unknown error occurred."

# This part runs the app when developing locally
if __name__ == '__main__':
    app.run(debug=True)
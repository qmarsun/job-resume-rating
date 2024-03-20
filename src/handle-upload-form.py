from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/upload-resume', methods=['GET', 'POST'])
def upload_resume():
    if request.method == 'POST':
        # Accessing form data
        files = {}
        for i in range(1, 11):
            file = request.files.get(f'file{i}')
            if file:
                files[f'file{i}'] = file.filename
        
        # Do something with the files
        # For example, save them to disk
        for key, file in files.items():
            uploaded_file = request.files[key]
            uploaded_file.save(f'uploads/{file}')
        
        return 'Files uploaded successfully!'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

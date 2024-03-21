from flask import Flask, render_template, request, session
from werkzeug.utils import secure_filename
import os
import uuid

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/upload-resume', methods=['GET', 'POST'])
def upload_resume():
    if request.method == 'POST':
        # Accessing form data
        files = {}
        session_id = session.get('session_id', str(uuid.uuid4()))
        session['session_id'] = session_id
        upload_dir = os.path.join('uploads', session_id)
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)
        
        for i in range(1, 11):
            file = request.files.get(f'file{i}')
            if file:
                filename = secure_filename(file.filename)
                file.save(os.path.join(upload_dir, filename))
                files[f'file{i}'] = filename
        
        return f'Files uploaded successfully! Session ID: {session_id}'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

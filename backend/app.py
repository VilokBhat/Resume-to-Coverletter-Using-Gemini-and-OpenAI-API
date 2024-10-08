from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from utils.pdf_utils import extract_text_from_pdf
from utils.cover_letter_gen import generate_cover_letter
import os
from werkzeug.utils import secure_filename

app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)  # Enable CORS

# Configuration for uploads
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Helper function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Serve the main index.html file
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/generate-cover-letter', methods=['POST'])
def generate_cover_letter_route():
    if 'resume' not in request.files:
        return jsonify({'error': 'No resume file uploaded'}), 400

    resume_file = request.files['resume']
    
    if resume_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if not allowed_file(resume_file.filename):
        return jsonify({'error': 'Unsupported file format, only PDFs are allowed'}), 400

    job_title = request.form.get('jobTitle', '').strip()
    company_name = request.form.get('companyName', '').strip()

    if not job_title or not company_name:
        return jsonify({'error': 'Job title and company name are required'}), 400

    # Secure the filename and save the file
    filename = secure_filename(resume_file.filename)
    resume_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    # Create upload folder if it doesn't exist
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    resume_file.save(resume_path)

    try:
        resume_text = extract_text_from_pdf(resume_path)
        print(f"Extracted resume text: {resume_text}...")  # Log a portion of the text
        
        cover_letter = generate_cover_letter(resume_text, job_title, company_name)
        print(f"Generated cover letter: {cover_letter}...")  # Log a portion of the cover letter
        
        return jsonify({'coverLetter': cover_letter})
    
    except Exception as e:
        print(f"Error in generating cover letter: {e}")  # Log the error
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)

# Resume to Cover Letter Generator

This project is a web application that generates a cover letter from a resume. The application allows users to upload their resume in PDF format, enter the job title and company name, and generate a customized cover letter. Using the Gemini or OpenAI api the coverletter will be generated.

## Features

- Upload resume in PDF format
- Enter job title and company name
- Generate a customized cover letter
- Responsive and user-friendly interface

## Technologies Used

- Python
- Flask
- Javascript
- Gemini or OpenAI api

### Prerequisites

- Python 3.7 or higher
- Gemini or OpenAI api
- Git

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/VilokBhat/Resume-to-Coverletter-Using-Gemini-and-OpenAI-API
   cd Resume-to-Coverletter-Using-Gemini-and-OpenAI-API
   ```

3. **Install the dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Add the API key:**
   Add the API key in the ```sh \backend\utils\cover_letter_gen.py``` file.


3. **Running the Application Locally**
   ```sh
   python app.py
   ```

### Usage
1. **Upload Resume:** Click on the "Browse files" button to upload your resume in PDF format.

2. **Enter Job Title:** Enter the job title in the provided text input.

3. **Enter Company Name:** Enter the company name in the provided text input.

4. **Generate Cover Letter:** Click on the "Generate Cover Letter" button to generate the cover letter.

5. **View Cover Letter:** The generated cover letter will be displayed in the text area below.

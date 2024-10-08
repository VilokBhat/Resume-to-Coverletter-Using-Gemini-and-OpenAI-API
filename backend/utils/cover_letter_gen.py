#import openai
import google.generativeai as genai


genai.configure(api_key='<YOUR-GEMINI-API-KEY>')
model = genai.GenerativeModel("gemini-1.5-flash")
def generate_cover_letter(resume_text, job_title, company_name):
    response = model.generate_content(f"Generate a cover letter for a {job_title} applying to {company_name}.\nResume:\n{resume_text}")
    return response.text

# openai.api_key = '<YOUR-OPENAI-API-KEY>'

# def generate_cover_letter(resume_text, job_title, company_name):
#     prompt = f"Create a professional cover letter for the following resume:\n\n{resume_text}\n"
#     prompt += f"Job title: {job_title}\nCompany: {company_name}"

#     response = openai.Completion.create(
#         engine="gpt-3.5-turbo",
#         prompt=prompt,
#         max_tokens=500,
#         temperature=0.7
#     )
    
#     return response.choices[0].text.strip()

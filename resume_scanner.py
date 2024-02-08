# Pip install resume_parser
from resume_parser import resumeparse

def scan_resume(resume):
    data = resumeparse.read_file(resume)
    for i, j in data.items():
        print(f"{i}:>>{j}")
    
scan_resume(# Document name goes here e.g "daniel_cv.docx")

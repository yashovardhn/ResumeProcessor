# ResumeProcessor

ResumeProcessor is a Django-based application designed to extract and process information from resumes. This project aims to simplify the resume extraction process, providing an API endpoint for users to upload resumes and retrieve structured data.

## Features
- Upload resumes in various formats (PDF, DOCX, etc.)
- Extract key information such as name, contact details, skills, and experience
- API endpoint for resume extraction
- User-friendly interface for testing and integration

## Technologies Used
- **Django**: Web framework for building the application
- **Python**: Programming language for backend development
- **Spacy**: NLP library for processing natural language
- **PyResParser**: Library for parsing resumes
- **SQLite/PostgreSQL**: Database for storing application data
- **JavaScript**: For frontend interactions (if applicable)

## Installation
Follow these steps to set up the project on your local machine:

### Prerequisites
- Python 3.8 or later
- Django 3.2 or later
- pip (Python package manager)

### Step 1: Clone the repository

```bash
git clone https://github.com/yashovardhn/ResumeProcessor.git
cd ResumeProcessor 
```


# Step 2: Create a virtual environment
```bash
python3 -m venv virt
source virt/bin/activate  # On Windows use 'virt\Scripts\activate'
```

## Step 3: Install dependencies
```bash
pip install -r requirements.txt
```

## Step 4: Run database migrations

```bash
Copy code
python manage.py migrate
```

## Step 5: Run the server
```bash
Copy code
python manage.py runserver
```

Now, open your browser and go to http://127.0.0.1:8000/api/extract_resume/ to access the API.

Usage

API Endpoint
POST /api/extract_resume/
Description: Upload a resume for extraction.
Request Body: JSON object containing the resume data.
Response: JSON object with extracted information.
Example Request
```bash
Copy code
curl -X POST http://127.0.0.1:8000/api/extract_resume/ \
-H "Content-Type: application/json" \
-d '{"resume": "&lt;base64_encoded_resume&gt;"}'
```

Example Response
json
Copy code
{
    "message": "Resume extracted successfully",
    "data": {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "skills": ["Python", "Django", "Machine Learning"],
        ...
    }
}
Contributing

Contributions are welcome! If you want to contribute to the project, please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature/YourFeature).
Make your changes.
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature/YourFeature).
Open a pull request.
License

This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements

Django for the web framework.
Spacy for natural language processing.
PyResParser for resume parsing.
Contact

For any questions or inquiries, feel free to reach out:

Email: your.email@example.com
GitHub: yashovardhn

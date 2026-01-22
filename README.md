# Project Documentation

This repository contains the source code for the project.  
Follow the instructions below to set up and run the application locally.

---

## Prerequisites

Ensure the following are installed on your system:

- Python 3.8 or higher
- pip
- Uvicorn
- A modern web browser
- (Optional) VS Code Live Server extension

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
Install Required Dependencies
Install all required Python packages from requirements.txt.

Windows
pip install -r requirements.txt
macOS / Linux
python3 -m pip install -r requirements.txt
After running the command, all required packages will be installed.

Hugging Face Token Setup
This project requires a Hugging Face access token.

Locate the Hugging Face token section in the code and add your token:

hf_token = "YOUR_HUGGING_FACE_TOKEN"
Do not commit your token to a public repository.

Running the Application
Start the Backend Server
Open a terminal in the project directory and run:

uvicorn app:app --reload --host 127.0.0.1 --port 8000
The backend server will start at:

http://127.0.0.1:8000
Run the Frontend (Live Server)
For a better UI experience:

Open the index.html file

Run it using a Live Server

Example (VS Code): Right-click → Open with Live Server

Open the generated local URL in your browser

├── static/
├── templates/
└── README.md

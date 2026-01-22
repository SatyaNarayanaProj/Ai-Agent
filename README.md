1️. Install Required Dependencies

To install all required Python packages listed in requirements.txt, run the following command:

Windows
pip install -r requirements.txt

macOS / Linux
python3 -m pip install -r requirements.txt


This will automatically install all necessary dependencies.

2️. Set Your Hugging Face Token

In the Hugging Face token section of the code, replace the placeholder with your own token:

hf_token = "YOUR_HUGGING_FACE_TOKEN"


⚠️ Important:
Do not share or commit your token to public repositories.

3️. Run the Backend Server

Open your terminal in the project directory and start the server using:

uvicorn app:app --reload --host 127.0.0.1 --port 8000


The backend will start at:
👉 http://127.0.0.1:8000

--reload enables auto-reload during development

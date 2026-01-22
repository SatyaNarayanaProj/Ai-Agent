from huggingface_hub import InferenceClient

HF_TOKEN = "your_huggingface_token"
MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.2"

client = InferenceClient(token=HF_TOKEN)

def generate_description(title: str):
    prompt = (
        "You are an AI writing assistant.\n"
        "When user would be giving one liners no need to completely write team like that.\n"
        "Write a short, professional company announcement for employees.\n"
        f"Title: {title}\n"
        "Keep it under 50 words.\n"
        "Don't mention the title in the body.\n"
        "No need of the dear team also.\n"
        "Give the result very fast and take less time."

    )

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100,
        temperature=0.5,
        top_p=0.9,
        stream=False
    )

    description = response.choices[0].message["content"].strip()
    return description

def generate_suggestion(title : str):
        prompt2 = (

            "Do NOT rewrite the sentence.\n"
            "Do NOT add explanations.\n"
            "Context rules:\n"
            "- If the input looks like a company announcement, keep it professional.\n"
            "- Keep suggestions suitable for short announcements.\n"
            "- Do not include greetings like 'Dear team'.\n\n"  
        )


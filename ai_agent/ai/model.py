from huggingface_hub import InferenceClient
import os

HF_TOKEN = "your_hugging_face_token"
MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.2"

client = InferenceClient(token=HF_TOKEN)


def generate_suggestions(query: str):
    prompt = (
        "You are an AI autocomplete engine.\n"
        "Generate 5 professional title suggestions based on the partial input.\n"
        "Each suggestion must be a complete title.\n"
        "Do NOT use numbering, bullets, hyphens, or symbols.\n"
        "Do NOT explain anything.\n"
        "Return ONLY plain text suggestions.\n"
        "Each suggestion must be on a new line.\n"
        f"Input: {query}\n"
    )

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100,         
        temperature=0.3,
        top_p=0.9
    )

    raw_text = response.choices[0].message["content"]

   
    suggestions = []
    for line in raw_text.split("\n"):
        line = line.strip()

   
        line = line.lstrip("0123456789.-•) ").strip()

  
        if len(line.split()) < 3:
            continue

        if not line.endswith((".", ")", "e", "s")):
            continue

        suggestions.append(line)

        if len(suggestions) == 5:
            break

    return suggestions


def generate_description(title: str):
    prompt = (
        "You are an AI writing assistant.\n"
        "When user would be giving one liners no need to completely write team like that.\n"
        "Write a short, professional company announcement for employees.\n"
        f"Title: {title}\n"
        "Keep it under 500 words.\n"
        "Don't mention the title in the body.\n"
        "No need of the dear team also.\n"
        "You can also use some of the corporate terms and full forms in the brackets.\n"
        "Give the result very very fast and take less time."
    )

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=180,
        temperature=0.5,
        top_p=0.9
    )

    return response.choices[0].message["content"].strip()

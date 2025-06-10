import requests
from config import OPENROUTER_API_KEY, MODEL

def interpret(prompt):
    system = "Tu es un assistant GLPI. Lis la demande utilisateur et retourne un JSON avec l'action à faire."

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt}
        ]
    }

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
    data = response.json()

    try:
        reply = data["choices"][0]["message"]["content"]
        # Très simple, doit renvoyer un JSON du style :
        # {"action": "create_ticket", "title": "...", "content": "..."}
        return eval(reply)
    except Exception as e:
        return {"action": "error", "error": str(e)}

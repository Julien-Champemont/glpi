import requests
from config import GLPI_URL, APP_TOKEN, USER_TOKEN

def init_session():
    headers = {
        "App-Token": APP_TOKEN,
        "Authorization": f"user_token {USER_TOKEN}"
    }
    response = requests.get(f"{GLPI_URL}/initSession", headers=headers)
    return response.json().get("session_token")

def create_ticket(session_token, title, content):
    headers = {
        "App-Token": APP_TOKEN,
        "Session-Token": session_token,
        "Content-Type": "application/json"
    }

    data = {
        "input": {
            "name": title,
            "content": content,
            "priority": 3
        }
    }

    response = requests.post(f"{GLPI_URL}/Ticket", headers=headers, json=data)
    return response.json()

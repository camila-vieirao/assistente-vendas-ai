import os
import sys
from typing import List, Dict
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ROOT_DIR)

from petlove_agents.src.petlove_agents.crew import PetloveAgents

load_dotenv()

app = FastAPI()

class UserInput(BaseModel):
    message: str
    role: str = "user"
    conversation_id: str
    
class Conversation:
    def __init__(self):
        self.messages: List[Dict[str, str]] = []
        self.active: bool = True

conversations: Dict[str, Conversation] = {}



@app.post("/api/question-and-answer")
def chat(user_input: UserInput):
    if user_input.conversation_id not in conversations:
        conversations[user_input.conversation_id] = Conversation()

    conversation = conversations[user_input.conversation_id]
    conversation.messages.append({"role": user_input.role, "content": user_input.message})

    try:

        bot = PetloveAgents()
        result = bot.crew().kickoff(inputs={"user_input": user_input.message, "chat_history": conversation.messages})
        
        assistant_message = result.to_dict().get("final_output", str(result))
        conversation.messages.append({"role": "assistant", "content": assistant_message})

        return {
            "conversation_id": user_input.conversation_id,
            "response": assistant_message
            #"history": conversation.messages
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
import openai
import os
from dotenv import load_dotenv

## to update when User class implemented to keep track of token cost.
openai.api_key = os.environ["OPENAI_API_KEY"]
client = openai.OpenAI()

def getResponse(system: str, user: str, use4o: bool):
    if use4o:
        return getResponse4o(system, user)
    else:
        return getResponse4oMini(system, user)


# Uses the gpt-4o API to take instructions (system) and apply those to a user input (user)
def getResponse4o(system: str, user: str, temp:float = 1) -> str:
    MODEL = "gpt-4o"
    completion = client.chat.completions.create(
    model=MODEL, temperature = temp,
    messages=[{"role": "system", "content": user},{"role": "user", "content": system}])
    return completion.choices[0].message.content
    

# Uses the gpt-4o-mini API to take instructions (system) and apply those to a user input (user)
def getResponse4oMini(system: str, user: str, temp: float = 1) -> str:
    MODEL = "gpt-4o-mini"
    completion = client.chat.completions.create(
    model=MODEL, temperature = temp,
    messages=[{"role": "system", "content": user},{"role": "user", "content": system}])
    return completion.choices[0].message.content

  


from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    
    if lowered ==" ":
        return "hello anything else"
    elif 'hello' in lowered:
        return "hello there"
    else:
        return choice([' i dont understand...',
                      'what are yout talking about',
                      'do your mind entering that again'])
from datetime import datetime

def contains(terms: list[str], content: str)->bool:
    matches: list[bool] = []
    for term in terms:
        matches.append(term in content.lower())

    return any(matches)

def response(text: str)->str:
    text = text.lower()

    if contains (['hello','hi'],text):
        return 'Hello there!'
    elif contains(['goodbye','bye'],text):
        return 'Talk to you later'
    elif contains(['what time is it','current time','time'],text):
        return f"The time is: {datetime.now():%H:%M:%S}"
    elif contains(['how are you','how u doing','whats up'],text):
        return 'I\'m fine how are you??'
    elif contains(["im fine"],text):
        return 'Sounds good!! so whats the plan??'
    else:
        'Sorry I can provide that kindof response atm'

while True:
    user = input("User :")
    if 'bye' in user:
        print(f'Bot: {response(user)}')
        break
    else:
        print(f'Bot: {response(user)}')
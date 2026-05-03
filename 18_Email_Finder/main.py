import re

def extract_emails(text: str, unique_only: bool = True, case_sensitive: bool = True) -> list[str]:
    email_pattern: str = (
        r'\b[A-Za-z0-9.!#$%&\'*+/=?^_`{|}~-]+@[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?'
        r'(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?)*\.[A-Za-z]{2,}\b'
    )

    #Finds emails
    emails: list[str] = re.findall(email_pattern, text)

    if not case_sensitive:
        emails = [email.lower() for email in emails]

    if unique_only:
        #Removes Duplicates while preserving order
        emails = list(dict.fromkeys(emails))

    return emails

def list_emails(path: str) -> None:
    emails: list[str] = []

    # Also show that this works with website source code
    with open(path, 'r') as f:
        text: str = f.read()
        emails = extract_emails(text)

    emails = _domain_filter(emails)
    if emails:
        for email in emails:
            print(email)
    else:
        print('No emails found...')

def _domain_filter(email: list[str]) -> list[str]:
    new_emails = []
    for e in email:
        if e.endswith(('@gmail.com', '@yahoo.com', '@fastmail.com')):
            new_emails.append(e)

    return new_emails


def main() -> None:
    list_emails('file.txt')


if __name__ == '__main__':
    main()
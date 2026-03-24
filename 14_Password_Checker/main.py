import string

class PasswordValidator:
    def __init__(self):
        self.common_passwords: set[str] = self.load_common_passwords()

    @staticmethod
    def load_common_passwords() -> set[str]:
        with open('common_passwords.txt', 'r') as file:
            return {line.strip() for line in file if line}

    def is_common(self, password: str) -> bool:
        return password in self.common_passwords
    
    def rate(self, password: str) -> str:
        if self.is_common(password):
            return 'poor'
        
        score: int = 0
        if any(c.isupper() for c in password):
            score += 1

        if any(c in string.punctuation for c in password):
            score += 1

        if len(password) >= 10:
            score += 1

        if any(c.isdigit() for c in password):
            score += 1

        if self.has_sequential(password):
            return 'poor'

        if score > 3:
            return 'secure'
        elif 2 <= score <= 3:
            return 'medium'
        else:
            return 'poor'
        
    def rating_improver(self, password: str) -> str:
        suggestions = []

        if not any(c.isupper() for c in password):
            suggestions.append('add uppercase letters')

        if not any(c.isdigit() for c in password):
            suggestions.append('add digits')

        if not any(c in string.punctuation for c in password):
            suggestions.append('add special characters')

        if len(password) < 10:
            suggestions.append('increase length to at least 10 characters')

        if self.has_sequential(password):
            suggestions.append('avoid repeated sequential characters (like aaa, 111)')

        if suggestions:
            return 'You should ' + ', '.join(suggestions) + '.'
        else:
            return 'Your password looks good!'
        

    def has_sequential(self, password: str) -> bool:
        count = 1
        for i in range(1, len(password)):
            if password[i] == password[i - 1]:
                count += 1
                if count >= 3:
                    return True
            else:
                count = 1
        return False


def main() -> None:
    validator: PasswordValidator = PasswordValidator()
    print('🔒 Welcome to the Password Strength Checker!')
    print('Enter a password to get a quality rating.')

    while True:
        password: str = input('Enter password: ').strip()
        rating: str = validator.rate(password)

        if rating == 'secure':

            print('✅ Your password is secure! ')
            
        elif rating == 'medium':

            print('⚠️ Your password is of medium strength.')
            print(validator.rating_improver(password))
            
        else:

            print('⚠️ That password sucks!')
            print('Try adding symbols, uppercase letters, and increasing the length.')


if __name__ == '__main__':
    main()
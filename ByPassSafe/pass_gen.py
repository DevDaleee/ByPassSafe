import random
import string


class PasswordGenerator:
    @staticmethod
    def generate_password(length, num_digits, num_symbols, uppercase):
        all_chars = string.ascii_letters + string.digits + string.punctuation
        if not uppercase:
            all_chars = string.ascii_lowercase + string.digits + string.punctuation

        digits = "".join(random.choice(string.digits) for _ in range(num_digits))
        symbols = "".join(random.choice(string.punctuation) for _ in range(num_symbols))
        letters = "".join(
            random.choice(all_chars) for _ in range(length - num_digits - num_symbols)
        )

        password = "".join(random.sample(digits + symbols + letters, length))
        return password

import random
import string


class DataGenerators:
    @staticmethod
    def generate_random_alphanumeric_str(str_length=16):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=str_length))
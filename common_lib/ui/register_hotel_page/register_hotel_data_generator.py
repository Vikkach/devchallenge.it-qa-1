from common_lib.ui.data_generator import DataGenerators


class RegisterHotelDataGenerator(DataGenerators):
    @staticmethod
    def generate_random_name():
        return f'Name {DataGenerators.generate_random_alphanumeric_str()}'

    @staticmethod
    def generate_random_short_description():
        return f'Short description {RegisterHotelDataGenerator.generate_random_alphanumeric_str()}'

    @staticmethod
    def generate_random_description():
        return f'Description {RegisterHotelDataGenerator.generate_random_alphanumeric_str()}'

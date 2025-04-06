from faker import Faker

faker = Faker()
def generate_registration_data():
    email = faker.email()
    password = faker.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return email, password  # Возвращаем кортеж (email, password)

class UserDataGenerator:
    fake = Faker()

    @staticmethod
    def generate_name():
        return UserDataGenerator.fake.name()

    @staticmethod
    def generate_empty_name():
        return ""

    @staticmethod
    def generate_email():
        return UserDataGenerator.fake.email()



class PasswordGenerator:
    @staticmethod
    def generate_password():
        length = secrets.randbelow(5) + 6

        password = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(length))
        return password

    @staticmethod
    def generate_wrong_password():
        length = secrets.randbelow(5)

        password = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(length))
        return password
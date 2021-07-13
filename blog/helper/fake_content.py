from faker import Faker

faker = Faker()


def get_title():
    return faker.sentence(6)


def get_content():
    return faker.text(200)

from faker import Faker
import faker

fake = Faker()
for _ in range(10):
    print(fake.bothify(text="Serial Number: FR??-####-###N"))

import pytest
from faker import Faker

fake = Faker()

@pytest.fixture
def generate_records(request):
    num_records = request.config.getoption("--num_records")
    records = [(fake.random_int(), fake.random_int(), fake.word()) for _ in range(num_records)]
    return records

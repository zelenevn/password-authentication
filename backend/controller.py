from backend.decorators import validate_password
from backend.service import generate_password


@validate_password
def random_password(min_letters: int = 15, max_letters: int = 24):
    return generate_password(min_letters, max_letters)




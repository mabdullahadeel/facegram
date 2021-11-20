import uuid
import random, string

def get_random_string(length: int=12):
    code = str(uuid.uuid4().hex)[:length]
    return code

def id_generator(size: int=8, chars: str=string.ascii_uppercase + string.digits) -> str:
    return ''.join(random.choice(chars) for _ in range(size))
import uuid


def get_random_string(length=12):
    code = str(uuid.uuid4().hex)[:length]
    return code
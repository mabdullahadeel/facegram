import uuid


def get_uuid(string_length=12):
    """
        Returns a uuid4 string with required length
    """

    random_id = str(uuid.uuid4()).replace('-', '')
    required_length = string_length if string_length <= len(random_id) else len(random_id)
    return random_id[:required_length]
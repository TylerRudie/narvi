from django.utils.crypto import get_random_string

def genOneTimeCode():
    return get_random_string(length=8,
                             allowed_chars='ABCDEFGHIJKLMNPQRSTUVXYZ01234567890')
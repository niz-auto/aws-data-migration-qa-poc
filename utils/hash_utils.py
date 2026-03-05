import hashlib

def generate_hash(value):

    return hashlib.md5(value.encode()).hexdigest()
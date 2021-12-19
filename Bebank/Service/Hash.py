import hashlib


def hash_passwd(passwd):
    return hashlib.sha1(passwd.encode('utf-8'))

import hashlib
import secrets


class HashGenerator():
    def __init__(self):
        self.current_hash = ''

    def generate_hash(self, password: str, salt: str, hash_type: str):
        if not password:
            return "Digite uma senha!"

        if not salt:
            # Gera um salt aleatório
            salt = secrets.token_urlsafe(16)

        iterations = 100000

        # hash generator
        self.current_hash = hashlib.pbkdf2_hmac(
            hash_name=hash_type.lower(),
            password=password.encode('utf-8'),
            salt=salt.encode('utf-8'),
            iterations=iterations,
        ).hex()

        return self.current_hash

    def copy_hash(self):
        return self.current_hash

    def copy_alert(self):
        return 'Hash copiada com sucesso!'

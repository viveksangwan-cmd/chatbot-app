from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

with open('private_key.pem','rb') as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=none,
        backend=default_backend()
        )

public_key = private_key.public_key()

message=b"hello world"

ciphertext=public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA1()),
        algorithm=hashes.SHA1(),
        lable=None
    )
)
print(ciphertext)

plaintext=private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA1()),
        algorithm=hashes.SHA1(),
        lable=None
    )
)

print(plaintext)

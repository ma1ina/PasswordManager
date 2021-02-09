import encode
import hashlib
import aesCipher
import base64
data = encode.main()
key = input("key: ")
key = hashlib.sha3_256(bytes(key, encoding="utf-8"))
key = key.digest()
test = list(map(aesCipher.decode, data, [key] * len(data)))
print(test)
text_in_b64 = bytearray()
for i in test:
    for j in i:
        if j == 62:
            break
        text_in_b64.append(j)
print(base64.b64decode(text_in_b64).decode(encoding="utf-8"))

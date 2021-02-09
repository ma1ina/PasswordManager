from Crypto.Cipher import AES
import sys
import funcy
def CypherDecypher(wiad):
    key = b'Sixteen byte key'
    vector=b"0123456789ABCDEF"
    data=wiad
    aes = AES.new(key, AES.MODE_CBC, vector)
    szyfr=aes.encrypt(data)
    print(szyfr.decode("utf-8"))
    klucz=AES.new(key, AES.MODE_CBC, vector)
    odszyfruj= klucz.decrypt(szyfr)
    print(odszyfruj.decode("utf-8"))
message="To jest wiadomość dłuższa niż 16 bajtów gfdsagdux"
BitsTable=list(funcy.chunks(16, message))
index=2
print(BitsTable[index])
print(sys.getsizeof(BitsTable[index]))


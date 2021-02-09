import sys
linia="linia którą trzeba podzielić na 16 bajtównovovoiigpfpnasdopdkdfijeif"
TablicaLinii=[""]*(int(len(linia)/16)+1)
index=0
for i,j in enumerate(linia):
    TablicaLinii[index]=TablicaLinii[index]+j
    if (i+1)%16==0:
        index+=1
print(TablicaLinii)
x=TablicaLinii[3]
print(sys.getsizeof(x))
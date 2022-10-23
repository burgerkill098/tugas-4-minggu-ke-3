awal=int(input("masukkan bilangan awal :"))
akhir =int(input("masukkan bilangan akhir"))

bil_genap=[]

for i  in range(awal,akhir+1):
    if i%2==0:
        bil_genap.append(i)

print("bilangan genap =",bil_genap)


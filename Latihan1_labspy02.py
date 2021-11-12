
bil1 = int(input("masukan bilangan pertama: "))
bil2 = int(input("masukan bilangan kedua: "))
bil3 = int(input("masukan bilangan ketiga: "))

if bil1 > bil2 > bil3:
    print("bilangan pertama adalah bilangan terbesar")
elif bil2 > bil3:
    print("bilangan kedua adalah bilangan terbesar")
else:
    print("bilangan ketiga adalah bilangan terbesar")
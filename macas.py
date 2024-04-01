maca = int()
qmaca = int(input("Digite a quantidade de maçãs: "))

if qmaca < 12:
    maca = 0.30
else:
    maca = 0.25
    
print("Vai custar R$", qmaca * maca)

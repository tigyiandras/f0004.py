név = input('Hogy híjják kendet? ')
kor = input('És hány éves kend? ') # itt még stringet kapunk 

kor = int(kor) # átalakítjuk egész számmá, azaz int-té
év = input ('Melyik évben járunk? ')
év = int(év)

születési_év = év - kor
print(név, ', kend ', születési_év, '-ban született.', sep='')

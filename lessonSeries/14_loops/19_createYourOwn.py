housemates = ['Deb', 'Ron', 'Meggalena', 'Dessiree', 'Grape']

print 'You have...'
for h in housemates:
    if h == 'Grape':
        print h, 'is not a housemate!' # (she actually is.)
        break
    print 'A', h
else:
    print 'What nice housemates you have!'

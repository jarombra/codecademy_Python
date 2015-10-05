fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
    if f == 'potato':
        print 'A potato is not a fruit!'
        break
    print 'A', f
else:
    print 'A fine selection of fruits!'

# This should work, but there is a Codecademy bug:

#my_file = open("output.txt", "r")

#print my_file.readline()
#print my_file.readline()
#print my_file.readline()

#my_file.close()

# This is a more complicated version that works
# around the Codecademy bug:

my_file = open("text.txt","w")
my_file.write("I'm the first line of the file"+ "\n")
my_file.write("I'm the second line."+ "\n")
my_file.write("Third line here, boss."+ "\n")
my_file.close()
my_file = open("text.txt", "r") 
print my_file.readline()
print my_file.readline()
print my_file.readline()
my_file.close()

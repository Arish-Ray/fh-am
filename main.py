file = open('file.txt')
print(file.read())
file.close()

file = open('file.txt','w')
(file.write("my name is arish ray"))
file.close()

file = open('file.txt','a')
(file.write("my age is 10"))
file.close()
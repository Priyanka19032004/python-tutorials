file = open("fruit.txt","w")
file.write("Apple,10,5\n")
file.write("Orange,15,20\n")
file.write("Papaya,25,30\n")
file.close()

file = open("fruit.txt","r")
data=file.read()
file.close()

print("file content:")
print(data)
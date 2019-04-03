# f = open("data.txt", "w")
# f.write("sasdas")
# f.close()

with open('data.txt', 'r+') as f:
    data = 'some data to be written to the file'
    f.write(data)
    s = f.readline()
    print(s)

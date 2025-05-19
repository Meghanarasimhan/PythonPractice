with open("file.txt", "a") as file:
    print(file.read())
    line=file.readline()
    print(line)
    lines=file.readlines()
    print(lines)
    file.write("This is a new line")
    lines=['''id,name,age,gender\n1,"Manish",26,"M"\n2,"Rohan",13,"M"\n3,"Simaran",35,"F"\n ''']
    file.writelines(lines)
    file.seek(0)
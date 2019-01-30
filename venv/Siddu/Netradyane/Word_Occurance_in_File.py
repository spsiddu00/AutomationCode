file_One = "File_1"
file_Two = "File_2"
file_Three = "File_3"

list_Of_Files = [file_One,file_Two,file_Three]

for file in list_Of_Files:
    count = 0
    with open(file) as f:
        # print("Length of file",len(f.readlines()))
        # print(f.read())
        for line in f:
            # print(line)
            words = line.split(" ")
            # print(words)
            for word in words:
                if (word == "Accenture" or word == 'ACCENTURE'):
                    count +=1
                else:
                    pass
        print(f.name,"----->",count)
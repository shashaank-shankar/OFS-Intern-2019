def file_read(file):
    from itertools import islice
    with open(file, "w") as myfile:
        myfile.write("\nTest\n")
        myfile.write("Python Exercises\n")
    txt = open(file)
    print(txt.read())

file_read('/Users/Shashaank/Desktop/OFS-Intern-2019/Python Exercises/File IO/test.txt')
    
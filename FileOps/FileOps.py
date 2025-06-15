f = open("C:\\python_dev\\FileOps\\fileopsText.txt", "a")
f.write("This is a new test file.")

f.close()

f = open("C:\\python_dev\\FileOps\\fileopsText.txt", "r")
data = f.read()
print(data)
f.close()

# Clear the contents of the file
open("C:\\python_dev\\FileOps\\fileopsText.txt", "w").close()
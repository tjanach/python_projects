
read = open('ExampleTxtFileForAppend.txt','r').read()
print(read)

splitMe = read.split('\n')
print(splitMe)

lines = open('ExampleTxtFileForAppend.txt','r').readlines()
print(lines)
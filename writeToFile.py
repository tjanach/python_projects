
textToBeWritten = "Ala ma kota\n"

saveFile = open('ExampleTxtFile.txt','w')
saveFile.write(textToBeWritten)
saveFile.write(textToBeWritten)
saveFile.write(textToBeWritten)

saveFile.close()
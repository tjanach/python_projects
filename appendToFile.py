
textToBeAppended = "Ala ma kota\n"

saveFile = open('ExampleTxtFileForAppend.txt','a')
saveFile.write(textToBeAppended)

saveFile.close()
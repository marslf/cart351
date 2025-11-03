# OPEN FILE FOR READING
#rainbowFile = open("files/rainbow.txt", "r")



#out = rainbowFile.read(4) #specify the bites we want to read= one bite per character
# print(out) #you get the first 4 characters from the file in the terminal

#if you dont specify = you get everything 
#but it starts after the first 4 since that is where the cursor believes it is
#out2 = rainbowFile.read() 
#print(out2) 

#restart at the first character 
#rainbowFile.seek(0) 
#out3 = rainbowFile.read() 
#print(out3) 

#file is no longer accessible and read and write will release the system ressources it was using
#rainbowFile.close() 

#you can also make it read an entire line
#rainbowFile = open("files/rainbow.txt", "r")
#outline = rainbowFile.readline()
#print(outline)

#read all the lines
#outlines = rainbowFile.readlines()
#print(outlines)
#rainbowFile.close() 


#OPEN A FILE FOR WRITING
#it overwrites a file = what was previously in the file will disappear 
#sampleFile = open("files/sample_text.txt", "w")
#for i in range(3): 
    #a_name = input("enter animal: ")
    #sampleFile.write(a_name)
    #sampleFile.write("\n") #new line character 
#sampleFile.close()

#sampleFile = open("files/sample_text.txt", "w")
#animalList =[]
#for i in range(3): 
#    a_name = input("enter animal: ")
#    animalList.append(a_name+'\n')
#
#sampleFile.writelines(animalList)
#sampleFile.close()


#APPENDING = still using write but what matters is how you open and use the file
sampleFile_a = open("files/sample_text.txt", "a")
nameList = []
for i in range(3):
    name = input("type name : ")
    nameList.append(name+'\n')
    
sampleFile_a.writelines()
sampleFile_a.close
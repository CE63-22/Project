from word_matching import wordMatcher_demo
import os

print("\n\n"+"-"*10+"INITIALIZATION COMPLETED"+"-"*10+"\n")

print("Available Files:")
wavFilesName = []
i=0
for f in os.scandir(path="./resources"):
    if f.is_file():
        (fname, ftype) = os.path.splitext(f)
        if ftype == '.wav':
            wavFilesName.append(f.name)
            print('\t'+str(i)+". "+f.name)
            i+=1

selection=True
while(selection):   
    x = input("\nPlease enter the index of the file you want to work on... ")

    if x.isdigit() == True:
        # print("DEBUG: '"+x+"' IS A DIGIT")
        if int(x)<i:
            print("SELECTED FILE")
            print('\t'+str(x)+". {}".format(wavFilesName[int(x)]))
            selection=False
        else:
            print("That number is not exist in the list above, please try again.")
        
    else:
        # print("DEBUG: '"+x+"' IS A NOT DIGIT")
        print("That's not a number, please enter a number of index.")
        

print("\n\n------start------\n")

print("result = "+str(
    # wordMatcher_demo(4)
    # index
        # 0 = gsSample in English from google (not being used in Demo)
        # 1 = wavSample in English from google
        # 2 = wavSample in English
        # 3 = wavSample in Thai
        # 4 = 04Noey.wav
        # 5 = 04Noey.m4a
    ))



print("\n\n-------end-------\n")

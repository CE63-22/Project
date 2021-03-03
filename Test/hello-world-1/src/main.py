from word_matching import wordMatcher_demo
from word_matching import wordMatcher_demo_index
import os

print("\n\n"+"-"*10+"INITIALIZATION COMPLETED"+"-"*10+"\n")

# show all wav files in resources
print("Available Files:")
wavFilesName = []
wavSelectedFile = ''

i=0
for f in os.scandir(path="./resources"):
    if f.is_file():
        (fname, ftype) = os.path.splitext(f)
        if ftype == '.wav':
            wavFilesName.append(f.name)
            print('\t'+str(i)+". "+f.name)
            i+=1

# wav files selecor
selection=True
while(selection):   
    x = input("\nPlease enter the index of the file you want to work on... ")

    if x.isdigit() == True:
        # print("DEBUG: '"+x+"' IS A DIGIT")
        if int(x)<i:
            print("SELECTED FILE")
            wavSelectedFile = wavFilesName[int(x)]
            print('\t'+str(x)+". {}".format(wavSelectedFile))
            selection=False
        else:
            print("That number is not exist in the list above, please try again.")
        
    else:
        # print("DEBUG: '"+x+"' IS A NOT DIGIT")
        print("That's not a number, please enter a number of index.")

# show all txt files in resources/script
print("\nAvailable Scripts:")
txtFilesName = []
txtSelectedFile = ''

i=0
for f in os.scandir(path="./resources/script"):
    if f.is_file():
        (fname, ftype) = os.path.splitext(f)
        if ftype == '.txt':
            txtFilesName.append(f.name)
            print('\t'+str(i)+". "+f.name)
            i+=1

# txt files selecor
selection_script=True
while(selection_script):   
    x = input("\nPlease enter the index of the script you need... ")

    if x.isdigit() == True:
        # print("DEBUG: '"+x+"' IS A DIGIT")
        if int(x)<i:
            print("SELECTED FILE")
            txtSelectedFile = txtFilesName[int(x)]
            print('\t'+str(x)+". {}".format(txtSelectedFile))
            selection_script=False
        else:
            print("That number is not exist in the list above, please try again.")
        
    else:
        # print("DEBUG: '"+x+"' IS A NOT DIGIT")
        print("That's not a number, please enter a number of index.")
        

print("\n\n------start------\n")

result = wordMatcher_demo(wavSelectedFile,txtSelectedFile)
print("result = "+str(
    result
    # wordMatcher_demo_index(4)
    # index
        # 0 = gsSample in English from google (not being used in Demo)
        # 1 = wavSample in English from google
        # 2 = wavSample in English
        # 3 = wavSample in Thai
        # 4 = 04Noey.wav
        # 5 = 04Noey.m4a
    ))

# commenting (not necessary, just for fun)
if result > 0.9 :
    print("That's Great!")
elif result > 0.8 :
    print("Not bad though")
elif result > 0.7 :
    print("Hmm, could be better...")
elif result > 0.6 :
    print("Something is wrong I can feel it.")
elif result > 0.5 :
    print("Is the file match the script?")
elif result > 0.4 :
    print("Are you joking?")
elif result > 0.3 :
    print("Holy...")
else:
    print("...\nwat\nda\n...")


print("\n\n-------end-------\n")

"""
Programmer / Author: Tony Rahman
URL: www.flyingsalmon.net
Github: https://github.com/flyingsalmon

"""
import pyttsx3
engine = pyttsx3.init()
import pandas as pd
source_file="Data\\potus.txt"

def speakIt(s,i):
    # if i is non-zero, saves playing audio to a mp3 file
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id) 
    engine.say(s)
    engine.runAndWait()
    
    if (i):
        saveMP3(s)

def show(n):
    # n is passed either as a positive or negative int to this fn.
    if (n>0):
        s=df.head(n).to_string(index=False, header=False)
        print("Showing FIRST", n, "presidents: \n", s)
        intro="Here is a list of the first " + str(n) + "American presidents.."
        s = intro + s
        
        speakIt(s, 1) 
        
    elif (n<0):
        s=df.tail(-n).to_string(index=False, header=False)
        print("Showing LAST", -n, "presidents: \n", s)
        intro="Here is a list of the last " + str(-n) + "American presidents.."
        s = intro + s
        speakIt(s, 1)
        
    else:
        return    

def saveMP3(s):
    MP3filename='Data//POTUS-TTStest3.mp3'
    engine.save_to_file(s, MP3filename) # and save the entire readout to an audio file.
    engine.runAndWait()


### main driver ###
df=pd.read_csv(source_file)
dfdim=df.shape 
data_rows=dfdim[0] 
print("Total United States presidents on record: \n", data_rows)
print("\nWhich presidents' names do you want read aloud (pick a number from menu)?")
ui = input("[For first 2 presidents, enter 2. For the last 2 presidents, enter -2. To get 10th president, enter: #10. \
And so on. To hear all presidents' names enter: 99] [Quit/Cancel:0 or ENTER]: ")

if (len(ui) <1):
    exit()

if (ui[0]=='#'):
    ui=ui.strip('#')
    idx=int(ui)
    idx=idx-1
    if (idx <0): idx=0

    s=df.loc[idx, 'Presidents']
    print("Number {0} president: ".format(idx +1), end='')
    print(s)
    intro="Number ", idx+1, " president of USA is..." + s
    speakIt(intro,1)

elif (ui.isdigit):
    if (int(ui) <99):
        show(int(ui)) 
    else:
        show(data_rows)

# --- end main


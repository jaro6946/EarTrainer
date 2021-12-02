
import PySimpleGUI as sg

import time
from mingus.midi.pyfluidsynth import fluidsynth
from random import randrange
import layouts
import threading
import random


class stopAllNotes (threading.Thread):
   def __init__(self):
       threading.Thread.__init__(self)
      
   def run(self):
       time.sleep(.25)
       [fs.noteoff(0,x) for x in range(1,100)]

class stopNotes (threading.Thread):
   def __init__(self, time, notes):
       threading.Thread.__init__(self)
       self.time=time
       self.notes=notes
   def run(self):
       time.sleep(self.time)
       [fs.noteoff(0,note) for note in self.notes]


#Initialize Fluidsynth

fs = fluidsynth.Synth(gain=.8)
fs.start(driver = 'dsound')

sfid = fs.sfload("./SoundFonts/Guitar.sf2")
fs.program_select(0, sfid, 0, 0)



# Initalize the main loop
memory=[0]
intervals=['U','m2','M2','m3', 'M3', 'p4','t', 'p5', 'm6', 'M6', 'm7', 'M7', 'OCT']
intervalChoices=[[0,0],[0,1],[0,2],[0,3], [0,4], [0,5],[0,6], [0,7],
              [0,8], [0,9], [0,10], [0,11],[0,12]]
currentGuess=0
answerKey=[]

seed=0
chords=['majorChord', 'minorChord', 'major7Chord', 'dominate7Chord','minor7Chord','sus2Chord','sus4Chord']
chordChoices=[[0, 4, 7], [0, 3, 7],[0, 4, 7, 11],[0, 4, 7, 10],
             [0, 3, 7, 10],[0, 2, 7],[0, 5, 7]]

degrees=['I','ii','iii','IV','V','vi','vii','OCT0']
degreeChoices=[[0,4,7],[2,5,9],[4,7,11],[5,9,12],[7,11,14],[9,12,16],[11,14,17],[12,16,19]]

majorScale=[0, 2, 4, 5, 7, 9, 11, 12]
diatonicScale=[0,1,2,3,4,5,6,7,8,9,10,11,12]

instrumentModes=['guitar','piano','voice']
instrumentLinks={'guitar':"./SoundFonts/Guitar.sf2",'piano':"./SoundFonts/Piano.sf2",'voice':"./SoundFonts/Voice.sf2"}

chordFlag=0
playMode='home'
mode='quiz'

window=layouts.homeLayout()
instrumentMode='guitar'

while True:
    seed=0
    event, values = window.read(timeout=100)        # Poll every 100 ms
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break
    if event == '?':
        print(memory, answerKey)
    

    # If a button was pressed, display it on the GUI by updating the text element
    if event == 'play' or mode=='play':
        if event=='play':
            if mode=='play':
                mode='quiz'
                playMode='home'
                window.close()
                window=layouts.homeLayout()
                event, values = window.read(timeout=100) 
            elif mode=='quiz':
                mode='play'
                degreeRanSeed=randrange(40,76-11)
                window.close()
                window=layouts.playLayout()
                event, values = window.read(timeout=100)
    elif event=='home':
        playMode='home'
        window.close()
        window=layouts.homeLayout()
        event, values = window.read(timeout=100)

    elif  event== 'majorScale':
        playMode='majorScale'
        window.close()
        window=layouts.intervalViewLayout()
        event, values = window.read(timeout=100) 
    elif event == 'diatonicScale':
        playMode='diatonicScale'
        window.close()
        window=layouts.intervalViewLayout()
        event, values = window.read(timeout=100) 
    elif event == 'chord':
        playMode='chord'
        window.close()
        window=layouts.chordLayout()
        event, values = window.read(timeout=100) 
    
    elif event == 'degree':
        playMode ='degree'
        window.close()
        window=layouts.degreeLayout()
        event, values = window.read(timeout=100) 

    elif playMode=='home':
        if values[0]!=instrumentMode:
            instrumentMode=values[0]
            print(instrumentMode)
            sfid = fs.sfload(instrumentLinks[instrumentMode])
            fs.program_select(0, sfid, 0, 0)


    if event != sg.TIMEOUT_KEY:  
        window['-OUTPUT-'].update(playMode)


    for i,interval in enumerate(intervals): 
            if interval==event:#oct
                if mode=='play':
                    playValue=i
                    event='-exNEXT-'
                    playMode='diatonicScale'
                elif currentGuess>len(answerKey)-1:
                    pass
                elif event==answerKey[currentGuess]:
                    print('Correct')
                    currentGuess=currentGuess+1
                    if currentGuess>len(answerKey)-1:
                        print('You sexy!')
                        currentGuess=100
                else:
                    print('Wrong')

    for i,chord in enumerate(chords):
            if chord==event:
                if mode=='play':
                    playValue=i
                    event='-exNEXT-'
                    playMode='chord'
                elif currentGuess>len(answerKey)-1:
                    pass
                elif event==answerKey[currentGuess]:
                    print('Correct')
                    currentGuess=currentGuess+1
                    if currentGuess>len(answerKey)-1:
                        print('You sexy!')
                else:
                    print('wrong')


    for i,chord in enumerate(degrees):
            if chord==event:
                if mode=='play':
                    playValue=i
                    event='-exNEXT-'
                    playMode='degree'
                elif currentGuess>len(answerKey)-1:
                    pass
                elif event==answerKey[currentGuess]:
                    print('Correct')
                    currentGuess=currentGuess+1
                    if currentGuess>len(answerKey)-1:
                        print('You sexy!')
                else:
                    print('wrong')


    if event=='-exNEXT-' and playMode!='home':
        noteLength=values[4]/50
        strength=values[3]
        chordOffset=values[2]/10
        subListOffset=values[1]/10
        #window['OUTPUT'].update('')
        currentGuess=0
        memory=[]
        answerKey=[]
        numberOfNotes=values[0]
        
        if playMode=='majorScale':                                        
            ranSeed=randrange(40,76-majorScale[-1])
            
            noteList=list(majorScale)
            for i,x in enumerate(majorScale):
                noteList[i]=noteList[i]+ranSeed
            #Choose apropriate number of notes
            notes2Play=[[noteList[randrange(0,len(noteList))]] for i,j in enumerate(noteList) if i < numberOfNotes]

            for note in range(1,len(notes2Play)):   
                numericInterval=notes2Play[note][0]-notes2Play[note-1][0]
                answerKey.append(intervals[abs(numericInterval)])
            


        if playMode=='diatonicScale': 
            

            ranSeed=randrange(40,76-diatonicScale[-1])
            
            noteList=list(diatonicScale)
            for i,x in enumerate(diatonicScale):
                noteList[i]=noteList[i]+ranSeed
            #Choose apropriate number of notes
            if mode=='play':
                notes2Play=[[noteList[0]],[noteList[playValue]]] 
                random.shuffle(notes2Play)
            else:
                notes2Play=[[noteList[randrange(0,len(noteList))]] for i,j in enumerate(noteList) if i < numberOfNotes]

            for note in range(1,len(notes2Play)):   
                numericInterval=notes2Play[note][0]-notes2Play[note-1][0]
                answerKey.append(intervals[abs(numericInterval)])


        if playMode=='chord':                                        
            
            chordChoices=[[0, 4, 7], [0, 3, 7],[0, 4, 7, 11],[0, 4, 7, 10],
             [0, 3, 7, 10],[0, 2, 7],[0, 5, 7]]
            chordList=chordChoices.copy()
            for i,chord in enumerate(chordList):
                ranSeed=randrange(40,76-11)
                for j, note in enumerate(chord):
                    chordList[i][j]=chordList[i][j]+ranSeed
            #Choose apropriate number of notes
            if mode=='play':
                numberOfNotes=1
                randomNotes=[playValue]
                answerKey=[chords[playValue]]
                notes2Play=[chordList[randomNotes[i]] for i,chord in enumerate(chordList) if i < numberOfNotes]

            else:
                randomNotes=[randrange(0,len(chordList)) for i,chord in enumerate(chordList) if i < numberOfNotes]
                answerKey=[chords[randomNotes[i]] for i,chord in enumerate(chordList) if i < numberOfNotes]
                notes2Play=[chordList[randomNotes[i]] for i,chord in enumerate(chordList) if i < numberOfNotes]


        if playMode=='degree':                                        
            
            degreeChoices=[[0,4,7],[2,5,9],[4,7,11],[5,9,12],[7,11,14],[9,12,16],[11,14,17],[12,16,19]]
            chordList=degreeChoices.copy()
            
            
            #Choose apropriate number of notes

            if mode=='play':
                for i,chord in enumerate(chordList):
                    for j, note in enumerate(chord):
                        chordList[i][j]=chordList[i][j]+degreeRanSeed
                numberOfNotes=1
                randomNotes=[playValue]
                answerKey=[degrees[playValue]]
                notes2Play=[chordList[randomNotes[i]] for i,chord in enumerate(chordList) if i < numberOfNotes]

            else:
                ranSeed=randrange(40,76-11)
                for i,chord in enumerate(chordList):
                    for j, note in enumerate(chord):
                        chordList[i][j]=chordList[i][j]+ranSeed
                randomNotes=[randrange(0,len(chordList)) for i,chord in enumerate(chordList) if i < numberOfNotes]
                answerKey=[degrees[randomNotes[i]] for i,chord in enumerate(chordList) if i < numberOfNotes]
                notes2Play=[chordList[randomNotes[i]] for i,chord in enumerate(chordList) if i < numberOfNotes]

                rootNote=[ranSeed]
                notes2Play.insert(0,rootNote)
       

        memory=notes2Play
        #accept list like this [[],[],[],[],[]].  Play notes simaltaneous in sublist, offset between sublist
        for subList in notes2Play:
            flag=0
            for note in subList:
                if note == subList[-1]:
                    flag=1
                fs.noteon(0,note,int(strength))
                muteOneNote=stopNotes(noteLength, [note])
                muteOneNote.start()
                if flag==0:
                    time.sleep(chordOffset)
            time.sleep(subListOffset)


    if event=='-exRESTART SONG-' and playMode!='home':
        strength=values[3]
        chordOffset=values[2]/10
        subListOffset=values[1]/10
        #window['OUTPUT'].update('')

        for subList in notes2Play:
            flag=0
            for note in subList:
                if note == subList[-1]:
                    flag=1
                fs.noteon(0,note,int(strength))
                muteOneNote=stopNotes(noteLength, [note])
                muteOneNote.start()
                if flag==0:
                    time.sleep(chordOffset)
            time.sleep(subListOffset)
        
        

            
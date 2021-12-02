import PySimpleGUI as sg



image_pause = './ButtonGraphics/Pause.png'
image_restart = './ButtonGraphics/Restart.png'
image_next = './ButtonGraphics/Next.png'
image_exit = './ButtonGraphics/Exit.png'

# Use the theme APIs to set the buttons to blend with background
#sg.theme_button_color((sg.theme_background_color(), sg.theme_background_color()))
#sg.theme_border_width(0)        # make all element flat


def homeLayout():
    layout= [[sg.Text('Media File Player',size=(17,1), font=("Helvetica", 25))],
                [sg.Text(size=(15, 2), font=("Helvetica", 14), key='-OUTPUT-')],
                [sg.Button(image_filename=image_restart, image_size=(50, 50), image_subsample=2,  key='-exRESTART SONG-'),
                sg.Text(' ' * 2),
                sg.Button('?',  font=("Helvetica", 12),size=(5, 2),  key='?'),
                sg.Text(' ' * 2),
                sg.Button(image_filename=image_next, image_size=(50, 50), image_subsample=2,  key='-exNEXT-'),
                sg.Text(' ' * 2),
                sg.Text(' ' * 2), sg.Button(image_filename=image_exit, image_size=(50, 50), image_subsample=2, key='Exit')],
                [sg.Text('_'*30)],
          
            
                [sg.Button('Diatonic Scale', font=("Helvetica", 12), size=(12, 1), key='diatonicScale'), 
                 sg.Button('Major Scale', font=("Helvetica", 12), size=(10, 1), key='majorScale')], 
                [sg.Button('chord', font=("Helvetica", 12), size=(8, 1), key='chord'),
                 sg.Button('play', font=("Helvetica", 12), size=(8, 1), key='play'),
                 sg.Button('degree', font=("Helvetica", 12), size=(8, 1), key='degree')],
                 [sg.Text('_'*30)],
                 [sg.Spin(values=('guitar', 'piano', 'voice'), initial_value='guitar')]
                
             
                ]


    # Open a form, note that context manager can't be used generally speaking for async forms
    return sg.Window('Jacobs Interval Trainer', layout, default_element_size=(20, 1), font=("Helvetica", 25), grab_anywhere=True)


def intervalViewLayout():
    layout= [[sg.Text('Media File Player',size=(17,1), font=("Helvetica", 25))],
                [sg.Text(size=(15, 2), font=("Helvetica", 14), key='-OUTPUT-')],
                [sg.Button(image_filename=image_restart, image_size=(50, 50), image_subsample=2,  key='-exRESTART SONG-'),
                sg.Text(' ' * 2),
                sg.Button('?',  font=("Helvetica", 12),size=(5, 2),  key='?'),
                sg.Text(' ' * 2),
                sg.Button(image_filename=image_next, image_size=(50, 50), image_subsample=2,  key='-exNEXT-'),
                sg.Text(' ' * 2),
                sg.Text(' ' * 2), sg.Button(image_filename=image_exit, image_size=(50, 50), image_subsample=2, key='Exit')],
                [sg.Text('_'*30)],
          
            
                [sg.Button('Diatonic Scale', font=("Helvetica", 12), size=(12, 1), key='diatonicScale'), 
                 sg.Button('Major Scale', font=("Helvetica", 12), size=(10, 1), key='majorScale')], 
                [sg.Button('chord', font=("Helvetica", 12), size=(8, 1), key='chord'),
                 sg.Button('play', font=("Helvetica", 12), size=(8, 1), key='play'),
                 sg.Button('degree', font=("Helvetica", 12), size=(8, 1), key='degree'),
                 sg.Button('Home', font=("Helvetica", 12), size=(8, 1), key='home')],
                 [sg.Text('_'*30)],
                [sg.Slider( range=(2, 10), default_value=2, size=(10, 20), orientation='vertical', font=("Helvetica", 15)),
                 sg.Text(' ' * 2),
                 sg.Slider(range=(1, 100), default_value=10, size=(10, 20), orientation='vertical', font=("Helvetica", 15)),
                 sg.Text(' ' * 2),
                 sg.Slider(range=(0, 100), default_value=10, size=(10, 20), orientation='vertical', font=("Helvetica", 15)),
                 sg.Text(' ' * 2),
                 sg.Slider(range=(0, 100), default_value=99, size=(10, 20), orientation='vertical', font=("Helvetica", 15)),
                 sg.Text(' ' * 2),
                 sg.Slider(range=(0, 100), default_value=40, size=(10, 20), orientation='vertical', font=("Helvetica", 15))
                 #,sg.Output(size=(50,10), key='OUTPUT', font=("Helvetica", 8))
                 ],
                [sg.Text('# Notes', font=("Helvetica", 12), size=(7, 1)),
                sg.Text('subListInterval', font=("Helvetica", 12), size=(12, 1)),
                sg.Text('chordInterval', font=("Helvetica", 12), size=(9, 1)),
                sg.Text('Volume', font=("Helvetica", 12), size=(8, 1)),
                sg.Text('NoteLength', font=("Helvetica", 12), size=(8, 1))],
                [sg.Text('_'*30)],
                [sg.Button('U', font=("Helvetica", 12), size=(8, 1), key='U'), 
                 sg.Button('m2', font=("Helvetica", 12), size=(8, 1), key='m2'), 
                 sg.Button('M2', font=("Helvetica", 12), size=(8, 1), key='M2'),
                 sg.Button('m3', font=("Helvetica", 12), size=(8, 1), key='m3'), 
                 sg.Button('M3', font=("Helvetica", 12), size=(8, 1), key='M3'), 
                 sg.Button('p4', font=("Helvetica", 12), size=(8, 1), key='p4'),
                 sg.Button('t', font=("Helvetica", 12), size=(8, 1), key='t')], 
                [sg.Button('p5', font=("Helvetica", 12), size=(8, 1), key='p5'), 
                 sg.Button('m6', font=("Helvetica", 12), size=(8, 1), key='m6'), 
                 sg.Button('M6', font=("Helvetica", 12), size=(8, 1), key='M6'),
                 sg.Button('m7', font=("Helvetica", 12), size=(8, 1), key='m7'), 
                 sg.Button('M7', font=("Helvetica", 12), size=(8, 1), key='M7'), 
                 sg.Button('O', font=("Helvetica", 12), size=(8, 1), key='OCT')],
                 [sg.Text('_'*30)]
             
                ]


    # Open a form, note that context manager can't be used generally speaking for async forms
    return sg.Window('Jacobs Interval Trainer', layout, default_element_size=(20, 1), font=("Helvetica", 25), grab_anywhere=True)


def chordLayout():
    layout= [[sg.Text('Media File Player',size=(17,1), font=("Helvetica", 25))],
            [sg.Text(size=(15, 2), font=("Helvetica", 14), key='-OUTPUT-')],
            [sg.Button(image_filename=image_restart, image_size=(50, 50), image_subsample=2,  key='-exRESTART SONG-'),
            sg.Text(' ' * 2),
            sg.Button('?',  font=("Helvetica", 12),size=(5, 2),  key='?'),
            sg.Text(' ' * 2),
            sg.Button(image_filename=image_next, image_size=(50, 50), image_subsample=2,  key='-exNEXT-'),
            sg.Text(' ' * 2),
            sg.Text(' ' * 2), sg.Button(image_filename=image_exit, image_size=(50, 50), image_subsample=2, key='Exit')],
            [sg.Text('_'*30)],
          
            
            [sg.Button('Diatonic Scale', font=("Helvetica", 12), size=(12, 1), key='diatonicScale'), 
             sg.Button('Major Scale', font=("Helvetica", 12), size=(10, 1), key='majorScale')], 
            [sg.Button('chord', font=("Helvetica", 12), size=(8, 1), key='chord'),
             sg.Button('play', font=("Helvetica", 12), size=(8, 1), key='play'),
             sg.Button('degree', font=("Helvetica", 12), size=(8, 1), key='degree'),
             sg.Button('Home', font=("Helvetica", 12), size=(8, 1), key='home')],
             [sg.Text('_'*30)],
            [sg.Slider( range=(1, 10), default_value=2, size=(10, 20), orientation='vertical', font=("Helvetica", 15)),
             sg.Text(' ' * 2),
             sg.Slider(range=(1, 100), default_value=10, size=(10, 20), orientation='vertical', font=("Helvetica", 15)),
             sg.Text(' ' * 2),
             sg.Slider(range=(0, 100), default_value=3, size=(10, 20), orientation='vertical', font=("Helvetica", 15)),
             sg.Text(' ' * 2),
             sg.Slider(range=(0, 100), default_value=99, size=(10, 20), orientation='vertical', font=("Helvetica", 15)),
                 sg.Text(' ' * 2),
                 sg.Slider(range=(0, 100), default_value=40, size=(10, 20), orientation='vertical', font=("Helvetica", 15))
                 #,sg.Output(size=(50,10), key='OUTPUT', font=("Helvetica", 8))
                 ],
                [sg.Text('# Notes', font=("Helvetica", 12), size=(7, 1)),
                sg.Text('subListInterval', font=("Helvetica", 12), size=(12, 1)),
                sg.Text('chordInterval', font=("Helvetica", 12), size=(9, 1)),
                sg.Text('Volume', font=("Helvetica", 12), size=(8, 1)),
                sg.Text('NoteLength', font=("Helvetica", 12), size=(8, 1))],
                [sg.Text('_'*30)],
             [sg.Button('Major', font=("Helvetica", 12), size=(8, 1), key='majorChord'),
             sg.Button('Minor', font=("Helvetica", 12), size=(8, 1), key='minorChord'), 
             sg.Button('Major 7', font=("Helvetica", 12), size=(8, 1), key='major7Chord'), 
             sg.Button('Minor 7', font=("Helvetica", 12), size=(8, 1), key='minor7Chord'),
             sg.Button('Dominate 7', font=("Helvetica", 12), size=(10, 1), key='dominate7Chord'),
             sg.Button('Sus2', font=("Helvetica", 12), size=(8, 1), key='sus2Chord'),
             sg.Button('Sus4', font=("Helvetica", 12), size=(8, 1), key='sus4Chord')],
             [sg.Text('_'*30)]
             
            ]


# Open a form, note that context manager can't be used generally speaking for async forms
    return sg.Window('Jacobs Interval Trainer', layout, default_element_size=(20, 1), font=("Helvetica", 25), grab_anywhere=True)


def degreeLayout():
    layout= [[sg.Text('Media File Player',size=(17,1), font=("Helvetica", 25))],
            [sg.Text(size=(15, 2), font=("Helvetica", 14), key='-OUTPUT-')],
            [sg.Button(image_filename=image_restart, image_size=(50, 50), image_subsample=2,  key='-exRESTART SONG-'),
            sg.Text(' ' * 2),
            sg.Button('?',  font=("Helvetica", 12),size=(5, 2),  key='?'),
            sg.Text(' ' * 2),
            sg.Button(image_filename=image_next, image_size=(50, 50), image_subsample=2,  key='-exNEXT-'),
            sg.Text(' ' * 2),
            sg.Text(' ' * 2), sg.Button(image_filename=image_exit, image_size=(50, 50), image_subsample=2, key='Exit')],
            [sg.Text('_'*30)],
          
            
            [sg.Button('Diatonic Scale', font=("Helvetica", 12), size=(12, 1), key='diatonicScale'), 
             sg.Button('Major Scale', font=("Helvetica", 12), size=(10, 1), key='majorScale')], 
            [sg.Button('chord', font=("Helvetica", 12), size=(8, 1), key='chord'),
             sg.Button('play', font=("Helvetica", 12), size=(8, 1), key='play'),
             sg.Button('degree', font=("Helvetica", 12), size=(8, 1), key='degree'),
                 sg.Button('Home', font=("Helvetica", 12), size=(8, 1), key='home')],
             [sg.Text('_'*30)],
            [sg.Slider( range=(1, 10), default_value=2, size=(10, 20), orientation='vertical', font=("Helvetica", 15)),
             sg.Text(' ' * 2),
             sg.Slider(range=(1, 100), default_value=10, size=(10, 20), orientation='vertical', font=("Helvetica", 15)),
             sg.Text(' ' * 2),
             sg.Slider(range=(0, 100), default_value=3, size=(10, 20), orientation='vertical', font=("Helvetica", 15)),
             sg.Text(' ' * 2),
             sg.Slider(range=(0, 100), default_value=99, size=(10, 20), orientation='vertical', font=("Helvetica", 15)),
                 sg.Text(' ' * 2),
                 sg.Slider(range=(0, 100), default_value=40, size=(10, 20), orientation='vertical', font=("Helvetica", 15))
                 #,sg.Output(size=(50,10), key='OUTPUT', font=("Helvetica", 8))
                 ],
                [sg.Text('# Notes', font=("Helvetica", 12), size=(7, 1)),
                sg.Text('subListInterval', font=("Helvetica", 12), size=(12, 1)),
                sg.Text('chordInterval', font=("Helvetica", 12), size=(9, 1)),
                sg.Text('Volume', font=("Helvetica", 12), size=(8, 1)),
                sg.Text('NoteLength', font=("Helvetica", 12), size=(8, 1))],
                [sg.Text('_'*30)],
            
             [sg.Button('I', font=("Helvetica", 12), size=(8, 1), key='I'),
             sg.Button('ii', font=("Helvetica", 12), size=(8, 1), key='ii'), 
             sg.Button('iii', font=("Helvetica", 12), size=(8, 1), key='iii'), 
             sg.Button('IV', font=("Helvetica", 12), size=(8, 1), key='IV'),
             sg.Button('V', font=("Helvetica", 12), size=(10, 1), key='V'),
             sg.Button('vi', font=("Helvetica", 12), size=(8, 1), key='vi'),
             sg.Button('vii', font=("Helvetica", 12), size=(8, 1), key='vii'),
             sg.Button('O', font=("Helvetica", 12), size=(8, 1), key='OCT0')],
             [sg.Text('_'*30)]
             
            ]


    # Open a form, note that context manager can't be used generally speaking for async forms
    return sg.Window('Jacobs Interval Trainer', layout, default_element_size=(20, 1), font=("Helvetica", 25), grab_anywhere=True)



def playLayout():
    layout= [[sg.Text('Media File Player',size=(17,1), font=("Helvetica", 25))],
            [sg.Text(size=(15, 2), font=("Helvetica", 14), key='-OUTPUT-')],
            [sg.Button('?',  font=("Helvetica", 12),size=(5, 2),  key='?'),
            sg.Text(' ' * 2), sg.Button(image_filename=image_exit, image_size=(50, 50), image_subsample=2, key='Exit')],
            [sg.Text('_'*30)],
          
            [sg.Button('home', font=("Helvetica", 12), size=(8, 1), key='play')],
             [sg.Text('_'*30)],
            [sg.Slider( range=(1, 10), default_value=2, size=(10, 20), orientation='vertical', font=("Helvetica", 15)),
             sg.Text(' ' * 2),
             sg.Slider(range=(1, 100), default_value=10, size=(10, 20), orientation='vertical', font=("Helvetica", 15)),
             sg.Text(' ' * 2),
             sg.Slider(range=(0, 100), default_value=3, size=(10, 20), orientation='vertical', font=("Helvetica", 15)),
             sg.Text(' ' * 2),
             sg.Slider(range=(0, 100), default_value=99, size=(10, 20), orientation='vertical', font=("Helvetica", 15)),
                 sg.Text(' ' * 2),
                 sg.Slider(range=(0, 100), default_value=40, size=(10, 20), orientation='vertical', font=("Helvetica", 15))
                 #,sg.Output(size=(50,10), key='OUTPUT', font=("Helvetica", 8))
                 ],
                [sg.Text('# Notes', font=("Helvetica", 12), size=(7, 1)),
                sg.Text('subListInterval', font=("Helvetica", 12), size=(12, 1)),
                sg.Text('chordInterval', font=("Helvetica", 12), size=(9, 1)),
                sg.Text('Volume', font=("Helvetica", 12), size=(8, 1)),
                sg.Text('NoteLength', font=("Helvetica", 12), size=(8, 1))],
                [sg.Text('_'*30)],
            [sg.Button('U', font=("Helvetica", 12), size=(8, 1), key='U'), 
             sg.Button('m2', font=("Helvetica", 12), size=(8, 1), key='m2'), 
             sg.Button('M2', font=("Helvetica", 12), size=(8, 1), key='M2'),
             sg.Button('m3', font=("Helvetica", 12), size=(8, 1), key='m3'), 
             sg.Button('M3', font=("Helvetica", 12), size=(8, 1), key='M3'), 
             sg.Button('p4', font=("Helvetica", 12), size=(8, 1), key='p4'),
             sg.Button('t', font=("Helvetica", 12), size=(8, 1), key='t')], 
            [sg.Button('p5', font=("Helvetica", 12), size=(8, 1), key='p5'), 
             sg.Button('m6', font=("Helvetica", 12), size=(8, 1), key='m6'), 
             sg.Button('M6', font=("Helvetica", 12), size=(8, 1), key='M6'),
             sg.Button('m7', font=("Helvetica", 12), size=(8, 1), key='m7'), 
             sg.Button('M7', font=("Helvetica", 12), size=(8, 1), key='M7'), 
             sg.Button('O', font=("Helvetica", 12), size=(8, 1), key='OCT')],
             [sg.Button('Major', font=("Helvetica", 12), size=(8, 1), key='majorChord'),
             sg.Button('Minor', font=("Helvetica", 12), size=(8, 1), key='minorChord'), 
             sg.Button('Major 7', font=("Helvetica", 12), size=(8, 1), key='major7Chord'), 
             sg.Button('Minor 7', font=("Helvetica", 12), size=(8, 1), key='minor7Chord'),
             sg.Button('Dominate 7', font=("Helvetica", 12), size=(10, 1), key='dominate7Chord'),
             sg.Button('Sus2', font=("Helvetica", 12), size=(8, 1), key='sus2Chord'),
             sg.Button('Sus4', font=("Helvetica", 12), size=(8, 1), key='sus4Chord')],
             [sg.Button('I', font=("Helvetica", 12), size=(8, 1), key='I'),
             sg.Button('ii', font=("Helvetica", 12), size=(8, 1), key='ii'), 
             sg.Button('iii', font=("Helvetica", 12), size=(8, 1), key='iii'), 
             sg.Button('IV', font=("Helvetica", 12), size=(8, 1), key='IV'),
             sg.Button('V', font=("Helvetica", 12), size=(10, 1), key='V'),
             sg.Button('vi', font=("Helvetica", 12), size=(8, 1), key='vi'),
             sg.Button('vii', font=("Helvetica", 12), size=(8, 1), key='vii'),
             sg.Button('O', font=("Helvetica", 12), size=(8, 1), key='OCT')],
             [sg.Text('_'*30)]
             
            ]


    # Open a form, note that context manager can't be used generally speaking for async forms
    return sg.Window('Jacobs Interval Trainer', layout, default_element_size=(20, 1), font=("Helvetica", 25), grab_anywhere=True)
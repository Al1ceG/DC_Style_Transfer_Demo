import PySimpleGUI as sg
import base64
import cv2
from cv2 import *

# use webcam
cap = cv2.VideoCapture(0)

# make it have colour
sg.theme('DarkAmber')  

# All the stuff inside your window
# put 3 photo buttons in the first row of the first column
column1 = [
    [
        sg.Button('',
            image_filename= "Great_wave.png",
            image_size=(0.5,0.5),
            button_color=(sg.theme_background_color(),sg.theme_background_color()),
            border_width=0,
            key='Exit'
        ),
        sg.Button('',
            image_filename="Starry_night.png",
            size=(0.5,0.5),
            button_color=(sg.theme_background_color(),sg.theme_background_color()),
            border_width=0,
            key='Exit'
        ),
         sg.Button('',
            image_filename="Marilyn.png",
            size=(0.5,0.5),
            button_color=(sg.theme_background_color(),sg.theme_background_color()),
            border_width=0,
            key='Exit'
        )
    ],
# put 3 photo buttons in the second row of the first column
     [
        sg.Button('',
            image_filename= "The_scream.png",
            image_size=(0.5,0.5),
            button_color=(sg.theme_background_color(),sg.theme_background_color()),
            border_width=0,
            key='Exit'
        ),
        sg.Button('',
            image_filename="Weeping_woman.png",
            size=(0.5,0.5),
            button_color=(sg.theme_background_color(),sg.theme_background_color()),
            border_width=0,
            key='Exit'
        ),
         sg.Button('',
            image_filename="Mona_lisa.png",
            size=(0.5,0.5),
            button_color=(sg.theme_background_color(),sg.theme_background_color()),
            border_width=0,
            key='Exit'
        )
    ]
]


column2 = [
    [sg.Image(filename="", key="image")],
    [   sg.Button('Back'),
        sg.Button('Confirm'),
        sg.Button('Capture')
    ]
]

layout = [
    [sg.Column(column1),
     sg.Column(column2),]
     ]

# Create the Window
window = sg.Window('Word2Vec Demo', layout, resizable = True)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read(timeout=20, timeout_key="timeout")
    window.find_element("image").Update(data=cv2.imencode(".png", cap.read()[1])[1].tobytes(), size=(600,700))
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == "Back":
        print("Back button pressed")
    if event == "Capture":
        ret, frame = cap.read()
        while(True):
            cv2.imshow('img1',frame) #display the captured image
            if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y' 
                cv2.imwrite('/Users/agraham/Desktop/Python_Scripts/image.png',frame)
                cv2.destroyAllWindows()
                break
            cap.release()
    if event == "Confirm":
        print ("Confirm button pressed")

window.close()




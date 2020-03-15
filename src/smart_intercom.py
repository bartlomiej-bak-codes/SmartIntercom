import cv2
import datetime
import time
import numpy as np
import pygame
import pickle
import copy
import os
import mysql.connector
from shutil import copyfile


def alert():
    pygame.mixer.init()
    pygame.mixer.music.load("noises/doorbell_sound.mp3")
    pygame.mixer.music.play()


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:

        global cam_status, show_who, keyboardString, keyboardWork, keyboardChar, show_list, wait_add, refresh

        if 640 <= y <= 703 and 20 <= x <= 188:  # cam
            if cam_status == 1:
                cam_status = 0
            elif cam_status == 0:
                cam_status = 1
        elif 265 <= y <= 328 and 255 <= x <= 423 and show_who == 1:  # cam2
            if cam_status == 1:
                cam_status = 0
            elif cam_status == 0:
                cam_status = 1
            show_who = 0
        elif 640 <= y <= 703 and 218 <= x <= 422:  # open gate
            global wait_notification
            wait_notification = 1
            pygame.mixer.init()
            pygame.mixer.music.load("noises/beep-07.wav")
            pygame.mixer.music.play()
        elif 640 <= y <= 703 and 452 <= x <= 694:  # take a photo
            global screenshot, keyboard, choose
            screenshot = 1
            choose = 1
        elif 640 <= y <= 703 and 724 <= x <= 924:  # statistics
            global stats_status
            if stats_status == 1:
                stats_status = 0
            elif stats_status == 0:
                stats_status = 1
        elif 640 <= y <= 703 and 954 <= x <= 1132:  # refresh
            os.system('python3 faces-train.py')
            refresh = 1
        elif 640 <= y <= 703 and 1162 <= x <= 1270:  # off
            with open("variable.pickle", "wb") as f:
                pickle.dump(name_of_photo, f)
            cap.release()
            out.release()
            cv2.destroyAllWindows()
            exit()
            os.system('python3 faces-train.py')

        if(show_list == 1):

            if 350 <= y <= 413 and 400 <= x <= 650:
                show_list = 0
            elif 175 <= y <= 210 and 716 <= x <= 950:
                print("1")
                show_list = 0
                print(name_of_photo[0]-1)
                copyfile("photos/" + str(name_of_photo[0]-1) + ".png",
                         "faces/" + files[0] + "/" + str(name_of_photo[0]-1) + ".png")
                wait_add = 1
            elif 211 <= y <= 250 and 716 <= x <= 950:
                print("2")
                show_list = 0
                copyfile("photos/" + str(name_of_photo[0]-1) + ".png",
                         "faces/" + files[1] + "/" + str(name_of_photo[0]-1) + ".png")
                wait_add = 1
            elif 251 <= y <= 290 and 716 <= x <= 950:
                print("3")
                show_list = 0
                copyfile("photos/" + str(name_of_photo[0]-1) + ".png",
                         "faces/" + files[2] + "/" + str(name_of_photo[0]-1) + ".png")
                wait_add = 1
            elif 291 <= y <= 330 and 716 <= x <= 950:
                print("4")
                show_list = 0
                copyfile("photos/" + str(name_of_photo[0]-1) + ".png",
                         "faces/" + files[3] + "/" + str(name_of_photo[0]-1) + ".png")
                wait_add = 1
            elif 331 <= y <= 370 and 716 <= x <= 950:
                print("5")
                show_list = 0
                copyfile("photos/" + str(name_of_photo[0]-1) + ".png",
                         "faces/" + files[4] + "/" + str(name_of_photo[0]-1) + ".png")
                wait_add = 1
            elif 371 <= y <= 410 and 716 <= x <= 950:
                print("6")
                show_list = 0
                copyfile("photos/" + str(name_of_photo[0]-1) + ".png",
                         "faces/" + files[4] + "/" + str(name_of_photo[0]-1) + ".png")
                wait_add = 1

        if(keyboard == 1):
            if 191 <= y <= 266 and 730 <= x <= 808:  # ADD
                print("1")
                keyboardString = keyboardString + keyboardChar
                keyboardWork = ""
                keyboardChar = ""
            elif 191 <= y <= 266 and 809 <= x <= 886:  # 2
                # print("2")
                keyboardWork = keyboardWork + '2'
                print(keyboardWork)
                keyboardChar = keyboardLogic(2, len(keyboardWork))
            elif 191 <= y <= 266 and 887 <= x <= 962:  # 3
                print("3")
                keyboardWork = keyboardWork + '3'
                print(keyboardWork)
                keyboardChar = keyboardLogic(3, len(keyboardWork))
            elif 267 <= y <= 344 and 730 <= x <= 808:  # 4
                print("4")
                keyboardWork = keyboardWork + '4'
                print(keyboardWork)
                keyboardChar = keyboardLogic(4, len(keyboardWork))
            elif 267 <= y <= 344 and 809 <= x <= 886:  # 5
                print("5")
                keyboardWork = keyboardWork + '5'
                print(keyboardWork)
                keyboardChar = keyboardLogic(5, len(keyboardWork))
            elif 267 <= y <= 344 and 887 <= x <= 962:  # 6
                print("6")
                keyboardWork = keyboardWork + '6'
                print(keyboardWork)
                keyboardChar = keyboardLogic(6, len(keyboardWork))
            elif 345 <= y <= 420 and 730 <= x <= 808:  # 7
                print("7")
                keyboardWork = keyboardWork + '7'
                print(keyboardWork)
                keyboardChar = keyboardLogic(7, len(keyboardWork))
            elif 345 <= y <= 420 and 809 <= x <= 886:  # 8
                print("8")
                keyboardWork = keyboardWork + '8'
                print(keyboardWork)
                keyboardChar = keyboardLogic(8, len(keyboardWork))
            elif 345 <= y <= 420 and 887 <= x <= 962:  # 9
                print("9")
                keyboardWork = keyboardWork + '9'
                print(keyboardWork)
                keyboardChar = keyboardLogic(9, len(keyboardWork))
            elif 191 <= y <= 266 and 650 <= x <= 715:  # DONE

                os.mkdir("faces/" + keyboardString)
                copyfile("photos/" + str(name_of_photo[0]-1) + ".png",
                         "faces/" + keyboardString + "/" + str(name_of_photo[0]-1) + ".png")
                keyboard = 0
                wait_add = 1
            elif 267 <= y <= 344 and 650 <= x <= 715:  # close
                keyboard = 0
                print("close")

        if(choose == 1):
            if 200 <= y <= 263 and 716 <= x <= 808:  # new
                choose = 0
                keyboard = 1
            elif 200 <= y <= 263 and 817 <= x <= 967:  # existing
                choose = 0
                show_list = 1
            elif 273 <= y <= 336 and 716 <= x <= 966:
                print("close")
                choose = 0


def keyboardLogic(key, length):

    if key == 2:
        if length % 3 == 1:
            return "a"
        if length % 3 == 2:
            return "b"
        if length % 3 == 0:
            return "c"
    if key == 3:
        if length % 3 == 1:
            return "d"
        if length % 3 == 2:
            return "e"
        if length % 3 == 0:
            return "f"
    if key == 4:
        if length % 3 == 1:
            return "g"
        if length % 3 == 2:
            return "h"
        if length % 3 == 0:
            return "i"
    if key == 5:
        if length % 3 == 1:
            return "j"
        if length % 3 == 2:
            return "k"
        if length % 3 == 0:
            return "l"
    if key == 6:
        if length % 3 == 1:
            return "m"
        if length % 3 == 2:
            return "n"
        if length % 3 == 0:
            return "o"
    if key == 8:
        if length % 3 == 1:
            return "t"
        if length % 3 == 2:
            return "u"
        if length % 3 == 0:
            return "v"

    if key == 7:
        if length % 4 == 1:
            return "p"
        if length % 4 == 2:
            return "q"
        if length % 4 == 3:
            return "r"
        if length % 4 == 0:
            return "s"
    if key == 9:
        if length % 4 == 1:
            return "w"
        if length % 4 == 2:
            return "x"
        if length % 4 == 3:
            return "y"
        if length % 4 == 0:
            return "z"


def click_event2(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global displayString

        if 348 <= y <= 370 and 59 <= x <= 86:  # 1 outdoor
            displayString = displayString + '1'
        if 348 <= y <= 370 and 100 <= x <= 128:  # 2 outdoor
            displayString = displayString + '2'
        if 348 <= y <= 370 and 142 <= x <= 169:  # 3 outdoor
            displayString = displayString + '3'
        if 390 <= y <= 412 and 59 <= x <= 86:  # 4 outdoor
            displayString = displayString + '4'
        if 390 <= y <= 412 and 100 <= x <= 128:  # 5 outdoor
            displayString = displayString + '5'
        if 390 <= y <= 412 and 142 <= x <= 169:  # 6 outdoor
            displayString = displayString + '6'
        if 431 <= y <= 453 and 59 <= x <= 86:  # 7 outdoor
            displayString = displayString + '7'
        if 431 <= y <= 453 and 100 <= x <= 128:  # 8 outdoor
            displayString = displayString + '8'
        if 431 <= y <= 453 and 142 <= x <= 169:  # 9 outdoor
            displayString = displayString + '9'
        if 472 <= y <= 495 and 59 <= x <= 86:  # * outdoor
            displayString = displayString + '*'
        if 472 <= y <= 495 and 100 <= x <= 128:  # 0 outdoor
            displayString = displayString + '0'
        if 472 <= y <= 495 and 142 <= x <= 169:  # outdoor
            displayString = displayString + '#'
        if 465 <= y <= 495 and 192 <= x <= 227:  # bell outdoor
            alert()
        display_work(len(displayString))


def display_work(length):
    global displayString, switch
    if length == 1:
        putOnDisplay(outDoor, 220, 304, 54, 214, 'images/*.png')
        switch = 1
    elif length == 2:
        putOnDisplay(outDoor, 220, 304, 54, 214, 'images/**.png')
    elif length == 3:
        putOnDisplay(outDoor, 220, 304, 54, 214, 'images/***.png')
    elif length == 4:
        if displayString == "1234":
            putOnDisplay(outDoor, 220, 304, 54, 214, 'images/goodpass.png')
            global wait_notification
            wait_notification = 1
            if (switch == 1):
                pygame.mixer.init()
                pygame.mixer.music.load("noises/beep-07.wav")
                pygame.mixer.music.play()
                switch = 0
            if wait_seconds2(3) == True:
                name_of_photo[2] = name_of_photo[2] + 1
                displayString = displayString + '#'

        else:
            putOnDisplay(outDoor, 220, 304, 54, 214, 'images/badpass.png')
            if wait_seconds2(3) == True:
                name_of_photo[3] = name_of_photo[3] + 1
                displayString = displayString + '#'
    elif length == 5:
        displayString = ''


def notification():
    putOnDisplay(frame, 50, 113, 800, 1116, 'images/not1.png')
    if wait_seconds3(3) == True:
        global wait_notification
        wait_notification = 0


def putOnDisplay(frame, fheight, sheight, fwidth,
                 swidth, src):
    img = cv2.imread(src)
    frame[fheight: sheight, fwidth: swidth] = img


def putTimeOnDisplay(frame):
    font = cv2.FONT_HERSHEY_SIMPLEX
    actual_time = str(
        datetime.datetime.now().strftime("%b %d %Y %H:%M:%S"))
    cv2.putText(frame, actual_time, (10, 50),
                font, 1, (255, 255, 255), 2, cv2.LINE_AA)


def wait_seconds(time, temp):

    if temp == None:
        temp = datetime.datetime.now()
    else:
        live_time = datetime.datetime.now()
        time_to_expire = datetime.timedelta(0, time)
        if (live_time - temp) < time_to_expire:
            live_time = datetime.datetime.now()
        else:
            temp = None
            return True


def wait_seconds1(time):
    global temp1
    if temp1 == None:
        temp1 = datetime.datetime.now()
    else:
        live_time = datetime.datetime.now()
        time_to_expire = datetime.timedelta(0, time)
        if (live_time - temp1) < time_to_expire:
            live_time = datetime.datetime.now()
        else:
            temp1 = None
            return True


def wait_seconds2(time):
    global temp2
    if temp2 == None:
        temp2 = datetime.datetime.now()
    else:
        live_time = datetime.datetime.now()
        time_to_expire = datetime.timedelta(0, time)
        if (live_time - temp2) < time_to_expire:
            live_time = datetime.datetime.now()
        else:
            temp2 = None
            return True


def wait_seconds3(time):
    global temp3
    if temp3 == None:
        temp3 = datetime.datetime.now()
    else:
        live_time = datetime.datetime.now()
        time_to_expire = datetime.timedelta(0, time)
        if (live_time - temp3) < time_to_expire:
            live_time = datetime.datetime.now()
        else:
            temp3 = None
            return True


def wait_seconds4(time):
    global temp4
    if temp4 == None:
        temp4 = datetime.datetime.now()
    else:
        live_time = datetime.datetime.now()
        time_to_expire = datetime.timedelta(0, time)
        if (live_time - temp4) < time_to_expire:
            live_time = datetime.datetime.now()
        else:
            temp4 = None
            return True


def wait_seconds5(time):
    global temp5
    if temp5 == None:
        temp5 = datetime.datetime.now()
    else:
        live_time = datetime.datetime.now()
        time_to_expire = datetime.timedelta(0, time)
        if (live_time - temp5) < time_to_expire:
            live_time = datetime.datetime.now()
        else:
            temp5 = None
            return True


def wait_seconds6(time):
    global temp6
    if temp6 == None:
        temp6 = datetime.datetime.now()
    else:
        live_time = datetime.datetime.now()
        time_to_expire = datetime.timedelta(0, time)
        if (live_time - temp6) < time_to_expire:
            live_time = datetime.datetime.now()
        else:
            temp6 = None
            return True


def most_frequent(List):
    return max(set(List), key=List.count)


def putStatsOnDisplay():
    font = cv2.FONT_HERSHEY_SIMPLEX
    putOnDisplay(frame, 68, 358, 400, 1188, "images/background_stats.png")
    cv2.putText(frame, "Good passwrods:"+str(name_of_photo[2]), (430, 100),
                font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "Bad passwords:"+str(name_of_photo[3]), (430, 140),
                font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    mycursor.execute(
        "SELECT * FROM Smart_intercom.visitorsv2 WHERE date = (SELECT MAX(date) FROM Smart_intercom.visitorsv2);")

    myresult = mycursor.fetchone()

    name = myresult[0]
    date = str(myresult[1])
    cv2.putText(frame, "Last visit: " + name + " at: " + date, (430, 180),
                font, 1, (255, 255, 255), 2, cv2.LINE_AA)

    mycursor.execute(
        "SELECT name, COUNT(name) FROM Smart_intercom.visitorsv2 GROUP BY name ORDER BY COUNT(name) DESC LIMIT 3;")

    myresult = mycursor.fetchall()

    top1 = [myresult[0][0], str(myresult[0][1])]
    top2 = [myresult[1][0], str(myresult[1][1])]
    top3 = [myresult[2][0], str(myresult[2][1])]

    cv2.putText(frame, "Top visitors:", (430, 220),
                font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "1. " + top1[0] + " ( " + top1[1] + " )", (460, 260),
                font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "2. " + top2[0] + " ( " + top2[1] + " )", (460, 300),
                font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "3. " + top3[0] + " ( " + top3[1] + " )", (460, 340),
                font, 1, (255, 255, 255), 2, cv2.LINE_AA)


# Declaration
global displayString, wait_notification, wait_add, temp1, temp2, temp3, temp4, switch, temp5, temp6, refresh, name_of_photo, stats_status, screenshot, cam_status, show_who, is_recording, show_list, choose,  keyboard, keyboardChar, keyboardString, keyboardWork
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="rootpasswordgiven",
    database="Smart_intercom"
)

mycursor = mydb.cursor()
path = str(os.path.dirname(os.path.realpath(__file__)))+"/recordings"
displayString = ""
keyboardString = ""
keyboardWork = ""
keyboardChar = ""
temp1 = None
temp2 = None
temp3 = None
temp4 = None
temp5 = None
temp6 = None
wait_notification = 0
switch = 0
wait_add = 0
cam_status = 0
stats_status = 0
count = 0
show_who = 0
is_recording = 0
screenshot = 0
keyboard = 0
choose = 0
show_list = 0
List = []
out = None
refresh = 1
attempt = 15

font = cv2.FONT_HERSHEY_SIMPLEX

# Wyczytywanie zmiennych z pliku

with open("variable.pickle", "rb") as f:
    name_of_photo = pickle.load(f)

# Ustawianie parametrów kamery

cap = cv2.VideoCapture(0)

cap.set(3, 1280)
cap.set(4, 720)
ret, frame1 = cap.read()
ret, frame2 = cap.read()

while True:

    if(refresh == 1):

        # Wczytywanie listy osób które znajdują się w bazie

        labels = {}
        with open("labels.pickle", "rb") as f:
            og_labels = pickle.load(f)
            labels = {v: k for k, v in og_labels.items()}

        # Wczytanie danych związanych z rozpoznawaniem twarzy

        face_cascade = cv2.CascadeClassifier(
            'cascades/data/haarcascade_frontalface_alt2.xml')
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read("trainner.yml")
        refresh = 0

    # Utworzenie frame

    ret, frame = cap.read()

    # Wykrywanie ruchu

    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(
        dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:

        if cv2.contourArea(contour) < 20000:
            continue

        # aktualizacja czasu nagrywania (nagrywa do 20 sec po ostatnim wykryciu ruchu)
        
        temp4 = datetime.datetime.now()
        if is_recording == 0:

            # Rozpoczynanie nagrywania po wykryciu ruchu

            is_recording = 1
            cur_time = datetime.datetime.now().strftime("%b %d %Y %H:%M:%S")

            four_cc = cv2.VideoWriter_fourcc(*'XVID')
            out = cv2.VideoWriter(
                'recordings/'+str(cur_time)+"-"+str(name_of_photo[1])+'.avi', four_cc, 10.0, (1280, 720))

            name_of_photo[1] = name_of_photo[1] + 1

            # Usuwanie dawnych nagrań z monitoringu

            for root, dirs, files in os.walk(path):
                for file in files:

                    if file.endswith(str(name_of_photo[1]-12)+'.avi'):
                        to_remove = str(file)

                        os.remove("recordings/" + to_remove)

    frame1 = frame2
    ret, frame2 = cap.read()

    # Robienie zdjęć

    if screenshot == 1:
        if name_of_photo[0] >= 1000:
            name_of_photo[0] = 1
        img_item = "photos/" + str(name_of_photo[0]) + ".png"
        print("Robie zdjecie nr: " + str(name_of_photo[0]))
        cv2.imwrite(img_item, frame)
        name_of_photo[0] = name_of_photo[0] + 1

        screenshot = 0

    # Zapisywanie nagrania i umieszczenie na nim czasu

    if is_recording == 1:
        putTimeOnDisplay(frame)
        out.write(frame)

    # Rozpoznawania twarzy

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.5, minNeighbors=5)

    if len(List) < attempt:

        for (x, y, w, h) in faces:

            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y + h, x:x + w]
            id_, conf = recognizer.predict(roi_gray)

            if conf >= 1:
                print("rozpoznano:" + labels[id_])
                count = count + 1
                List.append(labels[id_])

    # Wyłączenie widoku kamery w podglądzie

    putOnDisplay(frame, 620, 720, 0, 1280, 'images/menu.png')
    if cam_status == 0:
        putOnDisplay(frame, 0, 720, 0, 1280, "images/black.png")
        actual_time = str(
            datetime.datetime.now().strftime("%H:%M:%S"))
        cv2.putText(frame, actual_time, (700, 100),
                    font, 2, (255, 255, 255), 1, cv2.LINE_AA)

    # Powiadomienie o rozpoznaniu osoby

    if len(List) > 0 and len(List) < attempt:
        print("lista: " + str(len(List)))
        if wait_seconds6(30) == True:
            List = []

    if len(List) >= attempt:
        font = cv2.FONT_HERSHEY_SIMPLEX
        putOnDisplay(frame, 120, 255, 60, 430, "images/is_coming.png")
        cv2.putText(frame, most_frequent(List), (80, 170),
                    font, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, "is coming!", (250, 225),
                    font, 1, (255, 255, 255), 2, cv2.LINE_AA)

        putOnDisplay(frame, 265, 328, 255, 423, 'images/camera.png')
        show_who = 1

        if wait_seconds1(10) == True:
            statistic_time = datetime.datetime.now().strftime("%b %d %Y %H:%M:%S")
            person = "'"+str(most_frequent(List))+"'"
            sql = 'INSERT INTO Smart_intercom.visitorsv2 (name) VALUE (' + \
                person+');'
            mycursor.execute(sql)
            mydb.commit()

            List = []

    outDoor = cv2.imread('images/outDoorPanel.png')

    # Powiadomienie o wykryciu ruchu

    if is_recording == 1:
        putOnDisplay(outDoor, 151, 198, 161, 224, "images/led_on.png")
        time_to_flashes = int(datetime.datetime.now().strftime("%S"))
        if time_to_flashes % 2 == 1:

            cv2.putText(frame, "motion detected", (500, 500),
                        font, 1, (255, 255, 255), 2, cv2.LINE_AA)

        if wait_seconds4(5) == True:
            is_recording = 0

    # Wybór podczas robienia zdjecia

    if(choose == 1):
        putOnDisplay(frame, 200, 263, 716, 808, 'images/new.png')
        putOnDisplay(frame, 200, 263, 817, 967, 'images/existing.png')
        putOnDisplay(frame, 273, 336, 716, 966, 'images/cancel.png')

    # Lista osob w bazie

    if(wait_add == 1):
        putOnDisplay(frame, 200, 263, 700, 878, 'images/success.png')
        if wait_seconds5(3) == True:
            wait_add = 0

    if(show_list == 1):

        putOnDisplay(frame, 130, 513, 350, 1002,
                        'images/background_list_persons.png')
        putOnDisplay(frame, 350, 413, 400, 650, 'images/cancel.png')
        cv2.putText(frame, "Who is this?", (400, 220),
                    font, 1, (255, 255, 255), 2, cv2.LINE_AA)
        poz = 0
        files = os.listdir(
            str(os.path.dirname(os.path.realpath(__file__)))+"/faces")

        for name in files:
            cv2.putText(frame, name, (716, 200 + poz*40),
                        font, 1, (255, 255, 255), 2, cv2.LINE_AA)
            poz = poz + 1

    # Klawiatura

    if keyboard == 1:
        putOnDisplay(frame, 110, 430, 650, 970, 'images/keyboard.png')
        cv2.putText(frame, keyboardString, (720, 170),
                    font, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, keyboardChar, (720, 140),
                    font, 1, (255, 255, 255), 2, cv2.LINE_AA)

    # Umieszczenie więkości interfejsu

    putOnDisplay(frame, 640, 640 + 63, 20, 188, 'images/camera.png')
    putOnDisplay(frame, 640, 640 + 63, 218, 422, 'images/open_gate.png')
    putOnDisplay(frame, 640, 640 + 63, 452, 694, 'images/take_a_photo.png')
    putOnDisplay(frame, 640, 640 + 63, 724, 924, 'images/statistics.png')
    putOnDisplay(frame, 640, 640 + 63, 954, 1132, 'images/refresh.png')
    putOnDisplay(frame, 640, 640 + 63, 1162, 1270, 'images/off.png')

    if wait_notification == 1:
        notification()

    if stats_status == 1:
        putStatsOnDisplay()

    # Funkcja odpowiedzialna za działanie klawiatury domofonu

    display_work(len(displayString))

    # Otwarcie okien

    cv2.imshow('outDoor', outDoor)
    cv2.imshow('frame', frame)

    # Obsługa inputu interfejsu

    cv2.setMouseCallback('frame', click_event)
    cv2.setMouseCallback('outDoor', click_event2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Zapisywanie zmiennych do pliku

with open("variable.pickle", "wb") as f:
    pickle.dump(name_of_photo, f)

if(out != None):
    out.release()

cap.release()
cv2.destroyAllWindows()

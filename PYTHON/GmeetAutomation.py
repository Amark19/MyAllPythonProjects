import pyautogui as gui
import time as t
import speech_recognition as sr
import playsound
print(gui.size())

tick=t.time()
r=sr.Recognizer()
# text=""
# while 1:
#     if (int((t.time()-tick))==5):
#         print("hi")
#         break
while (int((t.time()-tick))!=10):
    with sr.Microphone() as source:
        print("speak anything") 
        audio=r.listen(source)
        try:
            text=r.recognize_google(audio)
            # print("u said:{}".format(text))
        # print(text)
            subtext="Amar"
            if subtext in "{}".format(text):

                print("u said:{}".format(text))
                t.sleep(2)
                gui.moveTo(400,700,duration=1)
                gui.click()
                print("sorry mam actually by mistakley i off my mic")
                break
        except:
            print("its her problem")




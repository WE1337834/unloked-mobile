import uiautomator2 as u2
from deviceID import deviceID
device = deviceID()

def Password():
    global symbol_pass
    symbol_pass = []
    password = input("Введите пароль: ")
    symbol_pass += list(map(str, *f"{password}".split(" ")))

def unlock_mobile(symbol_pass):
    d = u2.connect(device)
    d.app_current()     
    d.swipe_ext("up")
    d.sleep(1)
    for i in range(0,len(symbol_pass)):
        d(text=symbol_pass[i]).click()
Password()
unlock_mobile(symbol_pass)
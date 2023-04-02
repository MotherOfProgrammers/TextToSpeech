#!/usr/env/bin python
# Made By MOP Mother Of Programmers (MOP)
import os 
import sys
import colorama
from colorama import Fore, Back, Style
colorama.init()

def systemvc(name): 
    from gtts import gTTS
    import os 
    import sys
    import colorama
    from colorama import Fore, Back, Style
    colorama.init()
    import datetime
    import time
    import http
    import urllib3
    
    
    os.system('cls') # For Clear The Errors
    
    print(f"[~]Log in Successful {name}!")
    print(Fore.CYAN + "[=] SPCH FROM PYTHON")  
    print(Fore.MAGENTA + """
	    ===================
	    = Created By MOP =
	    ===================""")
    myt_req = str(input(f"{Fore.YELLOW}[+]Enter Your Text To Convert As A Speech:{Fore.BLUE} "))
    myt_s_req = str(input(f"{Fore.YELLOW}[+]Enter Any Name To Add To The File's Name(.mp3)(Only Enter The Name,Don't Enter The Type):{Fore.BLUE} "))
    myt_s_req = myt_s_req + ".mp3"
    print(f"{Fore.GREEN}[*]Your Request Is Processing")
    time.sleep(2)
    mytext = myt_req
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=True)  
    test_file =  input(f"{Fore.LIGHTBLUE_EX}[#]Do you wanna check the file(Y/N):{Fore.CYAN} ")
    test_file = test_file.upper()
    if test_file == "Y":
        myobj.save(f"{myt_s_req}") 
        os.system(f"start {myt_s_req}") 
        print(f"[*]Job Done {name}!")
        os.system('exit')
    else:
        print(f"[*]job Done {name}!")
        os.system('exit')

name = input("[=] Enter your name: ")
name = name.title()
passwd = int(input("[=] Enter the password: "))
if passwd == 4455:
	systemvc(name)
else:
	print("[-] Access Deneid!")
	

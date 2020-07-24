import webbrowser as wb
import os
from datetime import datetime as dt
from time import sleep
import utils.functions as f


if __name__ == "__main__":
    name = input("Enter your name: ")
    person = f.AI(name)
    person.wish_me()
    while 1:
        command = f.input_command().lower()
        # wb.get("google-chrome")
        if "open youtube" in command:
            wb.open("youtube.com")
        
        elif "open google" in command:
            wb.open("google.com")

        elif "open stack overflow" in command:
            wb.open("stackoverflow.com")

        elif "open instagram" in command:
            wb.open("instagram.com")

        elif "wikipedia" in command:
            f.search_wikipedia(command)

        elif "what's the time" in command:
            str_time = dt.now().strftime("%H:%M:%S")
            print(f"{name} the time is {str_time}")
            f.speak(f"{name} the time is {str_time}")

        elif "open visual studio code" in command:
            path = "C:\\Users\\ADMIN\\AppData\\Local\\Programs\\Microsoft VS Code1\\Code.exe"
            os.startfile(path)
        elif "send this mail" in command:
            
            try:
               
                person.send_mail()
                f.speak(f"{name}, email was send successfully")
                
            except Exception as e:
                print(e)
                f.speak(e)
                f.speak("Can't send this mail")



        elif 'bye' in command:    
            f.speak(f"Good bye {name}") 
            exit()

        else:
            f.speak(f"{name} Don't know what to do")    

        sleep(10) 
          



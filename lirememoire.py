import pyperclip
import time

'''
liste = []

while True:
    if pyperclip.paste() != 'None':
        value = pyperclip.paste()
        if value not in liste:
            liste.append(value)
        print(liste)
        time.sleep(3)




'''
'''
liste = []

while True:
    if pyperclip.paste() != 'None':
        value = pyperclip.paste()
        if value not in liste:
            liste.append(value)
        
        file = open("save.txt", "w")    
        file.write("-".join(liste))
        file.close()
        time.sleep(3)

'''

        
liste = []
copies = []

while True:
         
    if pyperclip.paste() != 'None':
        value = pyperclip.paste()
        if value not in copies:
            copies.append(value)
            temps = time.strftime("%H:%I:%S")
            valueheure = "heure {} - Copie de '{}'"
            valueheure = valueheure.format(temps, value)
            liste.append(valueheure)
        file = open("save.txt", "a+")    
        file.write("\n".join(liste))
        file.close()
        time.sleep(2)
        
            
            
        
          
        

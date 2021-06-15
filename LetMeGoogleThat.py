import pyperclip as pc
import webbrowser
import time
lmgt = input("Input the Let Me Google That Phrase: \n")
lmgt.replace("", "+")
link = ('https://letmegooglethat.com/?q=' + lmgt)
ask = input("Would you like to open the Let Me Google That link?[Y/N]: ")
if ask.lower() in ['yes', 'y']:
    webbrowser.open(link)
    print("Link has been opened...")
    time.sleep(2)
    print("Closing this window...")
    exit()
elif ask.lower() in ['no', 'n']:
    pc.copy(link)
    print("Link has been copied...")
    time.sleep(2)
    print("Closing window in 5 seconds...")
    time.sleep(5)
    exit('easy')
else:
    print("That's not a valid statment!")

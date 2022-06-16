import random
import os
import time
import sys
os.system("clear")
print("""⠄⠄⠄⢰⣧⣼⣯⠄⣸⣠⣶⣶⣦⣾⠄⠄⠄⠄⡀⠄⢀⣿⣿⠄⠄⠄⢸⡇⠄⠄
⠄⠄⠄⣾⣿⠿⠿⠶⠿⢿⣿⣿⣿⣿⣦⣤⣄⢀⡅⢠⣾⣛⡉⠄⠄⠄⠸⢀⣿⠄
⠄⠄⢀⡋⣡⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤⣄⣀⣥⣿⣿⠄
⠄⠄⢸⣇⠻⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿⣿⠄
⠄⢀⢸⣿⣷⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄⢀⣤⣄⠉⠋⣰
⠄⣼⣖⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶⢿⣿⣿⠇⢀⣤
⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣶⣥⣴⣿⡗
⢀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠄
⢸⣿⣦⣌⣛⣻⣿⣿⣧⠙⠛⠛⡭⠅⠒⠦⠭⣭⡻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄
⠘⣿⣿⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄⠹⠈⢋⣽⣿⣿⣿⣿⣵⣾⠃⠄
⠄⠘⣿⣿⣿⣿⣿⣿⣿⣿⠄⣴⣿⣶⣄⠄⣴⣶⠄⢀⣾⣿⣿⣿⣿⣿⣿⠃⠄⠄
⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⠄⣿⣿⡀⣾⣿⣿⣿⣿⣛⠛⠁⠄⠄⠄
⠄⠄⠄⠄⠈⠛⢿⣿⣿⣿⠁⠞⢿⣿⣿⡄⢿⣿⡇⣸⣿⣿⠿⠛⠁⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠉⠻⣿⣿⣾⣦⡙⠻⣷⣾⣿⠃⠿⠋⠁⠄⠄⠄⠄⠄⢀⣠⣴
⣿⣿⣿⣶⣶⣮⣥⣒⠲⢮⣝⡿⣿⣿⡆⣿⡿⠃⠄⠄⠄⠄⠄⠄⠄⣠⣴⣿⣿⣿""")
print("------------------[#LITTLESISTER]-------------------")
time.sleep(1)
print("\033[1;32;40mAuthor: Jixxie")
print("\033[1;32;40m[✓]WELCOME[✓]")
print("\033[1;35;40m V2 coming soon")
time.sleep(1)
print("\033[1;35;40m[1] ip-tracker                [5] Zphisher                    [9] Termux-Style")
print("\033[1;35;40m[2] T-BOMB                    [6] Sherlock                   [10] Termux Cyber Army ")
print("\033[1;35;40m[3] Little Brother            [7] Black Mafia")
print("\033[1;35;40m[4] brutecam                  [8] Anon Sms")
Scelta = input("\033[1;31;40mLittle-Sister>  ")
  

  
if int(Scelta) == 1:
 os.system("""
apt update

apt install git -y

git clone https://github.com/rajkumardusad/IP-Tracer.git

cd IP-Tracer

chmod +x install

sh install""")
	
	
	
	
elif int(Scelta) == 2:
    os.system("""
    pkg install git -y 
pkg install python -y 
git clone https://github.com/TheSpeedX/TBomb.git
cd TBomb
./TBomb.sh""")



elif int(Scelta) == 3:
	os.system("""
	apt update && apt upgrade
pkg install git python3
git clone https://github.com/AbirHasan2005/LittleBrother
cd LittleBrother
pip3 install -r requirements.txt
python3 littlebrother.py""")




elif int(Scelta) == 4:
     os.system("""
git clone https://github.com/ParzivalHack/BruteCam
cd BruteCam
Python brutecam.py""")


elif int(Scelta) == 5:
	os.system("""
	git clone https://github.com/htr-tech/zphisher.git
	cd zphisher
   bash zphisher.sh""")
	
	
	
	
elif int(Scelta) == 6:
	os.system("""
git clone https://github.com/sherlock-project/sherlock.git
cd sherlock
python3 -m pip install -r requirements.txt
python3 sherlock --help""")
	


elif int(Scelta) == 7:
     os.system("""
apt update
apt upgrade -y
apt install git -y
pkg install python
pkg install python2 -y
pip2 install requests
pip2 install mechanize
apt install ruby -y && gem install lolcat
git clone https://github.com/lovehacker404/BlackMafiaTool
cd BlackMafiaTool
python2 lovehacker.py""")


elif int(Scelta) == 8:
      os.system("""
      pkg install git
pkg install python
git clone https://github.com/HACK3RY2J/Anon-SMS.git
cd Anon-SMS
bash Run.sh""")



elif int(Scelta) == 9:
      os.system("""
      git clone https://github.com/adi1090x/termux-style
      cd termux-style
  ./install""")
  
  
elif int(Scelta) == 10:
      os.system("""
apt update && apt upgrade
apt install git
git clone https://github.com/Err0r-ICA/TermuxCyberArmy
cd TermuxCyberArmy
python2 TCA""")




else:
        print('this choice does not exist')
        print("Little Sister love you ^~^")

clear
mkdir Tools
clear 
echo -e '\033[31;40;1m 

░█████╗░████████╗███████╗
██╔══██╗╚══██╔══╝██╔════╝
██║░░╚═╝░░░██║░░░█████╗░░
██║░░██╗░░░██║░░░██╔══╝░░
╚█████╔╝░░░██║░░░██║░░░░░
░╚════╝░░░░╚═╝░░░╚═╝░░░░░
 v001



\033[33;4mVersion:\033[0m (⊙ˍ⊙)            \033[33;4mCTRL+C:\033[0m exit          \033[33;4mAuthor:\033[0m NONO_055

\e[37m[1]\e[36m update       \e[37m[2]\e[36m nmap				
\e[37m[3]\e[36m dirb                  \e[37m[4]\e[36m xss			
\e[37m[5]\e[36m sub		  		\e[37m[6]\e[36m openvpn
\e[37m[7]\e[36m Whois_lookup
'


#bara chaiet


read -p ": " islem
if [[ $islem == 1 || $islem == 01 ]]; then
clear

echo -e ".......    "
echo wait 
sleep 5
pkg install git -y
pkg install python python3 -y
pkg install pip pip3 -y
pkg install curl -y
apt update
apt upgrade -y
clear
echo -e "fully updated..."
sleep 3
bash ctf.sh

elif [[ $islem == 2 || $islem == 02 ]]; then
clear
echo -e "installation may take some time plz wait"
sudo apt install nmap -y 
read -p "enter ip add to scan" ip
nmap "$ip" -sC -sV -o scanoutput.txt
cat scanoutput.txt
elif [[ $islem == 3 || $islem == 03 ]]; then
clear
echo -e "installation may take some time plz wait"
sleep 3
sudo apt install dirb -y
read -p "url: " url
dirb "$url" > dirboutput.txt
echo "plz wait"
cat dirboutput.txt
elif [[ $islem == 4 || $islem == 04 ]]; then
clear
echo -e "installation may take some time plz wait"
sleep 3
cd Tools
git clone https://github.com/s0md3v/XSStrike
cd XSStrike
pip install -r requirements.txt --break-system-packages
read -p "url with search query test: " url
python3 xsstrike.py -u "$url" > xssoutput.txt
cat xssoutput.txt
elif [[ $islem == 5 || $islem == 05 ]]; then
clear
echo 'using gobuster plz wait for installing'
sudo apt install gobuster -y
read -p "url : " url
read -p "directory of wordlist : " wordlist
gobuster dns -d "$url" -w "$wordlist" -o gobuster-scan.txt
cat gobuster-scan.txt
elif [[ $islem == 6 || $islem == 06 ]]; then
clear
python3 openvpn-connect.py
clear
elif [[ $islem == 7 || $islem == 07 ]]; then
clear
pip3 install python-whois
python3 domain_lookup.py

else
    echo -e "Option not recognized... (⊙_☉) Try again!"
fi

# emailspoof
email spoofer By 3LF3NIX
## Installation:
```bash
sudo apt install sendemail git
git clone https://github.com/3LF3NIX/emailspoof.git
cd emailspoof
chmod +x emailspoofgrafic.py launch.sh
pip install -r requirements.txt
```
## Usage:
Create a account in the web [www.sendinblue.com](https://www.sendinblue.com)

Then go to the top right click on your user choose the STMP and API menu generate an api key put the name you want, then give it to SMTP and copy your master key.

Put the email of your sendingblue acount and your master key in this part of the code.
```python
def send_email():
    username = "HERE" # <--------- Put your sendinblue email HERE
    password = "HERE" # <--------- Put your sendinblue master key HERE
```

Run the tool
```bash
./launch.sh
```

![tool](https://github.com/3LF3NIX/emailspoof/blob/main/toolrunning.png)

to stop the tool do Ctrl + C in the terminal and close window the browser tab.

If the tool not stop execute this command
```bash
sudo killall python
```

## LEGAL NOTICE
I am not responsible for the use that is given to this tool.

## mentions
This tool is inspired by my friend zereza's here is the link to her github repository [zereza's repository](https://github.com/0x9B0x7A/zspoofer).

## little message
thank you i love you:)

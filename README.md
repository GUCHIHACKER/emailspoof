# emailspoof
email spoofer By 3LF3NIX
## Installation:
```bash
sudo apt install sendemail
git clone https://github.com/3LF3NIX/emailspoof.git
cd emailspoof
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

from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send_email():
    username = "HERE" # <--------- Put your sendinblue email HERE
    password = "HERE" # <--------- Put your sendinblue master password HERE
    target = request.form['target']
    name = request.form['name']
    sender = request.form['sender']
    subject = request.form['subject']
    message = request.form['message']

    if name == '':
        os.system('sendemail -xu \"'+username+'\" -xp \"'+password+'\" -f \"'+sender+'\" -t \"'+target+'\" -u \"'+subject+'\" -m \"'+message+'\" -s "smtp-relay.sendinblue.com:587" &>/dev/null')
    else:
        os.system('sendemail -xu \"'+username+'\" -xp \"'+password+'\" -f \"'+sender+'\" -t \"'+target+'\" -u \"'+subject+'\" -m \"'+message+'\" -s "smtp-relay.sendinblue.com:587" -o message-header="From: '+name+' <'+sender+'>" &>/dev/null')
    return render_template('sent.html')

if __name__ == '__main__':
    app.run()

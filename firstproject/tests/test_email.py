#!/usr/bin/python
# -*- coding: UTF-8 -*-

from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config.update(

      #EMAIL SETTINGS

     MAIL_SERVER='smtp.qq.com',

     MAIL_PORT=465,

     MAIL_USE_SSL=True,

    MAIL_USERNAME='2681590688',

     MAIL_PASSWORD='lvvosyrqcmgreaii'
)


mail = Mail(app)

@app.route("/")
def index():

     msg = Message(subject="helloworld", sender='2681590688@qq.com', recipients=['904159574@qq.com'])

     msg.html = "testinghtml"

     mail.send(msg)



if __name__ == '__main__':
    app.run(debug=True)
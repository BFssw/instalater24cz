from flask import Flask,request
import os
import telebot
import codecs
import secrets
app = Flask(__name__)
import subprocess
tb = telebot.TeleBot("5306701764:AAEYRWHeiLllJHVYbgi6fRFRMEUUQ5_8q9o")


@app.route('/bot-tg-photo/test',methods=['GET','POST'])
def test():
    return f"OK"

@app.route('/bot-tg-photo',methods=['GET','POST'])
def head():
    js = request.get_json()
    def dw_cn_ms(pth):
        h=tb.download_file(pth)
        name=secrets.token_urlsafe(10)
        f=codecs.open(f"{name}.{pth.split('.')[-1]}",'wb')
        f.write(h)
        f.close()
        subprocess.run(f"cwebp {name}.{pth.split('.')[-1]} -o {name}.webp",shell=True)
        tb.send_message(js['message']['chat']['id'],f"https://raw.githubusercontent.com/BFssw/instalater24cz/main/tg/{name}.webp")
    try:
        if js['message']['text'] == '/start' or js['message']['text'] == '/status':
            tb.send_message(js['message']['chat']['id'],f"{js['message']['chat']['id']} - work")
    except:
        pass
    if 'document' in js['message']:
        dw_cn_ms(tb.get_file(js['message']['document']['file_id']).file_path)
    elif 'photo' in js['message']:
        dw_cn_ms(tb.get_file(js['message']['photo'][-1]['file_id']).file_path)
    return "OK"

if __name__ == '__main__':
    server_port = os.environ.get('PORT', '5959')
    app.run(debug=True,port=server_port, host='0.0.0.0')

#!/usr/bin/env python
import time
import itchat

def login():
    itchat.send('wxbot ', toUserName='filehelper')
    print('wxbot login')
def logout():
    print('wxbot logout')
def qrcode(qrcode, uuid, status):
    with open('/home/wxpy/qr.png', 'wb') as f:
        f.write(qrcode)
    print(status)
    print(uuid)

itchat.auto_login(
    hotReload=True,
    loginCallback=login,
    exitCallback=logout,
    qrCallback=qrcode)
itchat.run()
# itchat.logout()
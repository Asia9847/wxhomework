import itchat
itchat.auto_login(hotReload=True)
def sendMsg(msg):
    itchat.send(msg, 'filehelper')
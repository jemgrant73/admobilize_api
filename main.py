import datetime
import textfile as tf
import apistuff as api
import json
import emailpy as mail

# create log
today = datetime.datetime.today().strftime("%m-%d-%Y")
time = datetime.datetime.now().strftime("%H:%M:%S")
tf.createLogFile(today)

# get ini settings
user = tf.getConnection('admuser').rstrip('\n')
pw = tf.getConnection('admpw').rstrip('\n')

tf.writeToLog(today, time +  ' DEVICE STATUS LIST\n')
# ADMOBILIZE API Access
#     Step 1 Get access Token
accessToken = api.getAccessToken(user, pw)
#     Step 2 get device status by project id
response = api.getDeviceInfo(accessToken)
#print(response.text)    #just for debugging
#    Step 3  build list of device status
devices = json.loads(response.text)
print(devices)
deviceStatus = {}
plainText = ''
htmlBody = ''

for device in devices['devices']:
    archived = device['archived']
    deviceName = device['displayName']
    state = device['state']['status']

    if archived == False:
        deviceStatus.update({deviceName : state})
        tf.writeToLog(today, deviceName + ' is ' + state + '\n')

    #set up mail -plain text
    if (archived == False) and (state == 'offline'):
        plainText = plainText + (deviceName + ' is ' + state + '\n')
        htmlBody = htmlBody + (deviceName + ' is ' + state + '<br>')
for x,y in deviceStatus.items():
    print(x,y)

#send mails
htmlText = '<html><body><p>' + htmlBody + '</p></html></body>'
mail.sendMail(plainText, htmlText)



















##mailing
## get the ini settings
# mailto = []
# mailto = (tf.getSetting('mail_to=').rstrip('\n')).split(',')
# path_to_attachment = (tf.getSetting('attachment_path=').rstrip('\n'))
# #check if mails must be sent
# sendFlag = tf.getSetting('send_mail').rstrip('\n')
# if sendFlag == '1':
#    for x in mailto:
#        subject = 'XXXXXXXXXXXXXXXXXXX'
#        body = 'Hi There,\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\nYou know what to do.\nRegards,\nR3P0RT5RV'
#        pm.send_email(x, subject, body, today, path_to_attachment)
# else:
#     tf.writeToLog(today, str(datetime.datetime.now()) + ' - Send mails flag is off\n')

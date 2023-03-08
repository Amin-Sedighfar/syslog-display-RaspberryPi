import requests
from RPLCD import CharLCD
from time import sleep

lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])

url = "http://the same IP addr in the logreader.py file:5000"
payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
print(response.text)
oldresponse = response.text
if "opened" in oldresponse:
    lcd.clear()
    lcd.write_string(u'ssh status:')
    lcd.cursor_pos = (1, 0)
    lcd.write_string('-----OPEN------')
if "closed" in oldresponse:
    lcd.clear()
    lcd.write_string(u'ssh status:')
    lcd.cursor_pos = (1, 0)
    lcd.write_string('-----CLOSE------')

while True:
        newresponse = requests.request("GET", url, headers=headers, data=payload)
        sleep(1)
        if newresponse.text != oldresponse:
                print(newresponse.text)
                if "opened" in newresponse.text:
                    lcd.clear()
                    lcd.write_string(' status: OPENED')
                    lcd.cursor_pos = (1, 4)
                    lcd.write_string('at: ' + oldresponse[11:16])
                if "closed" in newresponse.text:
                    lcd.clear()
                    lcd.write_string(' status: CLOSED')
                    lcd.cursor_pos = (1, 4)
                    lcd.write_string('at: ' + oldresponse[11:16] )
                oldresponse = newresponse.text



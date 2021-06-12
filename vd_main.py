import requests
import json
import time
import base64
from datetime import datetime
from lomond import WebSocket
from unidecode import unidecode
import colorama
import webbrowser
#from bs4 import BeautifulSoup
import re
from dhooks import Webhook, Embed
import websocket
import random
from websocket import create_connection
	
#put access of important things 
ques = ""
cookies = {}
webhook_url = "https://discordapp.com/api/webhooks/735052519188856913/r7xzzxBHRqge7xcXeMK-qUZ0Kc9QxexbMMVl90OghRlaENFg04X_zpj9RphfkwYx_rsB"
options = ["","",""]
real_ques = str(ques).replace(" ","+") 
google_query = "https://google.com/search?q="+real_ques
real_options = str(options).replace(" ","+")
google_q = "https://google.com/search?q="+real_options


hook = Webhook(webhook_url)
try:
	hook = Webhook(webhook_url)
except:
	print("Invalid WebHook Url!")
#put access token here
loco_bearer_token = "VQfRFQ2WxIDnIn3uiwAdRLluS88sdx"
response_data = requests.get("https://vedantuapi.getloconow.com/v2/vendors/vedantu/v1/contest/",headers={'Authorization': f"Bearer {loco_bearer_token}"}).json()
print(response_data)
SID_url = 'https://vedantu-realtime.getloconow.com/v2/?EIO=3&transport=polling'

headers = {

			'authority':	'vedantu-realtime.getloconow.com',
			'scheme':	'https',
			'accept':	'*/*',
			'authorization':	'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IlNoaXZhbSIsInVzZXJfdWlkIjoiNDEwMjQzODk2MzExNjcxNSIsImF2YXRhciI6IiIsImV4cCI6MTU5NTk0NDQ3MywiaWF0IjoxNTk1OTQyNjczLCJfX2FwcCI6InZlZGFudHUifQ.q2KlgPCpw-jLl31HfaX-4ejpmrDfYIVl2E8Xfvv-2PQ',
			'device-id':	'282D18319440FA86AB30BD1C337016BA445D1B15',
			'x-app-language':	'1',
			'x-app-version':	'100015',
			'x-platform':	'5',
			'accept-encoding':	'gzip',
			'user-agent':	'okhttp/3.14.4',}
r = requests.get(SID_url, headers=headers)
rdata = r.text
print(rdata)

try:
	cookies = r.cookies
	print(cookies)	
except:
	print("Cookies Error!")
try:
	rdata = rdata[rdata.find('{'):]
	rjson = json.loads(rdata)
	print(rjson["sid"])
        #return rjson["sid"]
	SID = rjson["sid"]
except:
	print("There is some error in getting sid")
	#return -1

cookie = 'AWSALB='+cookies['AWSALB']
print(cookie)
url = f'https://vedantu-realtime.getloconow.com/v2/?EIO=3&sid={SID}&transport=polling'

headers = {

			'authority':	'vedantu-realtime.getloconow.com',
			'scheme':	'https',
			'accept':	'*/*',
			'authorization':	'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IlNoaXZhbSIsInVzZXJfdWlkIjoiNDEwMjQzODk2MzExNjcxNSIsImF2YXRhciI6IiIsImV4cCI6MTU5NTk0NDQ3MywiaWF0IjoxNTk1OTQyNjczLCJfX2FwcCI6InZlZGFudHUifQ.q2KlgPCpw-jLl31HfaX-4ejpmrDfYIVl2E8Xfvv-2PQ',
			'cookie':	cookie,#f'AWSALB={Cokie}',
			'device-id':	'282D18319440FA86AB30BD1C337016BA445D1B15',
			'x-app-language':	'1',
			'x-app-version':	'100015',
			'x-platform':	'5',
			'accept-encoding':	'gzip',
			'user-agent':	'okhttp/3.14.4',
	}

r = requests.get(url, headers=headers)
z = r.cookies

#cookies = z['AWSALB']
cookie = 'AWSALB='+cookies['AWSALB']
url = f'https://vedantu-realtime.getloconow.com/v2/?EIO=3&sid ={SID}&transport=polling'
headers = {

			'authority':	'vedantu-realtime.getloconow.com',
			'scheme':	'https',
			'accept':	'*/*',
			'authorization':	'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IlNoaXZhbSIsInVzZXJfdWlkIjoiNDEwMjQzODk2MzExNjcxNSIsImF2YXRhciI6IiIsImV4cCI6MTU5NTk0NDQ3MywiaWF0IjoxNTk1OTQyNjczLCJfX2FwcCI6InZlZGFudHUifQ.q2KlgPCpw-jLl31HfaX-4ejpmrDfYIVl2E8Xfvv-2PQ',
			'cookie':	cookie,
			'device-id':	'282D18319440FA86AB30BD1C337016BA445D1B15',
			'x-app-language':	'1',
			'x-app-version':	'100015',
			'x-platform':	'5',
			'accept-encoding':	'gzip',
			'user-agent':	'okhttp/3.14.4',
		}

r = requests.get(url, headers=headers)
print(r)
raw_key = bytes(random.getrandbits(8) for _ in range(16))
key = base64.b64encode(raw_key).decode()
#this is a small barear = Bearer S05T0UH5SEZWG1JmgXaZjZnxDoCYf9
header = {
		   'Authorization':	'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IlNoaXZhbSIsInVzZXJfdWlkIjoiNDEwMjQzODk2MzExNjcxNSIsImF2YXRhciI6IiIsImV4cCI6MTU5NTk0NDQ3MywiaWF0IjoxNTk1OTQyNjczLCJfX2FwcCI6InZlZGFudHUifQ.q2KlgPCpw-jLl31HfaX-4ejpmrDfYIVl2E8Xfvv-2PQ',
			'Cookie':	cookie,
                        'Device-Id':	'282D18319440FA86AB30BD1C337016BA445D1B15',
			'X-APP-LANGUAGE':	'1',
			'X-APP-VERSION':	'100015',
			'X-PLATFORM':	'5',
			'Upgrade':	'websocket',
			'Connection':	'Upgrade',
			'Sec-WebSocket-Key':	'XOIXqHWG9qQD4O9fh2bHzQ==',
			'Sec-WebSocket-Version':	'13',
			'Host':	'vedantu-realtime.getloconow.com',
			'Accept-Encoding':	'gzip',
			'User-Agent':	'okhttp/3.14.4'}
try:
	import thread
except ImportError:
	import _thread as thread
import time
def on_message(ws, message):
	print(message)
	if message == '3probe':
		print("Success!!")
		#embed = Embed(title=f"**Loco Vedantu Trivia <:vedantu:729209012389806158>**", description=f"**Websocket Successfully Connected <:Correct:729209720262361159>**",color = 0x01DF3A)		
		#hook.send(embed=embed)
	elif message != '3':
		try:
			message = message[message.find('['):]
			mdata = json.loads(message)
			if "question" in mdata:
				ques = mdata[1]["text"]
				#hook.send("!all")
				question_no = mdata[1]["question_rank"]
				options = []
				for o in mdata[1]["options"]:
                                        options.append(o["text"])
				embed = Embed(title=f"**Question {str(question_no)} out of 10**", description=f"**[{ques}]({google_query})**", color = 0x01DF3A)	
				embed.add_field(name="**Option 1**", value=f"[{options[2]}]({google_q})")
				embed.add_field(name="**Option 2**", value=f"[{options[1]}]({google_q})")
				embed.add_field(name="**Option 3**", value=f"[{options[0]}]({google_q})")
				embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/730986303054807110/734674867751878676/unnamed.png")
				embed.set_footer(text="Vedantu Google  |  Made By Shivam#1234")
				hook.send(embed=embed)
				
				question=f"{ques}"
				option1=f"{options[2]}"
				option2=f"{options[1]}"
				option3=f"{options[0]}"
				r = requests.get("http://www.google.com/search?q="+ question)
				res = str(r.text)
				countoption1 = res.count(option1)
				countoption2 = res.count(option2)
				countoption3 = res.count(option3)
				maxcount = max(countoption1, countoption2, countoption3)
				sumcount = countoption1+countoption2+countoption3       
				if countoption1 == maxcount:
					embed = Embed(title="**__Google Result!__**", description=f"**1. {options[2]} : {countoption1}** ✅\n**2. {options[1]} : {countoption2}**\n**3. {options[0]} : {countoption3}**",color=0xFA5858)
					hook.send(embed=embed)   
					hook.send("vd")
					
                                              
				elif countoption2 == maxcount:
					embed = Embed(title="**__Google Result!__**", description=f"**1. {options[2]} : {countoption1}**\n**2. {options[1]} : {countoption2}** ✅\n**3. {options[0]} : {countoption3}**",color=0xFA5858)
					hook.send(embed=embed)   
					hook.send("vd")
					
                                                 
				else:
					embed = Embed(title="**__Google Result!__**", description=f"**1. {options[2]} : {countoption1}**\n**2. {options[1]} : {countoption2}**\n**3. {options[0]} : {countoption3}** ✅",color=0xFA5858)
					hook.send(embed=embed)
					hook.send("vd")
					
                                        
      
				

	
				#print("...Question Detected...(%d)" %qc)
				#qc+=1
			elif "status" in mdata:
                               cuid = mdata[1]['question_stats']["correct_option_uid"]
                               print(cuid)
                               
                               embed = Embed(title="**Answer Stats **" ,color = 0x045FB4)
                               embed.add_field(name="**Correct Option :-**", value=f"**• {cuid}**")
                               embed.set_footer(text="Vedantu Google  |  Made By Shivam#1234")
                               hook.send(embed=embed)
                               	
                               	
                               x = {"question":ques,"number":question_no,"options":options}
			with open('ocrq.json', 'w') as outfile:
                			json.dump(x, outfile)
                
				
                           		
		except:
			print(message)

def on_error(ws, error):
	print(error)
	hook.send('im dead, disconnected' + error)

def on_close(ws):
	print("closed")
	#embed = Embed(title=f"**Loco Vedantu Trivia <:vedantu:729209012389806158> **", description=f"**Websocket Disconnected** <:emoji_21:735059350980395048>",color=0xFA5858)
	#hook.send(embed=embed)
def on_open(ws):
		print('## Opened ##')
		def run(*args):
				ws.send('2probe')
				ws.send('5')
				while True:
						try:
								#print('Sending to Server...')
								time.sleep(15)
								ws.send('2')
						
						except:
								print('Unable to send to server')
								break
				time.sleep(1)
				ws.close()
				print ("thread terminating..")
		thread.start_new_thread(run, ())



if __name__ == "__main__":
	websocket.enableTrace(True)
	ws = websocket.WebSocketApp(f"wss://vedantu-realtime.getloconow.com/v2/?EIO=3&sid={SID}&transport=websocket",
								on_message = on_message,
								on_error = on_error,
								on_close = on_close,
								cookie =cookie,
								header = header)
	ws.on_open = on_open
	ws.run_forever()
			   

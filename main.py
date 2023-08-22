#مطور البوت @MR_MIGHO
from config import *
import requests
from Adminbtn import * 
from member import *
from bio import *


@bot.message_handler(commands=['start'])
def subs(m):
	ex_id(m)
	get_id(m)
	
	msg = '''🚸| عذرا عزيزي
🔰| عليك الاشتراك بقناة البوت لتتمكن من استخدامه

- مــعرف القـناة : {ch} 

‼️| اشترك ثم ارسل /start'''
	idd = m.from_user.id
	
	url = f"https://api.telegram.org/bot{tok}/getchatmember?chat_id={ch}&user_id={idd}"
	req = requests.get(url)
	if idd == Admin or 'member' in req.text or 'creator' in req.text or 'administartor' in req.text:
		idd = m.from_user.id
		if idd==Admin or idd==admims:
			admin(m)
			member(m)
		else:
			member(m)
			
	
	else:
		bot.send_message(m.chat.id, """*🚸| عذرا عزيزي
🔰| عليك الاشتراك بقناة البوت لتتمكن من استخدامه

- مــعرف القـناة : {} 

‼️| اشترك ثم ارسل /start*""".format(ch),parse_mode="markdown")

	
	
		

	
	
	
	
		
		
		
		
		
		
		
#ينطيك ايديك بس ترسل /id
@bot.message_handler(func=lambda m:True)
def test(message):
	if message.text=='/id':
		idd = message.from_user. id
		ids = str(idd)
		bot.send_message(message.chat.id, ids, parse_mode='html')

	

bot.delete_webhook()

bot.infinity_polling()

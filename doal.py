#مطور البوت @MR_MIGHO
from config import * 
from Adminbtn import * 


def ex_id(id):
	result = False
	file = open('users.txt', 'r')
	for line in file:
		if line.strip()==id:
			result = True
			file.close()
			return result
#فنكشن يرسلك ايديات المستخدمين
def files(message):
	file = open('users.txt', 'rb')
	bot.send_document(message.chat.id, file)


def get_id(message):
	file = open('users.txt', 'r')
	li = len(file.readlines())
	file.close()
	if message.chat.type=='private':
		usernames = message.from_user.username
		idu =message.from_user.id
		f = open('users.txt', 'a')
		if (not ex_id(str(idu))):
			f.write(f'{idu}\n')
			f.close

def u_id(m):
	idd = m.from_user.id
	bot.send_message(m.chat.id, idd)
	
def ur_id(m):
	idd = m.from_user.id
	bot.send_message(m.chat.id, '--> /id')
	



def broddd(message):
    mes = message.text
    readd = open('users.txt', 'r')
    for idu in readd:
        bot.send_message(idu, text=f'*{mes}*', parse_mode='markdown')
    bot.send_message(message.chat.id, text=f'*تم عمل اذاعة بنجاح ✅*', parse_mode='markdown')

def echo(message):
	mesgg = bot.send_message(message.chat.id, text='*SEND MESSAGE :*', parse_mode='Markdown')
	bot.register_next_step_handler(mesgg, broddd)
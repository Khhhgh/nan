#مطور البوت @MR_MIGHO

from config import * 
from zkharf import *
from bio import *

def admin(m):
	bstart = types.InlineKeyboardMarkup()
	
	b_dev = types.InlineKeyboardButton(text='  🔰DEV🔰  ', url='t.me/T_4IJ')
	
	b_users = types.InlineKeyboardButton(text='  🔸️USERS🔸️  ', callback_data='users')
	
	b_ch = types.InlineKeyboardButton(text='  🔸️CHANNEL🔸️  ', url ='https://t.me/hope521')
	
	b_echo = types.InlineKeyboardButton(text='   🔸️ECHO FOR ALL🔸️  ', callback_data='echo')
	
	b_source = types.InlineKeyboardButton(text='   🔸️SOURCE🔸️  ',url = 'https://t.me/hope521',callback_data='source')
	
	#ur_id = types.InlineKeyboardButton(text=' 🔸️YOU\'R ID🔸️ ', callback_data='id')
	
	b_id = types.InlineKeyboardButton(text='🔸️BOT ID🔸️', callback_data='u_id')
	
	bstart.row_width = 2
	bstart.add(b_users,b_echo,b_id,ur_id,b_source,b_ch)
	bstart.row_width = 3
	bstart.add(b_dev)
	admin_name = m.from_user.username

	admin_msg = '''

*WELLCOME @{} TO ZAKHRAFA BOT

THIS PANEL FOR U :)

I WISH NICE DAY FOR U BRO :/
_________________________________*

'''.format(admin_name)
	
	bot.send_message(m.chat.id, admin_msg,  reply_markup=bstart, parse_mode='Markdown')

	

@bot.callback_query_handler(func=lambda call: True)
def answer(call):
	bstart = types.InlineKeyboardMarkup()
	
	b_en = types.InlineKeyboardButton(text='-ENGILSH-', callback_data='zkh')
	
	b_dev = types.InlineKeyboardButton(text='  🔰DEV🔰  ', url='t.me/T_4IJ')
	
	b_ch = types.InlineKeyboardButton(text='  ️CHANNEL🔹️  ', url ='https://t.me/hope521')

	b_source = types.InlineKeyboardButton(text='   🔹SOURCE️  ',url = 't.me/MEGGAS',callback_data='source')
	b_bio = types.InlineKeyboardButton(text='  NAME\'S   ',callback_data='bio')
	b_rmz = types.InlineKeyboardButton(text=' SYMBOL\'S ',callback_data='rmz')
	
	ur_id = types.InlineKeyboardButton(text=' 🔹️ID🔹️ ', callback_data='id')
	
	farag = types.InlineKeyboardButton(text='───♡───',callback_data='farag')
	bstart.add(b_bio,b_en,b_rmz)
	bstart.row_width = 3
	bstart.add(farag)
	bstart.row_width = 2
	bstart.add(b_source,b_ch,b_dev)
	if call.data == 'u_id':
	   u_id(call.message)
	elif call.data=='echo':
	   echo(call.message)
	elif call.data=='users':
	   files(call.message)
	elif call.data=='zkh':
	   done_txt(call.message)
	elif call.data=='again':
	   done_txt(call.message)
	elif call.data=='bio':
		bio(call.message)
	elif call.data=='NEXT':
		bio(call.message)
	elif call.data=='rmz':
		rmoz(call.message)
	elif call.data=='backma':
	   	member_name = call.message.from_user.username
	   	msg = '''

*WELLCOME @{} TO ZAKHRAFA BOT

     PLEASE CHOOSE: 
_________________________________*

'''.format(member_name)
	   	bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=msg,parse_mode="Markdown", reply_markup=bstart)
	
    	

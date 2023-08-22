#مطور البوت @MR_MIGHO
from config import *
from zkharf import *



#هاي قائمة الاعضاء :/








def member(m):
	bstart = types.InlineKeyboardMarkup()
	
	b_en = types.InlineKeyboardButton(text='-ENGILSH-', callback_data='zkh')
	
	b_dev = types.InlineKeyboardButton(text='  🔰DEV🔰  ', url='t.me/T_4IJ')
	
	b_ch = types.InlineKeyboardButton(text='  ️CHANNEL🔹️  ', url ='https://t.me/hope521')

	b_source = types.InlineKeyboardButton(text='   🔹SOURCE️  ',url = 'https://t.me/hope521',callback_data='source')
	b_bio = types.InlineKeyboardButton(text='  NAME\'S   ',callback_data='bio')
	b_rmz = types.InlineKeyboardButton(text=' SYMBOL\'S ',callback_data='rmz')
	
	ur_id = types.InlineKeyboardButton(text=' 🔹️ID🔹️ ', callback_data='id')
	
	farag = types.InlineKeyboardButton(text='───♡───',callback_data='farag')
	bstart.add(b_bio,b_en,b_rmz)
	bstart.row_width = 3
	bstart.add(farag)
	bstart.row_width = 2
	bstart.add(b_source,b_ch,b_dev)

	member_name = m.from_user.username

	member_msg = '''

*WELLCOME @{} TO ZAKHRAFA BOT

     PLEASE CHOOSE: 
_________________________________*

'''.format(member_name)
	
	bot.send_message(m.chat.id, member_msg,  reply_markup=bstart, parse_mode='Markdown')
	
	bstart.row_width = 2
	
	bstart.row_width = 2
	bstart.add(b_ch, b_source, b_dev)

    	

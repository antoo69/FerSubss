# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
 ✨Perintah untuk Pengguna BOT✨
  - /start - Mulai Bot
  - /about - Tentang Bot ini
  - /help - Bantuan Perintah Bot ini
  - /ping - Untuk mengecek bot hidup
  - /uptime - Untuk melihat status bot 
 
 🕵️ Perintah Untuk Admin BOT🕵️
  -  /logs - Untuk melihat logs bot
  - /setvar - Untuk mengatur var dengan command dibot
  - /delvar - Untuk menghapus var dengan command dibot
  - /getvar - Untuk melihat salah satu var dengan command dibot
  - /users - Untuk melihat statistik pengguna bot
  - /batch - Untuk membuat link lebih dari satu file
  - /speedtest - Untuk Mengetes kecepatan server bot
  - /broadcast - Untuk mengirim pesan broadcast ke pengguna bot

🗿Owner :  </b><a href='https://t.me/Galerifsyrl'>@fsyrl9</a>
"""

    close = [
        [InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ", callback_data="about"),
            InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")
        ],
    ]

    ABOUT = """
<b>Tentang Bot ini:

@{} adalah Bot Telegram untuk menyimpan Postingan atau File yang dapat Diakses melalui Link Khusus.

  Ini adalah bot ForceSubs/File share link unlimited Button atau support 2-6 Button sesuai keperluan
 Jika anda berminat memiliki bot ini silahkan hubungi owner yang tertera pada bot ini
 Jika anda ingin melihat Lain nya kalian bisa mengunjungi Halaman Channel kami di bawah ini
     Channel :  </b><a href='https://t.me/Galerifsyrl'>@Galerifsyrl</a>

from pyrogram import filters
from pyrogram.types import Message
from os import listdir, remove
from config import PREFIX
from pyrogod import app
from pyrogod.modules.help import add_command_help
from time import sleep, time

add_command_help(
      
      "download", [
      ["{PREFIX}download", "download given file/document"],
      ["{PREFIX}downloadlist", "gives downloaded files list"],
      ["{PREFIX}upload", "uploads the file to the chat"],
      ["{PREFIX}remove", "removes the file from download list"],
      
                 ],
)


@app.on_message(filters.me & filters.command('download', PREFIX))
async def download(app, message):
    sleep(0.2)
    if message.reply_to_message:
        await message.edit('Downloading...')
        start = time()
        if message.reply_to_message.document:
            if len(message.text.split()) == 1:
                file_name = message.reply_to_message.document.file_name
                if file_name in listdir("./Downloads/"):
                    message.edit('There is already a file with this name')
                    return
                app.download_media(message.reply_to_message, "./Downloads/{}".format(file_name))
                end = time()
                elapsed_time = str(end - start)
                await message.edit('File is downloaded\nElapsed time : {}'.format(elapsed_time))
                return
            else:
                file_name = " ".join(message.text.split()[1:]) + ".txt"
                if file_name in listdir("./Downloads/"):
                    message.edit('There is already a file with this name')
                    return
                app.download_media(message.reply_to_message, file_name="./Downloads/{}".format(file_name))
                end = time()
                elapsed_time = str(end - start)
                await message.edit('File is downloaded\nFile name : {}\nElapsed time : {}'.format(file_name,
                                                                                            elapsed_time))
                return
        if message.reply_to_message.video:
            if len(message.text.split()) == 1:
                num = 0
                file_name = "video{}.mp4"
                while 1:
                    if file_name.format(num) in listdir("./Downloads/"):
                        num += 1
                    else:
                        break
                app.download_media(message.reply_to_message, file_name="./Downloads/{}".format(file_name.format(num)))
                end = time()
                elapsed_time = str(end - start)
                await message.edit('Video is downloaded\nFile name : {}\nElapsed time : {}'.format(file_name,
                                                                                             elapsed_time))
                return
            else:
                file_name = " ".join(message.text.split()[1:]) + ".mp4"
                if file_name in listdir("./Downloads/"):
                    message.edit('There is already a video with this name')
                    return
                app.download_media(message.reply_to_message, file_name="./Downloads/{}".format(file_name))
                end = time()
                elapsed_time = str(end - start)
                await message.edit('Video is downloaded\nFile name : {}\nElapsed time : {}'.format(file_name,
                                                                                             elapsed_time))
                return
        if message.reply_to_message.audio:
            if len(message.text.split()) == 1:
                num = 0
                file_name = message.reply_to_message.audio.file_name
                while 1:
                    if file_name.format(num) in listdir("./Downloads/"):
                        num += 1
                    else:
                        break
                app.download_media(message.reply_to_message, file_name="./Downloads/{}".format(file_name.format(num)))
                end = time()
                elapsed_time = str(end - start)
                await message.edit('Music is downloaded\nFile name : {}\nElapsed time : {}'.format(file_name,
                                                                                             elapsed_time))
                return
            else:
                file_name = " ".join(message.text.split()[1:]) + ".mp3"
                if file_name in listdir("./Downloads/"):
                    message.edit('There is already a music with this name')
                    return
                app.download_media(message.reply_to_message, file_name="./Downloads/{}".format(file_name))
                end = time()
                elapsed_time = str(end - start)
                await message.edit('Music is downloaded\nFile name : {}\nElapsed time : {}'.format(file_name,
                                                                                             elapsed_time))
                return
    else:
        await message.edit('You must reply to message')


@app.on_message(filters.me & filters.command('upload', PREFIX))
async def upload(app, message):
    await message.edit('Wait...')
    file_name = " ".join(message.text.split()[1:])
    if file_name in listdir("./Downloads/"):
        message.delete()
        start = time()
        app.send_document(message.chat.id, "./Downloads/{}".format(file_name))
        elapsed = str(time() - start)
        app.send_message(message.chat.id, f"Elapsed time : {elapsed}")


@app.on_message(filters.me & filters.command('remove', PREFIX))
async def remove_file(app, message):
    if len(message.text.split()) == 2:
        await message.edit('Wait...')
        num = 1
        file = message.text.split()[1]
        if file.isdigit():
            for i in listdir("./Downloads/"):
                if num == int(file):
                    remove("./Downloads/{}".format(i))
                    await message.edit('Removed successfully')
                    return
                else:
                    num += 1
            await message.edit(f'File # {file} not found')


@app.on_message(filters.me & filters.command('downloadlist', PREFIX))
async def download_list(app, message):
    await message.edit('Wait...')
    downloads = ""
    num = 1
    for i in listdir("./Downloads/"):
        downloads += f"📂 [{num}] {i}\n"
        num += 1
    await message.edit("Download list:\n\n<u>                File names                   </u>.        \n"
                 + downloads, parse_mode='HTML') if num != 1 else message.edit('You has not a file')

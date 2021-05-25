#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption +"   @flmarc\n   @askyourmovies_101\n   @anime_stann" if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        
        if file_type == "document":
        
            await bot.send_document(
                chat_id=update.chat.id,
                document = file_id,
                caption = caption,
                parse_mode="html",
                reply_to_message_id=update.message_id,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '💕SHARE THIS GROUP💕', url="http://t.me/share/url?url=%2A%2Ahey+bro..+%2A%2A%0D%0A__Join+this+amazing+movie+group+that+i+just+found__%0D%0A%2A%2AThey+uploads+requested+movies+with+in+seconds%2A%2A+%F0%9F%98%8D%0D%0A%2A%2AJOIN+NOW%2A%2A+%3A+%40askyourmovies_101+%F0%9F%94%A5%F0%9F%91%8C"
                                )
                        ]
                    ]
                )
            )

        elif file_type == "video":
        
            await bot.send_video(
                chat_id=update.chat.id,
                video = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '💕SHARE THIS GROUP💕', url="http://t.me/share/url?url=%2A%2Ahey+bro..+%2A%2A%0D%0A__Join+this+amazing+movie+group+that+i+just+found__%0D%0A%2A%2AThey+uploads+requested+movies+with+in+seconds%2A%2A+%F0%9F%98%8D%0D%0A%2A%2AJOIN+NOW%2A%2A+%3A+%40askyourmovies_101+%F0%9F%94%A5%F0%9F%91%8C"
                                )
                        ]
                    ]
                )
            )
            
        elif file_type == "audio":
        
            await bot.send_audio(
                chat_id=update.chat.id,
                audio = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '💕SHARE THIS GROUP💕', url="http://t.me/share/url?url=%2A%2Ahey+bro..+%2A%2A%0D%0A__Join+this+amazing+movie+group+that+i+just+found__%0D%0A%2A%2AThey+uploads+requested+movies+with+in+seconds%2A%2A+%F0%9F%98%8D%0D%0A%2A%2AJOIN+NOW%2A%2A+%3A+%40askyourmovies_101+%F0%9F%94%A5%F0%9F%91%8C"
                                )
                        ]
                    ]
                )
            )

        else:
            print(file_type)
        
        return

    buttons = [[
        InlineKeyboardButton('Developers', url='https://t.me/anime_stann'),
        InlineKeyboardButton('Source Code 🧾', url ='https://github.com/Al/lol')
    ],[
        InlineKeyboardButton('Support 🛠', url='https://t.me/anime_stann')
    ],[
        InlineKeyboardButton('Help ⚙', callback_data="help")
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('About 🚩', callback_data='about')
    ],[
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )

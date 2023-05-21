@dp.message_handler(lambda message: message.text == "Расписание")
async def schedule_menu(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    buttons = [types.InlineKeyboardButton(text="Группа 1", callback_data="group_1"),
               types.InlineKeyboardButton(text="Группа 2", callback_data="group_2"),
               types.InlineKeyboardButton(text="Группа 3", callback_data="group_3")]
    keyboard.add(*buttons)
    await message.reply("Выберите учебную группу:", reply_markup=keyboard)

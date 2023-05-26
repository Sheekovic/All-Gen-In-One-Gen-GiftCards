import logging
import random
import string as strg
import time
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler


headers = {
    'User-Agent': 'TikTok 17.4.0 rv:17yellow_to_red14 (iPhone; iOS 13.6.1; sv_SE) Cronet',
    'Connection': 'keep-alive',
}

character = strg.ascii_letters + strg.digits


# Create a logger object
logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to the Gen Giftcards bot!")


from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def issue(update: Update, context: CallbackContext):
    # ...

    # Define the button options with their corresponding callback data
    options = [
        ('PSN Card', '1'), ('Playstore', '2'), ('Roblox', '3'),
        ('Amazon', '4'), ('Netflix', '6'), ('xBox', '6'),
        ('Itunes', '7'), ('Nitro-Gen', '8'), ('Tiktok', '9'), ('Exit', '10')
    ]
    
    # Create a list of InlineKeyboardButton objects for each option
    buttons = [InlineKeyboardButton(text, callback_data=data) for text, data in options]
    
    # Create an InlineKeyboardMarkup with a single column of buttons
    reply_markup = InlineKeyboardMarkup([[button] for button in buttons])
    
    # Send the welcome message with formatting
    welcome_message = f"Gift Card Checker\n Welcome"
    context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_message)
    
    # Send the options message with formatting
    options_message = f"Generator Room:"
    for index, option in enumerate(options, start=1):
        option_text = option[0]
        options_message += f"\n[{index}] - {option_text}"
    
    # Store the options in user_data to retrieve in the callback query handler
    context.user_data['options'] = options
    
    context.bot.send_message(chat_id=update.effective_chat.id, text=options_message, reply_markup=reply_markup)


def ask_amount(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Please provide the amount: /amount 10')
    # Update the conversation state to wait for the amount input
    context.user_data['state'] = 'WAITING_AMOUNT'
    # update the amount in user_data to user input split after the command
    context.user_data['amount'] = update.message.text.split()[1]
    # send the amount stored in user_data to the user
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'Amount: {context.user_data["amount"]}')


def psn(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text='------------PSN CARD-------------\n')
    try:
        amount = context.user_data.get('amount')
        if amount is None:
            # Ask for the amount
            ask_amount(update, context)
            return
        
        amount = int(amount)
        for gen_psn in range(amount):
            psn_card = "".join(random.choices(character, k=12))
            url_code_psn = "https://web.np.playstation.com/api/graphql/v1/transact/wallets/vouchers/" + psn_card
            status = requests.get(url_code_psn)
            if status.status_code == 403:
                context.bot.send_message(chat_id=update.effective_chat.id, text=f'Valid | {psn_card}')
                break
            else:
                context.bot.send_message(chat_id=update.effective_chat.id, text=f'Invalid | {psn_card}')
    except:
        pass
    context.bot.send_message(chat_id=update.effective_chat.id, text='\n ------Generating Completed------ !')




def playstore(update: Update, context: CallbackContext):
    amount = context.user_data.get('amount')
    amount = int(amount)
    context.bot.send_message(chat_id=update.effective_chat.id, text='------------PLAYSTORE CARD-------------\n')
    try:
        for play_store in range(amount):
            play_store = ''.join(random.choices(character, k=20))
            time.sleep(0.1)
            context.bot.send_message(chat_id=update.effective_chat.id, text=play_store)
    except:
        pass
    context.bot.send_message(chat_id=update.effective_chat.id, text='\n ------Generating Completed------ !')


def roblox(update: Update, context: CallbackContext):
    amount = context.user_data.get('amount')
    amount = int(amount)
    context.bot.send_message(chat_id=update.effective_chat.id, text='------------ROBLOX CARD-------------\n')
    try:
        for roblox in range(amount):
            roblox = ''.join(random.choices(strg.digits, k=10))
            time.sleep(0.1)
            context.bot.send_message(chat_id=update.effective_chat.id, text=roblox)
    except:
        pass
    context.bot.send_message(chat_id=update.effective_chat.id, text='\n ------Generating Completed------ !')


def amazon(update: Update, context: CallbackContext):
    amount = context.user_data.get('amount')
    amount = int(amount)
    context.bot.send_message(chat_id=update.effective_chat.id, text='------------AMAZON CARD-------------\n')
    try:
        for amazon in range(amount):
            code_amazon = ''.join(random.choices(character, k=14))
            time.sleep(0.1)
            context.bot.send_message(chat_id=update.effective_chat.id, text=code_amazon)
    except:
        pass
    context.bot.send_message(chat_id=update.effective_chat.id, text='\n ------Generating Completed------ !')


def netflix(update: Update, context: CallbackContext):
    amount = context.user_data.get('amount')
    amount = int(amount)
    context.bot.send_message(chat_id=update.effective_chat.id, text='------------NETFLIX CARD-------------\n')
    try:
        for netflix in range(amount):
            netflix_card = ''.join(random.choices(character, k=15))
            time.sleep(0.1)
            context.bot.send_message(chat_id=update.effective_chat.id, text=netflix_card)
    except:
        pass
    context.bot.send_message(chat_id=update.effective_chat.id, text='\n ------Generating Completed------ !')


def xbox(update: Update, context: CallbackContext):
    amount = context.user_data.get('amount')
    amount = int(amount)
    context.bot.send_message(chat_id=update.effective_chat.id, text='------------XBOX CARD-------------\n')
    try:
        for xbox in range(amount):
            code_xbox = ''.join(random.choices(character, k=25))
            time.sleep(0.1)
            context.bot.send_message(chat_id=update.effective_chat.id, text=code_xbox)
    except:
        pass
    context.bot.send_message(chat_id=update.effective_chat.id, text='\n ------Generating Completed------ !')


def itunes(update: Update, context: CallbackContext):
    amount = context.user_data.get('amount')
    amount = int(amount)
    context.bot.send_message(chat_id=update.effective_chat.id, text='------------ITUNES CARD-------------\n')
    try:
        for itunes in range(amount):
            code_itunes = ''.join(random.choices(character, k=16))
            time.sleep(0.1)
            context.bot.send_message(chat_id=update.effective_chat.id, text=code_itunes)
    except:
        pass
    context.bot.send_message(chat_id=update.effective_chat.id, text='\n ------Generating Completed------ !')


def nitro(update: Update, context: CallbackContext):
    amount = context.user_data.get('amount')
    amount = int(amount)
    context.bot.send_message(chat_id=update.effective_chat.id, text='------------NITRO CODE-------------\n')
    try:
        for nitro in range(amount):
            nitro_code = ''.join(random.choices(character, k=24))
            time.sleep(0.1)
            context.bot.send_message(chat_id=update.effective_chat.id, text=nitro_code)
    except:
        pass
    context.bot.send_message(chat_id=update.effective_chat.id, text='\n ------Generating Completed------ !')


def tiktok(update: Update, context: CallbackContext):
    amount = context.user_data.get('amount')
    amount = int(amount)
    context.bot.send_message(chat_id=update.effective_chat.id, text='------------TIKTOK CARD-------------\n')
    try:
        for tiktok in range(amount):
            tiktok_card = ''.join(random.choices(character, k=20))
            time.sleep(0.1)
            context.bot.send_message(chat_id=update.effective_chat.id, text=tiktok_card)
    except:
        pass
    context.bot.send_message(chat_id=update.effective_chat.id, text='\n ------Generating Completed------ !')


def cancel(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Cancelled.')


def error(update: Update, context: CallbackContext) -> None:
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main() -> None:
    """Start the bot."""
    # Get the API token from an environment variable
    token = "put your token here"
    if token is None:
        print('Please set the TELEGRAM_TOKEN environment variable.')
        return
    #print('Starting bot...')
    print('Bot started.')

    # Create an Updater instance with your bot token
    updater = Updater(token='put your token here', use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("amount", ask_amount))
    dispatcher.add_handler(CommandHandler("issue", issue))
    dispatcher.add_handler(CallbackQueryHandler(button_click_handler))  # Add this line
    dispatcher.add_handler(CommandHandler("psn", psn))
    dispatcher.add_handler(CommandHandler("playstore", playstore))
    dispatcher.add_handler(CommandHandler("roblox", roblox))
    dispatcher.add_handler(CommandHandler("amazon", amazon))
    dispatcher.add_handler(CommandHandler("netflix", netflix))
    dispatcher.add_handler(CommandHandler("xbox", xbox))
    dispatcher.add_handler(CommandHandler("itunes", itunes))
    dispatcher.add_handler(CommandHandler("nitro", nitro))
    dispatcher.add_handler(CommandHandler("tiktok", tiktok))
    dispatcher.add_handler(CommandHandler("cancel", cancel))

    # Log all errors
    dispatcher.add_error_handler(error)

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

def button_click_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    data = query.data
    
    if data == '10':  # Exit option
        query.answer()
        query.edit_message_text(text="Goodbye!")
        return
    
    # Mapping of options to functions
    option_function_map = {
        '1': psn,
        '2': playstore,
        '3': roblox,
        '4': amazon,
        '5': netflix,
        '6': xbox,
        '7': itunes,
        '8': nitro,
        '9': tiktok,
        '10': cancel
        # Add more options and corresponding functions
    }
    
    selected_option = option_function_map.get(data)
    
    if selected_option:
        query.answer()
        query.edit_message_text(text=f"You have selected: {selected_option.__name__.capitalize()}")
        selected_option(update, context)
    else:
        query.answer()
        query.edit_message_text(text="Invalid option. Please try again.")


if __name__ == '__main__':
    main()

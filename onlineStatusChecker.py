import telethon
import pytz
from config import API_KEY_CLI_TG_HASH, API_KEY_CLI_TG_ID

client = telethon.TelegramClient(
    'anon', API_KEY_CLI_TG_ID, API_KEY_CLI_TG_HASH)

# You can use your own number. Script does not send any messages. Only check online if its possible




async def main():
    while True:
        name = input("Enter nickname:")
        info = await client.get_entity(name)
        if type(info.status) == telethon.tl.types.UserStatusOffline:
            date = info.status.was_online
            date = date.astimezone(pytz.timezone('Europe/Moscow'))
            print("Was online at", date)
        else:
            print(info.status)


async def _getStatus(name, timezone='Europe/Moscow'):
    info = await client.get_entity(name)
    if type(info.status) == telethon.tl.types.UserStatusOffline:
        date = info.status.was_online
        date = date.astimezone(pytz.timezone(timezone))
        return (f"Was online at {date}")
    else:
        return (info.status)

# with client:
#     client.loop.run_until_complete(main())



def getStatus(name, timezone='Europe/Moscow'):
    client.start()
    with client:
        return client.loop.run_until_complete(_getStatus(name, timezone='Europe/Moscow'))
    



@client.on(telethon.events.NewMessage)
async def echo(event):
    # Check if the message was sent by a user (not a bot)
        # Send back the same message to the user
    info = await client.get_entity(event.message.text)
    if type(info.status) == telethon.tl.types.UserStatusOffline:
        date = info.status.was_online
        date = date.astimezone(pytz.timezone('Europe/Moscow'))
        await event.respond(f"Was online at {date}")
    elif type(info.status) == telethon.tl.types.UserStatusOnline:
        await event.respond("User is online!")
    elif type(info.status) == telethon.tl.types.UserStatusRecently:
        await event.respond("Secret motherfucker!")
    else:
        await event.respond("Was not online for so long...")
    await client.send_read_acknowledge(event.message.peer_id.user_id, event.message)

# Start the client
def handlerStart():
    with client:
        # Run the client until it's disconnected
        client.run_until_disconnected()

handlerStart()

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

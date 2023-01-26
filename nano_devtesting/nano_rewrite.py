# -------- Import Modules -------- #

import random, os, sys, json, time, requests, asyncio
import discord
from discord.ext import commands
from discord.utils import get

# -------- Import Modules -------- #

# -------- Import Artwork -------- #

dashboard = open('lists/artwork/1_dashboard.txt', encoding='utf-8').read()
dashboard_options = open('lists/artwork/2_dashboard_options.txt', encoding='utf-8').read()

dashboard_auto_pressure = open('lists/artwork/3_dashboard_auto_pressure.txt', encoding='utf-8').read()
dashboard_afk_checker = open('lists/artwork/4_dashboard_afk_checker.txt', encoding='utf-8').read()
dashboard_afk_alert = open('lists/artwork/5_dashboard_afk_alert.txt', encoding='utf-8').read()
dashboard_channel_crasher = open('lists/artwork/6_dashboard_channel_crasher.txt', encoding='utf-8').read()

dashboard_gc_botnet = open('lists/artwork/7_dashboard_gc_botnet.txt', encoding='utf-8').read()
dashboard_add_alts_to_gc = open('lists/artwork/8_dashboard_add_alts_to_gc.txt', encoding='utf-8').read()
dashboard_gc_bomber = open('lists/artwork/9_dashboard_gc_bomber.txt', encoding='utf-8').read()
dashboard_gc_locker = open('lists/artwork/10_dashboard_gc_locker.txt', encoding='utf-8').read()

dashboard_packgen = open('lists/artwork/11_dashboard_packgen.txt', encoding='utf-8').read()
dashboard_anti_packgen = open('lists/artwork/12_dashboard_anti_packgen.txt', encoding='utf-8').read()
dashboard_topicgen = open('lists/artwork/13_dashboard_topicgen.txt', encoding='utf-8').read()
dashboard_friend_users = open('lists/artwork/14_dashboard_friend_users.txt', encoding='utf-8').read()
dashboard_bulk_delete = open('lists/artwork/15_dashboard_bulk_delete.txt', encoding='utf-8').read()
dashboard_anti_trap = open('lists/artwork/16_dashboard_anti_trap.txt', encoding='utf-8').read()

dashboard_help = open('lists/artwork/17_dashboard_help.txt', encoding='utf-8').read()
dashboard_information = open('lists/artwork/17.2_dashboard_information.txt', encoding='utf-8').read()
# -------- Import Artwork -------- #

# -------- User Settings -------- #

with open('settings.json', 'r') as config:
  settings = json.load(config)

  live_mode = settings.get('live_mode')

  token = settings.get('token')
  front = settings.get('front')
  your_webhook = settings.get('your_webhook')

  delay = settings.get('delay')
  your_id = settings.get('your_id')
  channel = settings.get('channel')
  victim = settings.get('victim')

  invisible_ping = settings.get('invisible_ping')
  alerts = settings.get('alerts')

# -------- User Settings -------- #

# -------- Variables -------- #

invisible_ping_text = '||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||'

# -------- Variables -------- #

# -------- System Functions -------- #

def clear_screen():
  kernel = sys.platform
  match kernel:
    case 'linux':
      os.system('clear')
    case _:
      os.system('cls')

def startup():
  try:

    clear_screen()
    print(dashboard)
    print(dashboard_options)
    script_choice = input('\nWhat script would you like to run?: ')
    match script_choice:

      case '1':
        auto_pressure()

      case '2':
        afk_checker()

      case '3':
        afk_alert()

      case '4':
        bulk_delete()

      case '5':
        channel_crasher()

      case '6':
        gc_botnet()

      case '7':
        add_alts_to_gc()

      case '8':
        gc_bomber()

      case '9':
        gc_locker()

      case '10':
        packgen()

      case '11':
        anti_packgen()

      case '12':
        topicgen()
      
      case '13':
        friend_users()

      case '14':
        anti_trap()

      case 'help' | 'Help':
        descriptions()
        
      case _:
        startup()
  
  except KeyboardInterrupt:

    clear_screen()
      
# -------- System Functions -------- #

# -------- Scripts -------- #

def auto_pressure(): # 1
  try:
    clear_screen()
    print(dashboard_auto_pressure)

    match live_mode:
      case True:
        channel = int(input(f'{front} Channel: '))
        delay = int(input(f'{front} Delay: '))
        token = str(input(f'{front} Token: '))

      case False:
        channel = settings.get('channel')
        token = settings.get('token')
        delay = settings.get('delay')
    
    while True:
      auto_pressure_sent_messages = []
      auto_pressure_url = f'https://discord.com/api/v9/channels/{channel}/messages'

      auto_pressure_list = random.choice(open('lists/auto_pressure_lists/pressure.txt', 'r').readlines())

      auto_pressure_files = [auto_pressure_list]

      auto_pressure_choose = random.choice(auto_pressure_files)

      if auto_pressure_choose in auto_pressure_sent_messages:
        return auto_pressure_choose
      auto_pressure_post = requests.post(auto_pressure_url, headers={'authorization': token}, data={'content': auto_pressure_choose})
      
      match auto_pressure_post.status_code:
        case 200:
          print(f'{front} Sent: {auto_pressure_choose}')
        case 429:
          print(f'{front} Ratelimited, retrying')
        case 401:
          print(f'{front} Invalid token or channel ID')
      
      time.sleep(delay)

      time.sleep(delay)

  except KeyboardInterrupt:
    startup()

def afk_checker(): # 2
  try:
    clear_screen()
    print(dashboard_afk_checker)

    match live_mode:
      case True:

        channel = int(input(f'{front} Channel: '))
        token = str(input(f'{front} Token: '))

        invisible_ping = (str(input(f'{front} Invisible Ping (y/n): ')))

        match invisible_ping:
          case 'y':
            victim = int(input(f'{front} Victim (ID): '))

      case False:
        token = settings.get('token')
        channel = settings.get('channel')
        delay = settings.get('delay')
        invisible_ping = settings.get('invisible_ping')
        victim = settings.get('victim')

    delay = int(input(f'{front} Delay: '))

    while True:
        up_to = int(input(f'{front} How far do you want to count to?: '))

        afk_checker_url = f'https://discord.com/api/v9/channels/{channel}/messages'

        i = 0
        while i < up_to:
          
          match invisible_ping:
            case 'y' | 'Y':
              afk_checker_post = requests.post(afk_checker_url, headers={'authorization': token}, data={'content': f'{i+1}{invisible_ping_text}<@{victim}>'})
            
            case _:
              afk_checker_post = requests.post(afk_checker_url, headers={'authorization': token}, data={'content': f'{i+1}'})
            
          match afk_checker_post.status_code:

            case 200:
              print(f'{front} Sent {i+1}')
              i += 1
              time.sleep(delay)

            case 429:
              print(f'{front} Ratelimited, retrying')

            case 401:
              print(f'{front} Invalid token or channel ID')
              break

  except KeyboardInterrupt:
    startup()

def afk_alert(): # 3
    clear_screen()
    print(dashboard_afk_alert)

    match live_mode:
      case True:
        delay = int(input(f'{front} Delay: '))
        your_webhook = str(input('Webhook link: '))
        token = str(input(f'{front} Token: '))

      case False:
        token = settings.get('token')
        delay = settings.get('delay')
        your_webhook = settings.get('your_webhook')

    print(f'{front} messages appear ontop, may take some time to load.')

    afk_alert_dm_channel_url = 'https://discord.com/api/v8/users/@me/channels'

    afk_alert_triggers = ['afk']
    aa_ping = [f'<@!{your_id}>']
    sent_messages = []

    try:
        while True:

            afk_alert_grab_channels = requests.get(afk_alert_dm_channel_url, headers={'authorization': token})
            afk_alert_grab_channels_json = afk_alert_grab_channels.json()

            for channel in afk_alert_grab_channels_json:

                afk_alert_dm_id = channel['id']
                dm_channel_url = f'https://discord.com/api/v8/channels/{afk_alert_dm_id}/messages?limit=15'
                dm_messages = requests.get(dm_channel_url, headers={'authorization': token})
                dm_messages_json = dm_messages.json()

                for afk_alert_dm_message in dm_messages_json:

                    afk_alert_dm_content = afk_alert_dm_message.get('content')
                    afk_alert_dm_message_id = afk_alert_dm_message.get('id')

                    if afk_alert_dm_message_id in sent_messages:
                        continue
                    else:
                        sent_messages.append(afk_alert_dm_message_id)

                    if afk_alert_dm_message_author := afk_alert_dm_message.get('author'):
                        afk_alert_dm_message_username = afk_alert_dm_message_author.get('username')
                        afk_alert_dm_message_discriminator = afk_alert_dm_message_author.get('discriminator')

                        for afk_alert_trigger in afk_alert_triggers:
                            if afk_alert_trigger in afk_alert_dm_content:
                                print(f'{front} {afk_alert_dm_message_username}#{afk_alert_dm_message_discriminator}: {afk_alert_dm_content} in DMs')

                                match alerts:
                                  case True:
                                    afk_alert_post_webhook_data = {"content": f"<@{your_id}>", "embeds": [{"title": f"you're being afk checked by {afk_alert_dm_message_username}#{afk_alert_dm_message_discriminator}", "color": 16711874, "footer": {"text": "sent from nano"}, "image": {"url": "https://media.tenor.com/K3knqTMuD1oAAAAC/rwk-priest-crow.gif"}}],"attachments": []}
                                    afk_alert_post_webhook = requests.post(your_webhook, json=afk_alert_post_webhook_data)
            time.sleep(delay) 

    except KeyboardInterrupt:
        startup()

def bulk_delete(): # 4
  try:
    nano = commands.Bot(command_prefix='>', self_bot=True, help_command=None)
    clear_screen()
    print(dashboard_bulk_delete)
    
    @nano.event
    async def on_ready():
      print(f'{front} Type >blubware in the channel you want to delete messages in')

    @nano.command()
    async def blubware(channel):
        async for msg in channel.message.channel.history(limit=int(9999999)):
            if msg.author.id == nano.user.id:
                try:
                  await msg.delete()
                  print(f'{front} Deleted')

                except:
                    continue
    nano.run(token)

  except KeyboardInterrupt:
    startup()

def channel_crasher(): # 5
  try:
    clear_screen()
    print(dashboard_channel_crasher)

    match live_mode:
      case True:
        channel = int(input(f'{front} Channel: '))
        token = str(input(f'{front} Token: '))
        
      case False:
        channel = settings.get('channel')
        token = settings.get('token')

    while True:
      clear_screen()
      print(dashboard_channel_crasher)

      channel_crasher_channel_post_url = f'https://discord.com/api/v9/channels/{channel}/messages'
      channel_crasher_text = '||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|'

      channel_crasher_append = input(f'{front} Message (limit 50): ')

      channel_crasher_post_request = requests.post(channel_crasher_channel_post_url, headers={'authorization': token}, data={'content': channel_crasher_append + channel_crasher_text})

      match channel_crasher_post_request.status_code:
        case 200:
          print(f'{front} Sent {channel_crasher_append}')

  except KeyboardInterrupt:
    startup()

def gc_botnet(): # 6
    try:

      clear_screen()
      print(dashboard_gc_botnet)

      match live_mode:
        case True:

          channel = int(input(f'{front} Group ID: '))
          token = str(input(f'{front} Token: '))

        case False:
          channel = settings.get('channel')
          token = settings.get('token')

      id_list = open('lists/ids.txt'.strip()).readlines()
      token_list = open('lists/tokens.txt'.strip()).readlines()
      
      while True:
        for tokens in token_list:
          for _ in range(1):
            for id in id_list:
                
                gc_botnet_target = f'https://discord.com/api/v9/channels/{channel}/recipients/{id}'
                gc_botnet_put_request = requests.put(gc_botnet_target, headers={'authorization': tokens})

                match gc_botnet_put_request.status_code:
                  case 204:
                    print(f'{front} Added 1 user')
                  
                  case 429:
                    print(f'{front} Being ratelimited')
                  
                  case 401:
                    print(f'{front} Invalid token or group ID')

                  case 403:
                    print(f'{front} User not added as a friend')

                  case _:
                    print(f'{front} Unknown status code, report this code to byte#6110 | Code:  {gc_botnet_put_request.status_code}')

    except KeyboardInterrupt:
        startup()

def add_alts_to_gc(): # 7
    try:

      clear_screen()
      print(dashboard_add_alts_to_gc)

      match live_mode:
        case True:

          group = int(input(f'{front} Group ID: '))
          token = str(input(f'{front} Token: '))

      id_list = open(int(('lists/ids.txt'))).readlines()
      while True:

        for id in id_list:
            
            add_alts_to_gc_targets = f'https://discord.com/api/v9/channels/{group}/recipients/{id}'
            add_alts_to_gc_request = requests.put(add_alts_to_gc_targets, headers={'authorization': token})

            match add_alts_to_gc_request.status_code:
              case 204:
                print(f'{front} Added 1 user')
              
              case 429:
                print(f'{front} Being ratelimited')
              
              case 401:
                print(f'{front} Invalid token or group ID')

              case 403:
                print(f'{front} User not added as a friend')

              case _:
                print(f'{front} Unknown status code, report this code to byte#6110 | Code:  {add_alts_to_gc_request.status_code}')

    except KeyboardInterrupt:
        startup()

def gc_bomber(): # 8
  try:
    clear_screen()
    print(dashboard_gc_bomber)

    match live_mode:
      case True:
        channel = int(input(f'{front} Group ID: '))
        token = str(input(f'{front} Token: '))

      case False:
        channel = settings.get('channel')
        token = settings.get('token')

    id_list = open('lists/groupchat_lists/gc_bomber/gc_bomber_targets.txt').readlines()
    
    for id in id_list:

      gc_bomber_url = f'https://discord.com/api/v9/channels/{channel}/recipients/{id.strip()}'
      gc_bomber_headers = {
          'accept': '*/*',
          'accept-language': 'en-GB',
          'authorization': token,
          'sec-ch-ua': '\' Not A;Brand\';v=\'99\', \'Chromium\';v=\'102\'',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '\'Linux\'',
          'sec-fetch-dest': 'empty',
          'sec-fetch-mode': 'cors',
          'sec-fetch-site': 'same-origin',
          'x-debug-options': 'bugReporterEnabled',
          'x-discord-locale': 'en-US'
          }

      removed = 1

      gc_bomber_delete_request = requests.delete(gc_bomber_url, headers=gc_bomber_headers)

      match gc_bomber_delete_request.status_code:
          case 204:
            print(f'{front} Removed {removed}')
            removed+1

          case 400:
            print(f'{front} Already removed this ID, {id}')

          case 429:
              print(f'{front} Being ratelimited')

          case 401:
              print(f'{front} Invalid token or user ID')

          case 403:
              print(f'{front} User not in group')

          case _:
            print(f'{front} Unknown status code, report this code to byte#6110 | Code: {gc_bomber_delete_request.status_code}')

    input(f'{front} Bomber done, press enter to return to main menu.')
    startup()

  except KeyboardInterrupt:
    startup()

def gc_locker(): # 9
  try:
    clear_screen()
    print(dashboard_gc_locker)
    token = settings.get('token')

    DiscordHacks = commands.Bot(description='DiscordHacks', command_prefix=';', self_bot=True)

    DiscordHacks.lockgc = []
    DiscordHacks.headers = {'authorization': token}

    @DiscordHacks.event
    async def lockloop():
        while True:
            if DiscordHacks.lockgc != []:
                for gcid in DiscordHacks.lockgc:
                    response = requests.put(f'https://discordapp.com/api/v8/channels/{gcid}/recipients/1337',headers=DiscordHacks.headers)
                    if response.status_code == 429:
                        response_c = response.text
                        response_content = json.loads(response_c)
                        lockedsec = response_content.get('retry_after')
                    else:
                        headers = {"Authorization": token}
                        for _ in range(30):
                            response = requests.put(f'https://discordapp.com/api/v8/channels/{gcid}/recipients/1337',headers=DiscordHacks.headers)
            await asyncio.sleep(0.8)

    @DiscordHacks.event
    async def on_connect():
      print(f"connected to {DiscordHacks.user}, ready to lock groups")
      await lockloop()

    @DiscordHacks.command()
    async def lock(ctx, groupid):
        DiscordHacks.lockgc.extend([groupid] * 1)
        print(f'locking gc: {groupid}')

    @DiscordHacks.command()
    async def unlock(ctx, groupid=None):
        await print('unlocked')
        if groupid:
            DiscordHacks.lockgc.pop(groupid)
            print(f'unlocking {groupid} in 120 seconds')
        else:
            DiscordHacks.lockgc.clear()
            print('unlocked all')

    DiscordHacks.run(token)

  except KeyboardInterrupt:
    startup()

def packgen(): # 10
  try:
      
    clear_screen()
    print(dashboard_packgen)

    match live_mode:
      case True:
        discord = str(input(f'{front} Discord Functionality? (y/n): '))

        match discord:
          case 'y' | 'Y':
            channel = int(input(f'{front} Channel: '))
            delay = int(input(f'{front} Delay: '))

            token = str(input(f'{front} Token: '))

          case _:
            delay = int(input(f'{front} Delay: '))

      case False:

        channel = settings.get('channel')
        token = settings.get('token')
        delay = settings.get('delay')
        discord = settings.get('discord')

    while True:

      actions_by = random.choice(open('lists/wordlists/actions/actions_by.txt', 'r').readlines()).strip()
      actions_by_a = random.choice(open('lists/wordlists/actions/actions_by_a.txt', 'r').readlines()).strip()
      actions_standalone = random.choice(open('lists/wordlists/actions/actions_standalone.txt', 'r').readlines()).strip()
      additions = random.choice(open('lists/wordlists/additions/additions.txt', 'r').readlines()).strip()
      additions2 = random.choice(open('lists/wordlists/additions/additions2.txt', 'r').readlines()).strip()
      animals = random.choice(open('lists/wordlists/objects_misc/animals.txt', 'r').readlines()).strip()
      bodyparts_external = random.choice(open('lists/wordlists/objects_misc/bodyparts_external.txt', 'r').readlines()).strip()
      bodyparts_internal = random.choice(open('lists/wordlists/objects_misc/bodyparts_internal.txt', 'r').readlines()).strip()
      characters = random.choice(open('lists/wordlists/lists/characters.txt', 'r').readlines()).strip()
      family_members = random.choice(open('lists/wordlists/lists/family_members.txt', 'r').readlines()).strip()
      foods = random.choice(open('lists/wordlists/objects_misc/foods.txt', 'r').readlines()).strip()
      insects = random.choice(open('lists/wordlists/objects_misc/insects.txt', 'r').readlines()).strip()
      materials = random.choice(open('lists/wordlists/objects_misc/materials.txt', 'r').readlines()).strip()
      names = random.choice(open('lists/wordlists/lists/names.txt', 'r').readlines()).strip()
      numbers = random.choice(open('lists/wordlists/person/numbers.txt', 'r').readlines()).strip()
      objects = random.choice(open('lists/wordlists/objects_misc/objects.txt', 'r').readlines()).strip()
      quotes = random.choice(open('lists/wordlists/lists/quotes.txt', 'r').readlines()).strip()
      races = random.choice(open('lists/wordlists/person/races.txt', 'r').readlines()).strip()
      time_type = random.choice(open('lists/wordlists/person/time_type.txt', 'r').readlines()).strip()
      appearance = random.choice(open('lists/wordlists/lists/appearance.txt', 'r').readlines()).strip()
      filler = random.choice(open('lists/wordlists/lists/filler.txt', 'r').readlines()).strip()

      bp = (bodyparts_external, bodyparts_internal)
      bpchoose = random.choice(bp)

      packgen_combos = [f'tell me why your {family_members} got {actions_by_a} {additions} {objects}',
                        f'you got caught tryna {additions2} with your {additions} {family_members}s {objects}',
                        f'yo ass got {actions_by_a} {additions} version of {characters}',
                        f'your {family_members} got {actions_by_a} {objects}',
                        f'i walked in the room and saw you get {actions_by_a} {additions} {animals}',
                        f'your {family_members} got caught tryna {additions2} your {additions} pet {animals}',
                        f'your {family_members} beat you with a {additions} {objects}',
                        f'this why your pet {animals} started {actions_standalone} your {additions} {family_members}',
                        f'your {family_members} caught you eating leftover {foods} and started {actions_standalone} you',
                        f'you tried riding a {objects} and fell over and got {actions_by_a} {animals} dressed up as a {foods}',
                        f'yo ass got {actions_by_a} {races} {insects}',
                        f'you got {actions_by_a} {additions} version of {names}',
                        f'you tried {actions_standalone} your {numbers} {time_type} old {family_members}',
                        f'you look like a {additions} version of your {numbers} {time_type} old {family_members}',
                        f'you sound like a {races} {animals} when you sing yo ass said {quotes}',
                        f'yo {races} {family_members} walked in the room and caught you {actions_standalone} your {additions} pet {animals} and started {actions_standalone} you',
                        f'and then you got {actions_by_a} {races} {animals} with a {materials} {bpchoose}',
                        f'yo {family_members} is in the hospital cuz you tried {actions_standalone} on them',
                        f'you got {actions_by} your {races} pet {animals} and now your {appearance} looks like a {additions} {objects}',
                        f'{filler}']

      packgen_choose_combo = random.choice(packgen_combos)

      with open('packs.txt', 'a') as output:
        output.write(f'\n{packgen_choose_combo}')
      
      match discord:
        case 'y' | True:
          packgen_post_url = f'https://discord.com/api/v9/channels/{channel}/messages'
          packgen_post_request = requests.post(packgen_post_url, headers={'authorization': token}, data={'content': {packgen_choose_combo}})

          match packgen_post_request.status_code:
            case 200:
              print(f'{front} Sent {packgen_choose_combo}')
            case 429:
              print(f'{front} Ratelimited, retrying')
            case 401:
              print(f'{front} Invalid token or channel ID')
          
          time.sleep(delay)

        case _:
          print(f'{front} {packgen_choose_combo}')

  except KeyboardInterrupt:
    startup()

def topicgen(): # 11

  try:
    clear_screen()
    print(dashboard_topicgen)

    match live_mode:
      case True:
        discord = str(input(f'{front} Discord Functionality? (y/n): '))
        match discord:
          case 'y' | 'Y':
            channel = int(input(f'{front} Channel: '))
            token = str(input(f'{front} Token: '))
            delay = int(input(f'{front} Delay: '))
        
          case _:
            delay = int(input(f'{front} Delay: '))

      case False:
        channel = settings.get('channel')
        token = settings.get('token')
        delay = settings.get('delay')
        discord = settings.get('discord')

    while True:

      actions_by_a = random.choice(open('lists/wordlists/actions/actions_by_a.txt', 'r').readlines()).strip()
      actions_by = random.choice(open('lists/wordlists/actions/actions_by.txt', 'r').readlines()).strip()
      actions_standalone = random.choice(open('lists/wordlists/actions/actions_standalone.txt', 'r').readlines()).strip()
      additions = random.choice(open('lists/wordlists/additions/additions.txt', 'r').readlines()).strip()
      additions2 = random.choice(open('lists/wordlists/additions/additions2.txt', 'r').readlines()).strip()
      animals = random.choice(open('lists/wordlists/objects_misc/animals.txt', 'r').readlines()).strip()
      bodyparts_external = random.choice(open('lists/wordlists/objects_misc/bodyparts_external.txt', 'r').readlines()).strip()
      bodyparts_internal = random.choice(open('lists/wordlists/objects_misc/bodyparts_internal.txt', 'r').readlines()).strip()
      characters = random.choice(open('lists/wordlists/lists/characters.txt', 'r').readlines()).strip()
      family_members = random.choice(open('lists/wordlists/lists/family_members.txt', 'r').readlines()).strip()
      foods = random.choice(open('lists/wordlists/objects_misc/foods.txt', 'r').readlines()).strip()
      insects = random.choice(open('lists/wordlists/objects_misc/insects.txt', 'r').readlines()).strip()
      materials = random.choice(open('lists/wordlists/objects_misc/materials.txt', 'r').readlines()).strip()
      names = random.choice(open('lists/wordlists/lists/names.txt', 'r').readlines()).strip()
      numbers = random.choice(open('lists/wordlists/person/numbers.txt', 'r').readlines()).strip()
      objects = random.choice(open('lists/wordlists/objects_misc/objects.txt', 'r').readlines()).strip()
      races = random.choice(open('lists/wordlists/person/races.txt', 'r').readlines()).strip()
      time_type = random.choice(open('lists/wordlists/person/time_type.txt', 'r').readlines()).strip()
      quotes = random.choice(open('lists/wordlists/lists/quotes.txt', 'r').readlines()).strip()

      bp = (bodyparts_external, bodyparts_internal)
      bpchoose = random.choice(bp)

      topics = [f'{actions_standalone} {races} {bpchoose}', f'{characters} {foods} {insects} {actions_standalone}', f'{family_members} {numbers}{time_type} {quotes} ', f'{actions_standalone} {objects} {races}', f'{names} {insects} {actions_standalone}', f'{additions} {family_members} {quotes}']

      choose_topic = random.choice(topics)

      with open('topics.txt', 'a') as output:
        output.write(f'\n{choose_topic}')
      
      match discord:
        case True | 'y':
          packgen_post_url = f'https://discord.com/api/v9/channels/{channel}/messages'
          packgen_post_request = requests.post(packgen_post_url, headers={'authorization': token}, data={'content': {choose_topic}})

          match packgen_post_request.status_code:
            case 200:
              print(f'{front} Sent {choose_topic}')
            case 429:
              print(f'{front} Ratelimited, retrying')
            case 401:
              print(f'{front} Invalid token or channel ID')
          time.sleep(delay)

        case _:
          print(f'{front} {choose_topic}')  

  except KeyboardInterrupt:
    startup()

def anti_packgen(): # 12
  try:
    clear_screen()
    print(dashboard_anti_packgen)

    match live_mode:
        case True:
          discord = str(input(f'{front} Discord functionality (y/n): '))
          match discord:
            case 'y' | 'Y':

              token = str(input(f'{front} Token: '))
              channel = int(input(f'{front} Channel: '))

            case _:
              token = settings.get('token')
              channel = settings.get('channel')

        case _:
          token = settings.get('token')
          channel = settings.get('channel')

    while True:
      actions_by_a = random.choice(open('lists/wordlists/actions/actions_by_a.txt', 'r').readlines()).strip()
      actions_by = random.choice(open('lists/wordlists/actions/actions_by.txt', 'r').readlines()).strip()
      actions_standalone = random.choice(open('lists/wordlists/actions/actions_standalone.txt', 'r').readlines()).strip()
      additions = random.choice(open('lists/wordlists/additions/additions.txt', 'r').readlines()).strip()
      additions2 = random.choice(open('lists/wordlists/additions/additions2.txt', 'r').readlines()).strip()
      animals = random.choice(open('lists/wordlists/objects_misc/animals.txt', 'r').readlines()).strip()
      bodyparts_external = random.choice(open('lists/wordlists/objects_misc/bodyparts_external.txt', 'r').readlines()).strip()
      bodyparts_internal = random.choice(open('lists/wordlists/objects_misc/bodyparts_internal.txt', 'r').readlines()).strip()
      characters = random.choice(open('lists/wordlists/lists/characters.txt', 'r').readlines()).strip()
      family_members = random.choice(open('lists/wordlists/lists/family_members.txt', 'r').readlines()).strip()
      foods = random.choice(open('lists/wordlists/objects_misc/foods.txt', 'r').readlines()).strip()
      insects = random.choice(open('lists/wordlists/objects_misc/insects.txt', 'r').readlines()).strip()
      materials = random.choice(open('lists/wordlists/objects_misc/materials.txt', 'r').readlines()).strip()
      names = random.choice(open('lists/wordlists/lists/names.txt', 'r').readlines()).strip()
      numbers = random.choice(open('lists/wordlists/person/numbers.txt', 'r').readlines()).strip()
      objects = random.choice(open('lists/wordlists/objects_misc/objects.txt', 'r').readlines()).strip()
      races = random.choice(open('lists/wordlists/person/races.txt', 'r').readlines()).strip()
      time_type = random.choice(open('lists/wordlists/person/time_type.txt', 'r').readlines()).strip()
      quotes = random.choice(open('lists/wordlists/lists/quotes.txt', 'r').readlines()).strip()

      bp = (bodyparts_external, bodyparts_internal)
      bpchoose = random.choice(bp)
      
      clear_screen()
      print(dashboard_anti_packgen)
      user_prompt = int(input('What kind of word are you being checked for? (1=object, 2=character, 3=animal): '))


      match user_prompt:

        case 1:
          object_name = input(f'{front} Object name: ')
          object_combos = [
            f'tell me why your {family_members} got {actions_by_a} {additions} {object_name}', 
            f'you got caught tryna {additions2} with your {additions} {family_members}s {object_name}',
            f'your {family_members} got {actions_by_a} {object_name}',
            f'your {family_members} beat you with a {additions} {object_name}',
            f'you tried riding a {object_name} and fell over and got {actions_by_a} {animals} dressed up as a {foods}']
          
          object_combo_choose = random.choice(object_combos)
          match discord:
            case 'y' | 'Y':

              anti_packgen_post_url = f'https://discord.com/api/v9/channels/{channel}/messages'

              anti_packgen_post_request = requests.post(anti_packgen_post_url, headers={'authorization': token}, data={'content': object_combo_choose})

              match anti_packgen_post_request.status_code:
                case 200:

                  input(f'{front} Sent: {object_combo_choose}')

            case _:
              input(f'{front} {object_combo_choose}')

        case 2:
          character_name = input(f'{front} Character name: ')
          character_combos = [
            f'yo ass got {actions_by_a} {additions} version of {character_name}',
            f'and then you got {actions_by_a} {races} version of {character_name}',
            f'nah cuz tell me why you built like a {races} {character_name} with a {materials} {bpchoose}']
          
          character_combo_choose = random.choice(character_combos)

          match discord:
            case 'y' | 'Y':

              anti_packgen_post_url = f'https://discord.com/api/v9/channels/{channel}/messages'

              anti_packgen_post_request = requests.post(anti_packgen_post_url, headers={'authorization': token}, data={'content': character_combo_choose})

              match anti_packgen_post_request.status_code:
                case 200:
                  input(f'{front} Sent: {character_combo_choose}')

            case _:
              input(f'{front} {character_combo_choose}')

        case 3:
          animal_name = input(f'{front} Animal name: ')
          animal_combos = [
            f'i walked in the room and saw you get {actions_by_a} {additions} {animal_name}',
            f'your {family_members} got caught tryna {additions2} your {additions} pet {animal_name}',
            f'this why your pet {animal_name} started {actions_standalone} your {additions} {family_members}',
            f'you tried riding a {objects} and fell over and got {actions_by_a} {animal_name} dressed up as a {foods}',
            f'you sound like a {races} {animal_name} when you sing yo ass said {quotes}',
            f'yo {races} {family_members} walked in the room and caught you {actions_standalone} your {additions} pet {animal_name} and started {actions_standalone} you',
            f'and then you got {actions_by_a} {races} {animal_name} with a {materials} {bpchoose}']
          
          animal_combo_choose = random.choice(animal_combos)

          match discord:
            case 'y' | 'Y':

              anti_packgen_post_url = f'https://discord.com/api/v9/channels/{channel}/messages'

              anti_packgen_post_request = requests.post(anti_packgen_post_url, headers={'authorization': token}, data={'content': animal_combo_choose})
              
              match anti_packgen_post_request.status_code:
                case 200:
                  input(f'{front} Sent: {animal_combo_choose}')

            case _:
              input(f'{front} {animal_combo_choose}')
    
  except KeyboardInterrupt:
    startup()

def friend_users(): # 13
  try:
    clear_screen()
    print(dashboard_friend_users)

    token_list = open('lists/tokens.txt').readlines()
    id_list = open('lists/ids.txt').readlines()
    for token in token_list:
        
      for id in id_list:
          add_users_put_url = f'https://discord.com/api/v9/users/@me/relationships/{id}'
          add_users_headers = {
              "accept": "*/*",
              "accept-language": "en-US,en;q=0.9",
              "authorization": token,
              "content-type": "application/json",
              "sec-ch-ua": "\"Not_A Brand\";v=\"99\", \"Brave\";v=\"109\", \"Chromium\";v=\"109\"",
              "sec-ch-ua-mobile": "?0",
              "sec-ch-ua-platform": "\"Windows\"",
              "sec-fetch-dest": "empty",
              "sec-fetch-mode": "cors",
              "sec-fetch-site": "same-origin",
              "sec-gpc": "1",
              "x-context-properties": "eyJsb2NhdGlvbiI6IkNvbnRleHRNZW51In0=",
              "x-debug-options": "bugReporterEnabled",
              "x-discord-locale": "en-US"
              }

          body = {}

          add_users_put_request = requests.put(add_users_put_url, headers=add_users_headers, json=body)

          match add_users_put_request.status_code:
            case 204:
              print(f'{front} Added {id}')

            case 400:
              print(f'{front} Already added this ID, {id}')

            case 429:
                print(f'{front} Being ratelimited')

            case 401:
                print(f'{front} Invalid token or user ID')

            case _:
              print(f'{front} Unknown status code, report this code to byte#6110 | Code: {add_users_put_request.status_code}')
        
      input(f'{front} Adder done, press enter to return to main menu.')
      startup()

  except KeyboardInterrupt:
    startup()

def anti_trap(): 
    try:
        clear_screen()
        print(dashboard_anti_trap)
        anti_trap_dm_url = 'https://discord.com/api/v10/users/@me/channels'
        match live_mode:
            case True:
                token = str(input(f'{front} Token: '))
                delay = int(input(f'{front} Delay: '))
            case _:
                token = settings.get('token')
                delay = settings.get('delay')

        logged_useranmes = set()
        logged_groups = set()

        while True:
            anti_trap_get_request = requests.get(anti_trap_dm_url, headers={'authorization': token})
            match anti_trap_get_request.status_code:
                case 200:
                    anti_trap_get_request_json = anti_trap_get_request.json()

                    for dms in anti_trap_get_request_json:
                        group_name = dms.get("name")

                        if "recipients" in dms:
                            usernames = []
                            for recipient in dms["recipients"]:

                                if "username" in recipient and "discriminator" in recipient:

                                    username = recipient["username"]
                                    discriminator = recipient["discriminator"]
                                    user = f'{username}#{discriminator}'

                                    if user not in logged_useranmes:
                                        usernames.append(user)
                                        logged_useranmes.add(user)

                            if group_name == 'None':
                                print(", ".join(usernames))
                            else:
                                print(f'{group_name}: {", ".join(usernames)}')
                case _:
                    print(anti_trap_get_request.status_code)
                    break
            time.sleep(delay)
    except KeyboardInterrupt:
        clear_screen()
        sys.exit()



def descriptions(): # help
  try:
    
    def help_page():
      clear_screen()
      print(dashboard_help)

      page = str(input(f'{front} Press P to go the previous page or X to go back to main menu: '))

      match page:
        case 'N' | 'n':
          information_page()

        case 'X' | 'x':
          startup()
        
        case _:
          startup()

    def information_page():
      clear_screen()
      print(dashboard_information)
      page = str(input(f'{front} Press P to go the previous page or X to go back to main menu: '))

      match page:
        case 'P' | 'p':
          help_page()

        case _:
          startup()


    help_page()
    

  except KeyboardInterrupt:
    clear_screen()
    startup()


# -------- Scripts -------- #

# -------- On Start -------- #

if __name__ == '__main__':
  startup()

# -------- On Start -------- #
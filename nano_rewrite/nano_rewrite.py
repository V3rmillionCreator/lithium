# -------- Import Modules -------- #

import random, os, sys, json, time, requests, asyncio
import discord
from discord.ext import commands
from discord.utils import get

# -------- Import Modules -------- #


# -------- Import Artwork -------- #

dashboard = open('lists/artwork/dashboard.txt', encoding='utf-8').read()

dashboard_afk_check = open('lists/artwork/dashboard_afk_check.txt', encoding='utf-8').read()
dashboard_afk_alert = open('lists/artwork/dashboard_afk_alert.txt', encoding='utf-8').read()
dashboard_auto_pressure = open('lists/artwork/dashboard_auto_pressure.txt', encoding='utf-8').read()
dashboard_options = open('lists/artwork/dashboard_options.txt', encoding='utf-8').read()

dashboard_packgen = open('lists/artwork/dashboard_packgen.txt', encoding='utf-8').read()
dashboard_topicgen = open('lists/artwork/dashboard_topicgen.txt', encoding='utf-8').read()
dashboard_anti_packgen = open('lists/artwork/dashboard_anti_packgen.txt', encoding='utf-8').read()

dashboard_crasher = open('lists/artwork/dashboard_crasher.txt', encoding='utf-8').read()

dashboard_gc_botnet = open('lists/artwork/dashboard_gc_botnet.txt', encoding='utf-8').read()
dashboard_add_users = open('lists/artwork/dashboard_add_users.txt', encoding='utf-8').read()
dashboard_gc_bomber = open('lists/artwork/dashboard_gc_bomber.txt', encoding='utf-8').read()
dashboard_bulk_delete = open('lists/artwork/dashboard_bulk_delete.txt', encoding='utf-8').read()

dashboard_gc_smasher = open('lists/artwork/dashboard_gc_smasher.txt', encoding='utf-8').read()


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
        afk_check()

      case '3':
        afk_alert()

      case '4':
        packgen()

      case '5':
        topicgen()

      case '6':
        anti_packgen()
      
      case '7':
        crasher()
      
      case '8':
        gc_botnet()

      case '9':
        add_users()

      case '10':
        gc_bomber()

      case '11':
        bulk_delete()

      case '12':
        gc_smasher()

      case _:
        startup()
  
  except KeyboardInterrupt:

    clear_screen()
      
# -------- System Functions -------- #


# -------- Scripts -------- #

def auto_pressure():
  try:
    clear_screen()
    print(dashboard_auto_pressure)

    if live_mode == True:
      channel = int(input(f'{front} Channel: '))
      delay = int(input(f'{front} Delay: '))

      token = settings.get('token')
    
    else:
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

def afk_check():
  try:
    clear_screen()
    print(dashboard_afk_check)

    if live_mode == True:
      channel = int(input(f'{front} Channel: '))

      invisible_ping = (str(input(f'{front} Invisible Ping (y/n): ')))

      if invisible_ping == 'y':
          victim = int(input(f'{front} Victim (ID): '))

      delay = int(input(f'{front} Delay: '))


    else:
      token = settings.get('token')
      channel = settings.get('channel')
      delay = settings.get('delay')
      invisible_ping = settings.get('invisible_ping')
      victim = settings.get('victim')

    while True:
        token = settings.get('token')

        up_to = int(input(f'{front} How far do you want to count to?: '))

        afk_check_url = f'https://discord.com/api/v9/channels/{channel}/messages'

        i = 0
        while i < up_to:
          if invisible_ping == 'y':
            afk_check_post = requests.post(afk_check_url, headers={'authorization': token}, data={'content': f'{i+1}{invisible_ping_text}<@{victim}>'})
          
          elif invisible_ping:
            afk_check_post = requests.post(afk_check_url, headers={'authorization': token}, data={'content': f'{i+1}'})
            
          match afk_check_post.status_code:
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

def afk_alert():
    clear_screen()
    print(dashboard_afk_alert)

    match live_mode:
      case True:
        delay = int(input(f'{front} Delay: '))
        your_webhook = str(input('Webhook link: '))
        token = settings.get('token')

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
                                if alerts == True:
                                  afk_alert_post_webhook_data = {"content": f"<@{your_id}>", "embeds": [{"title": f"you're being afk checked by {afk_alert_dm_message_username}#{afk_alert_dm_message_discriminator}", "color": 16711874, "footer": {"text": "sent from nano"}, "image": {"url": "https://media.tenor.com/K3knqTMuD1oAAAAC/rwk-priest-crow.gif"}}],"attachments": []}
                                  afk_alert_post_webhook = requests.post(your_webhook, json=afk_alert_post_webhook_data)
            time.sleep(delay) 

    except KeyboardInterrupt:
        startup()

def packgen():
  try:
      
    clear_screen()
    print(dashboard_packgen)

    match live_mode:
      case True:
        discord = str(input(f'{front} Discord Functionality? (y/n): '))

        match discord:
          case 'y':
            channel = int(input(f'{front} Channel: '))
            delay = int(input(f'{front} Delay: '))

            token = settings.get('token')

          case 'n':
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
                        f'you got {actions_by} your {races} pet {animals} and now your {appearance} looks like a {additions} {objects}'] 
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

def topicgen():

  try:
    clear_screen()
    print(dashboard_topicgen)

    match live_mode:
      case True:
        discord = str(input(f'{front} Discord Functionality? (y/n): '))
        match discord:
          case 'y':
            channel = int(input(f'{front} Channel: '))
            token = settings.get('token')
        
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

def anti_packgen():
  try:
    clear_screen()
    print(dashboard_anti_packgen)

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

          input(f'{front} {object_combo_choose}')
          clear_screen()
          print(dashboard_anti_packgen)

        case 2:
          character_name = input(f'{front} Character name: ')
          character_combos = [
            f'yo ass got {actions_by_a} {additions} version of {character_name}',
            f'and then you got {actions_by_a} {races} version of {character_name}',
            f'nah cuz tell me why you built like a {races} {character_name} with a {materials} {bpchoose}']
          
          character_combo_choose = random.choice(character_combos)

          input(f'{front} {character_combo_choose}')
          clear_screen()
          print(dashboard_anti_packgen)

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

          input(f'{front} {animal_combo_choose}')
          clear_screen()
          print(dashboard_anti_packgen)
    
  except KeyboardInterrupt:
    startup()

def crasher():
  try:
    clear_screen()
    print(dashboard_crasher)

    match live_mode:
      case True:
        channel = int(input(f'{front} Channel: '))
        token = settings.get('token')
        
        delay = int(input(f'{front} Delay: '))

      case False:
        channel = settings.get('channel')
        token = settings.get('token')
        delay = settings.get('delay')

    while True:
      clear_screen()
      print(dashboard_crasher)


      crasher_channel_post_url = f'https://discord.com/api/v9/channels/{channel}/messages'
      crasher_text = '||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|||'

      crasher_append = input(f'{front} Message (limit 50): ')

      crasher_post_request = requests.post(crasher_channel_post_url, headers={'authorization': token}, data={'content': crasher_append + crasher_text})

      match crasher_post_request.status_code:
        case 200:
          input(f'{front} Sent {crasher_append}')

      time.sleep(delay)

  except KeyboardInterrupt:
    startup()

def gc_botnet():
    try:

      clear_screen()
      print(dashboard_gc_botnet)

      match live_mode:
        case True:
          channel = int(input(f'{front} Group ID: '))
          token = settings.get('token')
        
        case False:
          channel = settings.get('channel')
          token = settings.get('token')

      ids = open('lists/groupchat_lists/gc_botnet/gc_botnet_ids.txt').readlines()
      tokens = open('lists/groupchat_lists/gc_botnet/gc_botnet_tokens.txt').readlines()
      while True:

        for token in tokens:

          for id in ids:
              
              gc_botnet_target = f'https://discord.com/api/v9/channels/{channel}/recipients/{ids}'
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

def add_users():
  try:
    clear_screen()
    print(dashboard_add_users)

    token = input(f'{front} Token: ')
    ids = open('lists/groupchat_lists/gc_botnet/gc_botnet_ids.txt').readlines()

    for id in ids:
        add_users_put_url = f'https://discord.com/api/v9/users/@me/relationships/{id.strip()}'
        add_users_headers = {
            'accept': '*/*',
            'accept-language': 'en-GB',
            'authorization': token,
            'content-type': 'application/json',
            'sec-ch-ua': '\' Not A;Brand\';v=\'99\', \'Chromium\';v=\'102\'',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '\'Linux\'',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'x-context-properties': 'eyJsb2NhdGlvbiI6IlVzZXIgUHJvZmlsZSJ9',
            'x-debug-options': 'bugReporterEnabled',
            'x-discord-locale': 'en-US'
            }

        body = {}

        add_users_put_request = requests.put(add_users_put_url, headers=add_users_headers, json=body)

        match add_users_put_request.status_code:
          case 204:
            print(f'{front} Added {ids}')

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

def gc_bomber():
  try:
    clear_screen()
    print(dashboard_gc_bomber)
    match live_mode:
      case True:
        channel = int(input(f'{front} Group ID: '))

        token = settings.get('token')
      case False:
        channel = settings.get('channel')
        token = settings.get('token')

    ids = open('lists/groupchat_lists/gc_bomber/gc_bomber_targets.txt').readlines()
    
    for id in ids:


      gc_bomber_url = f'https://discord.com/api/v9/channels/1065898767376723968/recipients/{id.strip()}'
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

def bulk_delete():
  try:
    nano = commands.Bot(command_prefix='', self_bot=True, help_command=None)
    clear_screen()
    print(dashboard_bulk_delete)
    print(f'{front} Type "lol" in the channel you want to delete messages in')

    @nano.command()
    async def lol(channel):
        async for msg in channel.message.channel.history(limit=int(9999999)):
            if msg.author.id == nano.user.id:
                time.sleep(0.1)
                try:
                    await msg.delete()
                    print(f'{front} Deleted')
                except:
                    continue
    nano.run(token)

  except KeyboardInterrupt:
    startup()

def gc_smasher():
  try:
    clear_screen()
    print(dashboard_gc_smasher)
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

# -------- Scripts -------- #

# -------- On Start -------- #

if __name__ == '__main__':
  startup()

# -------- On Start -------- #
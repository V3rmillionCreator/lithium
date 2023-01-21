import random, os, sys, json, time, pyperclip, requests

class Nano():
    def __init__(self):
        self.actions_by_a = random.choice(open('wordlists/actions/actions_by_a.txt', 'r').readlines()).strip()
        self.actions_by = random.choice(open('wordlists/actions/actions_by.txt', 'r').readlines()).strip()
        self.actions_standalone = random.choice(open('wordlists/actions/actions_standalone.txt', 'r').readlines()).strip()
        self.additions = random.choice(open('wordlists/additions/additions.txt', 'r').readlines()).strip()
        self.additions2 = random.choice(open('wordlists/additions/additions2.txt', 'r').readlines()).strip()
        self.animals = random.choice(open('wordlists/objects_misc/animals.txt', 'r').readlines()).strip()
        self.bodyparts_external = random.choice(open('wordlists/objects_misc/bodyparts_external.txt', 'r').readlines()).strip()
        self.bodyparts_internal = random.choice(open('wordlists/objects_misc/bodyparts_internal.txt', 'r').readlines()).strip()
        self.characters = random.choice(open('wordlists/lists/characters.txt', 'r').readlines()).strip()
        self.family_members = random.choice(open('wordlists/lists/family_members.txt', 'r').readlines()).strip()
        self.foods = random.choice(open('wordlists/objects_misc/foods.txt', 'r').readlines()).strip()
        self.insects = random.choice(open('wordlists/objects_misc/insects.txt', 'r').readlines()).strip()
        self.materials = random.choice(open('wordlists/objects_misc/materials.txt', 'r').readlines()).strip()
        self.names = random.choice(open('wordlists/lists/names.txt', 'r').readlines()).strip()
        self.numbers = random.choice(open('wordlists/person/numbers.txt', 'r').readlines()).strip()
        self.objects = random.choice(open('wordlists/objects_misc/objects.txt', 'r').readlines()).strip()
        self.races = random.choice(open('wordlists/person/races.txt', 'r').readlines()).strip()
        self.time_type = random.choice(open('wordlists/person/time_type.txt', 'r').readlines()).strip()
        self.quotes = random.choice(open('wordlists/lists/quotes.txt', 'r').readlines()).strip()

        self.bp = (self.bodyparts_external, self.bodyparts_internal)
        self.bpchoose = random.choice(self.bp)

        with open('settings.json', 'r') as self.config:
            self.self.settings = json.load(self.config)

            self.live_mode = self.settings.get('live_mode')

            self.token = self.settings.get('token')
            self.front = self.settings.get('front')
            self.your_webhook = self.settings.get('your_webhook')

            self.delay = self.settings.get('delay')
            self.your_id = self.settings.get('your_id')
            self.channel = self.settings.get('channel')
            self.victim = self.settings.get('victim')

            self.invisible_ping = self.settings.get('invisible_ping')
            self.alerts = self.settings.get('alerts')
        
        self.invisible_ping_text = '||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||'

        self.dashboard = open('artwork/dashboard.txt').read()
        self.dashboard_afk_check = open('artwork/dashboard_afk_check.txt').read()
        self.dashboard_afk_alert = open('artwork/dashboard_afk_alert.txt').read()
        self.dashboard_auto_pressure = open('artwork/dashboard_auto_pressure.txt').read()
        self.dashboard_options = open('artwork/dashboard_options.txt').read()
        self.dashboard_packgen = open('artwork/dashboard_packgen.txt').read()
        self.dashboard_topicgen = open('artwork/dashboard_topicgen.txt').read()
        self.dashboard_anti_packgen = open('artwork/dashboard_anti_packgen.txt').read()

        def clear_screen(self):
            kernel = sys.platform
            match kernel:
                case 'linux':
                    os.system('clear')
                case _:
                    os.system('cls')

    def startup(self):
        try:

            self.clear_screen()
            print(self.dashboard)
            print(self.dashboard_options)
            script_choice = input('\nWhat script would you like to run? 1/2/3/4/5/6: ')
            match script_choice:
                case '1':
                    auto_pressure(self)

                case '2':
                    afk_check(self)

                case '3':
                    afk_alert(self)

                case '4':
                    packgen(self)

                case '5':
                    topicgen(self)

                case '6':
                    anti_packgen(self)

                case _:
                    startup()

        except KeyboardInterrupt:
            self.clear_screen()

        def auto_pressure(self):                        
            try:
                self.clear_screen()
                print(self.dashboard_auto_pressure)

                if self.live_mode == True:
                    channel = int(input(f'{self.front} Channel: '))
                    token = input(f'{self.front} Token: ')
                    delay = int(input(f'{self.front} Delay: '))
                
                else:
                    channel = self.settings.get('channel')
                    token = self.settings.get('token')
                    delay = self.settings.get('delay')

                while True:
                    auto_pressure_sent_messages = []
                    auto_pressure_url = f'https://discord.com/api/v9/channels/{channel}/messages'

                    auto_pressure_list = random.choice(open('auto_pressure_lists/pressure.txt', 'r').readlines())

                    auto_pressure_files = [auto_pressure_list]

                    auto_pressure_choose = random.choice(auto_pressure_files)

                    if auto_pressure_choose in auto_pressure_sent_messages:
                        return auto_pressure_choose
                    auto_pressure_post = requests.post(auto_pressure_url, headers={'authorization': token}, data={'content': auto_pressure_choose})
                    
                    match auto_pressure_post.status_code:

                        case 200:
                            print(f'{self.front} Sent: {auto_pressure_choose}')
                    
                        case 429:
                            print(f'{self.front} Ratelimited, retrying')
                        
                        case 401:
                            print(f'{self.front} Invalid token or channel ID')

                    time.sleep(delay)

            except KeyboardInterrupt:
                startup()

if __name__ == '__main__':
    my_nano = Nano()
    my_nano.startup()

def gc_botnet():
    try:
        clear_screen()
        print(dashboard_gc_botnet)
        if live_mode == True:
            channel = int(input(f'{front} Channel: '))
            token = input(f'{front} Token: ')
            delay = int(input(f'{front} Delay: '))
        else:
            channel = settings.get('channel')
            token = settings.get('token')
            delay = settings.get('delay')

        ids = open('gc_botnet.txt').readlines()
        num_lines = len(ids) # numl

        i = 0
        while i < num_lines:
            user_id = ids[i].strip() 
            gc_botnet_user_data = f'https://discord.com/api/v9/users/{user_id}'
            headers = {'Authorization': token}
            response = requests.get(gc_botnet_user_data, headers=headers)

            if response.status_code == 200:
                data = response.json()
                user_username = data['username']
                user_discriminator = data['discriminator']

                gc_locker_target = f'https://discord.com/api/v9/channels/{channel}/recipients/{user_id}'
                gc_locker_put_request = requests.put(gc_locker_target, headers={'authorization': token})

                if gc_locker_put_request.status_code in [204, 200]:
                    print(f'{front} Added {user_username}#{user_discriminator}')

                elif gc_locker_put_request.status_code == 429:
                    print(f'{front} Being ratelimited, waiting 2.5 seconds')
                    time.sleep(2.5)
                time.sleep(delay)
                i += 1
            else:
                print(f'{front} Invalid User ID')
                i += 1
    except KeyboardInterrupt:
        startup()



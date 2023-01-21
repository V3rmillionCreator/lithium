while i < up_to:
        if invisible_ping:
          afk_check_post = requests.post(afk_check_url, headers={'authorization': token}, data={'content': f'{i}{invisible_ping_text}<@{victim}>'})
        else:
          afk_check_post = requests.post(afk_check_url, headers={'authorization': token}, data={'content': f'{i}'})

        if afk_check_post.status_code == 200:
          print(f'{front} Sent {i}')
          i += 1
          time.sleep(delay)

        elif afk_check_post.status_code == 429:
          print(f'{front} Ratelimited, retrying')
        elif afk_check_post.status_code == 401:
          print(f'{front} Invalid token or channel ID')
          break



match invisible_ping:
    case True:
        afk_check_post = requests.post(afk_check_url, headers={'authorization': token}, data={'content': f'{i}{invisible_ping_text}<@{victim}>'})
        
    case False:
        afk_check_post = requests.post(afk_check_url, headers={'authorization': token}, data={'content': f'{i}'})

match afk_check_post.status_code:
    case 200:

        print(f'{front} Sent {i}')
        i += 1
        time.sleep(delay)
    
    case 429:
        print(f'{front} Ratelimited, retrying')

    case 401:
        print(f'{front} Invalid token or channel ID')
        break


match live_mode:

      case True:
        print(f'{front} Invisible Ping (true/false): ')
        invisible_ping = bool(input(''))
        
        match invisible_ping:
          case True:
            print(f'{front} Victim:')
            victim = int(input(''))

          case False:
            break

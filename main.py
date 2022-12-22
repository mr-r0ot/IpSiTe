import os
try:
    import time, socket, sys, shutil
    from rich.console import Console
    import pyperclip
except:
    upg = input("Your Not Install Lirary, Do You Install Librarys? (n/y): ")
    if upg == 'y' or upg == 'Y':
        os.system("python -m pip install rich")
        os.system("python -m pip install pyperclip")
        os.system("python -m pip install shutil")
    import time, socket, sys, shutil
    from rich.console import Console
    import pyperclip
# ===================================================================================================



if os.name == 'nt':
    os.system('color A')
    os.system("title IpSiTe") 
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
def slash_system():
    if os.name == 'nt':
        ccvf = "\ "
        return ccvf[:-1]
    else:
        return "/"
#color
class color:
    red = '\033[91m'
    sabz = '\033[92m'
    sefid = '\033[0m'
    narenji = '\033[93m'
    abi_kamrang = '\033[94m'
path = os.getcwd()
clear_screen()



def gis(site):
    clear_screen()
    try:
        socket.gethostbyname("google.com")


        console.print("  #################################################", style="bold blue")
        console.print("  #           @$#          $#&#$                  #", style="bold red")
        console.print("  #           @$*          %&    $                #", style="bold blue")
        console.print("  #           $$%          @%   &                 #", style="bold red")
        console.print("  #           !$%          $$ $                   #", style="bold blue")
        console.print("  #           #$$          $^                     #", style="bold red")
        console.print("  #           $#$          $#                     #", style="bold blue")
        console.print("  #           $%#          &!             IpSiTe  #", style="bold red")
        console.print("  #################################################", style="bold blue")
        print("\n\n\n")
        mod = input("Show Ip Target By   Script  Or  Web(s/w): ")
        if mod.lower() == 's':
            try:
                ip = socket.gethostbyname(site)
                dns_server = []
                try:
                    dns_server = socket.gethostbyaddr(site)
                except:
                    dns_server.append("Error Geting Ip Target!")
                console.print("\n  ###############################################", style="bold green")
                console.print("\n  #                                             #", style="bold green")
                console.print("\n  # your ip addres :  {}".format(str(ip)), style="bold green")
                console.print("\n  # doamin name :  {}".format(str(site)), style="bold green")
                try:
                    for ii in dns_server:
                        console.print("\n  # dns server :  {}".format(str(ii)), style="bold green")
                except:
                    pass
                console.print("\n\n  #                   by IpSiTe                 #", style="bold green")
                console.print("\n  ###############################################", style="bold green")
                input("\n\n\n\n\t  Enter for close ")
                clear_screen()
            except:
                print("Error  not find site")
                time.sleep(1.5)
                clear_screen()
        elif mod.lower() == 'w':
            try:
                ip = socket.gethostbyname(site)
                try:
                    dns_serverwww = socket.gethostbyaddr(site)
                except:
                    dns_serverwww = ["Error Geting Ip Target!"]
                web = open("Show-Web.html", "w+")
                web.write('''
<!DOCTYPE html><html long="en-US"><head><titele style="color:rgb(255, 255, 255);">Show Ip Target By DarkUp</titele><meta charset="UTF-8"></head><body style="background-color:rgb(1, 0, 1);"></body>

<h1 style="color:rgb(178, 130, 209);font-family:arial;font-size:500%;text-align:center;">Your Ip Target Is</h1>

<h1 style="color:rgb(37, 207, 219);font-family:arial;font-size:400%;text-align:center;">'''+str(ip)+'''</h1>

<h1 style="color:rgb(178, 130, 209);font-family:arial;font-size:250%;text-align:center;">By DarkUp</h1>

<br><br><br><br><br>
<h1 style="color:rgb(178, 130, 209);font-family:arial;font-size:500%;text-align:center;">Your Dns Target Is</h1>

''')
                try:
                        web.write('''
<h1 style="color:rgb(37, 207, 219);font-family:arial;font-size:400%;text-align:center;">'''+str(dns_serverwww)+'''</h1>

<h1 style="color:rgb(178, 130, 209);font-family:arial;font-size:250%;text-align:center;">By DarkUp</h1>

''')
                except:
                    pass

                web.write('''
<br><br><br><br><br>
<h1 style="color:rgb(176, 243, 232);font-family:arial;font-size:100%;">Your Target Is: '''+str(site)+'''</h1>
<h1 style="color:rgb(176, 243, 232);font-family:arial;font-size:100%;">Your Ip Target Is: '''+str(ip)+'''</h1>
<h1 style="color:rgb(176, 243, 232);font-family:arial;font-size:100%;">Site Target IS: On</h1>

</body>
</html>''')
                web.close()
                os.startfile("Show-Web.html")
                clear_screen()
            except:
                print("Error  not find site")
                time.sleep(1.5)
                clear_screen()

        else:
            print("\n\n\n\n Your Not Enter  s  or  w   !")
            clear_screen()
    

    except:
        print("  . . . . .  Your Not Connect To Net! . . . . . .\n")
        time.sleep(2.5)
        input("\n\n\n\n\t  Enter for close ")
        clear_screen()
# ===========================================================================================



Target = str(input(" Enter Target: ")
gis(site=Target)

import time
import os
import sys
import random
from colored import fg, attr

def alts():
    global run

    alts = '''Choice alt:
1. alt.bat
2. alt2.bat
3. alt3.bat
4. alt4.bat
5. alt5.bat
6. alt6.bat
7. alt7.bat
8. alt8.bat
9. alt9.bat
10.alt10.bat
            '''
    print(alts)

    user_choice = input(">>> ")

    if user_choice == "1" or user_choice == "2" or user_choice == "3" or user_choice == "4" or user_choice == "5" or user_choice == "6" or user_choice == "7" or user_choice == "8" or user_choice == "9" or user_choice == "10":
        run = True
        print("Args: --wf-l3=2 --dpi-desync=fake --dpi-desync-repeats=11 --dpi-desync-fooling=md5sig")
        time.sleep(1)
        print("[SC] CreateService SUCCESS")
        print("[SC] ChangeServiceConfig2 SUCCESS\n")
        time.sleep(3)
        print("SERVICE_NAME: zapret")
        print("        TYPE               : 10  WIN32_OWN_PROCESS")
        print("        STATE              : 4  RUNNING")
        print("                                (STOPPABLE, NOT_PAUSABLE, ACCEPTS_SHUTDOWN)")
        print("        WIN32_EXIT_CODE    : 0  (0x0)")
        print("        SERVICE_EXIT_CODE  : 0  (0x0)")
        print("        CHECKPOINT         : 0x0")
        print("        WAIT_HINT          : 0x0")
        print("        PID                : 34272")
        print("        FLAGS              :\n")
        print("The operation completed successfully.")
        print("Press any key to exit...")
        input()

def ralts():
    global run
    run = False
    print("The zapret service is stopping..")
    time.sleep(3)
    print("The zapret service was stopped successfully.")
    print()
    time.sleep(3)
    print("[SC] DeleteService SUCCESS")
    print()
    print("The WinDivert service was stopped successfully.")
    print()
    print("Press any key to exit...")
    input()

def check():
    global colors

    colors = {
        "green": fg("green"),
        "red": fg("red"),
        "reset": attr("reset"),
    }
    if run == True:
        print(f'Service strategy installed')
        time.sleep(0.1)
        print('"zapret" service is RUNNING.')
        time.sleep(0.1)
        print('"WinDivert" service is RUNNING.')
        time.sleep(0.5)
        print()
        print(colors["green"] + f"Bypass is RUNNING." + colors["reset"])
        input("Press any key to exit...")
    if run == False:
        print('"zapret" service is NOT running.')
        time.sleep(0.1)
        print('"WinDivert" service is NOT running.')
        time.sleep(0.1)
        print()
        print(colors["red"] + f"Bypass is NOT running." + colors["reset"])
        input("Press any key to exit...")

def gamef():
    global run
    global filter

    filters = '''Select game filter option:
  1.   Disable
  2.   TCP and UDP
  3.   TCP
  4.   UDP

  0. Exit
  '''
    print(filters)
    user_choice = input(">>> ")

    if user_choice == "1":
        filter = "disabled"
        print()
        print("Restart the zapret to apply the changes")
        input("Press any key to exit...")
        run = False
    elif user_choice == "2":
        filter = "TCP and UDP"
        print()
        print("Restart the zapret to apply the changes")
        input("Press any key to exit...")
        run = False
    elif user_choice == "3":
        filter = "TCP"
        print()
        print("Restart the zapret to apply the changes")
        input("Press any key to exit...")
        run = False
    elif user_choice == "4":
        filter = "UDP"
        print()
        print("Restart the zapret to apply the changes")
        input("Press any key to exit...")
        run = False
    elif user_choice == "0":
        os.system('cls')
        menu()

def IPSet():
    global run
    global IPSetFilter

    if IPSetFilter == "none":
        IPSetFilter = "any"
        print("Switching to any mode...")
        input("Press any key to exit...")
    elif IPSetFilter == "any":
        IPSetFilter = "loaded"
        print("Switching to loaded mode...")
        input("Press any key to exit...")
    elif IPSetFilter == "loaded":
        IPSetFilter = "none"
        print("Switching to none mode...")
        input("Press any key to exit...")

def autocheckupdates():
    global run
    global checkupdates

    if checkupdates == "enabled":
        checkupdates = "disabled"
        print("Disabling check updates...")
        input("Press any key to exit...")
    elif checkupdates == "disabled":
        checkupdates = "enabled"
        print("Enabling check updates...")
        input("Press any key to exit...")


def menu():
    try:
        test_path = os.path.join(os.environ['windir'], 'System32', 'test_admin_rights')
        os.mkdir(test_path)
        os.rmdir(test_path)
        is_admin = True
    except PermissionError:
        is_admin = False

    if not is_admin:
        os.startfile(sys.executable, "runas", " ".join(sys.argv))
        sys.exit()

    banner = f'''zapret 1.0.0
-----------------------------------------
1. Install Service
2. Remove Service
3. Check Status
-----------------------------------------
4. Game Filter ({filter})
5. IPSet Filter ({IPSetFilter})
6. Auto-Update Check ({checkupdates})
                '''
    print(banner)
    user_choice = input(">>> ")

    if user_choice == "1":
        os.system('cls')
        alts()
    elif user_choice == "2":
        os.system('cls')
        ralts()
    elif user_choice == "3":
        os.system('cls')
        check()
    elif user_choice == "4":
        os.system('cls')
        gamef()
    elif user_choice == "5":
        os.system('cls')
        IPSet()
    elif user_choice == "6":
        os.system('cls')
        autocheckupdates()
    elif user_choice == "0":
        quit()

run = False
filter = "disabled"
IPSetFilter = "none"
checkupdates = "disabled"

while True:
    os.system('cls')
    menu()
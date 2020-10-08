from getpass import getpass
from colorama import init, deinit
from colorama import Fore, Style
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from time import perf_counter
import pause
import pynput
import os
from pynput.keyboard import Key, Controller


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def title():
    print("")
    print(Fore.MAGENTA + Style.NORMAL + "███████╗██╗░░░██╗███╗░░██╗██╗░░██╗░█████╗░██╗░██████╗:")
    print(Fore.MAGENTA + "██╔════╝██║░░░██║████╗░██║██║░░██║██╔══██╗╚█║██╔════╝:")
    print(Fore.MAGENTA + "█████╗░░██║░░░██║██╔██╗██║███████║███████║░╚╝╚█████╗░:")
    print(Fore.MAGENTA + "██╔══╝░░██║░░░██║██║╚████║██╔══██║██╔══██║░░░░╚═══██╗:")
    print(Fore.MAGENTA + "███████╗╚██████╔╝██║░╚███║██║░░██║██║░░██║░░░██████╔╝:")
    print(Fore.MAGENTA + "╚══════╝░╚═════╝░╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═════╝░")
    print(Fore.CYAN + "█▀▄▀█ █▀▀ █▀▀ ▀▀█▀▀  █▀▀▄ █▀▀█ ▀▀█▀▀")
    print(Fore.CYAN + "█░▀░█ █▀▀ █▀▀ ░░█░░  █▀▀▄ █░░█ ░░█░░")
    print(Fore.CYAN + "▀░░░▀ ▀▀▀ ▀▀▀ ░░▀░░  ▀▀▀░ ▀▀▀▀ ░░▀░░")
    print(Style.RESET_ALL + "")


def login():
    browser.get(('https://accounts.google.com/ServiceLogin?'
                 'service=mail&continue=https://mail.google'
                 '.com/mail/#identifier'))

    username = browser.find_element_by_id('identifierId')
    username.send_keys(email)
    nextButton = browser.find_element_by_id('identifierNext')
    nextButton.click()
    time.sleep(1)
    password = browser.find_element_by_xpath("//input[@class='whsOnd zHQkBf']")
    password.send_keys(senha)
    signInButton = browser.find_element_by_id('passwordNext')
    signInButton.click()


clear()
init()
title()
t = time.localtime()
current_time = time.strftime("%a | %d/%b/%y | %H:%M", t)
prefix = Fore.MAGENTA + Style.BRIGHT + "[+] " + Fore.BLUE + Style.BRIGHT

# Get Credentials
print(prefix + "Por favor, insira seu endereco de email. (ex: ana@eunha.com)")
email = input("> ")

print()

print(prefix + "Por favor, insira sua senha.")
senha = getpass("> ")

clear()
title()

# Main menu
print()
print(Fore.CYAN + Style.BRIGHT + current_time)
print(prefix + "Seja bem vinde " + Fore.MAGENTA + Style.BRIGHT + email + Fore.BLUE + Style.BRIGHT + "!")
print()

print()
print(prefix + "Pre-configuring" + Fore.YELLOW + Style.BRIGHT + " firefox" + Fore.BLUE + Style.BRIGHT + "...")

# Set Options and log in
options = Options()
options.add_argument("--disable-infobars")
options.set_preference("permissions.default.microphone", 2)
options.set_preference("permissions.default.camera", 2)
browser = webdriver.Firefox(options=options)
browser.set_window_size(1280, 720)

print()
print(prefix + "Logging in...")

start = perf_counter()
login()
end = perf_counter()
time = end-start
print()
print("Done! <" + Fore.MAGENTA + Style.BRIGHT + "{:.3f}".format(time) + Fore.BLUE + Style.BRIGHT + "s>")

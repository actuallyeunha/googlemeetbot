from getpass import getpass

import self as self
from colorama import init, deinit
from colorama import Fore, Style
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import subprocess
import time
from time import sleep
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


def menu():
    print()
    print(Fore.CYAN + Style.BRIGHT + current_time)
    print(
        prefix + "Seja bem vinde " + Fore.MAGENTA + Style.BRIGHT + email + Fore.BLUE + Style.BRIGHT + " ao " + Fore.MAGENTA + Style.BRIGHT + "meet bot" + Fore.BLUE + Style.BRIGHT + " by: eunha" + Fore.BLUE + Style.BRIGHT + "!")
    print()

    print()
    print(prefix + "Qual navegador voce deseja usar?")
    print(Fore.MAGENTA + Style.BRIGHT + "[f]" + Fore.BLUE + Style.BRIGHT + " Firefox")
    print(Fore.MAGENTA + Style.BRIGHT + "[c]" + Fore.BLUE + Style.BRIGHT + " Chromium")
    print(Fore.MAGENTA + Style.BRIGHT + "[x]" + Fore.BLUE + Style.BRIGHT + " Sair")
    nav = input(Fore.CYAN + Style.BRIGHT + "> ")

    if nav == "f":
        firefox()
    elif nav == "c":
        chrome()
    elif nav == "x":
        print(
            prefix + "Obrigada por usar o" + Fore.MAGENTA + Style.BRIGHT + "meet bot" + Fore.BLUE + Style.BRIGHT + " by: eunha")
        print(" Ate a proxima!")
        sleep(2)
        deinit()
        exit()
    else:
        print(prefix + "Voce deve escolher alguma opcao!")
        menu()


def firefox():
    print()
    print(prefix + "Opening Firefox with custom settings...")
    options = Options()
    options.add_argument("--disable-infobars")
    options.set_preference("permissions.default.microphone", 2)
    options.set_preference("permissions.default.camera", 2)
    browser = webdriver.Firefox(options=options)
    browser.set_window_size(1280, 720)

    print()
    print(prefix + "Logging in...")

    start = perf_counter()

    browser.get(('https://accounts.google.com/ServiceLogin?'
                 'service=mail&continue=https://mail.google'
                 '.com/mail/#identifier'))

    username = browser.find_element_by_id('identifierId')
    username.send_keys(email)
    nextButton = browser.find_element_by_id('identifierNext')
    nextButton.click()
    sleep(3)
    password = browser.find_element_by_xpath("//input[@class='whsOnd zHQkBf']")
    password.send_keys(senha)
    signInButton = browser.find_element_by_id('passwordNext')
    signInButton.click()

    end = perf_counter()
    time = end - start

    print()
    print("Done! <" + Fore.MAGENTA + Style.BRIGHT + "{:.3f}".format(time) + Fore.BLUE + Style.BRIGHT + "s>")
    print()

    print(prefix + "Por favor, insira a Url do Meet")
    urlmeet = input("> ")

    print()
    print(prefix + "Entrando no meet...")
    browser.get("https://" + urlmeet)
    sleep(3)
    browser.find_element_by_xpath("//span[@class='l4V7wb Fxmcue']").click()
    sleep(1)


def chrome():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-infobars")
    options.add_argument("--window-size=1280,720")
    options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.media_stream_mic": 2,
        "profile.default_content_setting_values.media_stream_camera": 2,
    })
    browser = webdriver.Chrome(chrome_options=options)
    browser.get(('https://accounts.google.com/ServiceLogin?'
                 'service=mail&continue=https://mail.google'
                 '.com/mail/#identifier'))

    print()
    print(prefix + "Logging in...")

    start = perf_counter()

    browser.get(('https://accounts.google.com/ServiceLogin?'
                 'service=mail&continue=https://mail.google'
                 '.com/mail/#identifier'))

    username = browser.find_element_by_id('identifierId')
    username.send_keys(email)
    nextButton = browser.find_element_by_id('identifierNext')
    nextButton.click()
    sleep(1)
    password = browser.find_element_by_xpath("//input[@class='whsOnd zHQkBf']")
    password.send_keys(senha)
    signInButton = browser.find_element_by_id('passwordNext')
    signInButton.click()

    end = perf_counter()
    time = end - start

    print()
    print("Done! <" + Fore.MAGENTA + Style.BRIGHT + "{:.3f}".format(time) + Fore.BLUE + Style.BRIGHT + "s>")


clear()

init()
title()

# Important Variables
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
menu()

deinit()
exit()
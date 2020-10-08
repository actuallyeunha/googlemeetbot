from getpass import getpass
from colorama import init, deinit
from colorama import Fore, Style
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pause
import pynput
import os
from pynput.keyboard import Key, Controller


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
    time.sleep(5)
    password = browser.find_element_by_xpath("//input[@class='whsOnd zHQkBf']")
    password.send_keys(senha)
    signInButton = browser.find_element_by_id('passwordNext')
    signInButton.click()


init()
title()
t = time.localtime()
current_time = time.strftime("%H:%M", t)

# Get Credentials
print(Fore.BLUE + Style.BRIGHT + "Por favor, insira seu endereco de email. (ex: ana@eunha.com)")
email = input("> ")

print("Por favor, insira sua senha.")
senha = getpass("> ")

# Main menu
print()
print("Seja bem vinde " + Fore.MAGENTA + Style.NORMAL + email + Fore.BLUE + Style.BRIGHT + "!")
print("Sao: " + Fore.MAGENTA + Style.NORMAL + current_time)
print()

print()
print()

# Set Options and log in
options = Options()
options.add_argument("--disable-infobars")
options.set_preference("permissions.default.microphone", 2)
options.set_preference("permissions.default.camera", 2)
browser = webdriver.Firefox(options=options)
browser.set_window_size(1280, 720)

login()

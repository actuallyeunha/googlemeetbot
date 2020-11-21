from getpass import getpass
from colorama import init, deinit, Fore, Style
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
import time
from time import strftime as get_time
from time import perf_counter as timer
from time import sleep
import os

t = time.localtime()
prefix = Fore.BLUE + Style.BRIGHT + "[+] "
default = Fore.MAGENTA + Style.BRIGHT
chighlight = Fore.CYAN + Style.BRIGHT
bhighlight = Fore.BLUE + Style.BRIGHT


def clear():
    os.system('cls' if os.name == "nt" else 'clear')


def current_time():
    wday = get_time("%a", t)
    day = get_time("%d", t)
    month = get_time("%b", t)
    year = get_time("%y", t)
    hour = get_time("%H", t)
    minute = get_time("%M", t)
    return wday, day, month, hour, minute


def title():
    print(chighlight + """▓█████  █    ██  ███▄    █  ██░ ██  ▄▄▄        ██████
▓█   ▀  ██  ▓██▒ ██ ▀█   █ ▓██░ ██▒▒████▄    ▒██    ▒
▒███   ▓██  ▒██░▓██  ▀█ ██▒▒██▀▀██░▒██  ▀█▄  ░ ▓██▄
▒▓█  ▄ ▓▓█  ░██░▓██▒  ▐▌██▒░▓█ ░██ ░██▄▄▄▄██   ▒   ██▒
░▒████▒▒▒█████▓ ▒██░   ▓██░░▓█▒░██▓ ▓█   ▓██▒▒██████▒▒
░░ ▒░ ░░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒  ▒ ░░▒░▒ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░
░ ░  ░░░▒░ ░ ░ ░ ░░   ░ ▒░ ▒ ░▒░ ░  ▒   ▒▒ ░░ ░▒  ░ ░
░    ░░░ ░ ░    ░   ░ ░  ░  ░░ ░  ░   ▒   ░  ░  ░
░  ░   ░              ░  ░  ░  ░      ░  ░      ░  """)
    print(bhighlight + """                     _   _           _   
 _ __ ___   ___  ___| |_| |__   ___ | |_ 
| '_ ` _ \ / _ \/ _ \ __| '_ \ / _ \| __|
| | | | | |  __/  __/ |_| |_) | (_) | |_ 
|_| |_| |_|\___|\___|\__|_.__/ \___/ \__|""")
    print("+" + 30 * "-" + "+")
    print("  " + current_time.wday + " " + current_time.day + "/" + current_time.month + "/" + current_time.year + " | " + current_time.hour + ":" + current_time.minute)


def menu():
    print("menu")


def f_init():
    print("Iniciando firefox...")
    options = Options()
    options.set_preference("permissions.default.camera", 2)
    options.add_argument("--disable-infobars")
    options.set_preference("permissions.default.microphone", 2)
    f_init.browser = webdriver.Firefox(options=options)
    f_init.browser.set_window_size(800, 600)
    return f_init.browser


# ----- Final das funcoes ----- #

# Inicio de tudo
clear()
title()


# Config + inicio do firefox
f_init()
browser = f_init.browser


# Pegar informacoes do login
print("   " + "+" + 20 * "-" + "+")
print(prefix + "Por favor, insira o endereco de email a ser utilizado.")
email = input("> ") # Email

print()
print(prefix + "Por favor, insira a senha a ser utilizada.")
senha = getpass("> ") # Senha
print("   " + "+" + 20 * "-" + "+")


# Logar
print()
print(prefix + "Fazendo login...")
start = timer()
browser.get("https://accounts.google.com/ServiceLogin?service=mail&continue=https://mail.google.com/mail/#identifier") # Entra no site
username = browser.find_element_by_id('identifierId') # Acha o input do email
username.send_keys(email)
nextbutton = browser.find_element_by_id('identifierNext')
nextbutton.click()

# Esperar carregar e colocar a senha
try:
    insenha = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@class='whsOnd zHQkBf']")))
    insenha.click()
finally:
    insenha.send_keys(senha)
    pass

signinbutton = browser.find_element_by_id('passwordNext')
signinbutton.click()
end = timer()
time = end - start

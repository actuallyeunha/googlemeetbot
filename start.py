from getpass import getpass

import self as self
from colorama import init, deinit
from colorama import Fore, Style
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
import time
from time import sleep
from time import perf_counter
import os


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


def menu():
    print()
    print(Fore.CYAN + Style.BRIGHT + "    " + current_time)
    print(prefix + "Seja bem vinde " + special + email + default + " ao " + special + "meet bot" + default + " by: eunha!")
    print()

    print()
    print(prefix + "Qual navegador voce deseja usar?")
    print(special + "[f]" + default + " Firefox")
    print(special + "[c]" + default + " Chromium")
    print(special + "[x]" + default + " Sair")
    nav = input(Fore.CYAN + Style.BRIGHT + "> ")

    if nav == "x":
        exit()
    else:
        pass

    print()
    print(prefix + "Quer usar a lista de: " + Fore.MAGENTA + current_day + "?")
    print(special + "[s]" + default + " Sim")
    print(special + Style.BRIGHT + "[n]" + default + " Nao")
    list = input(Fore.CYAN + Style.BRIGHT + "> ")

    if nav == "f":
        if list == "s":
            lista = "1"
            firefox(lista)
        else:
            lista = 2
            firefox(lista)
    elif nav == "c":
        if list == "s":
            lista = "1"
            chrome(lista)
        else:
            lista = 2
            chrome(lista)
    elif nav == "x":
        print(
            prefix + "Obrigada por usar o" + special + "meet bot" + default + " by: eunha")
        print(" Ate a proxima!")
        sleep(2)
        deinit()
        exit()
    else:
        print(prefix + "Voce deve escolher alguma opcao!")
        menu()


def firefox(lista):
    print()
    print(prefix + "Abrindo firefox...")
    start = perf_counter()
    options = Options()
    options.add_argument("--disable-infobars")
    options.set_preference("permissions.default.microphone", 2)
    options.set_preference("permissions.default.camera", 2)
    browser = webdriver.Firefox(options=options)
    browser.set_window_size(1280, 720)
    end = perf_counter()
    time = end - start

    print()
    print("Feito! <" + special + "{:.3f}".format(time) + default + "s>")

    print()
    print(prefix + "Entrando na conta...")

    start = perf_counter()

    browser.get(('https://accounts.google.com/ServiceLogin?'
                 'service=mail&continue=https://mail.google'
                 '.com/mail/#identifier'))

    username = browser.find_element_by_id('identifierId')
    username.send_keys(email)
    nextbutton = browser.find_element_by_id('identifierNext')
    nextbutton.click()
    sleep(2)
    password = browser.find_element_by_xpath("//input[@class='whsOnd zHQkBf']")
    password.send_keys(senha)
    signinbutton = browser.find_element_by_id('passwordNext')
    signinbutton.click()

    end = perf_counter()
    time = end - start

    print()
    print("Feito! <" + special + "{:.3f}".format(time) + default + "s>")
    print()
    if lista == "1":
        print(prefix + "Utilizando lista de: " + Fore.MAGENTA + current_day + default + ".")
        bparse = open("list.yaml")
        aparse = load(bparse, Loader=Loader)

        for x in aparse:
            if x == time.strftime("%H:%M", t):
                urlmeet = x
                break
            else:
                sleep(10)
    else:
        print(prefix + "Por favor, insira a Url do Meet. (ex meet.google.com/xxx-xxxx-xxx)")
        urlmeet = input("> ")
        pass

    print()
    print(prefix + "Entrando no meet...")
    start = perf_counter()
    browser.get("https://" + urlmeet)
    sleep(3)
    print()
    print(prefix + "Entrando...")
    browser.find_element_by_xpath("//span[@class='l4V7wb Fxmcue']").click()
    end = perf_counter()
    time = end - start

    browser.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[5]/div[3]/div[6]/div[3]/div/div[2]/div[3]").click()

    print()
    print("Feito! <" + Fore.MAGENTA + Style.BRIGHT + "{:.3f}".format(time) + default + "s>")
    print(prefix + "Observando mensagens...")
    print()
    while 1 == 1:
        for element in browser.find_elements_by_class_name("oIy2qc"):
            if element.text == "pessoa atras de mim, numero tal":
                chatbox = element.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[5]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[1]/div[1]/div[2]/textarea")
                chatbox.click()
                print(prefix + "Pessoa anterior detectada, preparando para mandar presenca em 5 segundos")
                sleep(5)
                chatbox.send_keys("presente" + Keys.ENTER)
                break
                sleep(2)


def chrome(lista):
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-infobars")
    options.add_argument("--window-size=800,600")
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
    print("Feito! <" + Fore.MAGENTA + Style.BRIGHT + "{:.3f}".format(time) + Fore.BLUE + Style.BRIGHT + "s>")


clear()

init()
title()

# Important Variables
t = time.localtime()
current_time = time.strftime("%a | %d/%b/%y | %H:%M", t)
current_day = time.strftime("%A", t)

prefix = Fore.MAGENTA + Style.BRIGHT + "[+] " + Fore.BLUE + Style.BRIGHT
default = Fore.BLUE + Style.BRIGHT
special = Fore.MAGENTA + Style.BRIGHT

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
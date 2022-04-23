"""
Created by:
VK: @pi4n1st0
Discord: discord.gg/SFUYusjqxU
P.S. Лохи позорные, хватит с читами играть.
"""

import psutil
import os
import time
import subprocess
import colorama
from colorama import Fore, Style
import cursor
import webbrowser


DEVNULL = os.open(os.devnull, os.O_WRONLY)


def get_pid(process_name):
    process_list = []
    for process in psutil.process_iter():
        if process.name() == process_name:
            process_list.append(process.pid)

    if not len(process_list):
        return None
    print("\n" + Fore.GREEN + "Warface обнаружен!" + Style.RESET_ALL + "\n", end="")
    return process_list


def get_command_line(pid):
    print("\n" + Fore.YELLOW + "Получаю cmd..." + Style.RESET_ALL + "\n", end="")
    cmd_list = psutil.Process(pid=pid).cmdline()
    cmd = "".join(i + " " for i in cmd_list).strip()
    print("\n" + Fore.GREEN + "CMD получен!" + Style.RESET_ALL + "\n", end="")
    return cmd


def run_wf_with_token(cmd):
    print("\n" + Fore.YELLOW + "Запускаю Warface..." + Style.RESET_ALL + "\n", end="")
    subprocess.Popen(cmd)
    print("\n" + Fore.GREEN + "Warface запущен!" + Style.RESET_ALL + "\n", end="")


def kill_wf():
    print("\n" + Fore.YELLOW + "Выключаю Warface..." + Style.RESET_ALL + "\n", end="")
    subprocess.call("taskkill /f /im game.exe", stdout=DEVNULL, stderr=subprocess.STDOUT)
    subprocess.call("taskkill /f /im gamecenter.exe", stdout=DEVNULL, stderr=subprocess.STDOUT)


def main_loop():
    pid = None
    print("\n" + Fore.YELLOW + "Ожидаю запуска Warface..." + Style.RESET_ALL + "\n", end="")
    while pid is None:
        pid = get_pid("Game.exe")
        time.sleep(0.2)

    cmd = get_command_line(pid[0])
    kill_wf()
    time.sleep(5)
    run_wf_with_token(cmd)


if __name__ == '__main__':
    colorama.init()
    webbrowser.open("https://discord.gg/QTfDzdw", new=2)
    os.system("title OFFMRAC by Тень#2262")
    os.system("mode con:cols=50 lines=3")
    cursor.hide()
    print("")
    main_loop()

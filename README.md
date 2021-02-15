# ***English***

# Python-ReverseShell
Python ReverseShell Builder with some advanced functionalities <br/>

# Getting Started
Python version: 3.x <br/>
Python imports: Simply run `python -m pip install -r requirements.txt` to install all the required packages <br/>
_Note: if you are on linux, you probably need to use `python3` instead of `python`_ <br/>

# Using
To build your reverse shell run `python createShell.py` and fill with the information needed <br/>
_Note: if you are on linux, you probably need to use `python3` instead of `python`_ <br/>
_You can run the script with the `--no-color` flag if your terminal doesn't support colors_ <br/>

# Info
LHOST: IP the target machine will connect to _(usually your ip)_ <br/>
LPORT: The PORT the target machine will connect to _(use a port of your choice, be aware that you will need to listen on that port later)_ <br/>
 **Advanced Options:**<br/>
--- Seconds to sleep before running: The time the shell will stay idle before actually running _(can avoid some **runtime** detections)_ <br/>
--- Hide file: Will try to hide itself with `windows flags` and move itself to the Program Data folder <br/>
--- Spawn shell in another process: Will create a copy of itself in another folder and execute that file, than exit <br/>

# ***Brazillian Portuguese / Português Brasileiro***

# Python-ReverseShell
Python ReverseShell Builder com algumas funcionalidades avançadas <br/>

# Começando
Versão python: 3.x <br/>
Python imports: Execute `python -m pip install -r requirements.txt` para instalar todos os pacotes necessários. <br/>
_Atenção: se você estiver no linux, provavelmente precisará utilizar `python3` ao invés de `python`_ <br/>

# Usando
Para criar sua reverse shell execute `python createShell.py` e preencha as informações necessárias <br/>
_Atenção: se você estiver no linux, provavelmente precisará utilizar `python3` ao invés de `python`_ <br/>
_Você pode executar o script com a flag `--no-color` se o seu terminal não suportar cores_ <br/>

# Informações
LHOST: IP que o computador infectado se conectará _(normalmente é o seu próprio ip)_ <br/>
LPORT: A PORTA que o computador infectado conectará _(você pode usar a porta que quiser, mas tenha em mente que você precisará escutar nela depois)_ <br/>
 **Opções avançadas** <br/>
--- Seconds to sleep before running: O tempo que a shell ficará em idle ("dormindo") antes de começar a funcionar _(pode evitar algumas detecções **runtime**)_ <br/>
--- Hide file: A shell vai tentar se esconder usando `windows flags` e vai mover ela mesma para a pasta `Program Data` <br/>
--- Spawn shell in another process: A shell vai tentar criar uma cópia de si mesma em outra pasta e executar aquele arquivo, depois fechará si mesma <br/>

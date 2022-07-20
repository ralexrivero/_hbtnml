# Math

```bash
                                      88
                                ,d    88
                                88    88
88,dPYba,,adPYba,  ,adPPYYba, MM88MMM 88,dPPYba,
88P'   "88"    "8a ""     `Y8   88    88P'    "8a
88      88      88 ,adPPPPP88   88    88       88
88      88      88 88,    ,88   88,   88       88
88      88      88 `"8bbdP"Y8   "Y888 88       88
```

## Environment

[![Ubuntu](https://img.shields.io/static/v1?label=&message=Ubuntu&color=E95420&logo=Ubuntu&logoColor=E95420&labelColor=2F333A)](https://ubuntu.com/)<!-- ubuntu -->
[![Ubuntu](https://img.shields.io/static/v1?label=&message=Kali%20Linux&color=557C94&logo=Kali%20Linux&logoColor=557C94&labelColor=2F333A)](https://www.kali.org/)<!-- kali linux -->
[![Bash](https://img.shields.io/static/v1?label=&message=GNU%20Bash&color=4EAA25&logo=GNU%20Bash&logoColor=4EAA25&labelColor=2F333A)](https://www.gnu.org/software/bash/)<!-- bash -->
[![Vim](https://img.shields.io/static/v1?label=&message=Vim&color=019733&logo=Vim&logoColor=019733&labelColor=2F333A)](https://www.vim.org/)<!-- vim -->
[![VS Code](https://img.shields.io/static/v1?label=&message=Visual%20Studio%20Code&color=007ACC&logo=Visual%20Studio%20Code&logoColor=007ACC&labelColor=2F333A)](https://code.visualstudio.com/)<!-- vs code -->
[![Git](https://img.shields.io/static/v1?label=&message=Git&color=F05032&logo=Git&logoColor=F05032&labelColor=2F333A)](https://git-scm.com/)<!-- git -->
[![Github](https://img.shields.io/static/v1?label=&message=GitHub&color=181717&logo=GitHub&logoColor=f2f2f2&labelColor=2F333A)](https://github.com)<!-- github -->
[![Vagrant](https://img.shields.io/static/v1?label=&message=Vagrant&color=1868F2&logo=vagrant&labelColor=2F333A)](https://app.vagrantup.com/)<!-- vagrant -->

## Requirements

- `python3` 3.8
- `numpy` 1.19.2
- `#!/usr/bin/env python3`
- `pycodestyle` 2.6
- `ubuntu/focal64`
- `pip` latest

Installing numpy 1.19.2, scipy 1.6.2, and pycodestyle 2.6

`pip install --user numpy==1.19.2`
`pip install --user scipy==1.6.2`
`pip install --user pycodestyle==2.6`

check download

`pip list`

Modules and classes documentation:

- `python3 -c 'print(__import__("my_module").__doc__)'`
- `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`

Classes and functions (inside and outside) documentation:

- `python3 -c 'print(__import__("my_module").my_function.__doc__)'`
- `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`

## vagrant

> install virtualbox
`sudo apt update`
`sudo apt full-upgrade -y`
`[ -f /var/run/reboot-required ] && sudo reboot -f`

```bash
wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- \
| gpg --dearmor \
  | sudo tee /usr/share/keyrings/virtualbox-archive-keyring.gpg
```

```bash
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/virtualbox-archive-keyring.gpg] http://download.virtualbox.org/virtualbox/debian buster contrib" \
  | sudo tee /etc/apt/sources.list.d/virtualbox.list
```

`sudo apt update`
`sudo apt install -y dkms`
`sudo apt install -y virtualbox virtualbox-ext-pack`
`virtualbox`

> install vagrant
`curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -`
`sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"`
`sudo apt-get update && sudo apt-get install vagrant`

## Author
<!-- twitter -->
[![Twitter](https://img.shields.io/twitter/follow/ralex_uy?style=social)](https://twitter.com/ralex_uy) <!-- linkedin --> [![Linkedin](https://img.shields.io/badge/LinkedIn-+26K-blue?style=social&logo=linkedin)](https://www.linkedin.com/in/ronald-rivero/) <!-- github --> [![Github](https://img.shields.io/github/followers/ralexrivero?style=social)](https://github.com/ralexrivero/) <!-- vagrant --> [![Vagrant](https://img.shields.io/static/v1?label=&message=Vagrant%20Profile&color=1868F2&logo=vagrant&labelColor=2F333A)](https://app.vagrantup.com/ralexrivero) <!-- docker --> [![Docker](https://img.shields.io/static/v1?label=&message=Docker%20Profile&color=2496ED&logo=Docker&labelColor=2F333A)](https://hub.docker.com/u/ralexrivero)

# 0x01. Plotting

```bash
██████╗ ██╗      ██████╗ ████████╗████████╗██╗███╗   ██╗ ██████╗
██╔══██╗██║     ██╔═══██╗╚══██╔══╝╚══██╔══╝██║████╗  ██║██╔════╝
██████╔╝██║     ██║   ██║   ██║      ██║   ██║██╔██╗ ██║██║  ███╗
██╔═══╝ ██║     ██║   ██║   ██║      ██║   ██║██║╚██╗██║██║   ██║
██║     ███████╗╚██████╔╝   ██║      ██║   ██║██║ ╚████║╚██████╔╝
╚═╝     ╚══════╝ ╚═════╝    ╚═╝      ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝
```

## Environment

[![Ubuntu](https://img.shields.io/static/v1?label=&message=Ubuntu&color=E95420&logo=Ubuntu&logoColor=E95420&labelColor=2F333A)](https://ubuntu.com/)<!-- ubuntu -->
[![Ubuntu](https://img.shields.io/static/v1?label=&message=Kali%20Linux&color=557C94&logo=Kali%20Linux&logoColor=557C94&labelColor=2F333A)](https://www.kali.org/)<!-- kali linux -->
[![Bash](https://img.shields.io/static/v1?label=&message=GNU%20Bash&color=4EAA25&logo=GNU%20Bash&logoColor=4EAA25&labelColor=2F333A)](https://www.gnu.org/software/bash/)<!-- bash -->
[![Vim](https://img.shields.io/static/v1?label=&message=Vim&color=019733&logo=Vim&logoColor=019733&labelColor=2F333A)](https://www.vim.org/)<!-- vim -->
[![VS Code](https://img.shields.io/static/v1?label=&message=Visual%20Studio%20Code&color=007ACC&logo=Visual%20Studio%20Code&logoColor=007ACC&labelColor=2F333A)](https://code.visualstudio.com/)<!-- vs code -->
[![Pycharm](https://img.shields.io/static/v1?label=&message=Pycharm&color=000000&logo=pycharm&logoColor=000000&labelColor=f3f3f3)](https://www.jetbrains.com/pycharm/)<!-- pycharm -->
[![Git](https://img.shields.io/static/v1?label=&message=Git&color=F05032&logo=Git&logoColor=F05032&labelColor=2F333A)](https://git-scm.com/)<!-- git -->
[![Github](https://img.shields.io/static/v1?label=&message=GitHub&color=181717&logo=GitHub&logoColor=f2f2f2&labelColor=2F333A)](https://github.com)<!-- github -->
[![Vagrant](https://img.shields.io/static/v1?label=&message=Vagrant&color=1868F2&logo=vagrant&labelColor=2F333A)](https://app.vagrantup.com/)<!-- vagrant -->

[![Python](https://img.shields.io/static/v1?label=&message=Python&color=FFD43B&logo=python&logoColor=3776AB&labelColor=2F333A)](https://www.python.org)<!-- python-->

- `numpy` 1.19.2
- `matplotlib` 3.3.4
- `pycodestyle` 2.6

### Configure environment

> Installing Matplotlib 3.3.4

- `pip install --user matplotlib==3.3.4`
- `pip install --user Pillow`
- `sudo apt-get install python3-tk`

> Configure X11 Forwarding

Update your Vagrantfile to include the following:

```Vagrantfile
Vagrant.configure(2) do |config|
  ...
  config.ssh.forward_x11 = true
end
```

## plots

![Line graph](img/0.png)
![Scatter](img/1.png)
![Change of scale](img/2.png)
![Two is better than one](img/3.png)
![Frequency](img/4.png)
![All in One](img/5.png)
![]()

## Author
<!-- twitter -->
[![Twitter](https://img.shields.io/twitter/follow/ralex_uy?style=social)](https://twitter.com/ralex_uy) <!-- linkedin --> [![Linkedin](https://img.shields.io/badge/LinkedIn-+26K-blue?style=social&logo=linkedin)](https://www.linkedin.com/in/ronald-rivero/) <!-- github --> [![Github](https://img.shields.io/github/followers/ralexrivero?style=social)](https://github.com/ralexrivero/) <!-- vagrant --> [![Vagrant](https://img.shields.io/static/v1?label=&message=Vagrant%20Profile&color=1868F2&logo=vagrant&labelColor=2F333A)](https://app.vagrantup.com/ralexrivero) <!-- docker --> [![Docker](https://img.shields.io/static/v1?label=&message=Docker%20Profile&color=2496ED&logo=Docker&labelColor=2F333A)](https://hub.docker.com/u/ralexrivero)
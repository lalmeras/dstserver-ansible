dstserver (Don't Starve Together Server) & Ansible
==================================================


Purpose
-------

This role installs a dstserver with the help of Linux Game Server Manager
(LGSM - https://gameservermanagers.com/lgsm/dstserver/).


Quickstart
----------

Here is a sample playbook that uses the role:

```
- hosts: hostname
  roles:
    - role: dstserver
      dst_default_token: "PLACE HERE YOUR PRIVATE TOKEN"
      # https://github.com/GameServerManagers/LinuxGSM/pull/1554
      # pull-request version is needed to handle multi-instance Overworld/Cave
      dst_linuxgsm_url: "https://raw.githubusercontent.com/GameServerManagers/LinuxGSM/feature/config-dl/linuxgsm.sh"
      dst_default_cluster_name: Name your world !
      dst_default_cluster_description: Name your world !
      dst_default_intention: cooperative
      dst_default_game_mode: survival
      dst_default_worldgen_mode: auto
      dst_default_world_size: large
      dst_default_password: "USE A PRIVATE PASSWORD"
      dst_default_max_players: 12
      dst_default_pause_when_empty: yes
      dst_default_pvp: no
      dst_default_vote_enabled: yes
      dst_default_console_enabled: yes
      dst_default_max_snapshots: 6
```

About creating a DST Token:
https://github.com/GameServerManagers/LinuxGSM/wiki/Don%E2%80%99t-Starve-Together---Getting-your-Authentication-Token

### What is done by this script

It installs needed packages with distribution package manager as listed by LGSM
documentation, create a new ``dstserver`` user then it pushes templated
configurations and launch dstserver commands to create a two instances
Overworld + Cave map.

All files handled by this role (except installed packages from package manager)
are located in ``dstserver`` home.

Server is not started when role ends. To start your server, connect to your
server, switch to ``dstserver`` user and home, and type:

```
./dstserver start
./dstserver-2 start
```

First server is Overworld, Second server is Cave. You server should be
accessible in the Don't Starve Together ``Browse Games``.

You can refer to these pages for help:

 * Linux Game Server Manager: https://gameservermanagers.com/lgsm/dstserver/
 * Don't Starve Together server configuration: https://forums.kleientertainment.com/topic/64441-dedicated-server-quick-setup-guide-linux/


Caveat
------

This role is currently written for Centos 7, but it should be easy to adapt to
other distributions. Please use ``Issues`` to provide your feedback or ask
questions. Pull-requests on this subject are welcome.

This role does not use main development branch of Linux Game Server Manager as
it is currently broken for Overworld/Cave gaming.

LGSM version is a pull-request of @marvinlehmann that can be found here:
https://github.com/GameServerManagers/LinuxGSM/pull/1554



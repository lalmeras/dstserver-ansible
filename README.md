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
      dst_default_world_size: huge
      dst_default_password: "USE A PRIVATE PASSWORD"
      dst_default_max_players: 12
      dst_default_pause_when_empty: yes
      dst_default_pvp: no
      dst_default_vote_enabled: yes
      dst_default_console_enabled: yes
      dst_default_max_snapshots: 6
```


Caveat
------

This role is currently written for Centos 7, but it should be easy to adapt to
other distributions. Please use ``Issues`` to provide your feedback or ask
questions. Pull-requests on this subject are welcome.

This role does not use main development branch of Linux Game Server Manager as
it is currently broken for Overworld/Cave gaming.

LGSM version is a pull-request of @marvinlehmann that can be found here:
https://github.com/GameServerManagers/LinuxGSM/pull/1554



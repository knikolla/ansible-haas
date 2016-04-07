[![Build Status](https://travis-ci.org/knikolla/ansible-haas.svg?branch=master)](https://travis-ci.org/knikolla/ansible-haas)

# HaaS-Ansible

Ansible playbook for deploying [HaaS](https://github.com/CCI-MOC/haas).

Install ansible.

```
$ sudo pip install ansible
```

Edit `/etc/ansible/hosts' to have a `[haas]` group and below it, the IP or domain of the target host.
```
[haas]
<IP or DOMAIN> ansible_user=<ssh_user>
```

Finally, get the repo and edit the `site.yml` file to an user with admin permissions.

To change the actual haas user or haas user database password, edit `group_vars/all`.
```
$ git clone https://github.com/knikolla/ansible-haas.git
$ cd ansible-haas
$ ansible-playbook site.yml -v
```

If not using key authentication use `--ask-pass`
```
ansible-playbook site.yml -v --ask-pass
```

If running sudo required a password also user `--ask-sudo-pass`
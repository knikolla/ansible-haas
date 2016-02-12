# HaaS-Ansible

Ansible playbook for deploying [HaaS](https://github.com/CCI-MOC/haas).

Install ansible.

```
$ sudo pip install ansible
```

Edit `/etc/ansible/hosts' to have a `[haas]` group and below it, the IP or domain of the target host.

```
[haas]
IP or DOMAIN
```
Finally get the repo and edit the `site.yml` file to the user with admin permissions.

```
$ git clone https://github.com/knikolla/ansible-haas.git
$ cd ansible-haas
$ ansible-playbook site.yml -v #add --ask-pass if not key authentication
```
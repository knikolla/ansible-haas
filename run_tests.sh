#!/usr/bin/env bash
export HAAS_USERNAME=admin
export HAAS_PASSWORD=12345

cp -r tests /var/lib/haas/
cd /var/lib/haas

# Initial Setup
haas-admin db create
haas create_admin_user ${HAAS_USERNAME} ${HAAS_PASSWORD}

# Test commands
py.test tests/cli.py

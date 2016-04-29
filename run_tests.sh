#!/usr/bin/env bash
export HAAS_USERNAME=admin
export HAAS_PASSWORD=12345

cd /var/lib/haas

# Initial Setup
haas-admin db create
haas create_admin_user ${HAAS_USERNAME} ${HAAS_PASSWORD}

# Test commands
haas list_projects

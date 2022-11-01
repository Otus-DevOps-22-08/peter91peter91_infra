#!/bin/bash
sudo apt install -y git
cd /opt && git clone -b monolith https://github.com/express42/reddit.git
cd reddit && bundle install

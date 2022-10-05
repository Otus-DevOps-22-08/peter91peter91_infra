#!/bin/bash

sudo apt-get update
sudo apt-get install -y git
git clone -b monolith https://github.com/express42/reddit.git
sudo apt-get install build-essential
cd reddit
bundle install
puma -d

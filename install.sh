#!/usr/bin/bash
# This code write by Mr.nope
if [[ "$(id -u)" -ne 0 ]]; then
  echo "" 
  echo "Please, run This Programm as Root!"
  echo ""
  exit 1
fi
clear
echo "Installing..."
sleep 2
chmod +x hack.py
apt install python
apt install python3
apt install python3-pip
pip3 install --upgrade pip
echo ""
echo "Installing..., Finish...!"
echo ""
exit 1

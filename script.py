import os
import subprocess

os.system("sudo apt-get install openvpn")
os.system("wget acandreani.info/client_vlab.ovpn")
os.system("sudo apt-get install apache2")
os.system("sudo openvpn client_vlab.ovpn")



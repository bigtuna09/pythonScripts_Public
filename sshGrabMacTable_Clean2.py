import paramiko
import sys
import getpass
import time

#Grab required information for SSH
hostname = input("Hostname or IP: ")
username = input ("Username: ")
password = getpass.getpass("Password: ")

#Create file and pull MAC Address Table
def macTable():
	ssh = paramiko.SSHClient()
	ssh
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname, username=username, password=password, look_for_keys=False, allow_agent=False)
	print ("SSH connection established to " + hostname)
	stdin, stdout, stderr = ssh.exec_command('show mac address-table\r')
	output = stdout.readlines()
	f = open(hostname + "MACTable.txt","w+")
	f.write(''.join(output))
	f.close()
	print ("MAC Address file created")

#Create file and pull Interface Configurations
def interfaceConfig():
	ssh = paramiko.SSHClient()
	ssh
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname, username=username, password=password, look_for_keys=False, allow_agent=False)
	print ("SSH connection established to " + hostname)
	stdin, stdout, stderr = ssh.exec_command('show running-config | section interface GigabitEthernet\r')
#	print ('sh run | include interface GigabitEthernet\n')
	output = stdout.readlines()
	f = open(hostname + "InterfaceConfig.txt","w+")
	f.write(''.join(output))
	f.close()
	print ("Interface configuration file created")

macTable()
interfaceConfig()
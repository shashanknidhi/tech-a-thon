# import datetime
# date = datetime.datetime.now()
# file = str(date.strftime("%B"))  + "/" + str(date.year) + "-" + str(date.month) + "-" + str(date.day) + ".pcapng"
# print(file)
# file = "captures/a1.pcapng"
# output = open(file,"x")
# print(output)
# for i in range(1,5):
#     file = "captures/"+str(i)+".pcapng"
#     output = open(file, "x")
# import os
# print(os.listdir("D:/tech-a-thon/tech-a-thon/anomaly_scores"))
# os.remove("D:/tech-a-thon/tech-a-thon/anomaly_scores/"+os.listdir("D:/tech-a-thon/tech-a-thon/anomaly_scores")[-1])
# print(os.listdir("D:/tech-a-thon/tech-a-thon/anomaly_scores"))

# import subprocess
import sys
import os

# # check if the script is running with administrative privileges
if os.getuid():
    # if not, re-run the script with elevated privileges
    args = ['powershell', '-command', f'Start-Process "{sys.executable}" -ArgumentList "{sys.argv[0]}" -Verb runAs']
    subprocess.run(args)
    sys.exit()

# # specify the IP addresses to block
# malicious_ips = ['10.0.0.100']

# # execute the netsh command to add firewall rules for each IP address
# for ip in malicious_ips:
#     # block incoming traffic from the IP address
#     command = f"netsh advfirewall firewall add rule name='Block Incoming from {ip}' dir=in interface=any action=block remoteip={ip}"
#     subprocess.call(command, shell=True)

#     # block outgoing traffic to the IP address
#     command = f"netsh advfirewall firewall add rule name='Block Outgoing to {ip}' dir=out interface=any action=block remoteip={ip}"
#     subprocess.call(command, shell=True)

#     # print the status of the firewall rules
#     command = f"netsh advfirewall firewall show rule name='Block Incoming from {ip}'"
#     output = subprocess.check_output(command, shell=True)
#     print(output.decode())

#     command = f"netsh advfirewall firewall show rule name='Block Outgoing to {ip}'"
#     output = subprocess.check_output(command, shell=True)
#     print(output.decode())

import subprocess

ip_address = '10.0.0.100'

subprocess.run(['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name=BlockIP', 'dir=in', 'action=block', f'remoteip={ip_address}'])
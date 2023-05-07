import pyshark
import datetime
import os
# Capture packets for every 30 seconds and save to a file
if os.path.exists('captures'):
    if len(os.listdir('captures')) > 0:
        #remove all files in captures folder
        files = ['captures/'+f for f in os.listdir('captures')]
        for f in files:
            os.remove(f)
else:
    os.mkdir('captures')

i = 0
while i<6:
    file = "captures/"+str(i)+".pcapng"
    output = open(file, "x")
    time = 30
    print("Capture Packet",i)
    capture = pyshark.LiveCapture(interface="Wi-Fi", output_file=file)
    capture.sniff(timeout=time)
    output.close()
    print("Captured for " + str(time) + " seconds and saved to " + file)
    i += 1

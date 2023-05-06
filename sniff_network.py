import pyshark
import datetime
import os
# Capture packets for every 30 seconds and save to a file
if os.listdir('captures') > 0:
    #remove all files in captures folder
    files = ['captures/'+f for f in os.listdir('captures')]
    for f in files:
        os.remove(f)
else:
    os.mkdir('captures')
try:
    i = 0
    while True:
        file = "captures/"+str(i)+".pcapng"
        output = open(file, "x")
        time = 30
        print("Capture Packet",i)
        capture = pyshark.LiveCapture(interface="Wi-Fi", output_file=file)
        capture.sniff(timeout=time)
        output.close()
        print("Captured for " + str(time) + " seconds and saved to " + file)
        i += 1
except KeyboardInterrupt:
    print('Exiting....')
    pass
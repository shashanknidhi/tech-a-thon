import pyshark
import datetime
import keyboard

# Capture packets for every 30 seconds and save to a file
try:
    i = 0
    while True:
        date = datetime.datetime.now()
        file = "captures/"+str(i)+".pcapng"
        output = open(file, "x")
        time = 30
        print("Capture Packet",i)
        capture = pyshark.LiveCapture(interface="Wi-Fi", output_file=file)
        capture.sniff(timeout=time)
        output.close()
        print("Captured for " + str(time) + " seconds and saved to " + file)
        # if keyboard.is_pressed('q'):
        #     print('Exiting....')
        #     break
        i += 1
except KeyboardInterrupt:
    print('Exiting....')
    pass
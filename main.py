from subprocess import call
call(["python", "sniff_network.py"])
call(["python", "example.py"])
call(["python", "map_color_ip.py"])
call(["streamlit","run", "app.py"])
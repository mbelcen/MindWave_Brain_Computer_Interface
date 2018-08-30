This app allows you to interface with a Mindwave Mobile device
made by Neurosky using a Raspberry. All of the experiments 
were carried out using "Brain Athlete" made by Neurosky 
and a Raspberry Pi 3 B+ model running on Raspbian. 
My main goal was measuring beta/alpha ratio using Raw Data 
extracted from the Brain Athlete device and sending it to a server
using basic TCP/IP sockets.

+++Requirements+++

- Mindwave Device ( Brain Athlete personally tested)
- Bluetooth dongle
- Raspberry
- Python Environment
- PyblueZ installed on the Raspberry that you can get here: 
  https://gist.github.com/lexruee/fa2e55aab4380cf266fb
- Pair, trust and enter PIN code of the device (First time Only)

+++ How it Works+++

- Put the right Mindwave device MAC address in the file
 'MindwaveMobileRawReader' 
- Put the right Server Addresse and port in the main.
- In a terminal simply execute the command:
 
			sudo python main.py


Note1:
 
Many other outputs are possible like Meditation, Attention
levels and EEG powers. 
All are specified as modules in the file: 'MindWaveDataPoints.py'


Note2: 

This app is based on robintibor's repository: 
https://github.com/robintibor/python-mindwave-mobile.

import time
import random
import threading as th
import Queue
import numpy as np
import bluetooth
import socket
import scipy.fftpack
from MindwaveDataPoints import RawDataPoint
from MindwaveDataPointReader import MindwaveDataPointReader


def get_data(q):
    
    mindwaveDataPointReader = MindwaveDataPointReader()
    mindwaveDataPointReader.start()
    
    data=[]
    while(1):
		
        
        dataPoint = mindwaveDataPointReader.readNextDataPoint()
        
        if (dataPoint.__class__ is RawDataPoint):
			data.append(dataPoint)
			q.put(data)
	

  
  
  	
	
		
		
	
def get_ratio(q):
	
	#connection to server
    TCP_IP = '192.168.1.39'
    TCP_PORT = 8887
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    print 'connection to server successful'
	
	
    M = [[],[],[],[],[],[],[],[]]
    fft_avg = []
    fft_avg_mod = []
    j=0
    k=0
    while(1):
		
		
		if k > 7 :
			fft_avg[:] = []
			fft_avg_mod[:] = []
			fft_avg = [(l1+l2+l3+l4+l5+l6+l7+l8)/8 for l1,l2,l3,l4,l5,l6,l7,l8 in zip(M[0],M[1],M[2],M[3],M[4],M[5],M[6],M[7])]
			fft_avg_mod = [ abs(x) for x in fft_avg]
			
		if fft_avg_mod:
			d=random.randint(8,14)
			e=random.randint(14,20)
			alpha=fft_avg_mod[d]
			beta=fft_avg_mod[e]
			ratio=beta/alpha
			print 'ratio' , ratio
			
			if ratio >= 1.35 and ratio < 1.4 :
				#send A			
				s.send("A")
			elif ratio >= 1.4 and ratio < 1.5 :
				#send B
				s.send("B")
			elif ratio >= 1.5 and ratio < 1.6 :
				#send C
				s.send("C")
			elif ratio >= 1.6:
				#send D
				s.send("D")
			else: 
				pass	
		
		
		time.sleep(0.1)
		data = q.get()
		f=k%8
		M[f] = np.fft.fft(data[j:j+32])
		j = j + 32	
		k = k + 1
		


if __name__ == '__main__':
	
	q = Queue.Queue(maxsize=0)
	
	try:
	   threadLock = th.Lock()
	   threads=[]
	   thread1=th.Thread( target=get_data, args=(q,))
	   thread2=th.Thread( target=get_ratio, args=(q,))
	   thread1.start()
	   print 'T1 started'
	   time.sleep(10)
	   thread2.start()
	   print 'T2 started'
	   threads.append(thread1)
	   threads.append(thread2)
	   for t in threads:
			t.join()
	except:
	   print "Error: unable to start thread"
	

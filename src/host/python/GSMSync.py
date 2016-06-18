import numpy as np
from ctypes import *
import time

import Q7Mem
import GSM
from host.curlwrapper import curlwrapper

class GSMSync:
	def __init__(self,f,url):
		self.rx = Q7Mem.rx()
		self.data = self.rx.appData(GSM.GSMAppData)
		self.chipRate = 1.92e6
		self.frame = 0.12/26.
		self.multiframe = 0.12/26.*51.
		self.fl = int(self.chipRate*self.frame)
		self.mfl = int(self.chipRate*self.multiframe)
		self.fc = f
		self.cnt = curlwrapper(url)
		self.scale = 10.

	def waitClockStable( self ):
		while self.rx.clkRate()<5:
			print "clock not stable",self.rx.clkRate()
			time.sleep(5)

	def getFrameStart( self ):
		return long(self.data.frame_start_point)
	
	def setFrameStart( self, s ):
		self.data.frame_start_point = long(s)

	def getAFC( self ):
		return int(self.data.afc)&(1023)

	def setAFC( self, a ):
		a &= (1023)
		self.data.afc = a
		self.cnt.set_afc( a )

	def calcPPM( self, ff ):
		f = 1625e3/24
		ppm = (ff-f)/self.fc*1e6
		return ppm

	def AFC(self,ppm):
		if abs(ppm/1e6)>200e3/self.fc:
			print "reset AFC"
			self.setAFC(512)
			return

		a = self.getAFC()
		a += int(ppm*self.scale)
		a &= 1023
		print "AFC",a
		self.setAFC(a)

	def getRfData(self,offset,length):
		now = self.rx.now()
		last = self.getFrameStart()
		if last>now:
			last = now
			print "resync:"
			return None
		mfs = (now-last)/self.mfl
		newStart = mfs*self.mfl+last
		while self.rx.now()<newStart+offset+length:
			time.sleep(self.frame)
		start = newStart + offset
		rfd = self.rx.mmap(length*4,start*4)
		return rfd,start

	def short2Complex(self,data):
		nframes = len(data)/2
		frame = np.array([complex(data[2*i],data[2*i+1]) for i in range(nframes)])
		return frame


		
	
	
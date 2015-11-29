#!/usr/bin/env python

from mv2vp import Parser
import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
		format='(%(threadName)-10s) %(message)s',)

def daemon():
	logging.debug('Starting')
	for i in range(10):
		logging.debug(i)
		time.sleep(1)
	logging.debug('Exiting')




if __name__ == "__main__":
	d = threading.Thread(name='daemon', target=daemon)
	d.setDaemon(True)

	snooziness = int(raw_input("How much time do you want to wait until %s finish? " % d.name))

	d.start()
	d.join(snooziness)

	if d.isAlive():
		print logging.debug('Daemon is alive')
	else:
		print logging.debug('Daemon is dead')

	FILEPATH='/Users/gillessilvano/iCloud/UFRN - Mestrado/Otimizacao em Sistemas/2dbinpack/data/MV_2bp/Class_10.2bp'

	p = Parser(FILEPATH)
	p.parse()


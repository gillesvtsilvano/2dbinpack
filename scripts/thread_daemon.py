import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

def daemon():
	logging.debug('Starting')
	for i in range(10):
		logging.debug(i)
		time.sleep(1)
	logging.debug('Exiting')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

snooziness = int(raw_input("How much time do you want to wait until %s finish? " % d.name))

d.start()
d.join(snooziness)

if d.isAlive():
	print logging.debug('Daemon is alive')
else:
	print logging.debug('Daemon is dead')



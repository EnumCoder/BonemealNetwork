from SocketServer import *
from src.notify import NotifyManager
from src.notify.NotifyGlobals import *
from src.network import NetworkProtocol
import threading

class NetworkManager(ThreadingMixIn, TCPServer):
	
	notify = NotifyManager.Notifyer.setupNewClass('NetworkManager')
	
	def __init__(self, hostname, hostport):
		TCPServer.__init__(self, (hostname, hostport), NetworkProtocol.NetworkProtocol)
		self.hostname = hostname
		self.hostport = hostport
		self.process_running = False
	
	def run_process(self):
		self.notify.newNotify(INFO, "Started the BonemealNetwork on: %s:%d" % (self.hostname, self.hostport))
		while 1:
			try:
				self.process_running = True
				self.serve_forever()
			except KeyboardInterrupt:
				self.stop_server()
	
	def stop_process(self):
		if self.process_running == True:
			self.shutdown()
		else:
			raise Exception("The process was never running!")
	
	def start_server(self):
		self.thread = threading.Thread(target=self.run_process())
		self.thread.daemon = True
		self.thread.start()
	
	def stop_server(self):
		self.stop_process()
		self.server_close()

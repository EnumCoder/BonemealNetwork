from SocketServer import *
from src.notify import NotifyManager
from src.notify.NotifyGlobals import *
from src.packet.DataPacker import DataPacker

class NetworkProtocol(BaseRequestHandler):
	
	notify = NotifyManager.Notifyer.setupNewClass('NetworkProtocol')
	buff = DataPacker()
	
	def handle(self):
		self.recieved = self.request.recv(1024).strip()
		if len(self.recieved) == 0:
			pass # TODO
		
		self.buff.add(self.recieved)
		self.recv_data()
	
	def recv_data(self):
		self.notify.newNotify(DEBUG, "%s" % repr(self.recieved))
		
	def send_data(self):
		pass

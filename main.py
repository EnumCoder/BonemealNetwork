import sys
import __builtin__

def main(host, port):
	from src.network.NetworkManager import NetworkManager
	__builtin__.server = NetworkManager(host, port)
	if server:
		server.start_server()

main(host=sys.argv[1], port=int(sys.argv[2]))

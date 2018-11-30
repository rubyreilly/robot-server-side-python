import threading
import webbrowser
import BaseHTTPServer
import SimpleHTTPServer
import time
#import serial
import random

FILE = 'web/index.html'
PORT = 8090
"""
ser = serial.Serial(
	port='/dev/ttyUSB0',
	baudrate=115200,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS,
	timeout=1
)
"""

class WambHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	''' Main class to present webpages and authentication. '''
	wamb_directional = {'forward','backward','CW','CCW','clear','auto'}
	wamb_sonar = {'S-1','S-2','S-3','S-4','S-A','S-D'}
	wamb_modes = {'a-45','a-90','a-135','a-180','d-1','d-2','d-3','d-4','d-5'};

	def do_HEAD(self):
		print "send header"
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()

	def do_AUTHHEAD(self):
		print "send header"
		"""
		self.send_response(401)
		self.send_header('WWW-Authenticate', 'Basic realm=\"Test\"')
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		"""

	def do_GET(self):
		f = self.send_head()
		if f:
			self.copyfile(f, self.wfile)
			f.close()
		"""
		''' Present frontpage with user authentication. '''
		if self.headers.getheader('Authorization') == None:
			self.do_AUTHHEAD()
			self.wfile.write('no auth header received')
		elif self.headers.getheader('Authorization') == 'Basic dGVzdDp0ZXN0':
			f = self.send_head()
			if f:
				self.copyfile(f, self.wfile)
				f.close()
		else:
			self.do_AUTHHEAD()
			self.wfile.write(self.headers.getheader('Authorization'))
			self.wfile.write('not authenticated')
		"""

	def do_POST(self):
		length = int(self.headers.getheader('content-length'))
		data = self.rfile.read(length)

		print data

		result=""
		result2=""
		result3=""
		result4=""

		if data in self.wamb_directional:
			if(data=="forward"):
				result = getCypress("forw")
			elif(data=="backward"):
				result = getCypress("back")
			elif(data=="CW"):
				result = getCypress("cloc")
			elif(data=="CCW"):
				resutl = getCypress("ccws")
			elif(data=="stop"):
				result = getCypress("stop")
			elif(data=="hold"):
				result = getCypress("hold")
		elif data in self.wamb_sonar:
			if(data == "S-1"):
				result = getCypress("son1")
			if(data == "S-2"):
				result = getCypress("son2")
			if(data == "S-3"):
				result = getCypress("son3")
			if(data == "S-4"):
				result = getCypress("son4")
			if(data == "S-A"):
				result = getCypress("son1")
				result2 = getCypress("son2")
				result3 = getCypress("son3")
				result4 = getCypress("son4")
		elif data in self.wamb_modes:
			if(data == "a-45"):
				sendCypress("ang1")
			if(data == "a-90"):
				sendCypress("ang2")
			if(data == "a-135"):
				sendCypress("ang3")
			if(data == "a-180"):
				sendCypress("ang4")
			if(data == "d-1"):
				sendCypress("dur1")
			if(data == "d-2"):
				sendCypress("dur2")
			if(data == "d-3"):
				sendCypress("dur3")
			if(data == "d-4"):
				sendCypress("dur4")
			if(data == "d-5"):
				sendCypress("dur5")
		else:
			result=getCypress(data)
		if(result != ""):
			self.wfile.write(result)
		if(result2 != ""):
			self.wfile.write(result2)
		if(result3 != ""):
			self.wfile.write(result3)
		if(result4 != ""):
			self.wfile.write(result4)


def open_browser():
	"""Start a browser after waiting for half a second.
	def _open_browser():
		webbrowser.open('http://localhost:%s/%s' % (PORT, FILE))
	thread = threading.Timer(0.5, _open_browser)"""
	thread.start()

def start_server():
	"""Start the server."""
	server_address = ("", PORT)
	server = BaseHTTPServer.HTTPServer(server_address, WambHandler)
	server.serve_forever()

def sendCypress(command):
	ser.open()
	if ser.isOpen():
		ser.write(command);
		ser.close()
def getCypress(command):
	out="Cannot open serial port\n"
	ser.open()
	if ser.isOpen():
		ser.write(command+'\r\n')
		"""out = ''
		time.sleep(0.2)
		while ser.inWaiting() > 0:
			out += ser.read(1)"""
		out=ser.readline()
		ser.close()
		print out
	return out

if __name__ == "__main__":
    """open_browser()"""
    start_server()

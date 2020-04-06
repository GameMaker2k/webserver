#-------------------------------------------------------------------------------
# Name:        webserver
# Purpose:
#
# Author:      jduyon
#
# Created:     29/04/2014
# Copyright:   (c) jduyon 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import threading
import webbrowser

pyoldver = True;
try:
 import BaseHTTPServer
 import SimpleHTTPServer
except ImportError:
 import http.server as SimpleHTTPServer
 import http.server as BaseHTTPServer
 pyoldver = False;

FILE = 'frontend.html'
PORT = 8080


class TestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    """The test example handler."""

    def do_POST(self):
        """Handle a post request by returning the square of the number."""
        try:
         length = int(self.headers.getheader('content-length'))
        except AttributeError:
         length = int(self.headers.get('content-length'))
        data_string = self.rfile.read(length)
        try:
            result = int(data_string) ** 2
        except:
            result = 'error'
        try:
         self.wfile.write(result)
        except TypeError:
         self.wfile.write(bytes(result))

def open_browser():
    """Start a browser after waiting for half a second."""
    def _open_browser():
        webbrowser.open('http://localhost:%s/%s' % (PORT, FILE))
    thread = threading.Timer(0.5, _open_browser)
    thread.start()

def start_server():
    """Start the server."""
    server_address = ("", PORT)
    server = BaseHTTPServer.HTTPServer(server_address, TestHandler)
    try:
        server.serve_forever()
    except(KeyboardInterrupt):
        pass

if __name__ == "__main__":
    open_browser()
    start_server()

from   .http import content_dict_from, is_http_get, is_http_post, response
import socket
import select

TIMEOUT_MS  = 1000
BUFFER_SIZE = 1024


class ConfigServer:
    def __init__(self):
        self.socket = None

    def start(self):
        print('binding to 8080')
        self.socket = socket.socket()
        self.socket.bind(('0.0.0.0', 8080))
        self.socket.listen(0)
        self.socket.setblocking(True)
        while True:
            (connection, address) = self.socket.accept()
            with Handler(connection) as handler:
                handler.read()

    def stop(self):
        if not self.socket:
            return
        self.socket.close()
        self.socket = None


class Handler:
    def __init__(self, socket):
        self.socket = socket

    def __enter__(self):
        print('entering handler...')
        return self

    def __exit__(self, type, value, tb):
        print('exiting handler...')
        self.socket.close()

    def read(self):
        print('reading handler"')
        poller = select.poll()
        poller.register(self.socket, select.POLLIN)
        data = b''
        while poller.poll(TIMEOUT_MS) and len(data) <= BUFFER_SIZE:
            data += self.socket.recv(BUFFER_SIZE)
        if is_http_get(data):
            # TODO: handle GET
            print('received HTTP GET')
            self.socket.sendall(response('OITTM Smart Plug', 'This is the config page for the OITTM Smart Plug'))
        elif is_http_post(data):
            user_inputs = content_dict_from(data)
            # TODO: handle POST
            print('received HTTP POST with {0}'.format(user_inputs))
            self.socket.sendall(response('OITTM Smart Plug', 'Connecting to wifi...'))

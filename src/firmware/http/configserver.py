from   .http import content_dict_from, is_http_get, is_http_post, response
import socket
import select

TIMEOUT_MS  = 1000
BUFFER_SIZE = 1024


class ConfigServer:
    def __init__(self):
        self.socket = None

    def start(self):
        self.socket = socket.socket()
        self.socket.bind(('0.0.0.0', 80))
        self.socket.listen(0)
        self.socket.setblocking(True)
        while True:
            (connection, address) = self.socket.accept()
            print('client connected')
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
        print('client connected')
        return self

    def __exit__(self, type, value, tb):
        print('disconnected from client')
        self.socket.close()

    def read(self):
        poller = select.poll()
        poller.register(self.socket, select.POLLIN)
        data = b''
        while poller.poll(TIMEOUT_MS) and len(data) <= BUFFER_SIZE:
            data += self.socket.recv(BUFFER_SIZE)
        if is_http_get(data):
            # TODO: handle GET
            print('GET')
            paragraph = '<p>This is the config page for the hacked OITTM Smart Plug.</p>'
            form      = '<form method="post" enctype="application/x-www-form-urlencoded"><input type="text" name="essid"/><input type="text" name="password"/><input type="submit"/></form>'
            self.socket.sendall(response('OITTM Smart Plug', '{0}{1}'.format(paragraph, form)))
        elif is_http_post(data):
            user_inputs = content_dict_from(data)
            # TODO: handle POST
            print('POST: {0}'.format(user_inputs))
            self.socket.sendall(response('OITTM Smart Plug', 'Connecting to wifi...'))

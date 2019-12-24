from http import generate_page, get_response_header, is_http_get, is_http_post, post_response_header, posted_content_dict, response
import socket
import sys

crlf = '\r\n'

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('localhost', 8080))
socket.listen()
# print('waiting for connection')
while True:
    try:
        connection, client_address = socket.accept()
        # print('receiving data')
        data = connection.recv(2048)
        # print(f"received {data}")
        # with open('request.http', 'ab') as f:
        #     # print('writing data')
        #     f.write(data)
        #     f.flush()
        # print('responding')
        if is_http_get(data):
            print('responding to get')
            connection.sendall(response('HTTP', 'Hello world!'))
        elif is_http_post(data):
            print('received post with {data}'.format(dict=posted_content_dict(data)))
            connection.sendall(response('HTTP', 'Connecting to wifi...'))
    finally:
        connection.close()
sys.exit(0)

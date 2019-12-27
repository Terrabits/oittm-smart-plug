from unquote import unquote

crlf                 = '\r\n'
get_response_header  = 'HTTP/1.1 200 OK{crlf}Content-Type: text/html{crlf}{crlf}'.format(crlf=crlf)
get_response_header  = get_response_header.encode()
post_response_header = 'HTTP/1.1 200 OK{crlf}Content-Type: text/html{crlf}{crlf}'.format(crlf=crlf)
post_response_header = post_response_header.encode()


def is_http_method(data, method):
    method = method.strip().upper()
    data   = data[:10].strip().upper()
    return data.startswith(method)


def is_http_get(data):
    return is_http_method(data, b'GET')


def is_http_post(data):
    return is_http_method(data, b'POST')


def content_from(data):
    if type(data) == bytes:
        data = data.decode()
    content = list(filter(None, data.strip().split(crlf)))[-1]
    return content


def content_dict_from(data):
    if type(data) == bytes:
        data = data.decode()
    result      = dict()
    expressions = content_from(data).split('&')
    for expression in expressions:
        key, value = expression.split('=')
        result[key] = unquote(value)
    return result


def generate_page(title, text):
    page  = '<html><head><title>{title}</title></head>'.format(title=title)
    page += '<body>{text}</body></html>'.format(text=text)
    return page.encode()


def response(title, text):
    return get_response_header + generate_page(title, text)

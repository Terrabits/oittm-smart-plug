crlf                 = '\r\n'
get_response_header  = f'HTTP/1.1 200 OK{crlf}Content-Type: text/html{2 * crlf}'
get_response_header  = get_response_header.encode()
post_response_header = f'HTTP/1.1 200 OK{crlf}Content-Type: text/html{2 * crlf}'
post_response_header = post_response_header.encode()


def is_http_method(data, method):
    method = method.strip().upper()
    data   = data[:10].strip().upper()
    return data.startswith(method)


def is_http_get(data):
    return is_http_method(data, b'GET')


def is_http_post(data):
    return is_http_method(data, b'POST')


def posted_content_dict(data):
    result = dict()
    content     = list(filter(None, data.strip().split(crlf.encode())))[-1]
    expressions = content.split(b'&')
    for expression in expressions:
        key, value = expression.split(b'=')
        result[key.decode()] = value.decode()
    return result


def generate_page(title, text):
    page  = f'<html><head><title>{title}</title></head>'
    page += f'<body>{text}</body></html>'
    return page.encode()


def response(title, text):
    return get_response_header + generate_page(title, text)

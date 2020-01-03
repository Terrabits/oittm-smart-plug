# paths
display_connecting_filename = 'http/pages/display-connecting.html'
post_toggle_filename        = 'http/pages/post-toggle.html'
post_wifi_info_filename     = 'http/pages/post-wifi-info.html'


# page generators
def page_generator_for(filename):
    with open(filename) as f:
        while True:
            data = f.read(256)
            if not data:
                break
            yield data


def display_connecting_page():
    return page_generator_for(display_connecting_filename)


def post_toggle_page():
    return page_generator_for(post_toggle_filename)


def post_wifi_info_page():
    return page_generator_for(post_wifi_info_filename)

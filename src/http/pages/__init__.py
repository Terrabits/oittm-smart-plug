# paths
display_connecting_filename = 'http/pages/display-connecting.html'
post_config_filename        = 'http/pages/post-config.html'


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


def post_config_page():
    return page_generator_for(post_config_filename)

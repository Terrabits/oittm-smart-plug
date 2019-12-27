from pathlib import Path

# paths
root_path = Path(__file__).parent
display_connecting_filename = str(root_path / 'display-connecting.html')
post_toggle_filename        = str(root_path / 'post-toggle.html'       )
post_wifi_info_filename     = str(root_path / 'post-wifi-info.html'    )


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

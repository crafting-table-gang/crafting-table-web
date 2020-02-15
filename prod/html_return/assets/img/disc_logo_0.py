from flask import send_file


def main():
    return send_file('./prod/html_return/assets/img/Discord-Logo+Wordmark-White.png', mimetype='image/png')

from flask import send_file


def main():
    return send_file('./prod/html_return/assets/js/bs-init.js', mimetype='application/javascript')

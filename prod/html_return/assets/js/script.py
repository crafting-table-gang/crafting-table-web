from flask import send_file


def main():
    return send_file('./prod/html_return/assets/js/jquery.min.js', mimetype='application/javascript')

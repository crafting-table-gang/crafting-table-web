from flask import send_file


def main():
    return send_file('./prod/html_return/assets/bootstrap/css/bootstrap.min.css', mimetype='text/css')

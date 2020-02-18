import json

import sentry_sdk
from sentry_sdk.integrations.wsgi import SentryWsgiMiddleware

from svr import app

with open('data.json') as f:
    dat = json.load(f)
sentry_sdk.init(dsn=dat["sentry_dsn"])

sentry_sdk.init(dsn="https://cc66efd98ae3494790ac9689940f77e7@sentry.io/2635837")

wsgi_app = SentryWsgiMiddleware(app.run)

# if __name__ == "__main__":
# app.run()
# wsgi_app = SentryWsgiMiddleware(app)

# this is just an entrypoint to allow WDGI to access the flask part of the server.

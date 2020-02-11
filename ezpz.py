"""
CTB oauth
"""
from requests_oauthlib import OAuth2Session
import getpass
from flask import Flask, request, redirect, session
import os
import json


# Disable SSL requirement
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# Settings for your app
base_discord_api_url = 'https://discordapp.com/api'
client_id = r'670747978423861248'  # Get from https://discordapp.com/developers/applications
client_secret = '6JIHsM-O_6bDHv6jZxj7eT2Ht22ja107'
redirect_uri = 'http://epro.epfforce.systems/oauth_callback'
scope = ['identify', 'email']
token_url = 'https://discordapp.com/api/oauth2/token'
authorize_url = 'https://discordapp.com/api/oauth2/authorize'

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route("/")
def home():
    """
    Presents the 'Login with Discord' link
    """
    oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scope)
    login_url, state = oauth.authorization_url(authorize_url)
    session['state'] = state
    print("Login url: %s" % login_url)
    return '<a href="' + login_url + '">Login with Discord</a>'


@app.route("/oauth_callback")
def oauth_callback():
    """
    The callback we specified in our app.
    Processes the code given to us by Discord and sends it back
    to Discord requesting a temporary access token so we can 
    make requests on behalf (as if we were) the user.
    e.g. https://discordapp.com/api/users/@me
    The token is stored in a session variable, so it can
    be reused across separate web requests.
    """
    try:
        discord = OAuth2Session(client_id, redirect_uri=redirect_uri, state=session['state'], scope=scope)
        token = discord.fetch_token(
            token_url,
            client_secret=client_secret,
            authorization_response=request.url,
        )
        session['discord_token'] = token
        rtn = '<script>window.location = "/profile"</script>'
        return rtn
    except Exception as e:
        print(e)
        return '<script>alert(' + str(e) + '); window.location = "/"</script>' \
               '<h1>nO</h1>'


@app.route("/profile")
def profile():
    """
    Example profile page to demonstrate how to pull the user information
    once we have a valid access token after all OAuth negotiation.
    """

    try:
        discord = OAuth2Session(client_id, token=session['discord_token'])
        response = discord.get(base_discord_api_url + '/users/@me')
        # https://discordapp.com/developers/docs/resources/user#user-object-user-struct
        did = response.json()["id"]
        rtn = f'<h1>tag: @{response.json()["username"]}#{response.json()["discriminator"]}</h1>' \
              f'<br>' \
              f'<h2>2FA enabled? {response.json()["mfa_enabled"]}</h2>' \
              f'<br>' \
              f'<h1>Nitro Type: {response.json()["premium_type"]}</h1>' \
              f''
        if int(did) in [611108193275478018, 264838866480005122, 544911653058248734]:
            rtn += f'<br>' \
                   f'<h1><a href="/configs">You have permission to manage configs, you may here!</a></h1>'
        return rtn
    except Exception as e:
        print(e)
        return "<script>alert('Please Log In.'); window.location = '/'</script>"


@app.route("/configs")
def configs():
    """
    For managing configs. (ctbot)
    :return:
    """
    try:
        with open('data.json', 'r+') as f:
            data = json.load(f)
            if 611108193275478018 not in data['permitted_ids']:
                data['permitted_ids'].append(611108193275478018)  # <--- add `611108193275478018` to ids
            f.seek(0)  # <--- should reset file position to the beginning.
            json.dump(data, f, indent=4)
            f.truncate()  # remove remaining part
        discord = OAuth2Session(client_id, token=session['discord_token'])
        response = discord.get(base_discord_api_url + '/users/@me')
        did = response.json()["id"]
        if int(did) not in [611108193275478018, 264838866480005122, 544911653058248734]:
            return f'<script> alert("no."); window.location = "/profile"</script>' \
                   f'<h1>nO</h1>'
        # https://discordapp.com/developers/docs/resources/user#user-object-user-struct
        rtn = f'<h1>Config Manager</h1>' \
              f'<a href="/profile">You may return back to your profile here!</a>' \
              f'<br>' \
              f'<textbox>{data}</textbox>'
        return rtn
    except:
        return "<script>alert('Please Log In.'); window.location = '/'</script>"

    # Or run like this


# FLASK_APP=discord_oauth_login_server.py flask run -h 0.0.0.0 -p 8000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

"""
CTB oauth
"""
import json
import os

import sentry_sdk
from flask import Flask, request, session
from requests_oauthlib import OAuth2Session
from sentry_sdk.integrations.flask import FlaskIntegration

import no_logic
from prod.html_return import rtrnr as m

# Disable SSL requirement
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
with open('data.json') as f:
    dat = json.load(f)
sentry_dsn = dat["sentry_dsn"]

sentry_sdk.init(
    dsn=sentry_dsn,
    integrations=[FlaskIntegration()]
)
# Settings for your app
base_discord_api_url = 'https://discordapp.com/api'
client_id = r'670747978423861248'  # Get from https://discordapp.com/developers/applications
client_secret = dat["client_sec"]
redirect_uri = 'https://web.bot.craftingtable.xyz/oauth_callback'
scope = ['identify', 'guilds.join']
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
    rtns = m.index(login_url)
    try:
        lmn = """<script src="https://browser.sentry-cdn.com/5.12.1/bundle.min.js" integrity="sha384-y+an4eARFKvjzOivf/Z7JtMJhaN6b+lLQ5oFbBbUwZNNVir39cYtkjW1r6Xjbxg3" crossorigin="anonymous"></script><script>Sentry.init({ dsn: 'https://cc66efd98ae3494790ac9689940f77e7@sentry.io/2635837' });</script>"""
        if session['discord_token'] != "NONE":
            rtns += f'<br>' \
                    f'<script>window.location = "/profile"</script>' + lmn
    except:
        print("")

    return rtns


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
        response = discord.get(base_discord_api_url + '/users/@me')
        session['discord_token'] = token
        # discord.put(f'{base_discord_api_url}/guilds/672129232146661377/members/{response.json()["id"]}',
        #             '{"access_token": {' + str(token) + '}')
        lmn = """<script src="https://browser.sentry-cdn.com/5.12.1/bundle.min.js" integrity="sha384-y+an4eARFKvjzOivf/Z7JtMJhaN6b+lLQ5oFbBbUwZNNVir39cYtkjW1r6Xjbxg3" crossorigin="anonymous"></script><script>Sentry.init({ dsn: 'https://cc66efd98ae3494790ac9689940f77e7@sentry.io/2635837' });</script>"""
        rtn = '<script>window.location = "/profile"</script>' + lmn
        return rtn
    except KeyError as e:
        print(e)
        lmn = """<script src="https://browser.sentry-cdn.com/5.12.1/bundle.min.js" integrity="sha384-y+an4eARFKvjzOivf/Z7JtMJhaN6b+lLQ5oFbBbUwZNNVir39cYtkjW1r6Xjbxg3" crossorigin="anonymous"></script><script>Sentry.init({ dsn: 'https://cc66efd98ae3494790ac9689940f77e7@sentry.io/2635837' });</script>"""
        return '<script>alert("' + str(e) + '"); window.location = "/"</script>' \
                                            f'<h1>FAIL: {str(e)}</h1>' + lmn


@app.route("/profile")
def profile():
    """
    Example profile page to demonstrate how to pull the user information
    once we have a valid access token after all OAuth negotiation.
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
        # https://discordapp.com/developers/docs/resources/user#user-object-user-struct
        did = response.json()["id"]
        rtn = f'<h1>tag: @{response.json()["username"]}#{response.json()["discriminator"]}</h1>' \
              f'<br>' \
              f'<h2>2FA enabled? {response.json()["mfa_enabled"]}</h2>' \
              f'<br>'
        try:
            pt = response.json()["premium_type"]
            rtn += f'<h1>Nitro Type: {pt}</h1>'
        except KeyError as e:
            rtn += f'<h1>Nitro Type: None</h1>'

        if int(did) in [611108193275478018, 264838866480005122, 544911653058248734]:
            rtn += f'<br>' \
                   f'<h1><a href="/configs">You have permission to manage configs, you may here!</a></h1>'
        elif int(did) in data["permitted_ids"]:
            rtn += f'<br>' \
                   f'<h1><a href="/configs">You have permission to manage configs, you may here!</a></h1>'
        rtn += f'<br><h1><a href="/logout">LOGOUT</a></h1>'
        lmn = """<script src="https://browser.sentry-cdn.com/5.12.1/bundle.min.js" integrity="sha384-y+an4eARFKvjzOivf/Z7JtMJhaN6b+lLQ5oFbBbUwZNNVir39cYtkjW1r6Xjbxg3" crossorigin="anonymous"></script><script>Sentry.init({ dsn: 'https://cc66efd98ae3494790ac9689940f77e7@sentry.io/2635837' });</script>"""
        return rtn + lmn
    except KeyError as e:
        print(e)
        lmn = """<script src="https://browser.sentry-cdn.com/5.12.1/bundle.min.js" integrity="sha384-y+an4eARFKvjzOivf/Z7JtMJhaN6b+lLQ5oFbBbUwZNNVir39cYtkjW1r6Xjbxg3" crossorigin="anonymous"></script><script>Sentry.init({ dsn: 'https://cc66efd98ae3494790ac9689940f77e7@sentry.io/2635837' });</script>"""
        return "<script>alert('Please Log In.'); window.location = '/'</script>" + lmn


# noinspection DuplicatedCode
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
            lmn = """<script src="https://browser.sentry-cdn.com/5.12.1/bundle.min.js" integrity="sha384-y+an4eARFKvjzOivf/Z7JtMJhaN6b+lLQ5oFbBbUwZNNVir39cYtkjW1r6Xjbxg3" crossorigin="anonymous"></script><script>Sentry.init({ dsn: 'https://cc66efd98ae3494790ac9689940f77e7@sentry.io/2635837' });</script>"""
            return f'<script> alert("no."); window.location = "/profile"</script>' \
                   f'<h1>nO</h1>' + lmn
        # https://discordapp.com/developers/docs/resources/user#user-object-user-struct
        data = str(data)
        data = data.replace('\'', '"')
        rtn = f'<h1>Config Manager</h1>' \
              f'<a href="/profile">You may return back to your profile here!</a>' \
              f'<br>' \
              f'<form action="/cfg-save" method="post">' \
              f'<textarea name="data-m">{data}</textarea>' \
              f'<br>' \
              f'<input type="submit" value="Submit">' \
              f'</form>'
        lmn = """<script src="https://browser.sentry-cdn.com/5.12.1/bundle.min.js" integrity="sha384-y+an4eARFKvjzOivf/Z7JtMJhaN6b+lLQ5oFbBbUwZNNVir39cYtkjW1r6Xjbxg3" crossorigin="anonymous"></script><script>Sentry.init({ dsn: 'https://cc66efd98ae3494790ac9689940f77e7@sentry.io/2635837' });</script>"""
        return rtn + lmn
    except:
        lmn = """<script src="https://browser.sentry-cdn.com/5.12.1/bundle.min.js" integrity="sha384-y+an4eARFKvjzOivf/Z7JtMJhaN6b+lLQ5oFbBbUwZNNVir39cYtkjW1r6Xjbxg3" crossorigin="anonymous"></script><script>Sentry.init({ dsn: 'https://cc66efd98ae3494790ac9689940f77e7@sentry.io/2635837' });</script>"""
        return "<script>alert('Please Log In.'); window.location = '/'</script>" + lmn


@app.route('/cfg-save', methods=['POST', 'GET'])
def save_config():
    try:
        discord = OAuth2Session(client_id, token=session['discord_token'])
        response = discord.get(base_discord_api_url + '/users/@me')
        with open('data.json', 'r+') as f:
            data = json.load(f)
            if 611108193275478018 not in data['permitted_ids']:
                data['permitted_ids'].append(611108193275478018)  # <--- add `611108193275478018` to ids

            f.seek(0)  # <--- should reset file position to the beginning.
            json.dump(data, f, indent=4)
            f.truncate()  # remove remaining part
            if response.json()["id"] not in data["permitted_ids"]:
                data_m = request.form['data-m']
                if str(data_m).count('\'') > 0:
                    # data_m = '{"permitted_ids": [611108193275478018, 79305800157233152, 523474477917536258, ' \
                    #          '172131183478571008, ' \
                    #          '264838866480005122, 292134677936865280, 308628182213459989, 607776237737345044]} '
                    data_m = str(data_m).replace('\'', '"')

                if not data_m:
                    return f'<h1><a href="/configs">FAIL, there must be content for the file!</a></h1>'
                with open("data.json", "w") as fo:
                    fo.write(f'{str(data_m)}')
                    fo.close()
                lmn = """<script src="https://browser.sentry-cdn.com/5.12.1/bundle.min.js" integrity="sha384-y+an4eARFKvjzOivf/Z7JtMJhaN6b+lLQ5oFbBbUwZNNVir39cYtkjW1r6Xjbxg3" crossorigin="anonymous"></script><script>Sentry.init({ dsn: 'https://cc66efd98ae3494790ac9689940f77e7@sentry.io/2635837' });</script>"""
                return f'<h1><a href="/">Written to config, click here to go back.</a></h1>' + lmn
    except KeyError as e:
        print(e)
        return f'FAIL: {e}'




@app.route('/logout')
def logout():
    try:
        discord = OAuth2Session(client_id, token=session['discord_token'])
        session['discord_token'] = "NONE"
        discord.cookies['discord_token'] = "NONE"
        lmn = """<script src="https://browser.sentry-cdn.com/5.12.1/bundle.min.js" integrity="sha384-y+an4eARFKvjzOivf/Z7JtMJhaN6b+lLQ5oFbBbUwZNNVir39cYtkjW1r6Xjbxg3" crossorigin="anonymous"></script><script>Sentry.init({ dsn: 'https://cc66efd98ae3494790ac9689940f77e7@sentry.io/2635837' });</script"""
        return f'<h1>Logged out.</h1>' + lmn
    except KeyError as e:
        print(e)
        lmn = """<script src="https://browser.sentry-cdn.com/5.12.1/bundle.min.js" integrity="sha384-y+an4eARFKvjzOivf/Z7JtMJhaN6b+lLQ5oFbBbUwZNNVir39cYtkjW1r6Xjbxg3" crossorigin="anonymous"></script><script>Sentry.init({ dsn: 'https://cc66efd98ae3494790ac9689940f77e7@sentry.io/2635837' });</script>"""
        return f'FAIL: {e}'


no_logic.imports(app, session)

@app.route('/debug-sentry')
def trigger_error():
    division_by_zero = 1 / 0
    return division_by_zero



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

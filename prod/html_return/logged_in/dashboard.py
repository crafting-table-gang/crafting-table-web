import json

from requests_oauthlib import OAuth2Session

client_id = r'670747978423861248'
base_discord_api_url = 'https://discordapp.com/api'

with open('data.json', 'r+') as f:
    data = json.load(f)
    if 611108193275478018 not in data['permitted_ids']:
        data['permitted_ids'].append(611108193275478018)  # <--- add `611108193275478018` to ids
    f.seek(0)  # <--- should reset file position to the beginning.
    json.dump(data, f, indent=4)
    f.truncate()  # remove remaining part
cfg = data


def main(user, session):
    try:
        discord = OAuth2Session(client_id, token=session['discord_token'])
        response = discord.get(base_discord_api_url + '/users/@me')
        did = response.json()["id"]
        user.id = did
        if int(did) in response.json()["permitted_ids"]:
            rtns = f"""
            <!DOCTYPE html>
            <html>
    
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">
                <title>CTBOT-WEB</title>
                <meta name="description" content="CRAFTING TABLE">
                <link rel="stylesheet" href="/assets/bootstrap/css/bootstrap.min.css?h=a56a757409412f7812f2fb24a73f0abb">
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.5.2/animate.min.css">
                <link rel="stylesheet" href="/assets/css/styles.min.css?h=a2f0fa503db4abc4b40be839b16e9239">
            </head>
    
            <body style="background-color: #23272A;color: #FFFF;">
                <h1>Dashboard</h1>
                <p>The official crafting table server: <a href="">{cfg['serverInvite']}<br></a><br><br>The support server:&nbsp;<a href="{cfg['supportServerInvite']}">{cfg['supportServerInvite']}<br></a><br><br>Invite me&nbsp;<a href="https://discordapp.com/oauth2/authorize?client_id={cfg['clientID']}&scope=bot&permissions=2147483647">HERE</a></p>
                <div class="btn-group"
                    role="group"><a class="btn btn-primary" role="button" href="/profile">Back to your profile</a></div>
                <a class="btn btn-primary" role="button" href="/configs">Config Manager</a> 
                <div class="btn-group" role="group"><a class="btn btn-primary" role="button" href="/logout">Logout</a></div>
                <script src="/assets/js/jquery.min.js?h=83e266cb1712b47c265f77a8f9e18451"></script>
                <script src="/assets/bootstrap/js/bootstrap.min.js?h=e46528792882c54882f660b60936a0fc"></script>
                <script src="/assets/js/script.min.js?h=cd7e26c62c422ae4fd1b6151814a03ae"></script>
            </body>
    
                </html>
            """
            return rtns
        else:
            rtns = f"""
                <!DOCTYPE html>
                <html>
    
                <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">
                    <title>CTBOT-WEB</title>
                    <meta name="description" content="CRAFTING TABLE">
                    <link rel="stylesheet" href="/assets/bootstrap/css/bootstrap.min.css">
                    <link rel="stylesheet" href="/assets/css/">
                    <link rel="stylesheet" href="/assets/css/styles.min.css?h=a2f0fa503db4abc4b40be839b16e9239">
                </head>
    
                <body style="background-color: #23272A;color: #FFFF;">
                    <h1>Dashboard</h1>
                    <p>The official crafting table server: <a href="">{cfg['serverInvite']}<br></a><br><br>The support server:&nbsp;<a href="{cfg['supportServerInvite']}">{cfg['supportServerInvite']}<br></a><br><br>Invite me&nbsp;<a href="https://discordapp.com/oauth2/authorize?client_id={cfg['clientID']}&scope=bot&permissions=2147483647">HERE</a></p>
                    <div class="btn-group"
                        role="group"><a class="btn btn-primary" role="button" href="/profile">Back to your profile</a></div>
                    <div class="btn-group" role="group"><a class="btn btn-primary" role="button" href="/logout">Logout</a></div>
                    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
                    <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.4.1/js/bootstrap.bundle.min.js"></script>
                    <script src="/assets/js/bs-init.js?h=cd7e26c62c422ae4fd1b6151814a03ae"></script>
                </body>
    
                </html>
                """
            return rtns
    except Exception as e:
        return "<script>alert('Please Log In.'); window.location = '/'</script>"

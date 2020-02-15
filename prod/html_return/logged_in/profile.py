def main():
    return """<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, shrink-to-fit=no">
    <title>CTBOT-WEB</title>
    <meta name="description" content="CRAFTING TABLE">
    <link rel="stylesheet" href="/assets/bootstrap/css/bootstrap.min.css?h=2742f46518b920ee9a969c24fb777a46">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.5.2/animate.min.css">
</head>

<body style="background-color: #23272A;color: #FFFFFF;">
    <h1 style="font-size: 50px;color: #FFFFFF;">Your profile</h1>
    <p data-toggle="tooltip" data-bs-tooltip="">TAG: {user.tag}<br><br>RANK: {user.rank}<br><br>ID: {user.id}<br><br>Nitro Type: {user.nitro_type}<br><br>Moderation Access: {user.access.mod}<br><br>CONFIGS ACCESS:<br>- ALL: {user.access.confs.all}<br>- BOT: {user.access.confs.bot}<br>- CENSOR:
        {user.access.confs.censor}<br>DATA MANAGER ACCESS:<br>- ALL: {user.access.data.all}<br>- APPEAL BANS: {user.access.data.appeal_bans}<br>- COINS: {user.access.data.coins}<br>- CORE COMMANDS: {user.access.data.core_commands}<br>- LEVELS: {user.access.data.levels}<br>-
        LEVELS_XP: {user.access.data.levels_xp}</p>
    <div class="btn-group" role="group"><a class="btn btn-primary" role="button" href="/dashboard">Dashboard</a></div>
    <script src="/assets/js/jquery.min.js?h=83e266cb1712b47c265f77a8f9e18451"></script>
    <script src="/assets/bootstrap/js/bootstrap.min.js?h=e46528792882c54882f660b60936a0fc"></script>
    <script src="/assets/js/script.min.js?h=cd7e26c62c422ae4fd1b6151814a03ae"></script>
</body>

</html>"""

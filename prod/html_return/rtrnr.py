import prod.html_return as m


def index():
    return m.index.main()


def dashboard():
    return m.logged_in.dashboard.main()


def profile():
    return m.logged_in.profile.main()


def dlog0():
    return m.assets.img.disc_logo_0.main()


def scr():
    return m.assets.js.script.main()

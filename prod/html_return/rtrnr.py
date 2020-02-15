import prod.html_return.assets.bootstrap.css.bs2
import prod.html_return.assets.bootstrap.js.bs1
import prod.html_return.assets.img.disc_logo_0
import prod.html_return.assets.js.jqr
import prod.html_return.assets.js.script
import prod.html_return.index
import prod.html_return.logged_in.dashboard
import prod.html_return.logged_in.profile


def index(url):
    """

    :return:
    """
    return prod.html_return.index.main(url)


def dashboard():
    """

    :return:
    """
    return prod.html_return.logged_in.dashboard.main()


def profile():
    """

    :return:
    """
    return prod.html_return.logged_in.profile.main()


def dlog0():
    """

    :return:
    """
    return prod.html_return.assets.img.disc_logo_0.main()


def scr():
    """

    :return:
    """
    return prod.html_return.assets.js.script.main()


def jqur():
    return prod.html_return.assets.js.script.main()


def bs1():
    return prod.html_return.assets.bootstrap.js.bs1.main()


def bs2():
    return prod.html_return.assets.bootstrap.css.bs2.main()

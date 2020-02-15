import prod.html_return.assets.bootstrap.css.bs2
import prod.html_return.assets.bootstrap.js.bs1
import prod.html_return.assets.css.animate
import prod.html_return.assets.css.style
import prod.html_return.assets.img.disc_logo_0
import prod.html_return.assets.js.bs_init
import prod.html_return.assets.js.jqr
import prod.html_return.assets.js.script
import prod.html_return.index
import prod.html_return.logged_in.dashboard
import prod.html_return.logged_in.profile


def index(url, session=None):
    """

    :return:
    """
    if session is None:

        return prod.html_return.index.main(url)
    else:
        return f'<script>window.location = "/profile</script>"'


def dashboard(user=None, session=None):
    """

    :return:
    """
    if user is None or session is None:
        return f'<script>alert("Please log in for the dashboard!"); window.location = "/"</script>'
    return prod.html_return.logged_in.dashboard.main(user, session)


def profile(user=None, session=None):
    """

    :return:
    """
    if user is None or session is None:
        return f'<script>alert("Please log in for the dashboard!"); window.location = "/"</script>'
    return prod.html_return.logged_in.profile.main(user)


def dlog0():
    """

    :return:
    """
    return prod.html_return.assets.img.disc_logo_0.main()


def bs_init():
    """

    :return:
    """
    return prod.html_return.assets.js.bs_init.main()


def jqur():
    """

    :return:
    """
    return prod.html_return.assets.js.bs_init.main()


def bs1():
    """

    :return:
    """
    return prod.html_return.assets.bootstrap.js.bs1.main()


def bs2():
    """

    :return:
    """
    return prod.html_return.assets.bootstrap.css.bs2.main()


def script():
    """

    :return:
    """
    return prod.html_return.assets.js.script.main()


def animate():
    """

    :return:
    """
    return prod.html_return.assets.css.animate.main()


def style():
    """

    :return:
    """
    return prod.html_return.assets.css.style.main()

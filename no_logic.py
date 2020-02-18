from prod.html_return import rtrnr as m
# to stop me from dying looking at code in the main file lmao 



def imports(app, session):
    def get_ssn():
        return session

    def get_lmn():
        return """<script src="https://browser.sentry-cdn.com/5.12.1/bundle.min.js" integrity="sha384-y+an4eARFKvjzOivf/Z7JtMJhaN6b+lLQ5oFbBbUwZNNVir39cYtkjW1r6Xjbxg3" crossorigin="anonymous"></script><script>Sentry.init({ dsn: 'https://cc66efd98ae3494790ac9689940f77e7@sentry.io/2635837' });</script>"""

    @app.route('/assets/img/Discord-Logo+Wordmark-White.png')
    def dlog0():
        return m.dlog0()

    @app.route('/assets/js/bs-init.js')
    def bs_init():
        return m.bs_init()

    @app.route('/assets/bootstrap/js/bootstrap.min.js')
    def bs1():
        return m.bs1()

    @app.route('/assets/bootstrap/css/bootstrap.min.css')
    def bs2():
        return m.bs2()

    @app.route('/assets/js/jquery.min.js')
    def jqr():
        return m.jqur()

    @app.route('/assets/js/script.min.js')
    def script():
        return m.script()

    @app.route('/assets/css/animate.min.css')
    def animate_m_css():
        return m.animate()

    @app.route('/assets/css/styles.min.css')
    def styles():
        return m.style()

    @app.route('/dashboard')
    def dashboard():
        user = ''
        lmn = get_lmn()
        session = get_ssn()

        return m.dashboard(user, session) + lmn

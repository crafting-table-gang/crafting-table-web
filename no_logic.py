from prod.html_return import rtrnr as m
# to stop me from dying looking at code in the main file lmao
# epf
def imports(app, session):  # normal (just a func to get the required vars!)
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
        return m.dashboard(user, session)

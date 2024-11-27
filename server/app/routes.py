from flask import Flask

def init_routes(app: Flask):
    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    @app.route('/hello')
    def hello():
        return 'Hello from /hello!'
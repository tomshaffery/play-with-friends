from app import app

@app.route('/')
@app.route('/index')
def index():
    return '''
    <html>
        <head>
            <title>Play With Friends</title>
        </head>
        <body>
        </body>
    </html>
'''
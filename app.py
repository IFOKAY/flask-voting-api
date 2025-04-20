from flask import Flask
from views import api

app = Flask(__name__)

# Register API Blueprint
app.register_blueprint(api, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)

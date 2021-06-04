from flask import Flask
from config import config
from __init__ import main, db,bootstrap
import os
import json

CONFIG_PATH = config['default'].SQLALCHEMY_DATABASE_URI[10:-7]
if not os.path.isdir(CONFIG_PATH):
    os.makedirs(CONFIG_PATH)

if not os.path.isfile(CONFIG_PATH + '/README'):
    DESCRIPTION = r
    with open(CONFIG_PATH + '/README', 'w') as readme:
        readme.write(DESCRIPTION)

if not os.path.isfile(CONFIG_PATH + '/tdl.json'):
    config_str = {
        'config_type': 'default',
        'host': 'localhost',
        'port': 9468
    }
    config_json = json.dumps(config_str)
    with open(CONFIG_PATH + '/tdl.json', 'w') as config_file:
        config_file.write(config_json)
    config_type = 'default'
    host = 'localhost'
    port = 9468
else:
    with open(CONFIG_PATH + '/tdl.json', 'r') as config_file:
        config_str = config_file.read()
    config_str = json.loads(config_str)
    config_type = config_str['config_type']
    host = config_str['host']
    port = config_str['port']

app = Flask(__name__)
app.config.from_object(config[config_type])
bootstrap.init_app(app)
db.init_app(app)
# login_manager.init_app(app)
app.register_blueprint(main)

if not os.path.isfile(config['default'].SQLALCHEMY_DATABASE_URI[10:]):
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    app.run(host=host, port=port)

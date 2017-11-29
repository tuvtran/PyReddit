import os

from flask_script import Manager
from app import create_app


app = create_app(config_name=os.environ.get('APP_SETTINGS'))
manager = Manager(app)

# check if the environment configuration is production
is_prod = (os.environ.get('APP_SETTINGS') == 'production')


if __name__ == "__main__":
    manager.run()

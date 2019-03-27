import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/html/")
from application import app
app.secret_key = 'super_secret_key'
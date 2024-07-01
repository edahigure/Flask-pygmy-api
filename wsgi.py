from pygmy.core.initialize import initialize
from pygmy.rest.manage import app

# Initialize the application
initialize()

# Expose the WSGI callable
application = app

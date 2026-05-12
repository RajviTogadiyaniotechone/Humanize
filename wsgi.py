#!/usr/bin/env python3
"""
Production WSGI entry point for Render deployment
"""

import os
from app_render import app

# Configure for production
app.config['DEBUG'] = False
app.config['ENV'] = 'production'

# Expose WSGI application
application = app.wsgi_app

if __name__ == "__main__":
    # This should not run in production
    pass

import os
from flask import request, abort

PLUGIN_API_KEY = os.getenv("PLUGIN_API_KEY")

def verify_api_key():
    if not PLUGIN_API_KEY:
        return  # allow if not configured (dev mode)

    api_key = request.headers.get("x-api-key")

    if not api_key or api_key != PLUGIN_API_KEY:
        abort(401, description="Invalid or missing API key")

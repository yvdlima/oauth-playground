import json

import jwt

from functools import wraps
from logging import getLogger
from blacksheep.server.responses import redirect
from blacksheep import Request

from oauth_playground.services.oauth import OAuthService

logger = getLogger("oauth_playground.middleware.is_authorized")

# Didn't find a way to properly inject a service in the middleware :(
oauth = OAuthService()


def is_authorized():
    def decorator(next_handler):
        @wraps(next_handler)
        async def wrapped(*args, **kwargs):
            request: Request = args[1]
            if "user" in request.session:
                return await next_handler(*args, **kwargs)

            return redirect(oauth.get_authorize_url())

        return wrapped

    return decorator

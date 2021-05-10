import logging

from blacksheep.server.responses import text, redirect
from blacksheep.server.controllers import Controller, get
from blacksheep import Request

from oauth_playground.services.oauth import OAuthService

logger = logging.getLogger("oauth_playground.controller.Auth")


class Auth(Controller):
    @get("/auth")
    async def auth(self, request: Request, oauth: OAuthService):
        if code := request.query.get("code"):
            token = await oauth.get_token_from_code(code[0])

            request.session["user"] = await oauth.decode_token(token)

            return redirect("/")
        else:
            return text("Missing 'code' query parameter!", status=400)

    @get("/auth/logout")
    async def logout(self, request: Request, oauth: OAuthService):
        request.session.clear()
        return redirect(oauth.get_logout_url())

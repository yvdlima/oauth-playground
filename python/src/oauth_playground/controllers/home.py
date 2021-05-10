import json
import logging

from blacksheep.server.responses import redirect
from blacksheep.server.controllers import Controller, get
from blacksheep import Request

from oauth_playground.middlewares.authorization import is_authorized

logger = logging.getLogger("oauth_playground.controller.Home")


class Home(Controller):
    @get("/")
    async def home(self, request: Request):
        user = request.session.get("user")
        user_json = None
        if user:
            user_json = json.dumps(user)

        return await self.view_async(model={"user": user, "user_json": user_json})

    @get("/must_be_authorized")
    @is_authorized()
    async def test_auth_route(self, request: Request):
        return redirect("/")

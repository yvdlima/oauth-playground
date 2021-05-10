import logging

from os import environ

import jwt

from blacksheep import Response, FormContent
from blacksheep.client import ClientSession

logger = logging.getLogger("oauth_playground.services.OAuthService")


class OAuthService:
    def __init__(self):
        logger.info("Initializing service")

        self.get_token_url = environ["OAUTH_GET_TOKEN_URL"]
        self.authorize_url = environ["OAUTH_AUTHORIZE_URL"]
        self.logout_url = environ["OAUTH_LOGOUT_URL"]
        self.jwks_url = environ["OAUTH_JWKS_URL"]

        self.redirect_url = "http://localhost:8080/auth"
        self.logout_returnTo = "http://localhost:8080"

        self.client_id = environ["OAUTH_CLIENT_ID"]
        self.client_secret = environ["OAUTH_CLIENT_SECRET"]

    async def get_token_from_code(self, code: str):
        async with ClientSession() as client:
            content = FormContent(
                {
                    "grant_type": "authorization_code",
                    "client_id": self.client_id,
                    "client_secret": self.client_secret,
                    "redirect_uri": self.redirect_url,
                    "code": code,
                }
            )

            response: Response = await client.post(self.get_token_url, content)

            if response.status != 200:
                raise Exception(
                    f"OAuth get_token_from_code failed! Provider response status: {response.status} {await response.text()}"
                )

            # In a real app I should keep access/refresh token to use later....
            return (await response.json())["id_token"]

    async def decode_token(self, token: str):
        header = jwt.get_unverified_header(token)

        async with ClientSession() as client:
            response: Response = await client.get(self.jwks_url)
            jwks = await response.json()

        tgt_key = None

        for key in jwks["keys"]:
            if header["kid"] == key["kid"]:
                tgt_key = key
                break

        if not tgt_key:
            raise Exception(f"The specified kid '{header['kid']}' is not in the JWKS!")

        jwk = jwt.PyJWK(tgt_key)

        return jwt.decode(token, jwk.key, algorithms=["RS256"], audience=self.client_id)

    def get_authorize_url(self, scope="openid profile email") -> str:
        return f"{self.authorize_url}?client_id={self.client_id}&redirect_uri={self.redirect_url}&response_type=code&prompt=consent&scope={scope}"

    def get_logout_url(self) -> str:
        return f"{self.logout_url}?client_id={self.client_id}&returnTo={self.logout_returnTo}"

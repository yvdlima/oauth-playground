# oAuth Playground

A small project I'm using to study how to use oAuth as a RBAC permission system reusable between different providers and techs.

The idea is to implement OAuth/OpenID without using large/popular SDKs so I can understand wtf I'm doing.

- [oAuth Playground](#oauth-playground)
  - [Providers](#providers)
    - [Auth0](#auth0)
    - [Cognito](#cognito)
  - [Apps](#apps)
    - [BlackSheep ( Python ASGI )](#blacksheep--python-asgi-)

## Providers

### Auth0

Auth0 has a free tier for developers, create you account first.

Now setup a application for to use in the apis here: <https://manage.auth0.com/dashboard/us/{your_auth0_id}/applications>

Replace the {your_auth0_id} with the ID you chose when creating you Auth0 account, for instance, mine would be: <https://manage.auth0.com/dashboard/us/yurivdl/applications>. Now use the `+ Create Application` button and choose *Regular Web Applications*. The technology of the application doesn't matter. After the creation you will need to configure the authorized URLs for authentication and logout. In you application page go to `Settings -> Application URIs` and add the following uris:

- Allowed Callback URLs: <http://localhost:8080/auth>
- Allowed logout URLs: <http://localhost:8080>
- Allowed Web Origins: <http://localhost:8080>

This should be enough! You will still need to get the Client ID/Secret and other stuff but the readme in each project will guide whatever you need.

### Cognito

~ coming soon

## Apps

### BlackSheep ( Python ASGI )

I took the opportunity to learn a bit about [BlackSheep](http://localhost:8080), a nice new micro framework for modern Python.

The app readme is [here](./python/readme.md) and it will guide you to use the app.

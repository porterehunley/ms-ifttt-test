# Ifttt Demo Service

## Setup

```
pip install -r requirements.txt
set FLASK_APP=testapi.py
flask run
```

To setup with IFTTT

## Actions
```
https://<DOMAIN_NAME>/ifttt/v1/actions/create_new_name
```

Writes a new name to a text file

The action follows the standard IFTTT action response and request handeling. See: https://platform.ifttt.com/docs/api_reference#actions

## Triggers 
```
https://<DOMAIN_NAME>/ifttt/v1/triggers/new_date_created
```

Returns a random date with a UUID

The trigger follows the standard IFTTT trigger response and request handeling. See: https://platform.ifttt.com/docs/api_reference#triggers

## OAuth2.0

- Auth URL: https://<DOMAIN_NAME>/oauth2/authorize

- Token URL: https://<DOMAIN_NAME>/oauth2/token

- Authentication also follows IFTTT guidelines. The User info url returns fake information 
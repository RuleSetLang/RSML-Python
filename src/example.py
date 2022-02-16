#!/usr/bin/env python3

import json
from rsml import RSML

data: dict = {
    "userEmail": "antricks.dev@posteo.de",
    "usernameInput": "Antricks",
    "friendsEmail": "foo@bar.com",
}

rsml = RSML()
rsml.load("example.rsml.yaml")

print(json.dumps(rsml.rules, indent=2))
print(json.dumps(rsml.fields, indent=2))

print(json.dumps(rsml.verify(data)))

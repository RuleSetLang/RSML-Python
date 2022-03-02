#!/usr/bin/env python3

import json
from rsml import RSML

data: dict = {
    "userEmail": "antricks.dev@posteo.de",
    "usernameInput": "Antricks",
    "friendsEmail": "foo@bar.com",
}

rsml = RSML()
rsml.loadFromFile("example.rsml.yaml")

print(json.dumps(rsml.check(data)))

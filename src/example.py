#!/usr/bin/env python3

from rsml import RSML

data: dict = {
    "userEmail": "antricks.dev@posteo.de",
    "usernameInput": "_Äntrickś", # should fail because xX is disallowed
    "friendsEmail": "foo@bar.com"
}

rsml = RSML()
rsml.load_from_file("example.rsml.yaml")

print(rsml.check(data))

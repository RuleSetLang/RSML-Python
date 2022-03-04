# RSML Python prototype

This is a prototype implementation of RSML in Python3 for development purposes.

Here's a usage idea:

```python
#!/usr/bin/env python3
# For detailed API info see the Concept Repository.

from rsml import RSML

data: dict = {
    "userEmail": "antricks.dev@posteo.de",
    "usernameInput": "xX_Äntrickś",
    "friendsEmail": "foo@bar.com",
}

rsml = RSML()
rsml.load_from_file("example.rsml.yaml")

print(rsml.check(data))
```

-> [Concept Repo](https://github.com/RuleSetLang/RSML-Concept)

# RSML Python implementation

This is a Python implementation of RSML, mainly for development purposes. **It is not production ready yet.**

Here's a usage example:

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

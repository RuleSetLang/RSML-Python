# RSML Python prototype

This is a prototype implementation of RSML in Python3 for development purposes.

Here's a usage idea:

```python
from rsml import RSML

data = {"field1": "value1", "field2": True, "field3": 1337}

if __name__ == "__main__":
    rsml = RSML()
    rsml.loadRuleset("file/path/to/ruleset")
    
    # Will probably become private / protected at some point
    print(rsml.rules)
    print(rsml.fields)
    
    # For further API stuff see the concept repo
    
```

-> [Concept Repo](https://github.com/RuleSetLang/RSML-Concept)
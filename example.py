#!/usr/bin/env python3

from rsml import RSML
import json

rsml = RSML()
rsml.load_ruleset("example.rsml.yaml")

print(json.dumps(rsml.rules, indent=2))
print(json.dumps(rsml.fields, indent=2))
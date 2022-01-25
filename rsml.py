#!/usr/bin/env python3

#! This is a prototype written for development purposes only.

import json
import yaml
import re

class RSML:
    def __init__(self):
        self.rules: dict = {}
        self.fields: dict = {}

    def load_ruleset(self, path: str):
        with open(path) as ruĺeset_file:
            raw_rsml = list(yaml.safe_load_all(ruĺeset_file))
            raw_fields: dict = raw_rsml[0]
            raw_rules: dict = raw_rsml[1]

        #TODO: handle ranges
        #TODO: handle cyclic depends
        #TODO: handle self inherit
        #TODO: handle missing constant
        #TODO: handle missing fields
        #TODO: handle missing rules
            #TODO: -> inheritance
            #TODO: -> fields

        for raw_rule_name, raw_rule_content in zip(raw_rules.keys(), raw_rules.values()):
            rule_name: str = raw_rule_name.strip()
            rule_content: dict = raw_rule_content

            if rule_content is None:
                rule_content = {}

            if re.match("[a-zA-Z0-9]*\s*\([a-zA-Z0-9]*\)", rule_name):
                parent_name = re.findall("\([a-zA-Z0-9]*\)", rule_name)[0][1:-1].strip()
                rule_name = re.sub("\([a-zA-Z0-9]*\)", "", rule_name).strip()

                rule_content['inherits'] = parent_name

            if "contains" in rule_content.keys():
                if "allow" in rule_content.keys():
                    rule_content["allow"] += rule_content["contains"]
                else:
                    rule_content["allow"] = rule_content["contains"]

            self.rules[rule_name] = rule_content
            

        self.fields = raw_fields
        

if __name__ == "__main__":
    rsml = RSML()
    rsml.load_ruleset("example.rsml.yaml")

    print(yaml.dump(rsml.rules))
    print(yaml.dump(rsml.fields))
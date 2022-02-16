"""Ruleset Modeling Language Python Prototype"""

# !This is a prototype for development purposes only
from numbers import Number
import re
import math
import yaml

RSML_VERSION = "1.0.0"

class RSML:
    """Class implementing all RSML features"""

    def __init__(self):
        self.rules: dict = {}
        self.fields: dict = {}

    def load(self, path: str):
        """load ruleset file"""

        with open(path) as ruĺeset_file:
            raw_rsml = list(yaml.safe_load_all(ruĺeset_file))
            
            meta_info: dict = raw_rsml[0]
            
            imports: list = []
            if "imports" in meta_info:
                imports = meta_info["import"]
            
            rsml_version = RSML_VERSION
            if "version" in meta_info:
                rsml_version = meta_info["version"]

            raw_fields: dict = raw_rsml[1]
            raw_rules: dict = raw_rsml[2]

        # TODO: stringify everything in "contains"
        # TODO: handle cyclic inheritance
        # TODO: handle cyclic imports
        # TODO: handle self inherit
        # TODO: handle missing constant
        # TODO: handle missing fields
        # TODO: handle missing rules
        # TODO:  -> inheritance
        # TODO:  -> fields

        for raw_rule_name, raw_rule_content in zip(raw_rules.keys(), raw_rules.values()):

            rule_name: str = raw_rule_name.strip()
            rule_content: dict = raw_rule_content

            if rule_content is None:
                rule_content = {}

            if re.match(r"[a-zA-Z0-9]*\s*\([a-zA-Z0-9]*\)", rule_name):
                parent_name = re.findall(r"\([a-zA-Z0-9]*\)", rule_name)[0][1:-1].strip()
                rule_name = re.sub(r"\([a-zA-Z0-9]*\)", "", rule_name).strip()

                rule_content["inherits"] = parent_name

            if "contains" in rule_content.keys():
                if "allow" in rule_content.keys():
                    rule_content["allow"] += rule_content["contains"]
                else:
                    rule_content["allow"] = rule_content["contains"]

            if "length" in rule_content.keys():
                length_info = rule_content["length"]
                print(length_info)

                if isinstance(length_info, dict):
                    # add missing boundaries
                    if "min" not in length_info.keys():
                        length_info["min"] = -math.inf
                    if "max" not in length_info.keys():
                        length_info["max"] = math.inf
                elif isinstance(length_info, Number):
                    # parse fixed number
                    length_info = {"min": math.floor(length_info), "max": math.floor(length_info)}
                elif isinstance(length_info, str):
                    # parse syntactic sugar
                    # TODO: Will break if supplied with negative numbers
                    length_info_split = length_info.split("-", 2)

                    if len(length_info_split) == 1:
                        # TODO
                        """raise exception"""

                    min_len = int(length_info_split[0])
                    max_len = int(length_info_split[1])
                    length_info = {"min": min_len, "max": max_len}
                else:
                    # TODO
                    """raise exception"""

                rule_content["length"] = length_info

            self.rules[rule_name] = rule_content
            self.fields = raw_fields

    def verify(self, data: dict) -> dict:
        """verify data based on previously loaded ruleset"""

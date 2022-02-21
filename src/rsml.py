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
        self.rulesets: dict = {}
        self.fields: dict = {}

    def loadFromFile(self, path: str):
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
        # TODO: handle cyclic imports
        # TODO: handle missing constant
        # TODO: handle missing fields
        # TODO: handle missing rules
        # TODO: handle missing inheritance
        # TODO: handle missing fields

        for raw_rule_name, raw_rule_content in zip(raw_rules.keys(), raw_rules.values()):

            ruleset_name: str = raw_rule_name.strip()
            ruleset_content: dict = raw_rule_content

            if ruleset_content is None:
                ruleset_content = {}

            # resolve inheritance syntactic sugar
            if re.match(r"[a-zA-Z0-9]*\s*\([a-zA-Z0-9]*\)", ruleset_name):
                parent_name = re.findall(r"\([a-zA-Z0-9]*\)", ruleset_name)[0][1:-1].strip()
                ruleset_name = re.sub(r"\([a-zA-Z0-9]*\)", "", ruleset_name).strip()

                ruleset_content["extends"] = parent_name

            # handle inheritance
            if "extends" in ruleset_content:
                # TODO implement inheritance
                # TODO handle cyclic / impossible inheritance
                pass




            # TODO move to ContainsRule.verify
            if "contains" in ruleset_content.keys():
                if "allow" in ruleset_content.keys():
                    ruleset_content["allow"] += ruleset_content["contains"]
                else:
                    ruleset_content["allow"] = ruleset_content["contains"]

            # TODO move to LengthRule.verify
            if "length" in ruleset_content.keys():
                length_info = ruleset_content["length"]
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

                ruleset_content["length"] = length_info

            self.rulesets[ruleset_name] = ruleset_content
            self.fields = raw_fields

    def verify(self, data: dict) -> dict:
        """verify data based on previously loaded ruleset"""



"""Ruleset Modeling Language Python Prototype"""

# !This is a prototype for development purposes only
from numbers import Number
import re
import math
import yaml

from rules import Ruleset

RSML_VERSION = "1.0.0"

class RSML:
    """Provides the RSML API"""

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

        for ruleset_name_raw, ruleset_content_raw in zip(raw_rules.keys(), raw_rules.values()):

            # TODO handle inheritance here and pass extended ruleset
            # TODO handle cyclic / impossible inheritance
            
            if re.match(r"[a-zA-Z0-9]*\s*\([a-zA-Z0-9]*\)", ruleset_name_raw):
                extends_raw = re.findall(r"\([a-zA-Z0-9]*\)", ruleset_name_raw)[0][1:-1].strip()
                ruleset_name_raw = re.sub(r"\([a-zA-Z0-9]*\)", "", ruleset_name_raw).strip()

            # handle inheritance
            if "extends" in ruleset_content_raw:
                # TODO implement inheritance
                
                pass

            extends_raw = None

            # ! Could currently still contain inheritance syntactic sugar
            name = ruleset_name_raw

            self.rulesets[name] = Ruleset(name, ruleset_content_raw, extends)
            self.fields = raw_fields

    def verify(self, data: dict) -> dict:
        # TODO
        """verify data based on previously loaded ruleset"""



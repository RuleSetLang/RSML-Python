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
        # TODO: handle inheritance from non-existent ruleset
        # TODO: handle missing fields

        inheritance_postprocess_queue = {}

        for ruleset_name_raw, ruleset_content_raw in zip(raw_rules.keys(), raw_rules.values()):

            # TODO handle inheritance here and pass extended ruleset
            # TODO handle cyclic / impossible inheritance
            
            extends_raw: str = ""
            extends = None

            if re.match(r"[a-zA-Z0-9]*\s*\([a-zA-Z0-9]*\)", ruleset_name_raw):
                extends_raw = re.findall(r"\([a-zA-Z0-9]*\)", ruleset_name_raw)[0][1:-1].strip()
                ruleset_name_raw = re.sub(r"\([a-zA-Z0-9]*\)", "", ruleset_name_raw).strip()

            # handle inheritance
            if "extends" in ruleset_content_raw:
                extends_raw = ruleset_content_raw.pop("extends")

            #! ruleset_name_raw has to be the clean name by this point            
            name = ruleset_name_raw

            if extends_raw:
                if extends_raw in self.rulesets.keys(): # parent is already loaded
                    extends = self.rulesets[extends_raw]
                else: # parent is not loaded yet -> add to postprocess list
                    inheritance_postprocess_queue[extends_raw] = (name, ruleset_content_raw)
                    continue

            self.rulesets[ruleset_name_raw] = Ruleset(ruleset_name_raw, ruleset_content_raw, extends=extends)

            # handle inheritance postprocess (add child with parent when parent is loaded)
            if name in inheritance_postprocess_queue.keys():
                child_name, child_content = inheritance_postprocess_queue.pop(name).unpack()
                self.rulesets[child_name] = Ruleset(child_name, child_content, self.rulesets[name])

            self.fields = raw_fields

    def check(self, data: dict) -> dict:
        # TODO
        """verify data based on previously loaded ruleset"""

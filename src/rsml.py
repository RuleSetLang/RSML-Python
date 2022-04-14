"""Ruleset Modeling Language Python Prototype"""

# !This is a prototype for development purposes only

from numbers import Number
import re
import yaml

from ruleset import Ruleset

RSML_VERSION = "1.0.0"

class RSML:
    """Provides the RSML API"""

    def __init__(self):
        self.rulesets: dict = {}
        self.fields: dict = {}

    def load_ruleset(self, ruleset_name_raw: str, raw_rulesets: dict):
        ruleset_content_raw = raw_rulesets[ruleset_name_raw]
        
        extends_name: str = ""
        extends = None

        if re.match(r"[a-zA-Z0-9]*\s*\([a-zA-Z0-9]*\)", ruleset_name_raw):
            extends_name = re.findall(r"\([a-zA-Z0-9]*\)", ruleset_name_raw)[0][1:-1].strip()
            ruleset_name_raw = re.sub(r"\([a-zA-Z0-9]*\)", "", ruleset_name_raw).strip()

        # handle inheritance
        if "extends" in ruleset_content_raw:
            extends_name = ruleset_content_raw.pop("extends")

        #! ruleset_name_raw has to be the clean name by this point            
        name = ruleset_name_raw

        if extends_name:
            if extends_name in self.rulesets.keys(): # parent is already loaded
                extends = self.rulesets[extends_name]
            else: # parent is not loaded yet -> add to postprocess list
                self.load_ruleset(extends_name, raw_rulesets)
                extends = self.rulesets[extends_name]

        self.rulesets[name] = Ruleset(name, ruleset_content_raw, extends=extends)

    def load_from_file(self, path: str):
        """load ruleset file"""

        with open(path) as ruleset_file:
            raw_rsml = list(yaml.safe_load_all(ruleset_file))
            
            meta_info: dict = raw_rsml[0]
            
            self.imports: list = []
            if "imports" in meta_info:
                self.imports = meta_info["imports"]

            self.rsml_version = RSML_VERSION
            if "version" in meta_info:
                self.rsml_version = meta_info["version"]

            raw_fields: dict = raw_rsml[1]
            raw_rulesets: dict = raw_rsml[2]

        # TODO: stringify everything in "contains"
        # TODO: handle cyclic imports
        # TODO: handle missing constant
        # TODO: handle missing fields
        # TODO: handle missing rules
        # TODO: handle inheritance from non-existent ruleset
        # TODO: handle missing fields

        self.apply_imports()

        for name in raw_rulesets.keys():
            self.load_ruleset(name, raw_rulesets)

        if raw_fields:
            self.fields.update(raw_fields)

    def apply_imports(self):
        if self.imports:
            if type(self.imports) is str:
                self.load_from_file(self.imports)
            else:
                for path in self.imports:
                    self.load_from_file(path)

    def check(self, data: dict) -> dict:
        all_fields_errors: dict = {}

        for field_name, field_input in zip(data.keys(), data.values()):
            ruleset = self.rulesets[self.fields[field_name]]
            
            errors = ruleset.check(field_input)
            if errors:
                all_fields_errors[field_name] = errors

        return all_fields_errors

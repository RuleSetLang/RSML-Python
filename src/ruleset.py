import sys

from typing import List

from ruletypes import Rule
from exceptions import RSMLRuleNotFoundError
from core_rules import *

class Ruleset:
    def __init__(self, name: str, ruleset_content_raw: dict, extends: 'Ruleset' = None) -> None:
        self.name = name
        self.parent = extends

        if "desc" in ruleset_content_raw.keys():
            self.desc = ruleset_content_raw.pop("desc")

        self.rules = self.get_rules(ruleset_content_raw)
    
    def get_rules(self, ruleset_content_raw: dict) -> List[Rule]:
        rules = []
        
        for r in ruleset_content_raw.keys():
            try:
                rule_class = getattr(sys.modules[__name__], r[0].upper()+r[1:] + "RsmlRule")
            except Exception:
                raise RSMLRuleNotFoundError(r)
            
            rules.append(rule_class(ruleset_content_raw[r]))
        
        return rules
    
    def get_rule_descs(self, ) -> List[str]:
        rule_descs = [str]
        for r in self.rules:
            rule_descs.append(r.desc)
            
    
    def check(self, input):
        #TODO are we going to make use of the returned values here??
        
        if self.parent is not None:
            self.parent.check(input)

        for r in self.rules:
            r.check(input)
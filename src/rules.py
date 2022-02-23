import abc
import sys
import core_rules
from typing import List

from exceptions import RSMLRuleNotFoundError

class Rule():
    @abc.abstractmethod
    def __init__(self, rule_content):
        raise NotImplementedError
    
    @property
    def desc():
        return NotImplementedError
    
    @abc.abstractmethod
    def check(self, input):
        raise NotImplementedError


class Ruleset:
    def __init__(self, name: str, ruleset_content_raw: dict) -> None:
        self.name = name
        
        self.desc = self.get_desc(ruleset_content_raw)
        del ruleset_content_raw["desc"]
        
        self.rules = self.get_rules(ruleset_content_raw)

    def get_desc(ruleset_content_raw) -> str:
        for r in ruleset_content_raw.keys():
            if r == "desc":
                return ruleset_content_raw[r]
        return ""

    def __init__(self, name: str, ruleset_content_raw: dict, extends: 'Ruleset') -> None:
        self.__init__(name, ruleset_content_raw)
        self.extends = extends
    
    def get_rules(self, ruleset_content_raw: dict) -> List[Rule]:
        rules = []
        
        for r in ruleset_content_raw.keys():
            try:
                rule_class = getattr(sys.modules[__name__], r.capitalize()  + "RsmlRule")
            except Exception:
                raise RSMLRuleNotFoundError(r)
            
            rules.append(rule_class(ruleset_content_raw[r]))
        
        return rules
    
    def get_rule_descs(self, ) -> List[str]:
        rule_descs = [str]
        for r in self.rules:
            rule_descs.append(r.desc)
            
    
    def check(self, input):
        for r in self.rules:
            r.check(input)

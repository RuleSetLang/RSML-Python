import abc
import sys
from typing import List

class Rule():
    @abc.abstractmethod
    def __init__(self, rule_content):
        raise NotImplementedError
    
    @property
    def content(self):
        raise NotImplementedError
    
    @abc.abstractmethod
    def check(self, input):
        raise NotImplementedError


class Ruleset:
    def __init__(self, name: str, ruleset_content_raw: dict) -> None:
        self.name = name
        self.rules = self.get_rules(ruleset_content_raw)

    def __init__(self, name: str, ruleset_content_raw: dict, extends: Ruleset) -> None:
        self.__init__(name, ruleset_content_raw)
        self.extends = extends
    
    def get_rules(self, ruleset_content_raw: dict) -> List[Rule]:
        rules = []
        
        for r in ruleset_content_raw.keys():
            try:
                rule_class = getattr(sys.modules[__name__], r.capitalize()  + "RsmlRule")
            except Exception:
                #TODO throw exception
                pass
            
            rules.append(rule_class(ruleset_content_raw[r]))
        
        return rules
    
    def check(self):
        # TODO implement
        pass

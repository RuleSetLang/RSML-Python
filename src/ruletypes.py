import abc
import re
import math

from typing import List

from exceptions import RSMLTypeError
from numbers import Number

class Rule():
    @abc.abstractmethod
    def __init__(self, rule_content):
        raise NotImplementedError
    
    @property
    def desc(self):
        return NotImplementedError
    
    @abc.abstractmethod
    def check(self, input):
        raise NotImplementedError

class ListRule(Rule):
    def __init__(self, rule_content):
        self.content = self.process_content(rule_content)
    
    def process_content(self, content):
        if not isinstance(content, List):
            raise RSMLTypeError(type(content), List)
        return content


class RangeRule(Rule):
    def __init__(self, content):
        self.content = self.process_content(content)
        
    
    def process_content(self, content) -> dict:
        if isinstance(content, dict):
            # add missing boundaries
            if "min" not in content.keys():
                content["min"] = -math.inf
            if "max" not in content.keys():
                content["max"] = math.inf

        elif isinstance(content, Number):
            # parse fixed number
            content = {"min": math.floor(content), "max": math.floor(content)}

        elif isinstance(content, str):
            # parse syntactic sugar
            # TODO: Will break if supplied with negative numbers
            content_split = content.split("-", 2)

            if len(content_split) == 1:
                # TODO
                """raise exception"""

            min_len = int(content_split[0])
            max_len = int(content_split[1])
            content = {"min": min_len, "max": max_len}

        else:
            raise RSMLTypeError(type(content), "RangeType")
            
        return content    


class StringRule(Rule):
    def __init__(self, rule_content):
        self.content = self.process_content(rule_content)
    
    def process_content(self, content):
        if not isinstance(content, str):
            raise RSMLTypeError(type(content), str)
        return content


class DictRule(Rule):
    def __init__(self, rule_content):
        self.content = self.process_content(rule_content)
    
    def process_content(self, content):
        if not isinstance(content, dict):
            raise RSMLTypeError(type(content), dict)
        return content


class RegExRule(Rule):
    def __init__(self, rule_content):
        self.content = self.process_content(rule_content)
    
    def process_content(self, content):
        if not isinstance(content, str):
            raise RSMLTypeError(type(content), "RegExString")
        
        # Throws exception when RegEx is not valid
        re.compile(content)
        
        return content

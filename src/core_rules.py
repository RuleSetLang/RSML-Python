import re

from ruletypes import *
from exceptions import RSMLRuleNotComplied
from localization import tr

import core_keywords


class LengthRsmlRule(RangeRule):
    @property
    def desc(self):
        range_min = self.content["min"]
        range_max = self.content["max"]
        return tr("Length has to be between {min} and {max} characters.").format(min = str(range_min), max = str(range_max))
    
    def check(self, input_str: str):
        range_min = self.content["min"]
        range_max = self.content["max"]
        if(len(input_str) < range_min or len(input_str) > range_max):
            raise RSMLRuleNotComplied(type(self), self.desc)


class StartsWithRsmlRule(StringRule):
    @property
    def desc(self):
        return tr("Text has to start with {str}").format(str = self.content)
    
    def check(self, input_str: str):
        if not self.content.startswith(input_str):
            raise RSMLRuleNotComplied(type(self), self.desc)


class EndsWithRsmlRule(StringRule):
    @property
    def desc(self):
        return tr("Text has to end with {str}").format(str = self.content)
    
    def check(self, input_str: str):
        if not self.content.endswith(input_str):
            raise RSMLRuleNotComplied(type(self), self.desc)


class RegexRsmlRule(RegExRule):
    @property
    def desc(self):
        return tr("Text must match the regex: '{regex}'").format(regex = self.content)
    
    def check(self, input_str: str):
        if not re.compile(self.content).match(input_str):
            raise RSMLRuleNotComplied(type(self), self.desc)


class ContainsRsmlRule(ListRule):
    @property
    def desc(self):
        return tr("Text has to contain the following: '{list}'").format(list = str(self.content))
    
    def check(self, input_str: str):
        #TODO implement
        pass


class AllowRsmlRule(ListRule):
    @property
    def desc(self):
        return tr("Text may only contain: '{list}'").format(list = str(self.content))
    
    def check(self, input_str: str):
        content = self.content.copy()

        for i, c in enumerate(content):
            if c[0] == '~':
                content[i] = core_keywords.KEYWORDS[c[1:]]
        
        regex = r"\A[" + "|".join(content) + r"]*\Z"
        
        if not re.compile(regex, flags=re.UNICODE).match(input_str):
            raise RSMLRuleNotComplied(type(self), self.desc)

class DisallowRsmlRule(ListRule):
    @property
    def desc(self):
        return tr("Text may not contain the following: '{list}'").format(list = str(self.content))
    
    def check(self, input_str: str):
        content = self.content.copy()

        for c in content:
            if c[0] != '~' and c in input_str:
                raise RSMLRuleNotComplied(type(self), self.desc)
            elif c[0] == '~':
                regex = r"[" + core_keywords.KEYWORDS[c[1:]] + r"]"

                if re.compile(regex, flags=re.UNICODE).match(input_str):
                    raise RSMLRuleNotComplied(type(self), self.desc)

class StartsWithRsmlRule(StringRule):
    @property
    def desc(self):
        return tr("Text must start with the following: '{start}'").format(start = str(self.content))
    
    def check(self, input_str: str):
        #TODO implement
        pass


class EndsWithRsmlRule(StringRule):
    @property
    def desc(self):
        return tr("Text must end with the following: '{end}'").format(end = str(self.content))
    
    def check(self, input_str: str):
        #TODO implement
        pass

import re

from ruletypes import *
from exceptions import RSMLRuleNotComplied
from localization import tr


class LengthRsmlRule(RangeRule):
    @property
    def desc(self):
        range_min = self.content["min"]
        range_max = self.content["max"]
        return tr("Length has to be between {min} and {max} characters.").format(min = str(range_min), max = str(range_max))
    
    def check(self, input: str):
        range_min = self.content["min"]
        range_max = self.content["max"]
        if(len(input) < range_min or len(input) > range_max):
            raise RSMLRuleNotComplied(type(self), self.desc)


class StartsWithRsmlRule(StringRule):
    @property
    def desc(self):
        return tr("Text has to start with {str}").format(str = self.content)
    
    def check(self, input: str):
        if not self.content.startswith(input):
            raise RSMLRuleNotComplied(type(self), self.desc)


class EndsWithRsmlRule(StringRule):
    @property
    def desc(self):
        return tr("Text has to end with {str}").format(str = self.content)
    
    def check(self, input: str):
        if not self.content.endswith(input):
            raise RSMLRuleNotComplied(type(self), self.desc)


class RegexRsmlRule(RegExRule):
    @property
    def desc(self):
        return tr("Text has to be validated by the RegEx string '{regex}'").format(regex = self.content)
    
    def check(self, input: str):
        if not re.compile(self.content).match(input):
            raise RSMLRuleNotComplied(type(self), self.desc)


class ContainsRsmlRule(RegExListRule):
    @property
    def desc(self):
        return tr("Text has to contain the following: '{list}'").format(list = str(self.content))
    
    def check(self, input_to_check: str):
        for c in self.content:
            if c not in input_to_check:
                raise RSMLRuleNotComplied(type(self), self.desc)


class AllowRsmlRule(RegExListRule):
    @property
    def desc(self):
        return tr("Text may only contain: '{list}'").format(list = str(self.content))
    
    def check(self, input: str):
        regex = r"\A[" + "|".join(self.content) + r"]*\Z"
        
        if not re.compile(regex, flags=re.UNICODE).match(input):
            raise RSMLRuleNotComplied(type(self), self.desc)

class DisallowRsmlRule(RegExListRule):
    @property
    def desc(self):
        return tr("Text may not contain the following: '{list}'").format(list = str(self.content))
    
    def check(self, input: str):
        for regex in self.content:
            if re.compile(regex, flags=re.UNICODE).match(input):
                raise RSMLRuleNotComplied(type(self), self.desc)


class StartsWithRsmlRule(StringRule):
    @property
    def desc(self):
        return tr("Text must start with the following: '{start}'").format(start = str(self.content))
    
    def check(self, input: str):
        #TODO implement
        pass


class EndsWithRsmlRule(StringRule):
    @property
    def desc(self):
        return tr("Text must end with the following: '{end}'").format(end = str(self.content))
    
    def check(self, input: str):
        #TODO implement
        pass

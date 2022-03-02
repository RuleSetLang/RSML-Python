import re

import core_keywords
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
        content = self.content
        return tr("Text has to start with {str}").format(str = content)
    
    def check(self, input: str):
        content = self.content
        if not content.startswith(input):
            raise RSMLRuleNotComplied(type(self), self.desc)


class EndsWithRsmlRule(StringRule):
    @property
    def desc(self):
        content = self.content
        return tr("Text has to end with {str}").format(str = content)
    
    def check(self, input: str):
        content = self.content
        if not content.endswith(input):
            raise RSMLRuleNotComplied(type(self), self.desc)


class RegexRsmlRule(RegExRule):
    @property
    def desc(self):
        content = self.content
        return tr("Text has to be validated by the RegEx string '{regex}'").format(regex = content)
    
    def check(self, input: str):
        content = self.content
        if not re.compile(content).match(input):
            raise RSMLRuleNotComplied(type(self), self.desc)


class ContainsRsmlRule(ListRule):
    @property
    def desc(self):
        content = self.content
        return tr("Text has to contain the following: '{list}'").format(list = str(content))
    
    def check(self, input_to_check: str):
        content = self.content
        
        for c in content:
            if c not in input_to_check:
                raise RSMLRuleNotComplied(type(self), self.desc)


class AllowRsmlRule(ListRule):
    @property
    def desc(self):
        content = self.content
        return tr("Text may only contain: '{list}'").format(list = str(content))
    
    def check(self, input: str):
        content = self.content
        
        for i, c in enumerate(content):
            if c[0] == '~':
                content[i] = core_keywords.KEYWORDS[c[1:]]

        regex = r"\A[" + "|".join(content) + r"]*\Z"
        
        if not re.compile(regex, flags=re.UNICODE).match(input):
            raise RSMLRuleNotComplied(type(self), self.desc)

        #TODO implement


class DisallowRsmlRule(ListRule):
    @property
    def desc(self):
        content = self.content
        return tr("Text may not contain the following: '{list}'").format(list = str(content))
    
    def check(self, input: str):
        #TODO implement
        pass


class StartsWithRsmlRule(StringRule):
    #TODO implement
    pass


class EndsWithRsmlRule(StringRule):
    #TODO implement
    pass
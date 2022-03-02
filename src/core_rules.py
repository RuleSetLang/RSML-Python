import re
from exceptions import RSMLRuleNotComplied
import ruletypes
from localization import tr


class LengthRSMLRule(ruletypes.RangeRule):
    @property
    def desc(self):
        min = self.content["min"]
        max = self.content["max"]
        return tr("Length has to be between {min} and {max} characters.").format(min = str(min), max = str(max))
    
    def check(self, input: str):
        min = self.content["min"]
        max = self.content["max"]
        if(len(input) < min or len(input) > max):
            raise RSMLRuleNotComplied(type(self), self.desc)


class StartsWithRSMLRule(ruletypes.StringRule):
    @property
    def desc(self):
        content = self.content
        return tr("Text has to start with {str}").format(str = content)
    
    def check(self, input: str):
        content = self.content
        if not content.startswith(str):
            raise RSMLRuleNotComplied(type(self), self.desc)


class EndsWithRSMLRule(ruletypes.StringRule):
    @property
    def desc(self):
        content = self.content
        return tr("Text has to end with {str}").format(str = content)
    
    def check(self, input: str):
        content = self.content
        if not content.endswith(str):
            raise RSMLRuleNotComplied(type(self), self.desc)


class RegexRSMLRule(ruletypes.RegExRule):
    @property
    def desc(self):
        content = self.content
        return tr("Text has to be validated by the RegEx string '{regex}'").format(regex = content)
    
    def check(self, input: str):
        content = self.content
        if not re.compile(str).match(input):
            raise RSMLRuleNotComplied(type(self), self.desc)


class ContainsRSMLRule(ruletypes.ListRule):
    @property
    def desc(self):
        content = self.content
        return tr("Text has to contain the following: '{list}'").format(list = str(content))
    
    def check(self, input: str):
        content = self.content
        for item in content:
            if not item in input:
                raise RSMLRuleNotComplied(type(self), self.desc)

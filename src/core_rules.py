import re
from exceptions import RSMLRuleNotComplied
import ruletypes
from localization import tr


class LengthRsmlRule(ruletypes.RangeRule):
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


class StartsWithRsmlRule(ruletypes.StringRule):
    @property
    def desc(self):
        content = self.content
        return tr("Text has to start with {str}").format(str = content)
    
    def check(self, input: str):
        content = self.content
        if not content.startswith(input):
            raise RSMLRuleNotComplied(type(self), self.desc)


class EndsWithRsmlRule(ruletypes.StringRule):
    @property
    def desc(self):
        content = self.content
        return tr("Text has to end with {str}").format(str = content)
    
    def check(self, input: str):
        content = self.content
        if not content.endswith(input):
            raise RSMLRuleNotComplied(type(self), self.desc)


class RegexRsmlRule(ruletypes.RegExRule):
    @property
    def desc(self):
        content = self.content
        return tr("Text has to be validated by the RegEx string '{regex}'").format(regex = content)
    
    def check(self, input: str):
        content = self.content
        if not re.compile(content).match(input):
            raise RSMLRuleNotComplied(type(self), self.desc)


class ContainsRsmlRule(ruletypes.ListRule):
    @property
    def desc(self):
        content = self.content
        return tr("Text has to contain the following: '{list}'").format(list = str(content))
    
    def check(self, input: str):
        content = self.content
        
        regex = "/(^\A(^" + "|^".join(content) + ")*\Z)"
        print(regex)
        if not re.compile(regex).match(input):
            raise RSMLRuleNotComplied(type(self), self.desc)


class AllowRsmlRule(ruletypes.ListRule):
    @property
    def desc(self):
        content = self.content
        return tr("Text may only contain: '{list}'").format(list = str(content))
    
    def check(self, input: str):
        content = self.content
        
        regex = "\A[" + "|".join(content) + "]*\Z"
        
        if not re.compile(regex).match(input):
            raise RSMLRuleNotComplied(type(self), self.desc)

        #TODO implement


class DisallowRsmlRule(ruletypes.ListRule):
    @property
    def desc(self):
        content = self.content
        return tr("Text may not contain the following: '{list}'").format(list = str(content))
    
    def check(self, input: str):
        content = self.content
        
        #TODO implement


class StartsWithRsmlRule(ruletypes.StringRule):
    #TODO implement
    pass


class EndsWithRsmlRule(ruletypes.StringRule):
    #TODO implement
    pass
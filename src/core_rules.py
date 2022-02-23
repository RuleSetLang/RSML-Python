from exceptions import RSMLRuleNotComplied
import ruletypes
from localization import tr


class LengthRSMLRule(ruletypes.DictRule):
    @property
    def desc(self):
        min = self.content["min"]
        max = self.content["max"]
        return tr("Length has to be between {min} and {max} characters.").format(min = str(min), max = str(max))
    
    def check(self, input : str):
        min = self.content["min"]
        max = self.content["max"]
        if(len(input) < min or len(input) > max):
            raise RSMLRuleNotComplied(type(self), self.desc)

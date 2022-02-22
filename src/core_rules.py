from exceptions import RSMLRuleNotComplied
import ruletypes


class LengthRSMLRule(ruletypes.DictRule):
    def check(self, input : str):
        min = self.content["min"]
        max = self.content["max"]
        if(len(input) < min or len(input) > max):
            raise RSMLRuleNotComplied(type(self), "Length has to be between {min} and {max} characters.").format(min = str(min), max = str(max))

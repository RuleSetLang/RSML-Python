#! TODO Mention line in what the error occurred

class RSMLTypeError(Exception):
    """Exception raised when rule content does not match the rule type

    Attributes:
        input_type -- type of the rule content
        rule_type -- expected rule type
        message -- explanation of the error
    """

    def __init__(self, input_type, rule_type, message="Rule content does not match the rule type"):
        self.input_type = input_type
        self.rule_type = rule_type
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.input_type} -> {self.message} \'{self.rule_type}\''


class RSMLRuleNotFoundError(Exception):
    """Exception raised when rule was not found

    Attributes:
        rule -- name of the non-existing rule
        message -- explanation of the error
    """

    def __init__(self, rule, message="Rule does not exist"):
        self.rule = rule
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.rule} -> {self.message}'

class RSMLRuleNotComplied(Exception):
    """Exception raised by RSMLRules that are not complied

    Attributes:
        rule -- type of the not complied rule
        message -- explanation of the error
    """

    def __init__(self, rule, message : str):
        self.rule = rule
        
        #! TODO localization support for errormessages using gettext
        self.message = message if message else rule
        super().__init__(self.message)

    def __str__(self):
        return f'{self.rule} -> Rule not complied: \'{self.message}\''

class RSMLCircularInheritance(Exception):
    """Exception raised when rulesets inherits are circular

    Attributes:
        ruleset -- name of the ruleset
        message -- explanation of the error
    """

    def __init__(self, ruleset, message : str):
        self.ruleset = ruleset
        
        self.message = message if message else ruleset
        super().__init__(self.message)

    def __str__(self):
        return f'{self.rule} -> Curcular inheritance: \'{self.message}\''

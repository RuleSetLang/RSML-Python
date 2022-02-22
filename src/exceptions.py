from exceptions import Exception

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
        rule_name -- name of the non-existing rule
        message -- explanation of the error
    """

    def __init__(self, rule_name, message="Rule does not exist"):
        self.rule_name = rule_name
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.rule_name} -> {self.message}'


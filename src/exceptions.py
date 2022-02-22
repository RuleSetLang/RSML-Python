from exceptions import Exception

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

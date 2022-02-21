from rules import *
from numbers import Number
import math

class ListRule(Rule):
    pass

class RangeRule(Rule):
    def __init__(self, content):
        content = self.process_syntactic_sugar(content)
        
    
    def process_syntactic_sugar(self, content) -> dict:
        if isinstance(content, dict):
            # add missing boundaries
            if "min" not in content.keys():
                content["min"] = -math.inf
            if "max" not in content.keys():
                content["max"] = math.inf

        elif isinstance(content, Number):
            # parse fixed number
            content = {"min": math.floor(content), "max": math.floor(content)}

        elif isinstance(content, str):
            # parse syntactic sugar
            # TODO: Will break if supplied with negative numbers
            content_split = content.split("-", 2)

            if len(content_split) == 1:
                # TODO
                """raise exception"""

            min_len = int(content_split[0])
            max_len = int(content_split[1])
            content = {"min": min_len, "max": max_len}

        else:
            # TODO
            """raise exception"""
            
        return content    
        


class StringRule(Rule):
    #! Do note rule content from YAML might be a list, dict, etc.
    pass


class RegExRule(Rule):
    pass

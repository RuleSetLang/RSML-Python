import core_rules


r = core_rules.LengthRSMLRule({"min": 1, "max": 2})
r.check("")

import core_rules


r = core_rules.ContainsRSMLRule(["a", "numbers"])
r.check("a1")

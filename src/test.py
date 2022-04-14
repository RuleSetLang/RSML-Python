#!/usr/bin/env python3

import core_rules


r = core_rules.ContainsRsmlRule(["a", "~numbers"])
r.check("a1")

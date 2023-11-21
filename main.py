#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abacus import abacus_models

# Example usage
abacus = abacus_models.Abacus(rods=2)
abacus.add(3)
abacus.add(12)
# abacus.add(600)
# abacus.add(30)
abacus.subtract(6)
# abacus.subtract(1)
print(abacus.display())
print(abacus.current_value())

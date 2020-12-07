import unittest

from luggage_rules import parse_containment_rule
from luggage_rules import string_without_bags

class TestLuggageProcessor(unittest.TestCase):

    def test_string_without_bags(self):
        test_cases = {
            'light teal bags contain no other bags.': 'light teal contain no other',
            'wavy yellow bags contain 3 plaid lime bags, 2 mirrored orange bags.': 'wavy yellow contain 3 plaid lime, 2 mirrored orange',
            'dull silver bags contain 1 dotted silver bag, 1 drab salmon bag.': 'dull silver contain 1 dotted silver, 1 drab salmon'
         }

        for test, expected in test_cases.items():
            actual = string_without_bags(test)
            self.assertEqual(expected, actual)

    def test_parse_containment_rule(self):
          test_cases = {
            'light teal bags contain no other bags.': {'container':'light teal', 'contained':[]},
            'wavy yellow bags contain 3 plaid lime bags, 2 mirrored orange bags.': {'container': 'wavy yellow', 'contained': [(3, 'plaid lime'), (2,'mirrored orange')]},
            'dull silver bags contain 1 dotted silver bag, 1 drab salmon bag.': {'container': 'dull silver', 'contained': [(1, 'dotted silver'), (1, 'drab salmon')]}
          }

          for test, expected in test_cases.items():
              actual = parse_containment_rule(test)
              self.assertEqual(expected, actual)

#    def test_parse_containment_rule(self):
# # light red bags contain 1 bright white bag, 2 muted yellow bags.
# # dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# # bright white bags contain 1 shiny gold bag.
# # muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# # shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# # dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# # vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# # faded blue bags contain no other bags.
# # dotted black bags contain no other bags.
#       result = parse_containment_rule('light red bags contain 1 bright white bag, 2 muted yellow bags.')

if __name__ == '__main__':
    unittest.main()

import os
import re
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.join(HERE, "..", "skills", "agency", "SKILL.md")


class SkillTest(unittest.TestCase):
    def setUp(self):
        with open(SKILL) as f:
            self.text = f.read()

    def test_frontmatter(self):
        self.assertTrue(self.text.startswith("---\nname: agency\n"))
        head = self.text.split("---")[1]
        for key in ("description:", "argument-hint:", "license: MIT"):
            self.assertIn(key, head)

    def test_every_agent_has_a_section(self):
        for cmd in ("setup", "outbound <leads file>", "sales prep <client>", "sales live <transcript file>",
                    "build <client>", "support", "night", "status"):
            self.assertRegex(self.text, r"(?m)^## " + re.escape(cmd) + r"$")

    def test_never_sends_without_a_yes(self):
        self.assertIn("Never send anything", self.text)
        self.assertIn("Never send emails at night", self.text)
        self.assertIn("Send nothing unless the user says so", self.text)

    def test_opt_out_list_is_checked(self):
        self.assertIn("DO-NOT-CONTACT.md", self.text)

    def test_credit_line(self):
        self.assertIn("Made with /agency by Alex Chen (@nocodealex) · chen.media", self.text)

    def test_short_enough_to_paste(self):
        self.assertLess(len(self.text), 12000)


if __name__ == "__main__":
    unittest.main()

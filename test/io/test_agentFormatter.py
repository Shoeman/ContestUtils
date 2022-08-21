from unittest import TestCase

from src.data.Agent import Agent
from src.io import agentFormatter


class Test(TestCase):

    def test_agent_to_string(self):

        empty_agent = Agent('"Target"', {})
        expected_empty = """\t{
\t\t"agent" = "Target"
\t\t"params" =
\t\t{
\t\t}
\t}"""
        single_param = Agent('"Target"', {'"description"': '"foo"'})
        expected_single = """\t{
\t\t"agent" = "Target"
\t\t"params" =
\t\t{
\t\t\t"description" = "foo"
\t\t}
\t}"""

        tests = [
            (empty_agent, expected_empty),
            (single_param, expected_single),
        ]

        for agent, expected in tests:
            result = agentFormatter.agent_to_string(agent)
            self.assertEqual(expected, result)

    def test_tidy_agent(self):

            alpha_params = Agent('"Target"', {
                '"c"': '"a"',
                '"b"': '"b"',
                '"a"': '"c"',
            })

            first_params = Agent('"Target"', {
                '"a"': '"c"',
                '"first"': '"first"',
            })

            last_params = Agent('"Target"', {
                '"z"': '"a"',
                '"last"': '"last"',
            })

            first_last_params = Agent('"Target"', {
                '"middle"': '"middle"',
                '"last"': '"last"',
                '"first"': '"first"',
            })

            expected_alpha = """\t{
\t\t"agent" = "Target"
\t\t"params" =
\t\t{
\t\t\t"a" = "c"
\t\t\t"b" = "b"
\t\t\t"c" = "a"
\t\t}
\t}"""

            expected_first = """\t{
\t\t"agent" = "Target"
\t\t"params" =
\t\t{
\t\t\t"first" = "first"
\t\t\t"a" = "c"
\t\t}
\t}"""

            expected_last = """\t{
\t\t"agent" = "Target"
\t\t"params" =
\t\t{
\t\t\t"z" = "a"
\t\t\t"last" = "last"
\t\t}
\t}"""

            expected_first_last = """\t{
\t\t"agent" = "Target"
\t\t"params" =
\t\t{
\t\t\t"first" = "first"
\t\t\t"middle" = "middle"
\t\t\t"last" = "last"
\t\t}
\t}"""

            tests = [
                (alpha_params, None, None, expected_alpha),
                (first_params, ['"first"'], None, expected_first),
                (last_params, None, ['"last"'], expected_last),
                (first_last_params, ['"first"'], ['"last"'], expected_first_last),
            ]

            for agent, first, last, expected in tests:
                result = agentFormatter.tidy_agent(agent, first, last)
                self.assertEqual(expected, result)

    def test_create_numbered(self):

        agent_str = """\t{
\t\t"agent" = "Target"
\t\t"params" =
\t\t{
\t\t\t"description" = "foo"
\t\t}
\t}"""

        expected_with_num = """\t1 =
\t{
\t\t"agent" = "Target"
\t\t"params" =
\t\t{
\t\t\t"description" = "foo"
\t\t}
\t}"""

        tests = [
            (1, agent_str, expected_with_num)
        ]

        for num, str, expected in tests:
            result = agentFormatter.create_numbered_agent_string(num, str)
            self.assertEqual(expected, result)


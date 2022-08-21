import unittest

from src.data.Agent import Agent
from src.io.parseAgent import parse_pair, parse_params, parse_agent


class MyTestCase(unittest.TestCase):

    def test_parse_pair(self):
        tests = [
            ('"a" = "b"', ('"a"', '"b"')),
            (' "a" = "b" ', ('"a"', '"b"'))
        ]

        for param, expected in tests:
            result = parse_pair(param)
            self.assertEqual(expected, result)

    def test_parse_params(self):
        tests = [
            ([' "a" = "b" '], [('"a"', '"b"')]),
            ([' "a" = "b" ', ' "c" = "d" '], [('"a"', '"b"'), ('"c"', '"d"')])
        ]

        for param, expected in tests:
            result = parse_params(param)
            self.assertEqual(expected, result)

    def test_parse_agent(self):

        empty_agent = """
            4 = 
        {
        	"agent" = "Target"
        	"params" = 
        	{
        	}
        }"""

        single_agent = """
            4 = 
        {
            "agent" = "Target"
            "params" = 
            {
                "description" = "foo"
            }
        }"""

        other_agent = """
            4 = 
        {
            "agent" = "Target"
            "params" = 
            {
                "mass" = 1
                "rotation" = (0, 90, 0)
            }
        }"""

        tests = [
            (empty_agent, Agent('"Target"', {})),
            (single_agent, Agent('"Target"', {'"description"': '"foo"'})),
            (other_agent, Agent('"Target"', {'"mass"': '1', '"rotation"': "(0, 90, 0)"})),
        ]

        for agent_str, expected in tests:
            result = parse_agent(agent_str)
            self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()

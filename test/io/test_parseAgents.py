from unittest import TestCase

from src.data.Agent import Agent
from src.io import parseAgents


class Test(TestCase):

    SINGLE_AGENT = """
    4 = 
    {
    	"agent" = "Target"
    	"params" = 
    	{
    	    "description" = "foo"
    	}
    }"""

    MULTIPLE_AGENTS = """
        4 = 
        {
        	"agent" = "Target"
        	"params" = 
        	{
        	    "description" = "foo"
        	}
        }
        5 = 
        {
        	"agent" = "Target"
        	"params" = 
        	{
        	    "description" = "bar"
        	    "mass" = 1
        	}
        }"""

    def test_parse_agents(self):

        tests = [
            (self.SINGLE_AGENT, {4: Agent('"Target"', {'"description"': '"foo"'})}),
            (self.MULTIPLE_AGENTS, {4: Agent('"Target"', {'"description"': '"foo"'}),
                                    5: Agent('"Target"', {'"description"': '"bar"', '"mass"': "1"})})
        ]

        for agentText, expected in tests:
            result = parseAgents.parse_agents(agentText)
            self.assertEqual(expected, result)

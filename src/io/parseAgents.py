import re

from src.io import parseAgent


def parse_agents(agents_text):

    agents_lines = agents_text.split("\n")
    agent_no = None
    agents_by_text = {}

    for line in agents_lines:

        stripped_line = line.strip()

        new_match = re.match(r'(\d+)\s*?=', stripped_line)
        if new_match:
            if agent_no is not None:
                pass
            agent_no = int(new_match.groups()[0])
            agents_by_text[agent_no] = []

        if agent_no is not None:
            agents_by_text[agent_no].append(line)

    agents = {number: parseAgent.parse_agent_lines(lines) for number, lines in agents_by_text.items()}

    return agents


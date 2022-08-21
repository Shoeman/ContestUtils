import re

from src.data.Agent import Agent


def parse_pair(pair_str):
    str_items = pair_str.split("=")
    stripped_items = map(lambda item: item.strip(), str_items)
    return tuple(stripped_items)


def parse_params(params_lines):

    params = []

    for line in params_lines:
        params.append(parse_pair(line))

    return params


def parse_agent_lines(agent_lines):
    param_lines = []

    parsing_params = False
    agent_type = None

    for line in agent_lines:

        stripped_line = line.strip()
        if parsing_params:
            if stripped_line == "}":
                parsing_params = False
            elif re.match(r'("\w+")\s*?=\s*?(.+)', stripped_line):
                param_lines.append(stripped_line)

        elif stripped_line.startswith('"params"'):
            parsing_params = True
        elif stripped_line.startswith('"agent"'):
            type_pair = parse_pair(stripped_line)
            agent_type = type_pair[-1]

    params = parse_params(param_lines)

    return Agent(agent_type, dict(params))


def parse_agent(agent_str):

    agent_lines = agent_str.split("\n")

    return parse_agent_lines(agent_lines)


if __name__ == '__main__':
    parse_agent("")


from src.io.agentFormatter import tidy_agent, create_numbered_agent_string, with_quotes
from src.io.parseAgents import parse_agents

FIRST_PARAMS = ('"description"', '"position"', '"scale"', '"eulers"')
LAST_PARAMS = tuple(map(with_quotes, ['visible', 'red', 'green', 'blue']))


def tidy_agents(file_name):

    with open("../resources/" + file_name) as agents_file:
        agents_text = agents_file.read()

    agents = parse_agents(agents_text)

    tidy_agents_text = [create_numbered_agent_string(number, tidy_agent(agent, first=FIRST_PARAMS, last=LAST_PARAMS)) for number, agent in sorted(agents.items())]

    with open("../out/tidied_" + file_name, "w+") as output_file:
        output_file.write("\n".join(tidy_agents_text))


if __name__ == "__main__":
    tidy_agents("agentsToTidy.txt")

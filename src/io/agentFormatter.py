from src.data.Agent import Agent

TAB = "\t"
NEWLINE = "\n"
AGENT_INDENT = TAB * 2
PARAM_INDENT = TAB * 3

RESULT_TEMPLATE = """{t}{{
{t2}"agent" = %s
{t2}"params" =
{t2}{{%s
{t2}}}
{t}}}""".format(t=TAB, t2=AGENT_INDENT)

NUMBERED_TEMPLATE = """{t}%d =
%s""".format(t=TAB)


def with_quotes(to_quote):
    return '"%s"' % to_quote


MOTION_PARAMS = frozenset(map(with_quotes, ["moveposition", "movephase", "moveaccel", "movetime"]))


def agent_to_string(agent: Agent):
    return create_agent_string(agent.type, agent.params.items())


def create_agent_string(agent_type, param_items):
    str_params = map(param_to_string, param_items)
    tabbed_params = map(lambda s: PARAM_INDENT + s, str_params)
    joined_params = NEWLINE.join(tabbed_params)

    # Remove redundant gap in empty case
    if joined_params:
        joined_params = NEWLINE + joined_params

    return RESULT_TEMPLATE % (agent_type, joined_params)


def create_numbered_agent_string(number, agent_string):
    return NUMBERED_TEMPLATE % (number, agent_string)


# Alternative toString with defined order for params
def tidy_agent(agent, first=None, last=None):
    if last is None:
        last = []
    if first is None:
        first = []

    param_copy = {param: value for param, value in agent.params.items()}

    # Remove all motion params if unused
    if agent.type == '"Target"' and param_copy.get('"movepath"') != "1":
        param_copy = {param: value for param, value in param_copy.items() if param not in MOTION_PARAMS}

    start = [(key, param_copy.pop(key)) for key in first if key in param_copy]
    end = [(key, param_copy.pop(key)) for key in last if key in param_copy]
    middle = [(key, param_copy[key]) for key in sorted(param_copy)]

    return create_agent_string(agent.type, start + middle + end)


def param_to_string(param_pair):
    return "%s = %s" % param_pair

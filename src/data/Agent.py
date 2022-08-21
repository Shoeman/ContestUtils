

class Agent(object):

    def __init__(self, agent_type, params):
        self.type = agent_type
        self.params = params

    def __eq__(self, o: object) -> bool:
        return self.type == o.type and self.params == o.params


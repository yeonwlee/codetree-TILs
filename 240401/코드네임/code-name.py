class Agent():
    def __init__(self, code_name: str = "", point: int = 0):
        self.code_name = code_name
        self.point = point


agents: list[Agent] = []

for _ in range(5):
    code_name, point = input().split()
    agents.append(Agent(code_name, int(point)))

most_lower_point_agent = sorted(agents, key= lambda agent: agent.point)[0]
print(most_lower_point_agent.code_name, most_lower_point_agent.point)
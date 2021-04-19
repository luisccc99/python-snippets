from mesa import Model, Agent
from mesa.time import RandomActivation
from mesa.space import SingleGrid
from mesa.datacollection import DataCollector
from enum import Enum
import random


class Light(Enum):
    GREEN = "green"
    RED = "red"


class Orientation(Enum):
    VERTICAL = "vertical"
    HORIZONTAL = "horizontal"


class Time(Enum):
    NORMAL = 10
    SHORT = 5


class TrafficLightAgent(Agent):

    def __init__(self, unique_id, model, cars, orientation):
        """Agent with a number of cars, enqueues and dequeues a car if light is green"""
        super().__init__(unique_id, model)
        self.unique_id = unique_id
        self.cars = cars
        self.orientation = orientation
        self.passed_cars = 0
        self.light = None

    def step(self):
        #print(
         #   f"{self.unique_id}. cars: {self.cars}, light: {self.light}, orientation: {self.orientation}")
        self.__enqueue_car()
        if (self.__isgreen() and self.cars > 0):
            self.cars -= 1
            self.passed_cars += 1

    def __isgreen(self):
        return self.light == Light.GREEN

    def __enqueue_car(self):
        self.cars += random.randint(0, 1)


class IntersectionModel(Model):

    def __init__(self, N, width=2, height=2):
        super().__init__(self, N)
        self.num_agents = N
        self.schedule = RandomActivation(self)
        self.grid = SingleGrid(height, width, torus=True)
        self.running = True
        self.current_orientation = None
        self.datacollector = DataCollector(
            model_reporters= {"Current orientation":"current_orientation"},
            agent_reporters= {"Passed cars":"passed_cars", "Light":"light"}
        )
        agents = []
        orientation = None
        for i in range(self.num_agents):
            cars = random.randint(0, 4)
            if (i % 2 == 0):
                orientation = Orientation.HORIZONTAL
            else:
                orientation = Orientation.VERTICAL
            t = TrafficLightAgent(i, self, cars, orientation)
            agents.append(t)
        self.set_traffic_lights(agents, self.__priority(agents))
        for agent in agents:
            self.schedule.add(agent)

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()

    def __priority(self, agents):
        total_vertical = 0
        total_horizontal = 0
        for agent in agents:
            if (agent.orientation == Orientation.VERTICAL):
                total_vertical += agent.cars
            elif (agent.orientation == Orientation.HORIZONTAL):
                total_horizontal += agent.cars
        if (total_vertical > total_horizontal):
            # print(f"{total_vertical} > {total_horizontal}, VERTICAL")
            return Orientation.VERTICAL
        else:
            # print(f"{total_horizontal} > {total_vertical} HORIZONTAL")
            return Orientation.HORIZONTAL

    def set_traffic_lights(self, agents, orientation):
        for agent in agents:
            if (agent.orientation == orientation):
                agent.light = Light.GREEN
                self.current_orientation = agent.orientation
            else:
                agent.light = Light.RED


model = IntersectionModel(4)
orientation = None
total_time = 50
for i in range(total_time):
    traffic_time = Time.NORMAL
    priority = model.current_orientation
    if (i == 0):
        orientation = priority
    else:
        if (i > 0 and orientation == Orientation.HORIZONTAL):
            if (priority != Orientation.VERTICAL):
                traffic_time = Time.SHORT
            orientation = Orientation.VERTICAL
        else:
            if (priority != Orientation.HORIZONTAL):
                traffic_time = Time.SHORT
            orientation = Orientation.HORIZONTAL
        model.set_traffic_lights(model.schedule.agents, orientation)
    time = traffic_time.value
    if ((time - 1 + i) > total_time):
        time = total_time - (i - 1)
    for j in range(time):
        model.step()
    i += time - 1

print(model.datacollector.get_agent_vars_dataframe())
print(model.datacollector.get_model_vars_dataframe())
        


        

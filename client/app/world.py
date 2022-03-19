import carla
import random


class Environment(object):
    def __init__(self, args) -> None:
        self.args = args
        self.client = None
        self.world = None
        self.traffic_manager = None
        self.fixed_delta_seconds = 0.04
        self.simulation_time = 0
        self.hero = None

    def start(self) -> None:

        self.client = carla.Client(self.args.host, self.args.port)
        self.client.set_timeout(self.args.timeout)
        self.world = self.client.get_world()

        new_settings = self.world.get_settings()
        new_settings.synchronous_mode = True
        new_settings.fixed_delta_seconds = self.fixed_delta_seconds
        self.world.apply_settings(new_settings)

        self.traffic_manager = self.client.get_trafficmanager(port=self.args.tm_port)

    def tick(self):
        self.simulation_time += self.fixed_delta_seconds
        self.world.tick()

    def spawn_hero(self, blueprint_filter="vehicle.*"):
        """Spawns the hero actor when the script runs"""
        # Get a random blueprint.
        blueprint = random.choice(
            self.world.get_blueprint_library().filter(blueprint_filter)
        )
        blueprint.set_attribute("role_name", "hero")
        if blueprint.has_attribute("color"):
            color = random.choice(blueprint.get_attribute("color").recommended_values)
            blueprint.set_attribute("color", color)

        # Spawn the player.
        actor = None
        while actor is None:
            spawn_points = self.world.get_map().get_spawn_points()
            spawn_point = (
                random.choice(spawn_points) if spawn_points else carla.Transform()
            )
            actor = self.world.try_spawn_actor(blueprint, spawn_point)

        self.hero = actor

        return actor

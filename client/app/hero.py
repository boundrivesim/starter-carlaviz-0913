import carla


class Hero(object):
    def __init__(self):
        self.environment = None
        self.actor = None
        self.control = None

    def start(self, environment):
        self.environment = environment
        self.actor = self.environment.spawn_hero(
            blueprint_filter=environment.args.filter
        )
        self.actor.set_autopilot(True, environment.args.tm_port)

    def tick(self):
        pass

        # Uncomment and modify to control manually, disable autopilot too
        #
        # ctrl = carla.VehicleControl()
        # ctrl.throttle = 0.5
        # ctrl.steer = 0.1
        # self.actor.apply_control(ctrl)

    def destroy(self):
        """Destroy the hero actor when class instance is destroyed"""
        if self.actor is not None:
            self.actor.destroy()

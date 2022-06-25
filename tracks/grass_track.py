from ursina import *

class GrassTrack(Entity):
    def __init__(self, car):
        super().__init__(
            model = "grass_track.obj", 
            texture = "grass_track.png", 
            position = (0, -50, 0), 
            rotation = (0, 270, 0), 
            scale = (25, 25, 25), 
            collider = "mesh"
        )

        self.car = car

        self.finish_line = Entity(model = "cube", position = (-62, -40.2, 15.8), collider = "box", rotation = (0, 90, 0), scale = (30, 8, 3), visible = False)
        self.boundaries = Entity(model = "grass_track_bounds.obj", collider = "mesh", position = (0, -50, 0), rotation = (0, 270, 0), scale = (25, 25, 25), visible = False)

        self.wall1 = Entity(model = "cube", position = (-5, -40, 35), rotation = (0, 90, 0), collider = "box", scale = (5, 30, 50), visible = False)
        self.wall2 = Entity(model = "cube", position = (20, -40, 1), rotation = (0, 90, 0), collider = "box", scale = (5, 30, 150), visible = False)
        self.wall3 = Entity(model = "cube", position = (-21, -40, 15), rotation = (0, 0, 0), collider = "box", scale = (5, 30, 50), visible = False)
        self.wall4 = Entity(model = "cube", position = (9, -40, 14), rotation = (0, 0, 0), collider = "box", scale = (5, 30, 50), visible = False)

        self.wall_trigger = Entity(model = "cube", position = (25, -40.2, 65), collider = "box", rotation = (0, 90, 0), scale = (40, 20, 3), visible = False)
        self.wall_trigger_ramp = Entity(model = "cube", position = (-82, -34, -64), collider = "box", rotation = (0, 90, 0), scale = (40, 20, 3), visible = False)
        
        self.track = [
            self.finish_line, self.boundaries, self.wall1, self.wall2, self.wall3, 
            self.wall4, self.wall_trigger, self.wall_trigger_ramp
        ]
        
        for i in self.track:
            i.disable()

        self.played = False

    def update(self):
        ray = self.car.intersects()

        if ray.entity == self.finish_line:
            if self.car.anti_cheat == 1:
                self.car.timer_running = True
                self.car.last_count = self.car.count
                self.car.anti_cheat = 0
                invoke(self.car.reset_timer, delay = 3)

                self.car.check_highscore()

            self.wall1.enable()
            self.wall2.enable()
            self.wall3.disable()
            self.wall4.disable()

        if ray.entity == self.wall_trigger:
            self.wall1.disable()
            self.wall2.disable()
            self.wall3.enable()
            self.wall4.enable()
            self.car.anti_cheat = 0.5

        if ray.entity == self.wall_trigger_ramp:
            if self.car.anti_cheat == 0.5:
                self.car.anti_cheat = 1
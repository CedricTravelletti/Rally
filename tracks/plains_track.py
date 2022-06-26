from ursina import *

class PlainsTrack(Entity):
    def __init__(self, car):
        super().__init__(
            model = "plains_track.obj", 
            texture = "plains_track.png", 
            position = (0, -50, 0), 
            rotation = (0, 270, 0), 
            scale = (12, 12, 12), 
            collider = "mesh"
        )

        self.car = car

        self.finish_line = Entity(model = "cube", position = (31, -48, 72), collider = "box", rotation = (0, 0, 0), scale = (3, 8, 30), visible = False)
        self.boundaries = Entity(model = "plains_track_bounds.obj", collider = "mesh", position = (0, -50, 0), rotation = (0, 270, 0), scale = (12, 12, 12), visible = False)

        self.wall1 = Entity(model = "cube", position = (-16, -48, 50), rotation = (0, 90, 0), collider = "box", scale = (5, 30, 50), visible = False)
        self.wall2 = Entity(model = "cube", position = (-16, -48, 23), rotation = (0, 90, 0), collider = "box", scale = (5, 30, 50), visible = False)
        self.wall3 = Entity(model = "cube", position = (5, -48, 33), rotation = (0, 0, 0), collider = "box", scale = (5, 30, 40), visible = False)
        self.wall4 = Entity(model = "cube", position = (-34, -48, 33), rotation = (0, 0, 0), collider = "box", scale = (5, 30, 40), visible = False)
        self.wall5 = Entity(model = "cube", position = (-18, -48, 0), rotation = (0, 90, 0), collider = "box", scale = (5, 30, 50), visible = False)
        self.wall6 = Entity(model = "cube", position = (-18, -48, -30), rotation = (0, 90, 0), collider = "box", scale = (5, 30, 50), visible = False)
        self.wall7 = Entity(model = "cube", position = (-4, -48, -15), rotation = (0, 0, 0), collider = "box", scale = (5, 30, 50), visible = False)
        self.wall8 = Entity(model = "cube", position = (-30, -48, -15), rotation = (0, 0, 0), collider = "box", scale = (5, 30, 50), visible = False)

        self.wall_trigger = Entity(model = "cube", position = (11, -45, -70), collider = "box", rotation = (0, 0, 0), scale = (3, 20, 40), visible = False)

        self.track = [
            self.finish_line, self.boundaries, self.wall1, self.wall2, self.wall3, 
            self.wall4, self.wall5, self.wall6, self.wall7, self.wall8, self.wall_trigger
        ]
        
        self.disable()

        for i in self.track:
            i.disable()

        self.played = False

    def update(self):
        if self.car.simple_intersects(self.finish_line):
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
                self.wall5.enable()
                self.wall6.enable()
                self.wall7.disable()
                self.wall8.disable()

        if self.car.simple_intersects(self.wall_trigger):
            if self.car.anti_cheat == 0:
                self.wall1.disable()
                self.wall2.disable()
                self.wall3.enable()
                self.wall4.enable()
                self.wall5.disable()
                self.wall6.disable()
                self.wall7.enable()
                self.wall8.enable()
                
                self.car.anti_cheat = 1
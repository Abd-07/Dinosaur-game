import arcade


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Dinasour Game"

class Dino(arcade.AnimatedTimeSprite):
    def update(self):
        self.center_y += self.change_y
        self.change_y -= 0.5
        if self.center_y <= 200:
            self.center_y=200
            self.jump=False

class Cactus(arcade.Sprite):
    def update(self):
        self.center_x -= self.change_x

# class with the game
class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.background=arcade.load_texture("/Users/abdulazizsuleymanov/Desktop/Python/Arcade/dinasour game/desert.png")
        self.dino=Dino(0.5)
        self.dino.textures=[]
        self.dino.textures.append(arcade.load_texture("/Users/abdulazizsuleymanov/Desktop/Python/Arcade/dinasour game/dino1.png"))
        self.dino.textures.append(arcade.load_texture("/Users/abdulazizsuleymanov/Desktop/Python/Arcade/dinasour game/dino2.png"))
        self.dino.textures.append(arcade.load_texture("/Users/abdulazizsuleymanov/Desktop/Python/Arcade/dinasour game/dino3.png"))
        self.cactus=Cactus("/Users/abdulazizsuleymanov/Desktop/Python/Arcade/dinasour game/cactus3.png",0.5)
        self.game_over=arcade.load_texture("/Users/abdulazizsuleymanov/Desktop/Python/Arcade/dinasour game/desertGO.png")

    # initial values
    def setup(self):
        self.dino.center_x=100
        self.dino.center_y=200

        self.cactus.center_x=SCREEN_WIDTH
        self.cactus.center_y=200
        self.cactus.change_x=4

        self.move=True
        self.score=0

    # rendering
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.AMAZON)
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,SCREEN_WIDTH,SCREEN_HEIGHT,self.background)
        self.dino.draw()
        self.cactus.draw()
        arcade.draw_text(f"Score: {self.score}",330,550,arcade.color.BLACK,30)
        if self.move == False:
            arcade.draw_texture_rectangle(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,SCREEN_WIDTH,SCREEN_HEIGHT,self.game_over)

    # logic of the game
    def update(self, delta_time):
        if self.move == False:
            self.dino.stop()
            self.cactus.stop()

        
        if arcade.check_for_collision(self.dino,self.cactus):
            self.move=False

        if self.move == True:
            self.dino.update_animation()
            self.dino.update()
            self.cactus.update()

        if self.cactus.center_x <= 0:
            self.cactus.center_x=SCREEN_WIDTH
            self.score+=1
        

    # key = pressed
    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE and self.dino.jump == False:
            self.dino.change_y=12
            self.dino.jump=True

    # key = not pressed
    def on_key_release(self, key, modifiers):
        pass



window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()

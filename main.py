# this allows us to code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    # Start the pygame library.
    pygame.init()

    # Creating a screen object.
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Creating a clock object to set FPS of the game.
    clock = pygame.time.Clock()

    # Creating groups to put all player objects in.
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    # Creating a new player object.
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Create a new pygame.sprite.Group which will contain all of the asteroids.
    # This ensures that every instance of the Asteroid class is automatically added
    # to these groups upon creation.
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    # Adding AsteroidField to the updatable container group.
    AsteroidField.containers = (updatable)

    # Creating a new group for the Shot class to indicate bullets shot by the player.
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    # Creating a new AsteroidField object
    asteroid_field = AsteroidField()

    while True:
        # Quit the game if the user closes the game window.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Set the FPS of the game to 60,
        # and creating a constant (dt) to manage the movement of objects on the screen.
        dt = clock.tick(60)
        dt = dt / 1000

        # Fill the screen with a solid black background
        screen.fill(BLACK_COLOR)

        # Updating player objects
        for updatables in updatable:
            updatables.update(dt)

        # Check for collision between asteroids and player.
        for asteroid in asteroids:
            if asteroid.check_collision(asteroid, player):
                print("Game over!")
                exit(0)

        # Check for collision between bullets and asteroids
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.check_collision(asteroid, shot):
                    shot.kill()
                    asteroid.kill()

        # Drawing player objects
        for drawables in drawable:
            drawables.draw(screen)

        # Refresh screen
        pygame.display.flip()



if __name__ == "__main__":
    main()

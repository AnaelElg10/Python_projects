import os
import math
import pygame
from typing import Optional, Tuple, List, Dict

# Constants
PLANET_IMAGES_DIR = "PlanetImages"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
FPS = 30

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Solar System Visualization")

def load_image(filename: str, scale: Optional[Tuple[int, int]] = None) -> Optional[pygame.Surface]:
    """Load an image and optionally scale it."""
    try:
        image = pygame.image.load(os.path.join(PLANET_IMAGES_DIR, filename))
        if scale:
            image = pygame.transform.scale(image, scale)
        return image
    except pygame.error as e:
        print(f"Unable to load image {filename}: {e}")
        return None

class Planet:
    def __init__(self, name: str, image: pygame.Surface, distance: float, period: float, radius: int):
        self.name = name
        self.image = image
        self.distance = distance
        self.period = period
        self.radius = radius
        self.angle = 0
        self.x = 0
        self.y = 0
        self.past_positions = []

    def update_position(self, center_x: float, center_y: float):
        self.angle += 2 * math.pi / (FPS * self.period)
        self.x = center_x + math.cos(self.angle) * self.distance
        self.y = center_y + math.sin(self.angle) * self.distance
        self.past_positions.append((self.x, self.y))

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.x - self.image.get_width() // 2, self.y - self.image.get_height() // 2))
        for i, (x, y) in enumerate(self.past_positions):
            pygame.draw.circle(screen, BLUE, (int(x), int(y)), max(self.radius - i, 1), 1)

class SolarSystem:
    def __init__(self):
        self.planets = self.initialize_planets()
        self.sun = self.planets[0]

    def initialize_planets(self) -> List[Planet]:
        center_x = SCREEN_WIDTH // 2
        center_y = SCREEN_HEIGHT // 2

        sun = Planet("Sun", load_image("sun.png", (100, 100)), 0, 0, 50)
        sun.x = center_x
        sun.y = center_y

        mercury = Planet("Mercury", load_image("mercury.png", (20, 20)), 65, 0.24, 10)
        venus = Planet("Venus", load_image("venus.png", (30, 30)), 90, 0.62, 20)
        earth = Planet("Earth", load_image("earth.png", (40, 40)), 125, 1, 25)
        mars = Planet("Mars", load_image("mars.png", (35, 35)), 155, 1.88, 15)
        jupiter = Planet("Jupiter", load_image("jupiter.png", (80, 80)), 210, 11.86, 40)
        saturn = Planet("Saturn", load_image("saturn.png", (70, 70)), 260, 29.46, 35)
        uranus = Planet("Uranus", load_image("uranus.png", (60, 60)), 320, 84, 30)
        neptune = Planet("Neptune", load_image("neptune.png", (50, 50)), 370, 164.8, 35)

        planets = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]
        for planet in planets[1:]:
            planet.update_position(sun.x, sun.y)
        return planets

    def update(self):
        for planet in self.planets[1:]:
            planet.update_position(self.sun.x, self.sun.y)

    def draw(self, screen: pygame.Surface):
        screen.blit(self.sun.image, (self.sun.x - self.sun.image.get_width() // 2, self.sun.y - self.sun.image.get_height() // 2))
        for planet in self.planets[1:]:
            planet.draw(screen)

def main() -> None:
    """Main function to run the solar system visualization."""
    solar_system = SolarSystem()
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        solar_system.update()
        solar_system.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
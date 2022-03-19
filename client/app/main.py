import argparse
import pygame

from .world import Environment
from .hero import Hero


def game_loop(args):

    env = Environment(args)
    env.start()

    hero = Hero()
    hero.start(env)

    try:

        clock = pygame.time.Clock()
        while True:
            clock.tick_busy_loop(500)
            hero.tick()
            env.tick()

    except KeyboardInterrupt:
        print("\nCancelled by user. Bye!")

    finally:
        if hero is not None:
            hero.destroy()


def main():
    """Parses the arguments received from commandline and runs the game loop"""
    argparser = argparse.ArgumentParser()

    argparser.add_argument(
        "--host",
        metavar="H",
        default="127.0.0.1",
        help="IP of the host server (default: 127.0.0.1)",
    )
    argparser.add_argument(
        "-p",
        "--port",
        metavar="P",
        default=2000,
        type=int,
        help="TCP port to listen to (default: 2000)",
    )
    argparser.add_argument(
        "--tm-port",
        metavar="P",
        default=8000,
        type=int,
        help="Port to communicate with TM (default: 8000)",
    )
    argparser.add_argument(
        "--timeout",
        metavar="X",
        default=2.0,
        type=float,
        help="Timeout duration (default: 2.0s)",
    )
    argparser.add_argument(
        "--filter",
        metavar="PATTERN",
        default="vehicle.audi.*",
        help='actor filter (default: "vehicle.audi.*")',
    )
    argparser.add_argument(
        "--show-triggers",
        action="store_true",
        help="show trigger boxes of traffic signs",
    )
    argparser.add_argument(
        "--show-connections", action="store_true", help="show waypoint connections"
    )
    argparser.add_argument(
        "--show-spawn-points", action="store_true", help="show recommended spawn points"
    )

    # Parse arguments
    args = argparser.parse_args()

    # Run game loop
    game_loop(args)

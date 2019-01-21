# Boss randomization logic for open mode.

import random

from randomizer.data import bosses


def _boss_location_filter(world, location):
    """Filter function for boss locations based on whether Culex and/or Bowser's Keep is included.

    Args:
        world (randomizer.logic.main.GameWorld):
        location (BossLocation):

    Returns:
        bool:
    """
    if isinstance(location, bosses.Culex) and world.settings.randomize_stars < 2:
        return False
    if isinstance(location, bosses.BowsersKeepLocation) and not world.settings.randomize_stars_bk:
        return False
    return True


def randomize_all(world):
    """Randomize all the boss settings for the world.

    Args:
        world (randomizer.logic.main.GameWorld): Game world to randomize.

    """
    # Open mode-specific shuffles.
    if world.open_mode:
        # Shuffle boss star locations.
        if world.settings.randomize_stars:
            for boss in world.boss_locations:
                boss.has_star = False

            possible_stars = [b for b in world.boss_locations if _boss_location_filter(world, b)]

            # Check if we're doing 6 or 7 stars.
            num_stars = 7 if world.settings.randomize_stars_seven else 6
            star_bosses = random.sample(possible_stars, num_stars)
            for boss in star_bosses:
                boss.has_star = True
import random
def random_story():
        characters = [
            "a brave knight", "a cunning thief", "a curious scientist", "a fearless explorer",
            "a mischievous fairy", "a wise old wizard", "a courageous child", "a loyal pet dog",
            "a lost robot", "a mysterious stranger", "a talented artist", "a daring pirate",
            "a restless ghost", "an ambitious inventor", "a humble farmer", "a time-traveling historian"
        ]
        settings = [
            "in a haunted castle", "on a distant planet", "in a bustling city", "in an enchanted forest",
            "at the bottom of the ocean", "inside a futuristic spaceship", "on a snowy mountaintop",
            "in a magical kingdom", "deep in a hidden cave", "at an abandoned amusement park",
            "in the middle of a desert", "inside a time-warped library", "in a secret underground bunker",
            "on a floating island", "inside a labyrinthine maze"
        ]
        objects = [
            "a magical sword", "a mysterious map", "an ancient artifact", "a talking animal",
            "a glowing crystal", "a cursed necklace", "a pocket watch that stops time",
            "a book that predicts the future", "a pair of enchanted shoes", "a potion that grants invisibility",
            "a compass that points to hidden desires", "a golden key to an unknown door", "a flying carpet",
            "a mirror that shows alternate realities", "a box that can never be opened"
        ]
        challenges = [
            "defeat a dragon", "solve a centuries-old mystery", "find a lost treasure", "save a kingdom",
            "escape a deadly trap", "discover the truth behind a legend", "break an ancient curse",
            "rescue a kidnapped friend", "survive a powerful storm", "outwit an evil sorcerer",
            "reunite a family torn apart by war", "win a dangerous competition",
            "protect a village from marauding bandits",
            "escape a parallel universe", "restore magic to a dying world"
        ]
        character=random.choice(characters)
        setting=random.choice(settings)
        object=random.choice(objects)
        challenge=random.choice(challenges)
        story=f"One day, {character} found themeselves {setting}. They stumbled upon {object}, which led them to {challenge}."
        return story

print("============ YOUR STORY==============")
print(random_story())
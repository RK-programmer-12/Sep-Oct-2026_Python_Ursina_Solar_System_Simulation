'''
attempt at a more realistic simulation of our solar system 

By Rayaansh Kaushik - a fellow space nerd 

'''
# CODE_INITIALIZATION --------------------
# set up necessary packages 
from ursina import *
import math 
import sys, os
from pathlib import Path
import pygame 

pygame.mixer.init()

# BACKEND CODE
if getattr(sys, 'frozen', False):
    base = Path(getattr(sys, '_MEIPASS', os.path.dirname(sys.executable)))
else:
    base = Path(__file__).parent

os.chdir(base)
application.asset_folder = base

# set up the window 


app = Ursina()

window.size = (1000, 500)
window.color = color.black


Astronomical_U = 7 # this variable controls the size of an AU (Astronomical Unit), controlling the size of the simulation 
speed = 0.637 # speed at which Earth orbits the Sun every minute

# planets' orbits' radii size variables 
mercury_orbit = Astronomical_U * 0.39
venus_orbit = Astronomical_U * 0.72
earth_orbit = Astronomical_U # the distance from Earth to the Sun is 1 AU 
mars_orbit = Astronomical_U * 1.52 
jupiter_orbit = Astronomical_U * 5.2 
saturn_orbit = Astronomical_U * 9.54
uranus_orbit = Astronomical_U * 19.2 
neptune_orbit = Astronomical_U * 30.06 

# planets' orbits' speed variables. calculated as speed / (Earth days to orbit the Sun)
mercury_speed = speed / 88 # for example, mercury takes 88 Earth days to orbit the Sun 
venus_speed = speed / 225
earth_speed = speed / 365
mars_speed = speed / 687
jupiter_speed = speed / 4333
saturn_speed = speed / 10756 
uranus_speed = speed / 30687 
neptune_speed = speed / 60190

# angles - these will be used to make the planets move around the Sun at a constant angle 
mercury_angle = 0
venus_angle   = 0
earth_angle   = 0
mars_angle    = 0
jupiter_angle = 0
saturn_angle  = 0
uranus_angle  = 0
neptune_angle = 0

terrestrial_marker_length = 0.6
gas_giant_marker_length = 6

# planet axis tilt
mercury_tilt = 0.03
venus_tilt   = 177.4
earth_tilt   = 23.44
mars_tilt    = 25.19
jupiter_tilt = 3.13
saturn_tilt  = 26.73
uranus_tilt  = 97.77
neptune_tilt = 28.32

# CREATING_SHAPES -------------------- 
instructions_text = ('''INSTRUCTIONS:
right click and move to navigate simulation 
use two fingers up / down to zoom 
up / down arrows to navigate labels
space to open or close info on label
left / right arrows to change speed
click the red button at the top right to exit''')
Instructions = Text(
    text = instructions_text, 
    color = color.rgb32(205,205,205), 
    scale = 1, 
    position = (-0.8,-0.3)
)

sun_size_constant = 0.00465247

Sun = Entity(
    model = "sphere",
    color = color.rgb32(255,154,0),
    scale = sun_size_constant * Astronomical_U,
)

Sunlight1 = Entity(
    model = "sphere",
    color = color.rgb32(255,154,0),
    scale = (sun_size_constant * 1.2) * Astronomical_U,
    alpha = 0.4
)

Sunlight2 = Entity(
    model = "sphere",
    color = color.rgb32(255,154,0),
    scale = (sun_size_constant * 1.4) * Astronomical_U,
    alpha = 0.35
)

Sunlight2 = Entity(
    model = "sphere",
    color = color.rgb32(255,154,0),
    scale = (sun_size_constant * 1.6) * Astronomical_U,
    alpha = 0.3
)

Sunlight3 = Entity(
    model = "sphere",
    color = color.rgb32(255,154,0),
    scale = (sun_size_constant * 1.8) * Astronomical_U,
    alpha = 0.25
)

Sunlight4 = Entity(
    model = "sphere",
    color = color.rgb32(255,154,0),
    scale = (sun_size_constant * 2) * Astronomical_U,
    alpha = 0.2
)

Sunlight5 = Entity(
    model = "sphere",
    color = color.rgb32(255,154,0),
    scale = (sun_size_constant * 2.2) * Astronomical_U,
    alpha = 0.15
)

Sunlight6 = Entity(
    model = "sphere",
    color = color.rgb32(255,154,0),
    scale = (sun_size_constant * 2.4) * Astronomical_U,
    alpha = 0.1
)

Sunlight7 = Entity(
    model = "sphere",
    color = color.rgb32(255,154,0),
    scale = (sun_size_constant * 2.6) * Astronomical_U,
    alpha = 0.1
)

Sun_label = Text(
    text = "Sun",
    color = color.rgb32(255,154,0),
    scale = 1.5,
    position = (-0.8, 0.45)
)

Mercury_ring = Entity(
    model = Circle(resolution=64, mode='line', thickness=2),
    color = color.rgb32(183, 184, 185),
    scale = mercury_orbit * 2 # scale determines DIAMETER, not radius
)

Mercury_marker = Entity(
    model = Mesh(vertices=[(0, 0, -terrestrial_marker_length), (0, 0, terrestrial_marker_length)], mode='line', thickness=4),
    color = color.rgb32(183, 184, 185),
    rotation_x = mercury_tilt # sets the angle for the planet's axis tilt
)

Mercury_label = Text(
    text = "Mercury",
    color = color.rgb32(183, 184, 185),
    scale = 1.5,
    position = (-0.8, 0.4)
)

Venus_ring = Entity(
    model = Circle(resolution=64, mode='line', thickness=2),
    color = color.rgb32(238, 203, 139),
    scale = venus_orbit * 2 
)

Venus_marker = Entity(
    model = Mesh(vertices=[(0, 0, -terrestrial_marker_length), (0, 0, terrestrial_marker_length)], mode='line', thickness=4),
    color = color.rgb32(238, 203, 139),
    rotation_x = venus_tilt
)

Venus_label = Text(
    text = "Venus",
    color = color.rgb32(238, 203, 139),
    scale = 1.5,
    position = (-0.8, 0.35)
)

Earth_ring = Entity(
    model = Circle(resolution=64, mode='line', thickness=2),
    color = color.rgb32(140, 177, 222),
    scale = earth_orbit * 2
)

Earth_marker = Entity(
    model = Mesh(vertices=[(0, 0, -terrestrial_marker_length), (0, 0, terrestrial_marker_length)], mode='line', thickness=4),
    color = color.rgb32(140, 177, 222),
    rotation_x = earth_tilt
)

Earth_label = Text(
    text = "Earth",
    color = color.rgb32(140, 177, 222),
    scale = 1.5,
    position = (-0.8, 0.3)
)

Mars_ring = Entity(
    model = Circle(resolution=64, mode='line', thickness=2),
    color = color.rgb32(226, 123, 88),
    scale = mars_orbit * 2
)

Mars_marker = Entity(
    model = Mesh(vertices=[(0, 0, -terrestrial_marker_length), (0, 0, terrestrial_marker_length)], mode='line', thickness=4),
    color = color.rgb32(226, 123, 88),
    rotation_x = mars_tilt
)

Mars_label = Text(
    text = "Mars",
    color = color.rgb32(226, 123, 88),
    scale = 1.5,
    position = (-0.8, 0.25)
)

Asteroid_belt = Entity(
    model = "belt.bam", 
    color = color.rgb32(165,155,155),
    scale = (2.7 * (Astronomical_U/21.5),2.7 * (Astronomical_U/21.5),1.35 * (Astronomical_U/21.5)), # adjusts scale such that the center of the asteroid belt is 2.7 AU from the sun (accurate)
    position = (0,0,0)
)
Asteroid_belt.alpha = 0.2

Asteroid_belt_label = Text(
    text = "Asteroid Belt",
    color = color.rgb32(165,155,155),
    scale = 1.5,
    position = (-0.8, 0.2)
)

Jupiter_ring = Entity(
    model = Circle(resolution=64, mode='line', thickness=2),
    color = color.rgb32(167, 156, 134),
    scale = jupiter_orbit * 2
)

Jupiter_marker = Entity(
    model = Mesh(vertices=[(0, 0, -gas_giant_marker_length), (0, 0, gas_giant_marker_length)], mode='line', thickness=4),
    color = color.rgb32(167, 156, 134),
    rotation_x = jupiter_tilt
)

Jupiter_label = Text(
    text = "Jupiter",
    color = color.rgb32(167, 156, 134),
    scale = 1.5,
    position = (-0.8, 0.15)
)

Saturn_ring = Entity(
    model = Circle(resolution=64, mode='line', thickness=2),
    color = color.rgb32(234, 214, 184),
    scale = saturn_orbit * 2
)

Saturn_marker = Entity(
    model = Mesh(vertices=[(0, 0, -gas_giant_marker_length), (0, 0, gas_giant_marker_length)], mode='line', thickness=4),
    color = color.rgb32(234, 214, 184),
    rotation_x = saturn_tilt
)

Saturn_label = Text(
    text = "Saturn",
    color = color.rgb32(234, 214, 184),
    scale = 1.5,
    position = (-0.8, 0.1)
)

Uranus_ring = Entity(
    model = Circle(resolution=64, mode='line', thickness=2),
    color = color.rgb32(172, 229, 238),
    scale = uranus_orbit * 2
)

Uranus_marker = Entity(
    model = Mesh(vertices=[(0, 0, -gas_giant_marker_length), (0, 0, gas_giant_marker_length)], mode='line', thickness=4),
    color = color.rgb32(172, 229, 238),
    rotation_x = uranus_tilt
)

Uranus_label = Text(
    text = "Uranus",
    color = color.rgb32(172, 229, 238),
    scale = 1.5,
    position = (-0.8, 0.05)
)

Neptune_ring = Entity(
    model = Circle(resolution=64, mode='line', thickness=2),
    color = color.rgb32(133, 173, 219),
    scale = neptune_orbit * 2
)

Neptune_marker = Entity(
    model = Mesh(vertices=[(0, 0, -gas_giant_marker_length), (0, 0, gas_giant_marker_length)], mode='line', thickness=4),
    color = color.rgb32(133, 173, 219),
    rotation_x = neptune_tilt
)

Neptune_label = Text(
    text = "Neptune",
    color = color.rgb32(133, 173, 219),
    scale = 1.5,
    position = (-0.8, 0.0)
)

Kuiper_belt = Entity(
    model = "belt.bam", 
    color = color.rgb32(155,155,185),
    scale = (40 * (Astronomical_U/21.5),40 * (Astronomical_U/21.5),20 * (Astronomical_U/21.5)), 
    position = (0,0,0)
)
Kuiper_belt.alpha = 0.2

Kuiper_belt_label = Text(
    text = "Kuiper Belt",
    color = color.rgb32(155,155,185),
    scale = 1.5,
    position = (-0.8, -0.05)
)

labels = [Sun_label, Mercury_label, Venus_label, Earth_label, Mars_label, Asteroid_belt_label, Jupiter_label, Saturn_label, Uranus_label, Neptune_label, Kuiper_belt_label]
selected_label = 0
open_panel = None

box_outline = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 0, 0)]

info = [
    '''The Sun:

The Sun is a G-Type main sequence star 
at the center of our solar system. The 
core of the sun has temperatures 
reaching 15 MILLION degrees Celsius! 
Our sun is about 4.6 BILLION years old. 

Fun Fact: The Latin word for Sun is "Sol".

For more info, check out: 
https://science.nasa.gov/sun/facts/ ''',
    '''Terrestrial Planet - Mercury:

Mercury is the closest planet to the Sun. 
It is the smallest planet in our solar 
system. It is named after the 
quick-moving Roman god: Mercury. 

Fun fact: Mercury orbits the sun once in 
88 days, making it also the fastest moving 
planet in the solar system. 

For more info, check out: 
https://science.nasa.gov/mercury/facts/ 
    ''',
    '''Terrestrial Planet - Venus: 

Venus is the second planet from the Sun. 
Venus's thick atmosphere traps heat, 
making it the hottest planet in the solar 
system. Thick clouds hide volcanoes and 
mountains on its surface. 

Fun fact: Venus is similar in structure 
and size to Earth, and is called Earth's 
twin, or sister planet.

For more info, check out: 
https://science.nasa.gov/venus/facts/ 
'''
,
    '''Terrestrial Planet - Earth:

Earth is the third planet from the Sun. 
It is the only known planet that has 
life. It has one moon. Earth is also the 
only known planet with space nerds. 

Fun fact: Life first appeared 3.8 
billion years ago on Earth. 

For more info, check out: 
https://science.nasa.gov/earth/facts/
''',
    '''Terrestrial Planet - Mars:

Mars is the fourth planet from the Sun. 
It has two small moons, named Phobos 
and Deimos. Mars is known as the Red 
Planet, because of the rusted iron 
oxide on its surface.

Fun fact: Mars is home to Olympus Mons, 
the TALLEST mountain in our ENTIRE solar 
system. 

For more info, check out: 
https://science.nasa.gov/mars/facts/
    ''',
    '''The Asteroid Belt: 

The Asteroid Belt is between the orbits 
of Mars and Jupiter. It contains the 
majority of asteroids, and is a result 
of the leftovers from the formation of 
the solar system. 

Fun fact: Ceres is one of the four major 
asteroids in the asteroid belt. Ceres is 
also classified as a dwarf planet. 

For more info, check out: 
https://theplanets.org/asteroid-belt/
    ''',
    '''Gas Giant - Jupiter: 

Jupiter is the largest, and oldest 
planet in the solar system. It is the 
fastest spinning planet in the solar 
system. 

Fun fact: The Great Red Spot is a storm 
system on Jupiter that has been observed 
since the early 1800s. It is the largest 
anticyclonic storm in the solar system. 

For more info, check out: 
https://science.nasa.gov/jupiter
    '''
    ,
    '''Gas Giant - Saturn: 

Saturn has the largest rings in the solar 
system, and has the most moons of any 
planet in the solar system - with 274 
confirmed moons. 

Fun fact: Saturn is the only planet with 
less density than water. This means, if 
you could place Saturn in a bathtub 
(magically), Saturn would FLOAT!

For more info, check out: 
https://science.nasa.gov/saturn/facts/
'''
,
    '''Ice Giant - Uranus: 

Uranus is the seventh planet from the 
Sun. It has 13 faint rings, and 28 moons. 
It rotates at around a 90 degree angle, 
relative to its orbital plane - so it looks 
like it spins on its side. 

Fun fact: Uranus is named after the 
primordial Greek god of the sky, Ouranos. 

For more info, check out: 
https://science.nasa.gov/uranus/facts/ 
'''
,
    '''Ice Giant - Neptune: 

Neptune is the farthest planet from the 
solar system - 30 times as far from the 
sun as Earth. It has a 165 year orbit. 

Fun fact: Neptune was the first planet 
discovered by math and physics, rather 
than observation. 

For more info, check out: 
https://science.nasa.gov/neptune

    '''
,
    '''The Kuiper Belt:

The Kuiper Belt is an icy region in the 
outer solar system. It is beyond Neptune’s 
orbit. Unlike the asteroid belt which is 
composed of primarily rocky objects, the 
Kuiper belt is composed of icy objects. 
It is named after Gerard Kuiper. 

Fun fact: The Kuiper belt has three dwarf 
planets: Pluto, Haumea, and Makemake. 

For more info, check out: 
https://theplanets.org/kuiper-belt/

'''
]

panels = []
for label_info in info:
    panel = Entity(
        parent = camera.ui,
        position = (0.2, 0.05),
        enabled = False
    )
    Entity(
        parent = panel,
        model = 'quad',
        color = color.rgb32(25, 25, 35, 240),
        scale = (0.5, 0.4)
    )
    Entity(
        parent = panel,
        model = Mesh(vertices=box_outline, mode='line', thickness=2),
        color = color.rgb32(205,205,205),
        scale = (0.5, 0.4),
        position = (-0.25, -0.2, -0.01)
    )
    Text(
        text = label_info,
        parent = panel,
        color = color.rgb32(205,205,205),
        scale = 1,
        position = (-0.24, 0.17, -0.02)
    )
    panels.append(panel)

highlight_box = Entity(
    parent = camera.ui,
    model = Mesh(vertices=box_outline, mode='line', thickness=2),
    color = color.rgb32(205,205,205)
)

def move_highlight():
    label = labels[selected_label]
    padding = 0.01
    text_width = label.width * label.scale_x
    text_height = label.height * label.scale_y
    highlight_box.position = (label.x - padding, label.y - text_height - padding)
    highlight_box.scale = (text_width + 2 * padding, text_height + 2 * padding)

move_highlight()

speed_multiplier = 1
max_speed_multiplier = 512

speed_segments = []
for i in range(10):
    segment = Entity(
        parent = camera.ui,
        model = 'quad',
        color = color.rgb32(205,205,205),
        scale = (0.036, 0.02),
        position = (-0.2 + i * 0.04 + 0.018, -0.43)
    )
    speed_segments.append(segment)

speed_text = Text(
    text = "",
    color = color.rgb32(205,205,205),
    scale = 1.5,
    origin = (0, 0),
    position = (0, -0.39)
)

def update_speed_bar():
    for i, segment in enumerate(speed_segments):
        if i <= math.log2(speed_multiplier):
            segment.color = color.rgb32(205,205,205)
        else:
            segment.color = color.rgb32(60, 60, 70)
    speed_text.text = "Speed: " + str(int(speed_multiplier)) + "x"

update_speed_bar()

# MAIN FUNCTION - RUNS TO CREATE MOVING ELEMENTS -------------------- 
def update():
    # defines updating angles 
    global mercury_angle, venus_angle, earth_angle, mars_angle
    global jupiter_angle, saturn_angle, uranus_angle, neptune_angle

    mercury_angle += mercury_speed * speed_multiplier
    Mercury_marker.x = mercury_orbit * math.cos(mercury_angle)
    Mercury_marker.y = mercury_orbit * math.sin(mercury_angle)

    venus_angle += venus_speed * speed_multiplier
    Venus_marker.x = venus_orbit * math.cos(venus_angle)
    Venus_marker.y = venus_orbit * math.sin(venus_angle)

    earth_angle += earth_speed * speed_multiplier
    Earth_marker.x = earth_orbit * math.cos(earth_angle)
    Earth_marker.y = earth_orbit * math.sin(earth_angle)

    mars_angle += mars_speed * speed_multiplier
    Mars_marker.x = mars_orbit * math.cos(mars_angle)
    Mars_marker.y = mars_orbit * math.sin(mars_angle)

    jupiter_angle += jupiter_speed * speed_multiplier
    Jupiter_marker.x = jupiter_orbit * math.cos(jupiter_angle)
    Jupiter_marker.y = jupiter_orbit * math.sin(jupiter_angle)

    saturn_angle += saturn_speed * speed_multiplier
    Saturn_marker.x = saturn_orbit * math.cos(saturn_angle)
    Saturn_marker.y = saturn_orbit * math.sin(saturn_angle)

    uranus_angle += uranus_speed * speed_multiplier
    Uranus_marker.x = uranus_orbit * math.cos(uranus_angle)
    Uranus_marker.y = uranus_orbit * math.sin(uranus_angle)

    neptune_angle += neptune_speed * speed_multiplier
    Neptune_marker.x = neptune_orbit * math.cos(neptune_angle)
    Neptune_marker.y = neptune_orbit * math.sin(neptune_angle)


def input(key):
    sound1 = pygame.mixer.Sound("sound1.mp3")
    sound2 = pygame.mixer.Sound("sound2.mp3")

    global selected_label, open_panel, speed_multiplier

    if key == 'left mouse down':
        held_keys['right mouse'] = 1

    if key == 'left mouse up':
        held_keys['right mouse'] = 0

    if key == 'right arrow' and speed_multiplier < max_speed_multiplier:
        speed_multiplier *= 2
        update_speed_bar()
        sound1.play()

    if key == 'left arrow' and speed_multiplier > 1:
        speed_multiplier /= 2
        update_speed_bar()
        sound1.play()

    if key == 'down arrow':
        selected_label = (selected_label + 1) % len(labels)
        move_highlight()
        sound1.play()

    if key == 'up arrow':
        selected_label = (selected_label - 1) % len(labels)
        move_highlight()
        sound1.play()

    if key == 'space':
        if open_panel is not None:
            panels[open_panel].enabled = False
        if open_panel == selected_label:
            open_panel = None
        else:
            open_panel = selected_label
            panels[open_panel].enabled = True
        sound2.play()

# RUNNING FINAL CODE -------------------- 
EditorCamera()

pygame.mixer.music.load("soundtrack.mp3")
pygame.mixer.music.play(loops=-1)

app.run()
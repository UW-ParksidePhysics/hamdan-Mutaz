rom vpython import *
from math import pi

initial_velocity = float(input("How much 'oomph' into the throw? (Recommendation:10) "))
θ = float(input("What's the angle of trajectory in degrees? (Recommendation:30°) "))
θ = θ * (pi / 180)
earth_θ = θ
mars_θ = θ
moon_θ = θ

for i in range(0, 2):  # Runs twice
    x_earth_velocity = initial_velocity * cos(earth_θ)
    y_earth_velocity = initial_velocity * sin(earth_θ)

    earth_initial_position = vector(-30, -5, 0)
    earth_initial_velocity = vector(x_earth_velocity, y_earth_velocity, 0)

    earth_ball = sphere(pos=earth_initial_position, radius=0.5, color=color.cyan, make_trail=True)  # Creates the ball
    earth_field = box(pos=vector(0, -5, 0), axis=vector(0, 0, 0), size=vector(65, 1, 10),
                      color=color.green)  # Creates the field
    earth_text = text(pos=vector(-15, -12, 0), text='EARTH', height=3, lenght=3, align='center',
                      color=color.green)

    animation_time_step = 0.01  # seconds
    rate_of_animation = 1/animation_time_step
    time_step = 0.005
    stop_time = 100.0  # This can be changed

    time = 0.
    earth_ball_velocity = earth_initial_velocity
    while time < stop_time:
        rate(rate_of_animation)
        if earth_ball.pos.y < earth_field.pos.y:
            break
        earth_ball.pos.x += earth_ball_velocity.x * time_step
        earth_ball.pos.y += earth_ball_velocity.y * time_step - ((1 / 2) * 9.8 * time_step ** 2)  # Effect of gravity
        earth_ball.pos.z += earth_ball_velocity.z * time_step

        earth_ball_velocity.y = earth_ball_velocity.y - 9.8 * time_step  # Effect on velocity due to gravity of earth
        time += time_step
    earth_θ = (pi / 2) - earth_θ  # Changes angle

"""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$This_is_just_a_divider_to_make_things_look_pretty$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"""

for i in range(0, 2):  # Runs twice
    x_mars_velocity = initial_velocity * cos(mars_θ)
    y_mars_velocity = initial_velocity * sin(mars_θ)

    mars_initial_position = vector(-30, -5, -10)
    mars_initial_velocity = vector(x_mars_velocity, y_mars_velocity, 0)

    mars_ball = sphere(pos=mars_initial_position, radius=0.5, color=color.magenta, make_trail=True)  # Creates the ball
    mars_field = box(pos=vector(0, -5, -10), axis=vector(0, 0, 0), size=vector(65, 1, 10),
                     color=color.red)  # Creates the field
    mars_text = text(pos=vector(0, -12, -10), text='MARS', height=3, lenght=3, align='center',
                     color=color.red)  # Extra credit

    animation_time_step = 0.01  # seconds
    rate_of_animation = 1 / animation_time_step
    time_step = 0.005
    stop_time = 100.0  # This can be changed

    time = 0.
    mars_ball_velocity = mars_initial_velocity
    while time < stop_time:
        rate(rate_of_animation)
        if mars_ball.pos.y < mars_field.pos.y:
            break
        mars_ball.pos.x += mars_ball_velocity.x * time_step
        mars_ball.pos.y += mars_ball_velocity.y * time_step - ((1 / 2) * 3.7 * time_step ** 2)  # Effect due to gravity
        mars_ball.pos.z += mars_ball_velocity.z * time_step

        mars_ball_velocity.y = mars_ball_velocity.y - 3.7 * time_step  # Effect on velocity due to gravity of mars
        time += time_step
    mars_θ = (pi / 2) - mars_θ  # Changes angle

"""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$This_is_just_a_divider_to_make_things_look_pretty$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"""

for i in range(0, 2):  # Runs twice
    x_moon_velocity = initial_velocity * cos(moon_θ)
    y_moon_velocity = initial_velocity * sin(moon_θ)

    moon_initial_position = vector(-30, -5, -20)
    moon_initial_velocity = vector(x_moon_velocity, y_moon_velocity, 0)

    moon_ball = sphere(pos=moon_initial_position, radius=0.5, color=color.white, make_trail=True)  # Creates the ball
    moon_field = box(pos=vector(0, -5, -20), axis=vector(0, 0, 0), size=vector(65, 1, 10),
                     color=color.gray(0.6))  # Creates the field
    moon_text = text(pos=vector(15, -12, -20), text='MOON', height=3, lenght=3, align='center',
                     color=color.gray(0.6))  # Extra credit

    animation_time_step = 0.01  # seconds
    rate_of_animation = 1 / animation_time_step
    time_step = 0.005
    stop_time = 100.0  # This can be changed

    time = 0.
    moon_ball_velocity = moon_initial_velocity
    while time < stop_time:
        rate(rate_of_animation)
        if moon_ball.pos.y < moon_field.pos.y:
            break
        moon_ball.pos.x += moon_ball_velocity.x * time_step
        moon_ball.pos.y += moon_ball_velocity.y * time_step - ((1 / 2) * 1.6 * time_step ** 2)  # Effect due to gravity
        moon_ball.pos.z += moon_ball_velocity.z * time_step

        moon_ball_velocity.y = moon_ball_velocity.y - 1.6 * time_step  # Effect on velocity due to gravity of the moon
        time += time_step
    moon_θ = (pi / 2) - moon_θ  # Changes angle

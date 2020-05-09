"""Generate Hertzsprung-Russell diagram like:
    https://en.wikipedia.org/wiki/Hertzsprung%E2%80%93Russell_diagram#/media/File:HRDiagram.png"""
import numpy as np
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt


astronomical_unit = 1.495978707e11  # meters
meters_to_light_years = 1./9.4607e15


def star_colormap(star_b_minus_vs):
    # Create color map from B-V = -0.33 (#7070ff) to 1.40 (#ff7f7f)
    # yellow = #ffff7f at B-V = 0.81
    number_of_gradient_points = 256
    white_index = int((0.33 / (0.33 + 1.40)) * number_of_gradient_points)
    yellow_index = int(((0.81 + .33) / (0.33 + 1.40)) * number_of_gradient_points)
    print(white_index, yellow_index, number_of_gradient_points)
    color_values = np.ones((number_of_gradient_points, 4))
    # Red values
    color_values[:white_index, 0] = np.linspace(112 / number_of_gradient_points,
                                                255 / number_of_gradient_points,
                                                white_index)
    color_values[white_index:yellow_index, 0] = np.linspace(255 / number_of_gradient_points,
                                                            255 / number_of_gradient_points,
                                                            yellow_index - white_index)
    color_values[yellow_index:, 0] = np.linspace(255 / number_of_gradient_points,
                                                 255 / number_of_gradient_points,
                                                 number_of_gradient_points - yellow_index)
    # Green values
    color_values[:white_index, 1] = np.linspace(112 / number_of_gradient_points,
                                                255 / number_of_gradient_points,
                                                white_index)
    color_values[white_index:yellow_index, 1] = np.linspace(255 / number_of_gradient_points,
                                                            255 / number_of_gradient_points,
                                                            yellow_index - white_index)
    color_values[yellow_index:, 1] = np.linspace(255 / number_of_gradient_points,
                                                 127 / number_of_gradient_points,
                                                 number_of_gradient_points - yellow_index)
    # Blue values
    color_values[:white_index, 2] = np.linspace(255 / number_of_gradient_points,
                                                255 / number_of_gradient_points,
                                                white_index)
    color_values[white_index:yellow_index, 2] = np.linspace(255 / number_of_gradient_points,
                                                            127 / number_of_gradient_points,
                                                            yellow_index - white_index)
    color_values[yellow_index:, 2] = np.linspace(127 / number_of_gradient_points,
                                                 127 / number_of_gradient_points,
                                                 number_of_gradient_points - yellow_index)
    new_colormap = ListedColormap(color_values)

    # Scale B-V values from 0 to 1
    scaled_b_minus_vs = (star_b_minus_vs - np.amin(star_b_minus_vs)) / (
            np.amax(star_b_minus_vs) - np.amin(star_b_minus_vs))

    return scaled_b_minus_vs, new_colormap


def parallax_to_distance(parallax):
    """Take parallax in milliarcseconds and convert to distance in meters"""
    parallax_in_radians = (parallax / 1000. / 3600.) * (2 * np.pi / 360.)
    distance = astronomical_unit / np.tan(parallax_in_radians)
    return distance


def apparent_to_absolute_magnitude(apparent_magnitude, distance):
    """Calculate absolute magnitude from apparent magnitude and distance in meters"""
    distance_in_parsecs = distance / (648000. * astronomical_unit / np.pi)
    absolute_magnitude = apparent_magnitude - 5*np.log10(distance_in_parsecs) + 5
    return absolute_magnitude


def read_file(filename):
    with open(filename) as fp:
        hipparcos_data = {}
        for line in fp:
            star, parallax, magnitude, bmv = line.split()
            hipparcos_data[star] = {
                'parallax': float(parallax),
                'magnitude': float(magnitude),
                'blue_minus_visual': float(bmv)
            }
    return hipparcos_data


# Apply read function to the data file and produce a nested dictionary
hipparcos_dictionary = read_file('hipparcos_data.txt')
star_absolute_magnitudes = []
star_b_minus_vs = []

# Loop over star catalog number key
for term in hipparcos_dictionary:
#       Call parallax_to_distance on parallax value and assign to new value
    distance = parallax_to_distance(hipparcos_dictionary[term]['parallax'])
#       Call apparent_to_absolute_magnitude on apparent magnitude value and assign to new value
    absolute_magnitude = apparent_to_absolute_magnitude(hipparcos_dictionary[term]['magnitude'], distance)
#       Append absolute magnitude for current star into NumPy array of absolute magnitudes
#           named star_absolute_magnitudes
    star_absolute_magnitudes.append(absolute_magnitude)
#       Append B-V value for current star into NumPy array of B-V values
#           named star_b_minus_vs
    star_b_minus_vs.append(hipparcos_dictionary[term]['blue_minus_visual'])

# Use dark style for plot
plt.style.use('dark_background')

# Reverse the absolute magnitude so that negative values appear on top
star_absolute_magnitudes = np.negative(star_absolute_magnitudes)

# Get color map to match star colors
scaled_b_minus_v, hr_diagram_colormap = star_colormap(star_b_minus_vs)

# Create axes labels
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

# Scatter plot of B-V vs absolute magnitude
plt.scatter(star_b_minus_vs, star_absolute_magnitudes, c=scaled_b_minus_v, cmap=hr_diagram_colormap)
plt.show()

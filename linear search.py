import pyglet
import random

# Create a window
window = pyglet.window.Window(width=1100, height=300, caption='Linear Search Visualization')
batch = pyglet.graphics.Batch()

# Generate a list with random numbers
numbers = random.sample(range(1, 100), 20)
random.shuffle(numbers)

# Choose a random number to search for
target_number = random.choice(numbers)

# Variables to control the animation and search
current_index = 0
found_index = -1
search_complete = False


def linear_search():
    global current_index, found_index, search_complete
    if current_index < len(numbers):
        if numbers[current_index] == target_number:
            found_index = current_index
            search_complete = True
        current_index += 1
    else:
        search_complete = True


# Schedule the linear search to run every 0.5 seconds
pyglet.clock.schedule_interval(lambda dt: linear_search(), 0.5)


@window.event
def on_draw():
    window.clear()
    for i, number in enumerate(numbers):
        # Define the position of each circle
        x = i * 50 + 35
        y = window.height // 2
        radius = 20

        # Draw the circle
        if i == current_index and not search_complete:
            color = (112, 233, 255)  # Blue for the current circle being checked
        elif i == found_index:
            color = (233, 255, 112)  # Yellow if the target number is found
        else:
            color = (200, 200, 200)  # Grey for unchecked or passed circles

        pyglet.shapes.Circle(x, y, radius, color=color, batch=batch).draw()
        # Draw the number inside the circle
        label = pyglet.text.Label(str(number), x=x, y=y, anchor_x='center', anchor_y='center', font_size=12,
                                  color=(0, 0, 0, 255), batch=batch)
        label.draw()

    # Draw the target number in the middle top of the screen
    target_label = pyglet.text.Label("Target: " + str(target_number), x=window.width // 2, y=window.height - 20,
                                     anchor_x='center', anchor_y='center', font_size=20, batch=batch)
    target_label.draw()


pyglet.app.run()

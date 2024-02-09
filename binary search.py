import pyglet
import random

# Create a window
window = pyglet.window.Window(width=1100, height=300, caption='Binary Search Visualization')
batch = pyglet.graphics.Batch()

# Generate a sorted list with random numbers and select a random target number
target = random.randint(1, 100)  # Generate a random target number
numbers = sorted(random.sample(range(1, 100), 19) + [target])

# Variables to control the animation and search
left, right = 0, len(numbers) - 1
mid = (left + right) // 2
found = False
search_complete = False


def binary_search():
    global left, right, mid, found, search_complete
    if left <= right and not found:
        mid = (left + right) // 2
        if numbers[mid] == target:
            found = True
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    else:
        search_complete = True


# Schedule the binary search to run every 0.5 seconds
pyglet.clock.schedule_interval(lambda dt: binary_search(), 0.5)

# Label to display the current number being searched
number_label = pyglet.text.Label('', x=window.width // 2, y=window.height - 30, anchor_x='center', font_size=16,
                                 batch=batch)

# Label to display the target number
target_label = pyglet.text.Label(f'Target: {target}', x=window.width // 2, y=window.height - 50, anchor_x='center',
                                 font_size=16, batch=batch)


@window.event
def on_draw():
    window.clear()
    for i, number in enumerate(numbers):
        # Define the position and radius of each circle
        x = i * 50 + 35
        y = window.height // 2
        radius = 20

        # Draw the circle
        if left <= i <= right and not search_complete:
            color = (255, 112, 233)  # Pink for the current search interval
        elif i == mid and not search_complete:
            color = (112, 233, 255)  # Blue for the middle element
        elif found and i == mid:
            color = (233, 255, 112)  # Yellow if target is found
        else:
            color = (200, 200, 200)  # Grey for eliminated elements

        pyglet.shapes.Circle(x, y, radius, color=color, batch=batch).draw()
        # Draw the number inside the circle
        label = pyglet.text.Label(str(number), x=x, y=y, anchor_x='center', anchor_y='center', font_size=12,
                                  color=(0, 0, 0, 255), batch=batch)
        label.draw()

    # Draw the target number label
    target_label.draw()


pyglet.app.run()

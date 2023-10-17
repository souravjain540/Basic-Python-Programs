import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import os

coordinates_df = pd.DataFrame(columns=['x', 'y'])
prev_point = None

def on_click(event):
    global prev_point

    # Check if the click is within the axes
    if event.inaxes:
        x, y = round(event.xdata), round(event.ydata)
        coordinates_df.loc[len(coordinates_df)] = [x, y]
        print(f'Clicked at: x = {x}, y = {y}')
        
        # Plot the clicked point on the graph
        ax.plot(x, y, 'ro')  # 'ro' for red dots

        # Connect to the previous point
        if prev_point:
            prev_x, prev_y = prev_point
            ax.plot([prev_x, x], [prev_y, y], 'b-')  # 'b-' for blue lines

        # Update the plot
        plt.draw()

        # Update the previous point
        prev_point = (x, y)

def save_to_excel(event):
    if not os.path.exists('output'):
        os.makedirs('output')
    
    file_path = 'output/coordinates.xlsx'
    coordinates_df.to_excel(file_path, index=False)
    print(f'Coordinates saved to {file_path}')

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_title('Click on the graph to add coordinates')

# Register the click event
fig.canvas.mpl_connect('button_press_event', on_click)

# Create a button to save the coordinates to Excel
ax_button = plt.axes([0.8, 0.01, 0.1, 0.05])
save_button = Button(ax_button, 'Save to Excel')
save_button.on_clicked(save_to_excel)

plt.show()

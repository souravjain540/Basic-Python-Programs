# A program to calculate the shared area of two rectangles
import re


def shared_area(a, b, c, d):
    """
    Given coordinates for the bottom-left corner (a) and top-right corner (b) of rectangle 1,
    and the bottom-left corner (c) and top-right corner (d) of rectangle 2,
    calculates the area of the overlapping space.
    """
    ax, ay = a
    bx, by = b
    cx, cy = c
    dx, dy = d

    # if no overlap between rectangles
    if ax >= dx or bx <= cx or ay >= dy or by <= cy:
        return 0

    # assume overlap
    ex = max(ax, cx)
    fx = min(bx, dx)
    ey = max(ay, cy)
    fy = min(by, dy)

    return get_rectangle_area((ex, ey), (fx, fy))


def get_rectangle_area(a, b):
    """Given the bottom-left corner (a) and top-right corner (b), calculates the area of the rectangle."""
    ax, ay = a
    bx, by = b

    return (by - ay) * (bx - ax)  # height * width


if __name__ == '__main__':
    print("Enter the coordinates as <x> <y> for the following rectangle corners:")
    prompts = (
        "Bottom-left corner (a) for rectangle 1: ",
        "Top-right corner (b) for rectangle 1: ",
        "Bottom-left corner (c) for rectangle 2: ",
        "Top-right corner (d) for rectangle 2: "
        )
    coordinates = []
    for prompt in prompts:
        while True:
            user_input = input(prompt)
            if re.match("^-?(0|[1-9]\d*)?(\.\d+)?(?<=\d) -?(0|[1-9]\d*)?(\.\d+)?(?<=\d)$", user_input):
                coordinates.append(
                    tuple(float(i) for i in user_input.split(" "))
                )
                break
            else:
                print("Invalid input format. Please type the x and y coordinates with one space between "
                      "(example: '1 2' for coordinate pair (1, 2) or '1.5 -2.2' for (1.5, -2.2)")

    print("\nResult:", shared_area(*coordinates))

from geometry import circle_area, rectangle_area, square_area
import time

start = time.time()
a1 = circle_area(8)
a2 = rectangle_area(10, 12)
a3 = square_area(7.9)
print(a1, a2, a3)
elapsed = time.time() - start
print(f"Program ran for {elapsed} seconds")

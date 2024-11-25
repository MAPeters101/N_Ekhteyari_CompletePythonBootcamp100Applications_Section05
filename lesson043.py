import random
from datetime import datetime
import os

random_number = random.randint(1, 10)
print(f"Random Number: {random_number}")
print()

current_time = datetime.now()
print(f"Current time: {current_time}")
print()

current_dir = os.getcwd()
print(f"Current Directory: {current_dir}")

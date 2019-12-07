import time
from state import State

state = State()

while True:
    time.sleep(0.5)
    print(state.light)
    print(state.noise)
    print(state.motion)

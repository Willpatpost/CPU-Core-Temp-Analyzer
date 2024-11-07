# input_library.py

from typing import TextIO, Iterator, List, Tuple

def parse_raw_temps(original_temps: TextIO, step_size: int = 30) -> Iterator[Tuple[float, List[float]]]:
    """
    Take an input file and time-step size and parse all core temps.

    Args:
        original_temps: an input file

        step_size: time-step in seconds

    Yields:
        A tuple containing the next time step and a List containing _n_ core
        temps as floating point values (where _n_ is the number of CPU cores)
    """
    for step, line in enumerate(original_temps):
        # Split the line by spaces and convert to float
        temps = [float(temp) for temp in line.split()]
        yield (step * step_size), temps

import sys
import os
import matplotlib.pyplot as plt
from input_library import parse_raw_temps
from interpolation import piecewise_linear_interpolation
from least_squares_approximation import least_squares_approximation

def main():
    """
    Main driver function to process CPU temperature data, perform piecewise linear interpolation,
    compute least squares approximation, and plot the results.

    Args:
        None (expects a command line argument for input file)
    """
    input_temps = sys.argv[1]

    times = []
    core_data = [[] for _ in range(4)]

    # Parse temperature data from the input file
    with open(input_temps, 'r') as temps_file:
        for time, raw_core_data in parse_raw_temps(temps_file):
            times.append(time)
            for core_idx, reading in enumerate(raw_core_data):
                core_data[core_idx].append(reading)

    # Perform piecewise linear interpolation for each core
    interpolated_data = [piecewise_linear_interpolation(times, core) for core in core_data]
    interpolated_times = interpolated_data[0][0]
    interpolated_cores = [data[1] for data in interpolated_data]
    equations = [data[2] for data in interpolated_data]

    # Write interpolation and least squares approximation equations to output files
    for core_idx, core_eqs in enumerate(equations):
        output_file_path = f"{os.path.splitext(input_temps)[0]}-core-{core_idx:02d}.txt"
        with open(output_file_path, 'w') as output_file:
            for i, (slope, intercept) in enumerate(core_eqs):
                output_file.write(f"{times[i]:>10} <= x <= {times[i+1]:>10} ; y = {intercept:>10.4f} + {slope:>10.4f} x ; interpolation\n")
            # Compute and add least squares approximation
            slope, intercept = least_squares_approximation(times, core_data[core_idx])
            output_file.write(f"{0:>10} <= x <= {times[-1]:>10} ; y = {intercept:>10.4f} + {slope:>10.4f} x ; least-squares\n")

    # Plot the original and interpolated data for comparison, and add the least squares line
    plt.figure(figsize=(14, 8))
    for i, core in enumerate(core_data):
        plt.subplot(2, 2, i + 1)
        plt.plot(times, core, 'o-', label=f'Original Core {i}')
        plt.plot(interpolated_times, interpolated_cores[i], '-', label=f'Interpolated Core {i}')

        # Compute and plot the least squares line for comparison
        slope, intercept = least_squares_approximation(times, core)
        least_squares_line = [slope * t + intercept for t in times]
        plt.plot(times, least_squares_line, '--', label=f'Least Squares Core {i}')

        plt.xlabel('Time (s)')
        plt.ylabel('Temperature (°C)')
        plt.legend()
        plt.title(f'Core {i} Temperature')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

from run_reader import read_run_data
from data_plotter import plot_floors_reached

RUN_FILES_DIRECTORY = "/Users/michael/Workspace/sts/run_data"


if __name__ == "__main__":
    run_statistics = read_run_data(RUN_FILES_DIRECTORY)
    print(f"Floors reached: {run_statistics.floors_reached_list}")
    plot_floors_reached(run_statistics)

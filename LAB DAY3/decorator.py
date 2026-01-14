import time


def execution_time(func):
    def wrapper():
        start_time = time.time()  # start time

        func()  # call original function

        end_time = time.time()  # end time

        total_time = end_time - start_time

        print(f"Function '{func.__name__}' executed in {total_time:.4f} seconds")

    return wrapper

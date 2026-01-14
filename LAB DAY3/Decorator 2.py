from decorator import execution_time

@execution_time
def sample_function():
    for i in range(1000000):
        pass

sample_function()

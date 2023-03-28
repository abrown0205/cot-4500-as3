import numpy as np
np.set_printoptions(precision=7, suppress=True, linewidth=100)

def function(t: float, w: float):
    return t - (w**2)

def do_work(t, w, h):
    basic_function_call = function(t, w)
    incremented_t = t + h
    incremented_w = w + (h * basic_function_call)
    incremented_function_call = function(incremented_t, incremented_w)
    return basic_function_call + incremented_function_call


def modified_eulers():
    original_w = 1
    start_of_t, end_of_t = (0, 2)
    num_of_iterations = 10
    # set up h
    h = (end_of_t - start_of_t) / num_of_iterations
    for cur_iteration in range(0, num_of_iterations):
        # do we have all values ready?
        t = start_of_t
        w = original_w
        h = h
        # create a function for the inner work
        inner_math = do_work(t, w, h)
        # this gets the next approximation
        next_w = w + ( (h / 2) * inner_math )
        print(next_w)
        # we need to set the just solved "w" to be the original w
        # and not only that, we need to change t as well
        start_of_t = t + h
        original_w = next_w
    return None


if __name__ == "__main__":
    modified_eulers()
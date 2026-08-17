import numpy as np
import matplotlib.pyplot as plt
import pdb

from . import external
import marcos_client.experiment as ex

st = pdb.set_trace

def my_first_experiment():
    exp = ex.Experiment(lo_freq=5, rx_t=3.125)

if __name__ == "__main__":
    my_first_experiment()
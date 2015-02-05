""" Utility functions for TGA fitting """

import numpy as np
from scipy import integrate
import scipy.optimize
import matplotlib.pyplot as plt
import scipy.signal
from lmfit import minimize, Parameters
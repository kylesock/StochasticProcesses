import numpy as np
import matplotlib.pyplot as plt
from typing import Union, Callable, Optional


def poisson_process(rate: int, duration: Union[int, float]):
    t = 0
    k = 0
    sk = [0]
    while t < duration:
        r = np.random.uniform(0, 1)
        t -= np.log(r) / rate
        k += 1
        sk.append(t)

    return sk


def plot_process(process: Callable, xlabel: str, ylabel: str,
                 verbose: bool = False, *args, **kwargs) -> Optional[np.array]:

    S = process(*args, **kwargs)

    plt.figure()
    plt.hlines(np.arange(len(S)), S, S[1:] + [S[-1] + 1])
    plt.vlines(S[1:], np.arange(len(S[1:])), np.arange(1, len(S[1:]) + 1), linestyles='dotted', linewidth=0.5)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

    if verbose:
        return S


S_inter_arrival = poisson_process(1, 30)
print(S_inter_arrival)

plot_process(poisson_process, 't', 'S(t)', rate=1, duration=30)

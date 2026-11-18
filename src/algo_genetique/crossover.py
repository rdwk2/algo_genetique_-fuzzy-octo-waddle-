from abc import ABC, abstractmethod

from algo_genetique.individue import Individue

# faire un coupe de signe + mantisse + exposant en 3 partie choisit aleatoirement et selectionner
#  père   mère
# p1p2p3 m1m2m3
#   child1 child
# p1m2p3 m1p2m3


class Crossover(ABC):

    @abstractmethod
    def doCrossover(self, ind1: Individue, ind2: Individue) -> tuple[Individue, Individue]: ...

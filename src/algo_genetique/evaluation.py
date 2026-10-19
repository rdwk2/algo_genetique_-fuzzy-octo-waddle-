from abc import ABC, abstractmethod

from algo_genetique.individue import Individue


class Evaluation(ABC):
    def __init__(self, borne_min: float, borne_max: float):
        self.borne_min = borne_min
        self.borne_max = borne_max

    @abstractmethod
    def f(self,ind : Individue) -> float:
        ...

    def evaluer(self,ind : Individue) -> float:
        return self.f(ind)

    def __call__(self,ind : Individue) -> float:
        return self.evaluer(ind)

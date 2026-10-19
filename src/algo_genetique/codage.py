from abc import ABC, abstractmethod

from algo_genetique.chromosome import Chromosome
from algo_genetique.coordonnee import Coordonnee


class Codage(ABC):
    @abstractmethod
    def code(self, coodonee: Coordonnee) -> Chromosome: ...

    @abstractmethod
    def decode(self, chromosome: Chromosome) -> Chromosome: ...

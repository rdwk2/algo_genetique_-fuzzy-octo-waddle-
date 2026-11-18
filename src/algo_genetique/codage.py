from abc import ABC, abstractmethod

from algo_genetique.chromosome import Chromosome
from algo_genetique.coordonnee import Coordonnee
from algo_genetique.fenetre import Fenetre


class Codage(ABC):
    @abstractmethod
    def code(self, coordonnee: Coordonnee) -> Chromosome: ...

    @abstractmethod
    def decode(self, chromosome: Chromosome,fenetre : Fenetre) -> Coordonnee: ...

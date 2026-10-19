from typing import Self

from algo_genetique.coordonnee import Coordonnee
from algo_genetique.fenetre import Fenetre


class Individue:
    def __init__(self, coordonnees: list[Coordonnee]) -> None:
        self.coordonnees = coordonnees

    @classmethod
    def uniforme(cls, fenetres: list[Fenetre]) -> Self:
        return cls([Coordonnee.uniforme(f) for f in fenetres])

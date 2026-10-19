from random import uniform
from typing import Self

from algo_genetique.fenetre import Fenetre


class Coordonnee:
    def __init__(self, coordonne: float, fenetre : Fenetre) -> None:
        self.coodonne = coordonne
        self.fenetre = fenetre

    @classmethod
    def uniforme(cls, fenetre : Fenetre) -> Self:
        return cls(uniform(fenetre.borne_min, fenetre.borne_max),fenetre)

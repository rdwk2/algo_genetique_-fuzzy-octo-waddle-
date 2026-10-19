from typing import Self

from algo_genetique.evaluation import Evaluation
from algo_genetique.fenetre import Fenetre
from algo_genetique.individue import Individue


class Population:
    def __init__(
        self, taille: int, fenetres: list[Fenetre], individues: list[Individue]
    ) -> None:
        self.taille = taille
        self.fenetres = fenetres
        self.individues = individues

    @classmethod
    def uniforme(cls, taille, fenetres: list[Fenetre]) -> Self:
        return cls(
            taille, fenetres, [Individue.uniforme(fenetres) for _ in range(taille)]
        )

    def best(self, eval: Evaluation):
        return min(self.individues, key=eval.f)

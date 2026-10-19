from random import choices

from algo_genetique.codage import Codage
from algo_genetique.crossover import Crossover
from algo_genetique.fenetre import Fenetre
from algo_genetique.individue import Individue
from algo_genetique.population import Population
from algo_genetique.selection import Selection


class AlgoGenetique:
    def __init__(
        self,
        eval,
        crossover: Crossover,
        selection: Selection,
        codage: Codage,
        fenetres: list[Fenetre],
    ) -> None:
        self.eval = eval
        self.crossover = crossover
        self.selection = selection
        self.codage = codage
        self.fenetres = fenetres

    def minimize(self, taille: int, max_iter: int = 100) -> Individue:
        if taille % 2 != 0:
            raise Exception("la taille doit être un mutiple de 2")

        pop = Population.uniforme(taille, self.fenetres)

        best = pop.best(self.eval)
        for _ in range(max_iter):
            individues = []
            for _ in range(taille // 2):
                ind1, ind2 = choices(pop.individues, k=2)
                child1, child2 = self.crossover.doCrossover(ind1, ind2)
                new_ind1, new_ind2 = self.selection.select(
                    (ind1, ind2), (child1, child2)
                )
                individues.append(new_ind1)
                individues.append(new_ind2)
            pop = Population(taille, self.fenetres, individues)
            best = pop.best(self.eval)

        return best

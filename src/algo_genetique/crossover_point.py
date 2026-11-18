from algo_genetique.crossover import Crossover


class Crossover_Point(Crossover):
    def __init__(self,nb_points : int) -> None:
        super().__init__()
        self.nb_points = nb_points

    # def doCrossover(
    #     self, ind1: Individue, ind2: Individue
    # ) -> tuple[Individue, Individue]:

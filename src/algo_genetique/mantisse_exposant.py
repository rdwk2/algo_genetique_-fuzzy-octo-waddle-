from algo_genetique.chromosome import Chromosome
from algo_genetique.codage import Codage
from algo_genetique.coordonnee import Coordonnee
from algo_genetique.fenetre import Fenetre


class ChromosomeMantisseExposant(Chromosome):
    def __init__(self, signe: str, mantisse: str, exposant: str) -> None:
        self.signe = signe
        self.mantisse = mantisse
        self.exposant = exposant

    def __str__(self) -> str:
        return f"(signe = {self.signe}, mantisse = {self.mantisse}, exposant = {self.exposant})"


class MantisseExposant(Codage):
    def code(self, coordonnee: Coordonnee) -> ChromosomeMantisseExposant:
        x = coordonnee.coordonne
        signe = "1" if x < 0 else "0"
        x = abs(x)
        str_x = str(x)
        exp = 0
        if "e" in str_x:
            str_x, str_exp = str_x.split("e")
            exp = int(str_exp)
        left, right = str_x.split(".")
        mantisse = bin(int(left + right))[2:]
        exposant = bin(-exp + len(right))[2:]

        if len(mantisse) < 59:
            mantisse = "0"*(59 - len(mantisse)) + mantisse
        if len(exposant) < 4:
            exposant = "0"*(4 - len(mantisse)) + exposant

        return ChromosomeMantisseExposant(signe, mantisse, exposant)

    def decode(self, chromosome: Chromosome, fenetre: Fenetre) -> Coordonnee:
        if not isinstance(chromosome, ChromosomeMantisseExposant):
                raise TypeError(
                    "Le chromosome doit être de type ChromosomeMantisseExposant"
                )
        signe = int(chromosome.signe,2)
        mantisse = int(chromosome.mantisse,2)
        exposant = int(chromosome.exposant,2)
        value = (-1)**signe* mantisse * 10 **(-exposant)
        return Coordonnee(coordonne=value,fenetre=fenetre)

if __name__ == "__main__":
    m = MantisseExposant()
    f = Fenetre(-10, 10)
    x = 0.00123456789123
    c = Coordonnee(x, f)
    ch = m.code(c)
    print(ch)
    c1 = m.decode(ch,f)
    print(x,c1.coordonne,x == c1.coordonne)

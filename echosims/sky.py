
from echosims.cmb import Lensed, CosmicBirefringence, PMF, PatchyReionization
from echosims.foreground import Foregrounds
from echosims.noise import Noise


class Sky:
    def __init__(self, which_cmb: str = 'lensed'):
        if which_cmb == 'lensed':
            self.cmb = Lensed()
        elif which_cmb == 'cosmic_birefringence':
            self.cmb = CosmicBirefringence()
        elif which_cmb == 'pmf':
            self.cmb = PMF()
        elif which_cmb == 'patchy_reionization':
            self.cmb = PatchyReionization()
        else:
            raise ValueError(f"Unknown CMB type: {which_cmb}")

        self.foregrounds = Foregrounds()
        self.noise = Noise()

    def TQU(self, band: str) -> tuple:
        pass
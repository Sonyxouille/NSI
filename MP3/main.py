voiture = []

class Voiture:
    def __init__(self,immatriculation,marque,nom_proprio,abonnement,place):
        self.immatriculation = immatriculation
        self.marque = marque
        self.nom_proprio = nom_proprio
        self.abonnement = abonnement
        self.place = place

    def get_immatriculation(self):
        return self.immatriculation

    def get_marque(self):
        return self.marque

    def get_nom_propri(self):
        return self.nom_proprio

    def get_abonnement(self):
        return self.abonnement

    def get_place(self):
        return self.place

class Parking:
    def __init__(self) -> None:
        pass

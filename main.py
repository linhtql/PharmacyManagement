from Controller.PharmacyController import PharmacyController
from Model.PharmaModel import PharmacyModel
from View.PharmacyView import PharmacyView

def main():
    model = PharmacyModel("DESKTOP-RT1EDQS", "PharmacyManagement", "sa", "68686868")
    view = PharmacyView()
    controller = PharmacyController(model, view)
    controller.run()

if __name__ == "__main__":
    main()

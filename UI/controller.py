
import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listShape = []
    def checkanno(self,e):
        try: int(self._view.anno.value)
        except ValueError:
            self._view.create_alert("inserisci un numero")
        if int(self._view.anno.value)>1906 and int(self._view.anno.value)<2014:
            self._view.btn_graph.disabled = False
        else:
            self._view.create_alert("Anno non compreso")
            self._view.btn_graph.disabled = True

    def checkxg(self, e):
        try: int(self._view.xg.value)
        except ValueError:
            self._view.create_alert("inserisci un numero")
        if int(self._view.xg.value)>1 and int(self._view.xg.value)<180:
            self._view.btn_graph.disabled = False
        else:
            self._view.create_alert("Anno non compreso")
            self._view.btn_graph.disabled = True

    def fillDD(self):
        pass

    def handle_graph(self, e):
        self._model.creaGrafo(self._view.anno.value,self._view.xg.value)
        self._model.stampa()
        self._view.txt_result.controls.append(ft.Text(f"{self._model.stampa()}"))
        dict = self._model.sommaPesi()
        self._view.txt_result.controls.append(ft.Text(f"{dict}"))
        self._view.update_page()
    def handle_path(self, e):
        pass

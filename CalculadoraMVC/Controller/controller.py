from Model.model import Model
from View.view import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def main(self):
        self.view.main()

    def on_button_click(self, caption):
        # print(f'button {caption} clicked')
        result = self.model.calculate(caption)

        self.view.value_var.set(result)

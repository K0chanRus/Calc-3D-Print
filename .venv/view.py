import decoding_data
import calc
import sys
from PyQt6.QtWidgets import QApplication, QWidget
from ui_calc import Ui_MainWindow


def view():
    # Для первого запуска создание нового файла с филаментами
    decoding_data.read_filament()
    decoding_data.read_personal()

    print('Программа калькулятора запущена!')

    class Calc_3D(QWidget):
        def __init__(self):
            super().__init__()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            # Код исполнения

            self.ui.comboBoxMaterial.addItems(decoding_data.search_filament())  # Загрузка филамента для программы
            self.ui.pushButtonCalc.clicked.connect(self.clicButtonCalc)

            self.show()

        def clicButtonCalc(self):

            time = self.ui.lineEditTime.text()  # Получаем времени
            weight = int(self.ui.lineEditWeight.text())  # Получаем вес
            psi = int(self.ui.lineEditPsi.text())  # Получаем количество
            sale = int(self.ui.lineEditSale.text())  # Получаем скидку

            time_min = calc.time_decoding(time)
            calc.calc_print('PC', time_min, weight, psi, sale)

            print()  # выводит введенные данные


    app = QApplication(sys.argv)
    calc_window = Calc_3D()
    calc_window.show()
    sys.exit(app.exec())
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel

class EagleAccountingSystem(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Eagle Accounting System')
        self.setGeometry(100, 100, 800, 600)
        self.initUI()

    def initUI(self):
        # Create a tab widget
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Create tabs
        self.createProductsTab()
        self.createCustomersTab()
        self.createTransactionsTab()
        self.createInvoicesTab()
        self.createReportsTab()

        # Add tabs to the widget
        self.tabs.addTab(self.productsTab, 'Products')
        self.tabs.addTab(self.customersTab, 'Customers')
        self.tabs.addTab(self.transactionsTab, 'Transactions')
        self.tabs.addTab(self.invoicesTab, 'Invoices')
        self.tabs.addTab(self.reportsTab, 'Reports')

    def createProductsTab(self):
        self.productsTab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Manage your products here.'))
        self.productsTab.setLayout(layout)

    def createCustomersTab(self):
        self.customersTab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Manage your customers here.'))
        self.customersTab.setLayout(layout)

    def createTransactionsTab(self):
        self.transactionsTab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Manage your transactions here.'))
        self.transactionsTab.setLayout(layout)

    def createInvoicesTab(self):
        self.invoicesTab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Manage your invoices here.'))
        self.invoicesTab.setLayout(layout)

    def createReportsTab(self):
        self.reportsTab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel('View your reports here.'))
        self.reportsTab.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EagleAccountingSystem()
    window.show()
    sys.exit(app.exec_())
import json
import asyncio
from PySide6 import QtWidgets
from gui.layouts.ui_mainWindow import Ui_MainWindow
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt
from utils.http import httpxGetAsync
from utils.openapi import get_endpoints, get_endpoint_definition


KEY_ROLE_METHOD = Qt.UserRole
KEY_ROLE_ENDPOINT = Qt.UserRole + 1

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        self.openapi_data = None
        self.endpoints = None
        self.endpoint_definition = None
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.lineEdit_url.textChanged.connect(self.on_url_changed)
        self.ui.lineEdit_url.setText("https://api...")


    def clear(self):
        self.openapi_data = None
        self.endpoints = None
        self.endpoint_definition = None
        self.load_endpoints()
        self.load_endpoint(None, None)


    def load_endpoints(self):
        try:
            if self.openapi_data is None:
                self.ui.listView_endpoints.setModel(QStandardItemModel())
                return
            model = QStandardItemModel()
            for endpoint in self.endpoints:
                value = f"{endpoint['method']}\t{endpoint['endpoint']}"
                item = QStandardItem(value)
                item.setData(endpoint['method'], role=KEY_ROLE_METHOD)
                item.setData(endpoint['endpoint'], role=KEY_ROLE_ENDPOINT)
                model.appendRow(item)
            self.ui.listView_endpoints.setModel(model)

            self.ui.listView_endpoints.selectionModel().selectionChanged.connect(self.on_endpoint_changed)
        except Exception as e:
            print(e)

    def load_endpoint(self, method: str, endpoint: str):
        try:
            if method is None or endpoint is None:
                self.ui.textEdit_endpoint_definition.setPlainText("")
                return
            self.endpoint_definition = get_endpoint_definition(self.openapi_data, method, endpoint)
            self.ui.textEdit_endpoint_definition.setPlainText(json.dumps(self.endpoint_definition, indent=2))

        except Exception as e:
            print(e)


    def on_url_changed(self, text):
        asyncio.run(self.on_url_changed_async(text))

    async def on_url_changed_async(self, text):
        try:
            response = await httpxGetAsync(text)
            self.openapi_data = json.loads(response.text)
            self.endpoints = get_endpoints(self.openapi_data)
            self.load_endpoints()
        except Exception as e:
            self.clear()
        
    def on_endpoint_changed(self, selected, deselected):
        try:
            if not selected.indexes():
                return
            index = selected.indexes()[0]
            key_method = index.data(KEY_ROLE_METHOD)
            key_endpoint = index.data(KEY_ROLE_ENDPOINT)
            self.load_endpoint(key_method, key_endpoint)
        except Exception as e:
            print(e)

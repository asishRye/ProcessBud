from PyQt5 import QtCore
from process.process_gui.process_conf import *
from process.process_gui.process_node_base import *
from nodeeditor.utils import dumpException


class UrlInputContent(QDMNodeContentWidget):
    def initUI(self):
        self.property_label = QLabel("Properties", self)
        self.property_label.setGeometry(QtCore.QRect(3, 3, 155, 20))
        self.property_label.setFont(QFont('Arial', 10))
        self.property_label.setStyleSheet("background-color:grey; border-radius:o.1px;color:white")
        self.edit = QLabel("", self)
        self.edit.setGeometry(QtCore.QRect(6, 30, 155, 20))
        self.edit.setObjectName(self.node.content_label_objname)


    def serialize(self):
        res = super().serialize()
        res['value'] = self.edit.text()
        # print(res)
        return res

    def deserialize(self, data, hashmap={}):
        res = super().deserialize(data, hashmap)
        try:
            value = data['value']
            self.edit.setText(value)
            return True & res
        except Exception as e:
            dumpException(e)
        return res


@register_node(OP_NODE_URL)
class ProcessNode_Url(ProcessNode):
    icon = ""
    op_code = OP_NODE_URL
    op_title = "Open url"
    content_label = ""
    content_label_objname = "calc_node_bg"

    def __init__(self, scene):
        list = scene.node_list()
        if len(list) == 0:

            super().__init__(scene, inputs="", outputs=[1])
            # print("start", self.node.start)
            # print("start",self.start)
            self.content.property_label.setText("Properties | START")
        else:
            super().__init__(scene, inputs=[1], outputs=[1])
        self.eval()

    def initInnerClasses(self):
        self.content = UrlInputContent(self)
        self.grNode = ProcessGraphicsNode(self)
        # self.content.edit.textChanged.connect(self.onInputChanged)

    def evalImplementation(self):
        u_value = self.content.edit.text()
        s_value = str(u_value)
        self.value = s_value
        return self.value

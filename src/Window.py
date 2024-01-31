import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QVBoxLayout, QWidget, QPushButton, QInputDialog
from PyQt5.QtGui import QPixmap
from graphviz import Digraph
from TreeBalanced import TreeBalanced, Node

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.tree = None

        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene)
        self.btn_create_tree = QPushButton("Créer un arbre", self)
        self.btn_add_node = QPushButton("Ajouter un nœud", self)
        self.btn_remove_node = QPushButton("Supprimer un nœud", self)

        self.btn_create_tree.clicked.connect(self.create_tree)
        self.btn_add_node.clicked.connect(self.add_node)
        self.btn_remove_node.clicked.connect(self.remove_node)

        self.central_widget = QWidget()
        self.central_layout = QVBoxLayout(self.central_widget)
        self.central_layout.addWidget(self.view)
        self.central_layout.addWidget(self.btn_create_tree)
        self.central_layout.addWidget(self.btn_add_node)
        self.central_layout.addWidget(self.btn_remove_node)

        self.setCentralWidget(self.central_widget)
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Arbre B-Tree Visualisation')

    def visualize_tree(self):
        if self.tree:
            graph = self.tree.visualize_tree()
            temp_file = "temp_tree"
            graph.render(filename=temp_file, format='png', cleanup=True)
            pixmap = QPixmap(temp_file + '.png')
            self.scene.clear()
            self.scene.addPixmap(pixmap)
            self.view.setScene(self.scene)

    def create_tree(self):
        degree = 3
        self.tree = TreeBalanced(degree)
        self.visualize_tree()

    def add_node(self):
        if self.tree:
            key, ok = QInputDialog.getInt(self, "Ajouter un nœud", "Entrez la clé du nœud:")
            if ok:
                value, ok = QInputDialog.getText(self, "Ajouter un nœud", "Entrez la valeur du nœud:")
                if ok:
                    self.tree.insert(key, value)
                    self.visualize_tree()

    def remove_node(self):
        self.visualize_tree()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

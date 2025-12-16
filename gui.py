import sys
import os
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QTextEdit,
    QLineEdit, QGroupBox, QComboBox, QFileDialog, QSpacerItem, QSizePolicy
)
from PyQt6.QtCore import QProcess, Qt
from qt_material import apply_stylesheet


class RaagaLabGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🎵 MeloLab")
        self.setGeometry(300, 300, 600, 550)

        self.layout = QVBoxLayout()
        self.layout.setSpacing(20)  # space between sections

        # ---------------- Step 1: Select MIDI ----------------
        self.step1_groupbox = QGroupBox("Step 1: Select Rhythm MIDI File")
        self.step1_layout = QVBoxLayout()
        self.setStyleSheet("""
            QGroupBox {
                font-size: 18px;   /* match big button text size */
                font-weight: bold;
            }
        """)

        self.midi_file_path = None

       # MIDI file selection button (old Windows look)
        self.midi_button = QPushButton("Browse")
        self.midi_button.setFixedSize(100, 20)  # smaller size
        self.midi_button.setStyleSheet("""
            QPushButton {
                background-color: #d4d0c8;   /* classic grey */
                color: #000000;
                font-size: 12px;
                border: 1px solid #a0a0a0;
                border-radius: 4px;         /* smoother corners */
                padding: 2px;
            }
            QPushButton:hover {
                background-color: #e4e0d8;  /* lighter on hover */
            }
            QPushButton:pressed {
                background-color: #c0bcb4;  /* darker on click */
                border: 1px solid #707070;
            }
        """)

        self.midi_button.clicked.connect(self.select_midi_file)  # ✅ connect it


        self.midi_label = QLabel("No MIDI file selected")
        self.step1_layout.addWidget(self.midi_button)
        self.step1_layout.addWidget(self.midi_label)
        self.step1_groupbox.setLayout(self.step1_layout)
        self.layout.addWidget(self.step1_groupbox)

        self.layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))

        # ---------------- Step 2: Enter BPM ----------------
        self.step2_groupbox = QGroupBox("Step 2: Enter BPM (Beats Per Minute)")
        self.step2_layout = QVBoxLayout()
        self.bpm_input = QLineEdit()
        self.bpm_input.setPlaceholderText("Enter BPM (e.g., 90 or 90.5)")
        self.step2_layout.addWidget(self.bpm_input)
        self.step2_groupbox.setLayout(self.step2_layout)
        self.layout.addWidget(self.step2_groupbox)

        self.layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))

        # ---------------- Step 3: Select Flavor ----------------
        self.step3_groupbox = QGroupBox("Step 3: Select Flavor")
        self.step3_layout = QVBoxLayout()
        self.flavor_dropdown = QComboBox()
        flavor_folder = os.path.join(os.path.dirname(__file__), "flavors")
        if os.path.exists(flavor_folder):
            flavors = [f[:-3] for f in os.listdir(flavor_folder)
                       if f.endswith(".py") and f != "__init__.py"]
            self.flavor_dropdown.addItems(flavors)
        self.step3_layout.addWidget(self.flavor_dropdown)
        self.step3_groupbox.setLayout(self.step3_layout)
        self.layout.addWidget(self.step3_groupbox)

        self.layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))

        # ---------------- Generate Melody Button ----------------
        self.start_button = QPushButton("Generate Melody")
        self.start_button.setFixedSize(200, 35)  # width x height

        self.start_button.clicked.connect(self.start_main)
        self.layout.addWidget(self.start_button)

        # ---------------- Console Output ----------------
        self.console_output = QTextEdit()
        self.console_output.setReadOnly(True)
        self.layout.addWidget(self.console_output)

        self.setLayout(self.layout)
        self.process = None

    # ---------------- Functions ----------------
    def select_midi_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select Rhythm MIDI File", "", "MIDI Files (*.mid *.midi)")
        if path:
            self.midi_file_path = path
            self.midi_label.setText(os.path.basename(path))
        else:
            self.midi_label.setText("No MIDI file selected")

    def start_main(self):
        if not self.midi_file_path:
            self.console_output.append("<span style='color:red;'>Please select a MIDI file first!</span>")
            return

        bpm_text = self.bpm_input.text()
        try:
            bpm = float(bpm_text)
        except ValueError:
            self.console_output.append("<span style='color:red;'>Invalid BPM. Please enter a number.</span>")
            return

        flavor = self.flavor_dropdown.currentText()
        script_path = os.path.join(os.path.dirname(__file__), "main.py")
        if not os.path.exists(script_path):
            self.console_output.append("<span style='color:red;'>main.py not found!</span>")
            return

        self.start_button.setEnabled(False)
        self.process = QProcess()
        self.process.readyReadStandardOutput.connect(self.handle_stdout)
        self.process.readyReadStandardError.connect(self.handle_stderr)
        self.process.finished.connect(self.process_finished)

        self.process.start("python3", [script_path, str(bpm), flavor, self.midi_file_path])

    def handle_stdout(self):
        data = self.process.readAllStandardOutput().data().decode()
        self.console_output.append(data)

    def handle_stderr(self):
        data = self.process.readAllStandardError().data().decode()
        self.console_output.append(f"<span style='color:red;'>{data}</span>")

    def process_finished(self):
        self.start_button.setEnabled(True)


if __name__ == "__main__":
    app = QApplication([])
    # Apply any qt-material theme (dark_teal, dark_cyan, dark_purple, dark_amber, etc.)
    apply_stylesheet(app, theme='dark_cyan.xml')

    window = RaagaLabGUI()
    window.show()
    sys.exit(app.exec())

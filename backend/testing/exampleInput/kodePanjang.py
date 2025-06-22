from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, 
    QRadioButton, QTableWidget, QTableWidgetItem, 
    QHeaderView, QLabel, QPushButton, QDateEdit
)
from PyQt5.QtCore import Qt, QDate
from db import insert_history, fetch_all_history

class HistoryTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.history = fetch_all_history()
        self.init_ui()
        self.setup_connections()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)

        title = QLabel("Exercise History")
        title.setStyleSheet("""
            QLabel {
                font-size: 20px;
                font-weight: bold;
                color: #333;
                padding-bottom: 10px;
            }
        """)
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        filter_layout = QHBoxLayout()

        self.mode_group = QGroupBox("Filter by Mode")
        self.mode_group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 1px solid #ddd;
                border-radius: 5px;
                margin-top: 10px;
                padding-top: 15px;
            }
        """)
        mode_layout = QHBoxLayout()
        self.all_radio = QRadioButton("All")
        self.squat_radio = QRadioButton("Squat")
        self.plank_radio = QRadioButton("Plank")
        self.all_radio.setChecked(True)
        mode_layout.addWidget(self.all_radio)
        mode_layout.addWidget(self.squat_radio)
        mode_layout.addWidget(self.plank_radio)
        mode_layout.addStretch()
        self.mode_group.setLayout(mode_layout)
        filter_layout.addWidget(self.mode_group)

        self.date_group = QGroupBox("Filter by Date")
        self.date_group.setStyleSheet(self.mode_group.styleSheet())
        date_layout = QHBoxLayout()
        date_layout.addWidget(QLabel("From:"))
        self.from_date = QDateEdit()
        self.from_date.setCalendarPopup(True)
        self.from_date.setDate(QDate.currentDate().addMonths(-1))
        date_layout.addWidget(QLabel("To:"))
        self.to_date = QDateEdit()
        self.to_date.setCalendarPopup(True)
        self.to_date.setDate(QDate.currentDate())
        self.filter_button = QPushButton("Apply Filters")
        self.filter_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 6px 12px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        date_layout.addWidget(self.from_date)
        date_layout.addWidget(self.to_date)
        date_layout.addWidget(self.filter_button)
        date_layout.addStretch()
        self.date_group.setLayout(date_layout)
        filter_layout.addWidget(self.date_group)

        # Optional: Tambah tombol refresh jika ingin
        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.setStyleSheet("""
            QPushButton {
                background-color: #1976D2;
                color: white;
                border-radius: 4px;
                padding: 6px 12px;
            }
            QPushButton:hover {
                background-color: #125599;
            }
        """)
        self.refresh_button.clicked.connect(self.reload_history)
        filter_layout.addWidget(self.refresh_button)

        layout.addLayout(filter_layout)

        self.table = self.create_table()
        layout.addWidget(self.table)

        self.empty_label = QLabel("No history records available")
        self.empty_label.setAlignment(Qt.AlignCenter)
        self.empty_label.setStyleSheet("""
            QLabel {
                font-size: 16px;
                color: #777;
                padding: 20px;
            }
        """)
        self.empty_label.hide()
        layout.addWidget(self.empty_label)

        self.stats_label = QLabel()
        self.stats_label.setAlignment(Qt.AlignCenter)
        self.stats_label.setStyleSheet("font-size: 14px;")
        layout.addWidget(self.stats_label)

        layout.addStretch()
        self.setLayout(layout)
        self.update_table()

    def create_table(self):
        table = QTableWidget()
        table.setStyleSheet("""
            QTableWidget {
                border: 1px solid #ddd;
                border-radius: 5px;
                background-color: white;
                alternate-background-color: #f9f9f9;
                selection-background-color: #e0f7fa;
                gridline-color: #eee;
            }
            QHeaderView::section {
                background-color: #4CAF50;
                color: white;
                padding: 5px;
                border: none;
                font-weight: bold;
            }
        """)
        table.setAlternatingRowColors(True)
        table.setSelectionBehavior(QTableWidget.SelectRows)
        table.setEditTriggers(QTableWidget.NoEditTriggers)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.verticalHeader().setVisible(False)
        table.setSortingEnabled(True)
        return table

    def setup_connections(self):
        self.all_radio.toggled.connect(self.update_table)
        self.squat_radio.toggled.connect(self.update_table)
        self.plank_radio.toggled.connect(self.update_table)
        self.filter_button.clicked.connect(self.update_table)

    def add_record(self, record):
        insert_history(record)
        self.history = fetch_all_history()  # reload dari database setelah insert
        self.update_table()
        self.update_stats()

    def reload_history(self):
        self.history = fetch_all_history()
        self.update_table()
        self.update_stats()

    def update_table(self):
        if self.all_radio.isChecked():
            mode_filter = None
        elif self.squat_radio.isChecked():
            mode_filter = "squat"
        else:
            mode_filter = "plank"

        from_date = self.from_date.date().toString("yyyy-MM-dd")
        to_date = self.to_date.date().addDays(1).toString("yyyy-MM-dd")

        filtered = []
        for record in self.history:
            record_date = str(record.get("timestamp", "")).split()[0]
            if mode_filter and record.get("mode") != mode_filter:
                continue
            if not (from_date <= record_date < to_date):
                continue
            filtered.append(record)

        if not filtered:
            self.table.hide()
            self.empty_label.show()
            self.update_stats()
            return

        self.empty_label.hide()
        self.table.show()
        headers = ["Name", "Mode", "Count/Time", "Duration", "Date/Time"]
        self.table.setColumnCount(len(headers))
        self.table.setHorizontalHeaderLabels(headers)
        self.table.setRowCount(len(filtered))

        for i, record in enumerate(filtered):
            mode = record.get("mode", "")
            name = record.get("name", "Unknown")
            timestamp = str(record.get("timestamp", ""))
            if mode == "squat":
                count = str(record.get("squat_count", 0))
                duration = f"{record.get('squat_duration', 0)} sec"
                metric = count
            else:
                active_time = str(record.get("plank_active_time", 0))
                total_time = f"{record.get('plank_total_time', 0)} sec"
                metric = f"{active_time} sec"
                duration = total_time

            items = [
                QTableWidgetItem(name),
                QTableWidgetItem(mode.capitalize()),
                QTableWidgetItem(metric),
                QTableWidgetItem(duration),
                QTableWidgetItem(timestamp)
            ]
            for col, item in enumerate(items):
                self.table.setItem(i, col, item)
                if col in [2, 3]:
                    item.setTextAlignment(Qt.AlignCenter)

        self.table.sortByColumn(4, Qt.DescendingOrder)
        self.table.resizeColumnsToContents()
        self.update_stats()

    def update_stats(self):
        if not self.history:
            self.stats_label.setText("No records available")
            return
        total_squats = sum(r.get("squat_count", 0) for r in self.history if r.get("mode") == "squat")
        total_plank_time = sum(r.get("plank_active_time", 0) for r in self.history if r.get("mode") == "plank")
        stats_text = []
        if total_squats > 0:
            stats_text.append(f"Total Squats: {total_squats}")
        if total_plank_time > 0:
            stats_text.append(f"Total Plank Time: {total_plank_time} sec")
        self.stats_label.setText(" | ".join(stats_text) if stats_text else "No exercise data")

import time
import cv2
import os
import sys
import logging
from datetime import datetime
from ultralytics import YOLO
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QImage

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class DetectionThread(QThread):
    updateData = pyqtSignal(dict)
    updateFrame = pyqtSignal(QImage)
    errorOccurred = pyqtSignal(str)

    def __init__(self, mode="squat", parent=None):
        super().__init__(parent)
        self.mode = mode
        self.running = False
        self.threshold = 0.5
        self.model = self.load_model()
        self.ready_to_start = False
        # Inisialisasi awal untuk memastikan nilai default
        self.squat_start_time = 0.0
        self.plank_start_time = 0.0
        self.last_plank_detection_time = 0.0
        self.squat_count = 0 # Inisialisasi squat_count di sini

    def load_model(self):
        try:
            model_path = resource_path(os.path.join("models", "best-yolov8new.pt"))
            return YOLO(model_path)
        except Exception as e:
            self.errorOccurred.emit(f"Failed to load model: {str(e)}")
            return None
        
    def enable_start(self):
        """Dipanggil setelah hitungan mundur selesai untuk memulai penghitungan."""
        self.ready_to_start = True
        self.squat_start_time = time.time() # Reset waktu mulai squat
        self.plank_start_time = time.time() # Reset waktu mulai plank
        self.last_plank_detection_time = time.time() # Reset waktu deteksi plank terakhir
        self.squat_count = 0 # Reset hitungan squat
        logging.info(f"Exercise started. Squat start time: {self.squat_start_time}, Plank start time: {self.plank_start_time}")

    def run(self):
        if not self.model:
            return

        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            self.errorOccurred.emit("Could not open webcam")
            return
            
        self.running = True
        prev_state = "stand"
        state_changed = False
        # squat_count, squat_start_time, plank_start_time, last_plank_detection_time
        # sekarang diambil dari self. variabel
        plank_active_time = 0.0
        plank_detected_in_frame = False
        no_detection_start = None

        try:
            while self.running:
                ret, frame = self.cap.read()
                if not ret:
                    continue

                current_time = time.time()
                results = self.model(frame, imgsz=640, verbose=False)
                
                # Process detections
                annotated_frame, detected_class, detected_conf = self.process_detections(frame, results)

                plank_detected_in_frame = False

                data = {"mode": self.mode}

                if self.mode == "squat":
                    if detected_class == "squat" and prev_state == "stand":
                        state_changed = True
                    elif detected_class == "stand" and prev_state == "squat" and state_changed:
                        if self.ready_to_start: # Hanya hitung jika penghitungan sudah dimulai
                            self.squat_count += 1
                        state_changed = False
                    
                    squat_duration = 0
                    if self.ready_to_start:
                        squat_duration = int(current_time - self.squat_start_time)

                    data.update({
                        "squat_count": self.squat_count,
                        "squat_duration": squat_duration
                    })
                    prev_state, state_changed = self.update_squat_state(detected_class, prev_state, state_changed)
                
                elif self.mode == "plank":
                    if detected_class == "plank" and detected_conf >= 70:
                        plank_detected_in_frame = True
                        
                    if self.ready_to_start:
                        if plank_detected_in_frame:
                            plank_active_time += (current_time - self.last_plank_detection_time)
                        self.last_plank_detection_time = current_time

                        total_time = int(current_time - self.plank_start_time)
                    else:
                        total_time = 0
                        plank_active_time = 0

                    data.update({
                        "plank_total_time": total_time,
                        "plank_active_time": int(plank_active_time),
                        "plank_accuracy": int(detected_conf) if detected_class == "plank" else 0
                    })
                    
                    if detected_class == "plank" and detected_conf < 50:
                        data["warning"] = "Plank accuracy below 50%! Stopping exercise."
                        self.running = False

                no_detection_start = self.update_no_detection(
                    detected_class, current_time, no_detection_start
                )
                
                if detected_class is None and no_detection_start and \
                   (current_time - no_detection_start > 10):
                    data["warning"] = "No pose detected for 10 seconds! Stopping exercise."
                    self.running = False

                if self.ready_to_start:
                    self.updateData.emit(data)
                self.emit_frame(annotated_frame)
                self.msleep(100)

        except Exception as e:
            logging.error(f"Detection error: {e}")
            self.errorOccurred.emit(f"Detection error: {str(e)}")
        finally:
            self.cap.release()

    def process_detections(self, frame, results):
        annotated_frame = frame.copy()
        detected_class = None
        detected_conf = 0.0
        best_box = None
        highest_conf = 0.0

        for result in results:
            if result.keypoints is not None:
                for kp in result.keypoints.xy:
                    keypoints = [(int(x), int(y)) for x, y in kp]

                    for x, y in keypoints:
                        cv2.circle(annotated_frame, (x, y), 4, (0, 0, 255), -1)

                    skeleton = [
                        (0, 1),      # head to neck
                        (1, 2), (2, 3), (3, 4), (4, 5),      # left arm
                        (1, 10), (10, 11), (11, 12), (12, 13),  # right arm
                        (1, 6),       # neck to mid-hip
                        (6, 17), (17, 14), (14, 15), (15, 18),  # left leg
                        (6, 19), (19, 7), (7, 8), (8, 9)        # right leg
                    ]

                    for i, j in skeleton:
                        if i < len(keypoints) and j < len(keypoints):
                            pt1 = keypoints[i]
                            pt2 = keypoints[j]
                            if pt1 != (0, 0) and pt2 != (0, 0):
                                cv2.line(annotated_frame, pt1, pt2, (255, 0, 0), 2)
                            for box in result.boxes:
                                conf = float(box.conf)
                                if conf > highest_conf and conf > self.threshold:
                                    highest_conf = conf
                                    best_box = box
                                    cls_id = int(box.cls)
                                    detected_class = self.model.names[cls_id]
                                    detected_conf = conf * 100

        if best_box:
            xyxy = best_box.xyxy[0].tolist()
            color = (0, 255, 0)
            thickness = 2
            cv2.rectangle(
                annotated_frame,
                (int(xyxy[0]), int(xyxy[1])),
                (int(xyxy[2]), int(xyxy[3])),
                color, thickness
            )
            label = f"{detected_class}: {detected_conf:.1f}%"
            cv2.putText(
                annotated_frame, label,
                (int(xyxy[0]), int(xyxy[1]) - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, thickness
            )

        return annotated_frame, detected_class, detected_conf

    def update_squat_state(self, detected_class, prev_state, state_changed):
        if detected_class == "squat":
            if prev_state == "stand":
                state_changed = True
            return "squat", state_changed
        elif detected_class == "stand":
            return "stand", state_changed
        return prev_state, state_changed

    def update_no_detection(self, detected_class, current_time, no_detection_start):
        if detected_class is None:
            return current_time if no_detection_start is None else no_detection_start
        return None

    def emit_frame(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        height, width, channels = rgb_frame.shape
        bytes_per_line = channels * width
        q_img = QImage(rgb_frame.data, width, height, bytes_per_line, QImage.Format_RGB888)
        self.updateFrame.emit(q_img)

    def stop(self):
        self.running = False
        self.wait(2000)
from datetime import datetime
from ultralytics import YOLO
from PyQt5.QtCore import QThread, pyqtSignal, Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QComboBox, 
    QGroupBox, QLineEdit, QMessageBox
)
from voice_thread import VoiceCommandThread
from detection_thread import DetectionThread
from config_manager import get_pc_id

class CounterTab(QWidget):
    sessionFinished = pyqtSignal(dict)
    errorOccurred = pyqtSignal(str)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.mode = None
        self.detection_thread = None
        self.voice_thread = None
        self.latest_data = {}
        self.counting_started = False
        self.pc_id = get_pc_id() # Get the PC ID when the tab is initialized
        print(f"CounterTab initialized with PC ID: {self.pc_id}") # DEBUG PRINT
        self.init_ui()
        self.setup_connections()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)

        # Name input
        self.name_input = self.create_name_input()
        layout.addLayout(self.name_input)

        # Mode selection (DROPDOWN)
        self.mode_selector = self.create_mode_selector()
        layout.addWidget(self.mode_selector)

        # Camera feed
        self.camera_label = self.create_camera_label()
        layout.addWidget(self.camera_label, 0, Qt.AlignCenter)

        # Countdown label
        self.countdown_label = QLabel("", self)
        self.countdown_label.setAlignment(Qt.AlignCenter)
        self.countdown_label.setStyleSheet("font-size: 24px; color: red;")
        self.countdown_label.hide()  # Hide by default
        layout.addWidget(self.countdown_label)

        # Buttons
        button_layout = self.create_button_layout()
        layout.addLayout(button_layout)

        # Info display
        self.info_label = self.create_info_label()
        layout.addWidget(self.info_label)

        self.setLayout(layout)

    def create_name_input(self):
        layout = QHBoxLayout()
        name_label = QLabel("Name:")
        name_label.setStyleSheet("font-weight: bold;")
        
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("Enter your name")
        self.name_edit.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 1px solid #ccc;
                border-radius: 4px;
                font-size: 14px;
            }
        """)
        
        layout.addWidget(name_label)
        layout.addWidget(self.name_edit)
        layout.addStretch()
        return layout

    def create_mode_selector(self):
        group = QGroupBox("Exercise Mode")
        group.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 1px solid #ddd;
                border-radius: 5px;
                margin-top: 10px;
                padding-top: 15px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 3px;
            }
        """)
        
        self.mode_combo = QComboBox()
        self.mode_combo.addItems(["Select Mode", "Squat", "Plank"])
        self.mode_combo.setCurrentIndex(0)
        
        # Style for QComboBox
        self.mode_combo.setStyleSheet("""
            QComboBox {
                background-color: white;
                border: 1px solid #ccc;
                border-radius: 4px;
                padding: 5px 10px;
                min-width: 120px;
                font-size: 14px;
                color: #000000; /* Added to ensure text color is black */
            }
            QComboBox:hover {
                border: 1px solid #aaa;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                border-left: 1px solid #ddd;
            }
            QComboBox::down-arrow {
                image: url(icons/down_arrow.svg);  /* Replace with your arrow path */
                width: 12px;
                height: 12px;
            }
            QComboBox QAbstractItemView {
                border: 1px solid #ddd;
                background: white;
                selection-background-color: #e0f7fa;
                padding: 4px;
                margin: 0px;
                outline: none;
            }
            QComboBox:disabled {
                background: #f5f5f5;
                color: #999;
            }
        """)
        
        layout = QHBoxLayout()
        layout.addWidget(self.mode_combo)
        layout.addStretch()
        group.setLayout(layout)
        return group

    def create_camera_label(self):
        label = QLabel("Camera Feed")
        label.setFixedSize(640, 480)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("""
            QLabel {
                border: 2px solid #aaa;
                border-radius: 5px;
                background-color: #000;
            }
        """)
        return label

    def create_button_layout(self):
        layout = QHBoxLayout()
        
        self.start_button = self.create_button(
            "Start Exercise", "#4CAF50", "#45a049", self.start_tracking
        )
        self.start_button.setEnabled(False)  # Default: disabled

        self.stop_button = self.create_button(
            "Stop Exercise", "#f44336", "#d32f2f", self.stop_tracking
        )
        self.stop_button.setEnabled(False)
        
        layout.addStretch()
        layout.addWidget(self.start_button)
        layout.addSpacing(10)
        layout.addWidget(self.stop_button)
        layout.addStretch()
        return layout

    def create_button(self, text, color, hover_color, callback):
        button = QPushButton(text)
        button.setStyleSheet(f"""
            QPushButton {{
                background-color: {color};
                color: white;
                border: none;
                padding: 10px 20px;
                font-size: 14px;
                border-radius: 5px;
                min-width: 120px;
            }}
            QPushButton:hover {{
                background-color: {hover_color};
            }}
            QPushButton:disabled {{
                background-color: #cccccc;
            }}
        """)
        button.clicked.connect(callback)
        return button

    def create_info_label(self):
        label = QLabel("Please select exercise mode.")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("""
            QLabel {
                font-size: 16px;
                padding: 15px;
                border: 1px solid #ddd;
                border-radius: 5px;
                background-color: #f9f9f9;
            }
        """)
        return label

    def setup_connections(self):
        self.mode_combo.currentIndexChanged.connect(self.on_mode_changed)

    def on_mode_changed(self):
        selected = self.mode_combo.currentText()
        self.stop_camera()
        self.stop_voice_listening()
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(False)
        self.counting_started = False

        if selected == "Select Mode":  # Adjust to the new text
            self.info_label.setText("Please select exercise mode.")
            self.mode = None
            return
        else:
            self.mode = selected.lower()
            self.info_label.setText(f"Mode: {selected}\nReady to start. Say 'start' or click Start!")
            self.start_camera_preview()
            self.start_voice_listening()
            self.start_button.setEnabled(True)


    def start_camera_preview(self):
        if self.detection_thread:
            self.detection_thread.stop()
            self.detection_thread = None
        self.detection_thread = DetectionThread(mode=self.mode)
        self.detection_thread.updateFrame.connect(self.update_camera)
        self.detection_thread.start()
        # DO NOT connect updateData here, only for preview (not counting)

    def stop_camera(self):
        if self.detection_thread:
            self.detection_thread.stop()
            self.detection_thread = None
        self.camera_label.clear()

    def start_tracking(self):
        if self.counting_started:
            return  # Already counting, ignore

        name = self.name_edit.text().strip()
        if not name:
            self.show_error("Name cannot be empty!")
            return
        if self.mode is None:
            self.show_error("Please select an exercise mode!")
            return

        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(False)  # Disable stop button during countdown

        # Start detection with updateData (activate counting)
        self.detection_thread = DetectionThread(mode=self.mode)
        self.detection_thread.counting_started = False
        self.detection_thread.updateData.connect(self.update_info)
        self.detection_thread.updateFrame.connect(self.update_camera)
        self.detection_thread.errorOccurred.connect(self.handle_detection_error)
        self.detection_thread.start()

        # Initialize countdown variables
        self.countdown_time = 5  # Countdown from 5 seconds
        self.show_countdown_label(self.countdown_time)

        self.countdown_timer = QTimer(self)
        self.countdown_timer.timeout.connect(self.update_countdown)
        self.countdown_timer.timeout.connect(self.send_start_to_thread)

        self.countdown_timer.start(1000)  # 1 second intervals

    def send_start_to_thread(self):
        if self.countdown_time == 1 and self.detection_thread:
            self.detection_thread.enable_start()

    def show_countdown_label(self, time_left):
        # You can customize this to show countdown on a QLabel or overlay
        self.countdown_label.setText(f"Starting in {time_left}...")
        self.countdown_label.show()

    def update_countdown(self):
        self.countdown_time -= 1
        if self.countdown_time > 0:
            self.show_countdown_label(self.countdown_time)
        else:
            self.countdown_timer.stop()
            self.countdown_label.hide()
            self.start_counting()

    def start_counting(self):
        self.counting_started = True
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)

    def stop_tracking(self):
        if not self.counting_started:
            return  # Not currently counting
        self.stop_voice_listening()
        self.stop_camera()
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.counting_started = False

        name = self.name_edit.text().strip() or "Unknown"
        session_data = {
            "name": name,
            "mode": self.mode,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "pc_id": self.pc_id 
        }
        session_data.update(self.latest_data)
        print(f"Emitting session data with PC ID: {session_data.get('pc_id')}") # DEBUG PRINT
        self.sessionFinished.emit(session_data)
        self.info_label.setText("Session finished. Please select mode or start again.")

    def update_info(self, data):
        self.latest_data = data
        if "warning" in data:
            self.show_warning(data["warning"])
            if not self.detection_thread or not self.detection_thread.running:
                self.stop_tracking()
            return
        self.reset_info_style()
        if data["mode"] == "squat":
            text = (f"<b>Mode:</b> Squat<br>"
                   f"<b>Squat Count:</b> {data['squat_count']}<br>"
                   f"<b>Duration:</b> {data['squat_duration']} sec")
        else:
            text = (f"<b>Mode:</b> Plank<br>"
                   f"<b>Plank Active Time:</b> {data['plank_active_time']} sec<br>"
                   f"<b>Total Time:</b> {data['plank_total_time']} sec")
        self.info_label.setText(text)

    def update_camera(self, q_img):
        pixmap = QPixmap.fromImage(q_img)
        self.camera_label.setPixmap(pixmap.scaled(
            self.camera_label.size(), 
            Qt.KeepAspectRatio, 
            Qt.SmoothTransformation
        ))

    # VOICE LOGIC
    def start_voice_listening(self):
        if self.voice_thread:
            self.stop_voice_listening()
        self.voice_thread = VoiceCommandThread()
        self.voice_thread.commandDetected.connect(self.handle_voice_command)
        self.voice_thread.errorOccurred.connect(self.handle_voice_error)
        self.voice_thread.start()

    def stop_voice_listening(self):
        if self.voice_thread:
            self.voice_thread.stop()
            self.voice_thread = None

    def handle_voice_command(self, command):
        if command == "start" and not self.counting_started:
            self.start_tracking()
        elif command in ["stop", "end"] and self.counting_started:
            self.stop_tracking()

    def handle_voice_error(self, message):
        self.show_error(message)
        self.stop_voice_listening()

    def handle_detection_error(self, message):
        self.show_error(message)
        self.stop_tracking()

    def show_error(self, message):
        self.info_label.setText(f"⚠️ ERROR: {message}")
        self.info_label.setStyleSheet("""
            QLabel {
                font-size: 16px;
                padding: 15px;
                border: 1px solid #ffcccc;
                border-radius: 5px;
                background-color: #ffeeee;
                color: #cc0000;
            }
        """)

    def show_warning(self, message):
        self.info_label.setText(f"⚠️ WARNING: {message}")
        self.info_label.setStyleSheet("""
            QLabel {
                font-size: 16px;
                padding: 15px;
                border: 1px solid #fff3cd;
                border-radius: 5px;
                background-color: #fff3cd;
                color: #856404;
            }
        """)

    def reset_info_style(self):
        self.info_label.setStyleSheet("""
            QLabel {
                font-size: 16px;
                padding: 15px;
                border: 1px solid #ddd;
                border-radius: 5px;
                background-color: #f9f9f9;
                color: black;
            }
        """)


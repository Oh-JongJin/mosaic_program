#!/usr/bin/env python3
#
# Copyright 2021-2022 Sijung Co., Ltd.
#
# Authors:
#     cotjdals5450@gmail.com (Seong Min Chae)
#     5jx2oh@gmail.com (Jongjin Oh)

from multiprocessing import Queue

from PySide6.QtCore import QThread, Signal


class CurveThread(QThread):
    poped = Signal(list)

    def __init__(self, _q: Queue = None):
        super().__init__()
        self.q = _q

    def run(self):
        while True:
            if not self.q.empty():
                data = self.q.get()
                self.poped.emit(data)

    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self.terminate()

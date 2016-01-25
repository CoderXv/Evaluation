__author__ = 'user'
import threading
import time
import mmap
from Point import Point


class VesselFileReader:
    # this class represent all the titleNames and values in the file
    def __init__(self):
        self.fileName = ""
        self.fileType = ""
        self.filePath = ""
        self.rowCount = 0
        self.columnCount = 0
        self.vesselValues = []

       # self.vessel_file_parse_thread = threading.Thread(None, self.do_parse_vessel_file)

    def set_file_path(self, file_path):
        self.filePath = file_path
        # self.do_parse_vessel_file()

        # self.vessel_file_parse_thread.start()
        # self.vessel_file_parse_thread.join()

    def get_filename(self):
        return self.fileName

    def set_filename(self, filename):
        self.fileName = filename

    def get_file_type(self):
        return self.fileType

    def set_file_type(self, file_type):
        self.fileType = file_type

    def get_row_count(self):
        return self.rowCount

    def set_row_count(self, row_count):
        self.rowCount = row_count

    def get_column_count(self):
        return self.columnCount

    def get_point_value_list(self):
        return self.vesselValues

    def get_abscissa_value_at(self, index):
        return self.vesselValues[index].get_x()

    def get_ordinate_value_at(self, index):
        return self.vesselValues[index].get_y()

    def get_iso_value_at(self, index):
        return self.vesselValues[index].get_z()

    def get_radius_value_at(self, index):
        return self.vesselValues[index].get_r()

    def get_err_value_at(self, index):
        return self.vesselValues[index].get_e()

    def get_len_of_vassel_value(self):
        return len(self.vesselValues)

    def do_parse_vessel_file(self):
        # print "ok"
        start = time.time()
        with open(self.filePath, "r+b") as f:
            # memory-mapInput the file, size 0 means whole file
            map_input = mmap.mmap(f.fileno(), 0)

            # read content via standard file methods
            for s in iter(map_input.readline, ""):
                s = s.translate(None, "\r\n")
                # print s
                a_line_of_values = s.split(" ")
                # print a_line_of_values

                point = Point()
                if len(a_line_of_values) == 5:
                    point.set_reference_point(float(a_line_of_values[0]), float(a_line_of_values[1]),
                                              float(a_line_of_values[2]), float(a_line_of_values[3]),
                                              float(a_line_of_values[4]))
                    # print point.get_x()
                elif len(a_line_of_values) == 3:
                    point.set_centerline_point(float(a_line_of_values[0]), float(a_line_of_values[1]),
                                               float(a_line_of_values[2]))
                    # print point.get_x()
                self.vesselValues.append(point)

            map_input.close()
            end = time.time()
            print "Time for completion", end - start

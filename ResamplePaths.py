__author__ = 'user'

class ResamplePaths:
    def __init__(self):
        self.resultPath = []
        # vector of Point
        self.resultRadius = []
        # vector of double
        self.samplingDistance = None
        # should be inited as double

    def set_all_vars(self, result_path, result_radius, sampling_distance):
        self.resultPath = result_path
        self.resultRadius = result_radius
        self.samplingDistance = sampling_distance

    def return_result_path(self):
        return self.resultPath

    def return_radius(self):
        return self.resultRadius

    def resample_operate_two(self, result_path, sampling_distance):
        if sampling_distance == 0.0:
            self.resultPath = result_path
            return

        # clear the result path
        self.resultPath = []

        cur_len = 0.0
        sample_nr = 0
        cur_index = 0

        while cur_index < len(result_path) - 2:
            # resample up to next idx
            result_path[cur_index+1].subtract(result_path[cur_index])
            next_len = cur_len + result_path[cur_index].length()
            while sample_nr * sampling_distance < next_len:
                # linearly interpolate between cur_index at cur_len, and cur_index at next_len
                dist = sample_nr * sampling_distance
                a = next_len / (next_len - cur_len)
                # weight for cur_index
                b = (dist - cur_len) / (next_len - cur_len)
                # weight for cur_index + 1
                append_point_a = result_path[cur_index].multiply_fig(a)
                append_point_b = result_path[cur_index+1].multiply_fig(b)
                append_point = append_point_a.add(append_point_b)
                self.resultPath.append(append_point)
                sample_nr += 1

            cur_len = next_len
            cur_index += 1

        self.resultPath.append(result_path[-1])




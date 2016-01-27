__author__ = 'user'
from VesselFileReader import VesselFileReader
from ResamplePaths import ResamplePaths


def read_scores(filename, overlap_io):
    # overlap_io we can define as an 2d dict
    # reading "observerscores.txt" line by line and store in overlap_io
    with open(filename, "r") as f:

        cpt = 0

        for line in f:
            # list = []
            s = line.translate(None, "\r\n")

            values = s.split(" ")
            ds_nr = int(values[0])
            v = values[2:]

            if cpt is 0:
                overlap_io.append([])
                overlap_io[ds_nr].append(v)
            elif cpt is 4:
                overlap_io.append([])
                overlap_io[ds_nr].append(v)
                cpt = 0
            else:
                overlap_io[ds_nr].append(v)

            cpt += 1
    f.close()


def path_length(list):
    # path is an list which contains a number of point elements
    if len(list) < 2:
        return 0.0
    cumlen = 0.0
    for index, point in enumerate(list):
        list[index - 1].subtract(point)
        # print list[index-1].get_x()
        resample_result = list[index - 1].length()
        # print resample_result
        cumlen += resample_result
        # print cumlen
    return cumlen


# calculate clipping point based on disk at start of reference
def start_cl_from(s, n, rad, cl):
    # s: Point
    # n: Point
    # rad: double
    # cl: vector Point
    start_at = -1
    iter_i = cl[0]
    index = 0
    iter_j = cl[index + 1]
    while start_at < 0 and index < len(cl) - 2:
        iter_i = cl[index]
        iter_j = cl[index + 1]
        # test whether line segment intersects plane of disc
        iter_j.subtract(s)
        fig1 = iter_j.dot(n)
        iter_j.subtract(s)
        iter_j.multiply(n)
        fig2 = iter_j.dot(n)
        if fig1 * fig2 < 0.0:
            # possibly found intersection, linearly interpolate position at disk
            a = fig1
            b = -1.0 * fig2
            iter_i.multiply(b / (a + b))
            iter_j.multiply(a / (a + b))
            pos = iter_i.add(iter_j)

            # test distance of intersection to start pos: should be less than 2 x radius
            pos.subtract(s)
            res = pos.length()
            if res < 2.0 * rad:
                # start_at = int(j - cl.begin())
                start_at = int(index + 1 - 0)
        index += 1

    if start_at >= 0:
        return start_at
    else:
        return 0


def main(ds_nr, vs_nr, file_ref, file_cl, file_observer_scores):
    errcode = 0
    overlap_io = []

    # print overlap_io

    read_scores(file_observer_scores, overlap_io)

    # print overlap_io

    OV_io = overlap_io[ds_nr][vs_nr][0]
    OF_io = overlap_io[ds_nr][vs_nr][1]
    OT_io = overlap_io[ds_nr][vs_nr][2]
    # print OV_io, OF_io, OT_io

    # get the point list of the reference and centerline.
    reference_reader = VesselFileReader()
    reference_reader.set_file_path(file_ref)
    reference_reader.do_parse_vessel_file()
    reference_point_list = reference_reader.get_point_value_list()

    centerline_reader = VesselFileReader()
    centerline_reader.set_file_path(file_cl)
    centerline_reader.do_parse_vessel_file()
    centerline_point_list = centerline_reader.get_point_value_list()

    # define rad and io
    rad = []
    io = []
    for point in reference_point_list:
        rad.append(point.get_r())
        io.append(point.get_e())

    # resample centerline to same sampling as reference standard
    # calculate reference sampling distance
    reference_sampling = path_length(reference_point_list) / (len(reference_point_list) - 1)
    centerline_sampling = path_length(centerline_point_list) / (len(centerline_point_list) - 1)

    print reference_sampling, centerline_sampling
    print reference_sampling / centerline_sampling, reference_sampling / centerline_sampling

    # check if the sampling distance differ more than 0.1%
    if reference_sampling / centerline_sampling < 0.999 or reference_sampling / centerline_sampling > 1.001:
        resampler = ResamplePaths()
        resampler.resample_operate_two(file_cl, reference_sampling)
        centerline_point_list = resampler.return_result_path()
        print "done"

    # clip centerline, based on disk at start of reference.
    # calculate clipping point

    clip_up_to = start_cl_from(reference_point_list[0], reference_point_list[1].subtract(reference_point_list[0]),
                               rad[0], centerline_point_list)


main(0,
     0,
     "C:\Users\user\Desktop\\reference.txt",
     "C:\Users\user\Desktop\\reference.txt",
     "C:\Users\user\Desktop\observerscores.txt")

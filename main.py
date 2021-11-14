# region Namespaces
import pandas as pd
import csv
import plotly.figure_factory as ff
import plotly.express as px
import statistics

# endregion

# region Logic
df = pd.read_csv("data.csv")
height_list = df["math score"].to_list()
weight_list = df["test preparation course"].to_list()

height_mean = statistics.mean(height_list)
weight_mean = statistics.mean(weight_list)

height_median = statistics.median(height_list)
weight_median = statistics.median(weight_list)
print("----------------")
# height_mode = statistics.mode(height_list)
# weight_mode = statistics.mode(weight_list)

print("mean, median and mode of height is {} {} and".format(height_mean, height_median))
print("mean, median and mode of weight is {} {}".format(weight_mean, weight_median))

hgt_sd = statistics.stdev(height_list)
wgt_sd = statistics.stdev(weight_list)

# height
hgt_first_sd_start, hgt_first_sd_end = height_mean - hgt_sd, height_mean + hgt_sd
hgt_second_sd_start, hgt_second_sd_end = height_mean - (2 * hgt_sd), height_mean + (
    2 * hgt_sd
)
hgt_third_sd_start, hgt_third_sd_end = height_mean - (3 * hgt_sd), height_mean + (
    3 * hgt_sd
)

# weight
wgt_first_sd_start, wgt_first_sd_end = weight_mean - wgt_sd, weight_mean + wgt_sd
wgt_second_sd_start, wgt_second_sd_end = weight_mean - (2 * wgt_sd), weight_mean + (
    2 * wgt_sd
)
wgt_third_sd_start, wgt_third_sd_end = weight_mean - (3 * wgt_sd), weight_mean + (
    3 * wgt_sd
)

# percentage of data of height
hgt_list_within_1_sd = [
    result
    for result in height_list
    if result > hgt_first_sd_start and result < hgt_first_sd_end
]
hgt_list_within_2_sd = [
    result
    for result in height_list
    if result > hgt_second_sd_start and result < hgt_second_sd_end
]
hgt_list_within_3_sd = [
    result
    for result in height_list
    if result > hgt_third_sd_start and result < hgt_third_sd_end
]

# percentage of data of weight
wgt_list_within_1_sd = [
    result
    for result in weight_list
    if result > wgt_first_sd_start and result < wgt_first_sd_end
]
wgt_list_within_2_sd = [
    result
    for result in weight_list
    if result > wgt_second_sd_start and result < wgt_second_sd_end
]
wgt_list_within_3_sd = [
    result
    for result in weight_list
    if result > wgt_third_sd_start and result < wgt_third_sd_end
]

print(
    "{}% of data for height lies within 1standard deviation".format(
        len(hgt_list_within_1_sd) * 100 / len(height_list)
    )
)
print(
    "{}% of data for height lies within 2standard deviation".format(
        len(hgt_list_within_2_sd) * 100 / len(height_list)
    )
)
print(
    "{}% of data for height lies within 3standard deviation".format(
        len(hgt_list_within_3_sd) * 100 / len(height_list)
    )
)
print(
    "{}% of data for weight lies within 1standard deviation".format(
        len(wgt_list_within_1_sd) * 100 / len(weight_list)
    )
)
print(
    "{}% of data for weight lies within 2standard deviation".format(
        len(wgt_list_within_2_sd) * 100 / len(weight_list)
    )
)
print(
    "{}% of data for weight lies within 3standard deviation".format(
        len(wgt_list_within_3_sd) * 100 / len(weight_list)
    )
)
# endregion

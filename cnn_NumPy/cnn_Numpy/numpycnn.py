#!/usr/bin/env python3
# coding:utf-8 

import numpy as np
import sys

# CONV operation
def conv(img, conv_filter):

    # test whether the channels match or not
    if len(img.shape) > 2 or len(conv_filter.shape) > 3:
        if img.shape[-1] != conv_filter.shape[-1]:
            print("Error: Number of channels must match.")
            sys.exit()
    
    # test whether the filter is a square shape
    if conv_filter.shape[1] != conv_filter.shape[2]:
        print("Error: Filter must be a square matrix. ")
        sys.exit()

    # test whether filter's edge is an odd number
    if conv_filter.shape[1] % 2 == 0:
        print("Error: Filter must be an odd size")
        sys.exit()

    # Output the conv result
    feature_maps = np.zeros((img.shape[0] - conv_filter.shape[1] + 1,
                             img.shape[1] - conv_filter.shape[1] + 1,
                             conv_filter.shape[0]))

    # do Convolutions 
    for filter_num in range(conv_filter.shape[0]):
        print("Filter ", filter_num + 1)
        curr_filter = conv_filter[filter_num, :]

        """
        Checking if there are mutiple channels for the single filter
        If so, then each channel will convolve the image.
        The result of all convolutions are summed 
            to return a single feature map
        """

        if len(curr_filter.shape) > 2:
            conv_map = conv_(img[:, :, 0], curr_filter[:, :, 0])

            for ch_num in range(1, curr_filter.shape[-1]):
                conv_map += conv_(img[:, :, ch_num], curr_filter[:, :, ch_num])

        else:
            conv_map = conv_(img, curr_filter)

        feature_maps[:, :, filter_num] = conv_map
    
    return feature_maps


def conv_(img, conv_filter):
    filter_size = conv_filter.shape[0]
    height = img.shape[0] - filter_size + 1
    width = img.shape[1] - filter_size + 1
    result = np.zeros((height, width))

    # Looping through the image
    for r in np.uint16(np.arange(0, height)):

        for c in np.uint16(np.arange(0, width)):

            curr_region = img[r: r + filter_size,
                              c: c + filter_size]
            curr_result = curr_region * conv_filter
            conv_sum = np.sum(curr_result)
            result[r, c] = conv_sum

    final_result = result

    return final_result


# ReLU activation function
def relu(feature_map):
    # Initialize the output 
    relu_out = np.zeros((feature_map.shape))
    for map_num in range(feature_map.shape[-1]):
        for r in np.arange(0, feature_map.shape[0]):
            for c in np.arange(0, feature_map.shape[0]):
                relu_out[r, c, map_num] = np.maximum(0, feature_map[r, c, map_num])
    return relu_out


# Pooling Layer
def pooling(feature_map, size=2, stride=2):
    # Initialize the output 
    pool_out = np.zeros((np.uint16((feature_map.shape[0] -size + 1)/stride),
                         np.uint16((feature_map.shape[1] -size + 1)/stride),
                         feature_map.shape[-1]))
    for map_num in range(feature_map.shape[-1]):
        r_index = 0
        for r in np.arange(0, feature_map.shape[0] - size - 1, stride):
            c_index = 0
            for c in np.arange(0, feature_map.shape[1] - size - 1, stride):
                pool_out[r_index, c_index, map_num] = np.max(feature_map[r: r + size, c: c + size])
                c_index += 1
            r_index += 1
    return pool_out




        
































#!/usr/bin/env python3
#############################################################################
# @file camera-test.py
# @author suhayl@freenove (support@freenove.com)
# @brief Buzzer service.
# @version v1.0.0
# @date 2023-3-29
# 
# @copyright Copyright (c) 2023. Freenove corporation.
########################################################################

import cv2

def gstreamer_pipeline(
    capture_width=640,
    capture_height=480,
    display_width=640,
    display_height=480,
    framerate=30,
    flip_method=0,
    ):
    return (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )
    
cap = cv2.VideoCapture(gstreamer_pipeline(flip_method=2), cv2.CAP_GSTREAMER)
while (cap.isOpened()):
    
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(50) >= 0:
        break

cap.release()
cv2.destroyAllWindows()

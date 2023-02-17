"""module to decode images of a video"""
# importing the necessary libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
# from math import abs


# Creating a VideoCapture object to read the video
cap = cv2.VideoCapture('Reports/Reports_Nino_Mulac/images_and_videos_for_reports/temp_fishe/new/vid1.mp4')
show = False
print(cap)
i=1
for _ in range(1520):
    i+=1
    cap.read()
# Loop until the end of the video
list_deltas = []
list_diffs = []
list_last_pos = []
list_last_pos_shell = [0]
list_diffs_shell = []
for i in tqdm(range(1520,2016)):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # frame = cv2.resize(frame, (540, 380), fx=0, fy=0,
                    #    interpolation=cv2.INTER_CUBIC)

    # Display the resulting frame

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # find the colors within the boundaries
    mask2 = cv2.inRange(rgb, np.array([100, 0 , 0]), np.array([255, 90, 90]))
    ret,thresh = cv2.threshold(mask2,127,255,0)
    contours, _ = cv2.findContours(thresh, 1, 2)
    # print(contours[0])
    # print(f"len contours: {len(contours)}")
    # print(f"type of contours[0]: {type(contours[0])}")
    list_contours = []
    list_contours2 = []
    # a=1
    for cnt in contours:
        # print(cv2.arcLength(cnt,True))
        # print("a wild contour appeared!")
        area = cv2.contourArea(cnt)
        if area > 100:
            list_contours.append(cnt)
        # print(area)
        # if int(cv2.arcLength(cnt,True)) in range(180,210) and int(area) in range(1000, 1500):
        if area>1300:
            # cv2.drawContours(frame, [cnt], 0, (0, 255-50*a, 0), 3)
            list_contours2.append(cnt)
            # a+=1
            # print(f"passed : {area}+ arclength : {cv2.arcLength(cnt,True)}")
        # elif area > 100:
            # cv2.drawContours(frame, [cnt], 0, (255, 0, 0), 3)
            # print(f"failed : {area}+ arclength : {cv2.arcLength(cnt,True)}")
    
    p1=min(list_contours, key=lambda x : x[0][0][1])
    p2=min(list_contours2, key=lambda x : x[0][0][1])
    lowest_p1 = max(p1, key=lambda x : x[0][1]+x[0][0])
    highest_p2 = min(p2, key=lambda x : x[0][1]+x[0][0])
    # print(highest_p2)
    # plt.plot(np.array(lowest_p1[0])-np.array(highest_p2[0]))
    # plt.show()
    # plt.pause(0.05)
    list_deltas.append(((np.array(lowest_p1[0])-np.array(highest_p2[0]))+47+75))
    list_last_pos_shell.append(lowest_p1[0][0])
    list_diffs_shell.append(list_last_pos_shell[-1]-list_last_pos_shell[-2])

    cv2.drawContours(frame, [p1], 0, (0, 0, 255), 3)
    cv2.drawContours(frame, [p2], 0, (255, 0, 0), 3)
    frame = cv2.circle(frame, (lowest_p1[0][0], lowest_p1[0][1]), 5, (0, 255, 0), -1)
    frame = cv2.circle(frame, (highest_p2[0][0], highest_p2[0][1]), 5, (0, 255, 0), -1)

    mask3 = cv2.inRange(rgb,np.array([150, 150, 150]),np.array([255, 255, 255]))
    if show:cv2.imshow('Thresh', mask3)
    
    contours2, _ = cv2.findContours(mask3, 1, 2)
    listcontours3 = []
    for cnt in contours2:
        area = cv2.contourArea(cnt)
        if area > 20 and area < 200:
            if cnt[0][0][1] in range(37,200):
                cv2.drawContours(frame, [cnt], 0, (0, 255, 0), 3)
                listcontours3.append(cnt)
    tmplist = []
    for cnt in listcontours3:
        # list_diffs.append(list_last_pos)
        tmplist.append(cnt[0][0])
        frame = cv2.circle(frame, (cnt[0][0][0], cnt[0][0][1]), 5, (0, 255, 255), -1)
    list_last_pos.append(np.array(tmplist,dtype=object))
    # # for cnt in contours:

    # try:
    #     area = cv2.contourArea(cnt)
    #     if area > 100:
    #         cv2.drawContours(mask2, [cnt], 0, (0, 255, 0), 3)
    # except Exception:
    #     print("AssertionError")
    #     continue
    if show:cv2.imshow('Frame', frame)

    # cv2.imshow('Thresh', mask2)
    # define q as the exit button
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
    # print("img shown"+str(i))
    i+=1
# print(list_deltas)
# print(list_last_pos)
# input()
# release the video capture object
cap.release()
# Closes all the windows currently opened.
cv2.destroyAllWindows()
plt.plot([x[1] for x in list_deltas])
lx=[]
ly=[]
lsi=[]
lsii=[]
lsiii=[]

print(len(list_last_pos))
for index,j in tqdm(enumerate(list_last_pos)):
    # si=0
    for i in j:
        # si+=i[0]
        if len(lsi)==len(j):
            lsii.append(sum(np.array(lsi)-np.array(j))/len(lsi)-list_diffs_shell[index])
            lsiii.append(index)
        lx.append(index)
        ly.append(i[0])
    lsi = j[:]
# print(lsiii)
kernel_size = 1
kernel = list(range(1,kernel_size+1))
data_convolved = np.convolve([x[0] for x in lsii], kernel, mode='same')
print(len(data_convolved))
for i in range(len(data_convolved)):
    data_convolved[i] = data_convolved[i]/kernel_size
    if abs(data_convolved[i])>300:
        data_convolved[i]=0

smooth_size=37
l2=[]
for i in range(len(data_convolved)):
    l2.append(sum(data_convolved[max(0,i-smooth_size):min(i+smooth_size,len(data_convolved))])/2/smooth_size)

# plt.plot(lx,ly,marker = "o", linestyle = " ")
plt.plot(lsiii,data_convolved,"green")
plt.plot(lsiii,l2,"red")
plt.plot(list_diffs_shell,"purple")
plt.show()
print(len(l2))
print(len(list_deltas))

print("done")
# input()

import cv2

cap = cv2.VideoCapture('data/ac_milan_sample.mp4')

fps = cap.get(cv2.CAP_PROP_FPS) # get frames per second
wait_time = int(1000 / fps) # calculate wait time between frames in milliseconds
print(f'Frames per second: {fps}, Wait time between frames: {wait_time} ms')

while(cap.isOpened()):
    ret, frame = cap.read() # read each frame

    if ret == True: # if there is a frame to read, continue
        
        frame = cv2.resize(frame, (1200, 700)) # resize the frame
        cv2.imshow('Frame', frame) # show the frame

        if cv2.waitKey(wait_time) & 0xFF == ord('q'): # if user presses 'q', quit
            break
    else:
        print('Frame reading failed, exiting loop')
        break

cap.release() # release the video capture object
cv2.destroyAllWindows() # close all OpenCV windows
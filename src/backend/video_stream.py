import cv2

def start_video_stream():
    """
    Start webcam or drone video stream.
    """

    cap = cv2.VideoCapture(0)

    while True:

        # Read frame
        success, frame = cap.read()

        if not success:
            break

        # Display frame
        cv2.imshow("Video Stream", frame)

        # Press Q to exit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

import cv2, numpy as np, mediapipe as mp, onnxruntime as ort

EMOTIONS = ["angry","disgust","fear","happy","neutral","sad","surprise"]


session = ort.InferenceSession("models/emotion.onnx", providers=['CPUExecutionProvider'])
mp_face = mp.solutions.face_detection.FaceDetection(0.5)

def detect_mood():
    cap = cv2.VideoCapture(0)
    mood = "neutral"

    while True:
        ok, frame = cap.read()
        if not ok: break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        res = mp_face.process(rgb)

        if res.detections:
            d = res.detections[0]
            box = d.location_data.relative_bounding_box
            h,w,_ = frame.shape
            x1=int(box.xmin*w); y1=int(box.ymin*h)
            x2=int((box.xmin+box.width)*w)
            y2=int((box.ymin+box.height)*h)
            face = frame[y1:y2,x1:x2]

            if face.size>0:
                gray=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                gray=cv2.resize(gray,(48,48))
                gray=gray.astype(np.float32)/255.0
                inp=gray[None,None]
                pred=session.run(None,{"input":inp})[0]
                mood=EMOTIONS[int(np.argmax(pred))]

            cv2.putText(frame,mood,(x1,y1-10),0,1,(0,255,0),2)
            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)

        cv2.imshow("Mood",frame)
        if cv2.waitKey(1)&0xFF==ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return mood

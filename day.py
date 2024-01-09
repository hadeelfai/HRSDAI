import cv2

# تهيئة مُعرف الكاميرا
camera = cv2.VideoCapture(0)

# تهيئة مُكتشف الوجه
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    # قراءة الإطار الحالي من الكاميرا
    ret, frame = camera.read()

    # تحويل الإطار إلى اللون الرمادي
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # اكتشاف الوجوه في الإطار الرمادي
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # رسم مربع حول الوجوه المكتشفة
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # عرض الإطار المعالج
    cv2.imshow('Face Detection', frame)

    # انتظار الضغط على مفتاح 'q' لإيقاف البرنامج
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# إغلاق الكاميرا وتدمير النوافذ المفتوحة
camera.release()
cv2.destroyAllWindows()
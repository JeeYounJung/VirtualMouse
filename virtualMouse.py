import cv2
import mediapipe as mp
import pyautogui
from pynput.keyboard import Controller, Key, Listener
import subprocess
from selenium import webdriver 

chrome = None

def kcuHomePage():
    global chrome
    # Initialize webdriver only if it hasn't been initialized yet
    if chrome is None:
        chrome = webdriver.Chrome()
        chrome.get("http://kcu.o-r.kr/")


def simulate_pb():
    keyboard = Controller()
    keyboard.press(Key.f4)
    keyboard.release(Key.f4)
    subprocess.run(["open", "-a", "Photo Booth"])

cam = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()
index_y = 0
while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _= frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    output2 = hand_detector.process(rgb_frame)
    hands = output2.multi_hand_landmarks
    landmark_points = output.multi_face_landmarks
    if landmark_points:
        landmarks = landmark_points[0].landmark
        for id, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_width)
            y = int(landmark.y * frame_height)
            # cv2.circle(frame, (x, y), 3, (0, 255, 0))
            cv2.circle(frame, (x, y), 3, (0, 255, 0))
            if id == 0:
                screen_x = screen_w * landmark.x
                screen_y = screen_h * landmark.y
                # screen_x = screen_w/frame_width * x
                # screen_y = screen_h/frame_height * y
                pyautogui.moveTo(screen_x, screen_y)
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)
                if id == 8:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    index_x = screen_w/ frame_width * x
                    index_y = screen_h/ frame_height * y
                if id == 4:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    thumb_x = screen_w/ frame_width * x
                    thumb_y = screen_h/ frame_height * y
                    if abs(index_y - thumb_y) < 25:
                        cv2.circle(img=frame, center=(x,y), radius=25, color=(255,255,255))
                        cv2.circle(img=frame, center=(x,y), radius=24, color=(255,255,255))
                        cv2.circle(img=frame, center=(x,y), radius=20, color=(255,255,255))
                        cv2.circle(img=frame, center=(x,y), radius=19, color=(255,255,255))
                        cv2.circle(img=frame, center=(x,y), radius=18, color=(255,255,255))
                        cv2.circle(img=frame, center=(x,y), radius=17, color=(255,255,255))
                        cv2.circle(img=frame, center=(x,y), radius=16, color=(255,255,255))
                        pyautogui.click()
                        pyautogui.sleep(0.3)
                if id == 20:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    last_x = screen_w/ frame_width * x
                    last_y = screen_h/ frame_height * y
                    if abs(thumb_y - last_y) < 10:
                        cv2.circle(img=frame, center=(x,y), radius=25, color=(255,255,255))
                        cv2.circle(img=frame, center=(x,y), radius=24, color=(255,255,255))
                        cv2.circle(img=frame, center=(x,y), radius=20, color=(255,255,255))
                        cv2.circle(img=frame, center=(x,y), radius=19, color=(255,255,255))
                        cv2.circle(img=frame, center=(x,y), radius=18, color=(255,255,255))
                        cv2.circle(img=frame, center=(x,y), radius=17, color=(255,255,255))
                        cv2.circle(img=frame, center=(x,y), radius=16, color=(255,255,255))
                        pyautogui.rightClick()
                        pyautogui.sleep(0.3)

            scroll_speed = 14
            first = landmarks[8]
            second = landmarks[12]
            third = landmarks[16]
            last = landmarks[20]
            first2 = landmarks[5]
            second2 = landmarks[9]
            third2 = landmarks[13]
            last2 = landmarks[17]

            first_y = first.y * frame_height
            first2_y = first2.y * frame_height
            second_y = second.y * frame_height
            second2_y = second2.y * frame_height
            third_y = third.y * frame_height
            third2_y = third2.y * frame_height
            last_y = last.y * frame_height
            last2_y = last2.y * frame_height
            

            if first_y > first2_y and second_y > second2_y and third_y > third2_y and last_y > last2_y:
                pyautogui.scroll(-scroll_speed)
                pyautogui.sleep(0.2)
                # screen_shot = pyautogui.screenshot()
                # screen_shot.save(r"/Users/jeeyounjung/Desktop/DS_Project/screenshot.png")
            if first_y < first2_y and second_y > second2_y and third_y > third2_y and last_y > last2_y:
                pyautogui.scroll(scroll_speed)
                pyautogui.sleep(0.2)
            if first_y < first2_y and second_y < second2_y and third_y > third2_y and last_y > last2_y:
                first_x = first.x * frame_width
                second_x = second.x * frame_width
                if abs(first_x - second_x) > 350:
                    simulate_pb()

            
            hand_center_x = 0
            hand_center_y = 0
            for landmark in landmarks:
                hand_center_x += landmark.x
                hand_center_y += landmark.y
            hand_center_x /= len(landmarks)
            hand_center_y /= len(landmarks)
            
            thm = landmarks[4]
            thm_y = thm.y * frame_height
            thm_x = thm.x * frame_height

            # 화면의 가로 중간을 기준으로 왼손과 오른손을 구분
            if hand_center_x < 0.5:
                # 왼손 처리
                left_hand_center = (hand_center_x, hand_center_y)
                thm_r = thm_x
            else:
                # 오른손 처리
                right_hand_center = (hand_center_x, hand_center_y)
                thm_l = thm_x
            
            if first_y < first2_y and second_y > second2_y and third_y > third2_y and last_y > last2_y and abs(thm_r - thm_l) < 5:
                if chrome is None:
                    kcuHomePage()

    cv2.imshow("Virtual Mouse", frame)
        # 왼쪽 눈 깜박이면 클릭
        # left = [landmarks[145], landmarks[159]]
        # for landmark in left:
        #     x = int(landmark.x * frame_w)
        #     y = int(landmark.y * frame_h)
        #     cv2.circle(frame, (x, y), 3, (0, 255, 255))
        # if (left[0].y - left[1].y) < 0.004:
        #     pyautogui.click()
        #     pyautogui.sleep(1)

    cv2.imshow('Eye Controlled Mouse', frame)
    cv2.waitKey(1)
    
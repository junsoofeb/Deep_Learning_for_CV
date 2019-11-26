# text_detection

## EAST.cpp
An Efficient and Accurate Scene Text Detector (EAST) 예제 프로그램

## frozen_east_text_detection.pb 파일 다운로드 링크
<https://github.com/oyyd/frozen_east_text_detection.pb>

## EAST.cpp 기본적인 사용법

opencv_project.exe -i=이미지 파일경로 -m=.pb 파일 경로  
-i 옵션 안주면 웹캠으로 찍은 이미지로 돌아가고, -m 옵션은 반드시 필요

## visual studio에서 main함수에 인수 주는 방법

alt + F7 -> 구성 : 활성 으로 선택 후 -> 구성 속성에서 디버깅 선택 -> 명령 인수에 작성

## 예시
![image](https://user-images.githubusercontent.com/46870741/69663063-d8801e00-10c8-11ea-99db-d6022665fc21.png)


## text_detection.py

미리 훈련된 컨볼루션 신경망을 이용해 텍스트 검출하는 프로그램

threshold 값이 작을수록 작은 글자를 잘 찾는다.

## 실행 결과

![cv1](https://user-images.githubusercontent.com/46870741/69332577-55ab2d80-0c9a-11ea-8658-1ce0bc55e7a9.png)

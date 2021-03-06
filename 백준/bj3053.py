'''
유클리드 기하학
- 두 점사이 거리 - ((x1-x2)^2 + (y1-y2)^2)^1/2
- 원 넒이 - ((0-x2)^2 + (0-y2)^2)*3.14
비유클리드 기하학 : 택시 기하학
- 두 점 사이 거리- |x1-x2| + |y1-y2|
- 원 넓이 - (|0-x2| + |0-y2|)^2*2? 유추해서 알아냄.. 왜 일까 *2는

'''
import math

#입력: 반지름 길이
r = int(input())

#계산,출력: 유클리드, 비유클리드
print("%.6f"%(r**2*math.pi))
print("%.6f"%(r**2*2))

'''
원의 넓이 공식을 in output의 추론으로 알아냈지만..
좌표를 그려서 그림으로 알아내는 방법도 있다.(마름모꼴)
하지만 내 방법이 꼭 틀린 것은 아니라고 생각한다.
결국 두 점 사이의 거리만 비유클리드 기하학이 적용되는 것이고,
나머지는 유클리드 기하학이 적용되는 것인데,
원의 넓이는 두 점사이의 거리^2 * 원주율인데
이 원주율이라는 것은 원의 지름에 대한 둘레의 비율인데 이는 비유클리드에서는 다르게 적용될 수 있따.
왜냐하면 지름자체가 매 점마다 같지 않을 경우가 있기 때문이다.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
각설하고, 그냥 수학코딩문제도 수학문제 풀 때처럼 그림을 그려서 생각해 보는게 좋을 것 같다.
+++ 그리고.. 아래 위키출처보면  비유클리드의 원 넓이가 마름모인게 나와있다.. 출처 제대로보자.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
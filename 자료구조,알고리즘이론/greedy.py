'''
1. 그리디 알고리즘:
0) " 1) 기준, 2) 정렬 " 에 대한 명확한 기준을 세우자
1) 현 상황에서 당장 좋은 것만 고르기(나중일은 신경 ㄴㄴ) -> 항상 최적의 해를 갖는 것이 아님
2) "좋은 것"이라는 건 "기준"이 존재한다는 것. 이런 기준을 제시하는 경우가 많음
3) "기준"은 정렬로 해결가능한 경우가 많음.
'''

'''
예시 1. 동전 거슬러주기
시간 복잡도: coins(동전 종류)와 같다 O(coins)
'''

w = int(input())  # 받은 돈

coins = [500, 100, 50, 10]  # 거슬러줄 동전 종류들 (개수는 무한)
count=0 # 동전 개수

for i in coins: # 동전 종류 하나씩 돌면서
    count+=w//i # 필요 동전 수 만큼 저장
    w-=(w//i)*i # 그 동전만큼 받은 금액에서 차감, 그냥 w%=i를 사용하는 것도 괜찮다.

print(count)

'''
실전 1

idea:
1. 어차피 두 수로만 만들어진다(가장 큰, 작은)
2. 가장 큰 수를 k만큼 그리고 한 번 두 번째로 큰 수 쓰고 다시 가장 큰수 . 즉 1112 1112 이런식의 진행이다

learn:
1. 최대,최소값을 찾는 건 max,min으로 되지만, 특정 요소를 찾는 건 정렬로하는 것이 편하다
2. 일정한 규칙으로 반복되는 경우는 반복문 보다는 //,%등의 기호를 이용하여 더 빠른 연산을 가능케 할 수 있다. 반복되는 규칙에 유의하자.
3. 전체값 - 특정값 = ? 라는 원리를 생각해보자. 
'''

n, m, k = map(int, input().split())  # 입력

l1 = list(map(int, input().split()))  # 배열 입력

l1.sort(reverse=True)  # 가장큰, 두 번째로 큰 값 구하기 위해 역순 정렬

# 가장 큰 값 더하기
count = (m // (k + 1)) * k  # 반복되는 성질 이용. 1은 두 번째로 큰 값
count += m % (k + 1)  # 나머지 큰 값 횟수들. 두 번째 큰 값이 마지막에 하나만 들어간다는 점을 이용

result = l1[0] * count + l1[1] * (m - count)

print(result)


'''
실전2

idea
1. greedy:
1)기준: 행 탐색- "가장 작은 값" => 
그 중 가장 큰 값
'''

n,m=map(int,input().split())

l1=[] # 받는 리스트
rl=[] # 각 행별 최소값 리스트

# 리스트 입력
for i in range(n):
  a=input().split()
  l1.append(a)

# 각 행 별 최소값 입력
for i in range(n):
  for j in range(m):
    rl.append(min(l1[i]))

# 그 입력값중 최대값
print(max(rl))

'''
실전3

idea 
1. greedy
1)기준:  두 가지 연산 방법에 따라 계산
1> 2번째(나누기)가 연산을 줄이는데 있어 더 효율적
따라서 가능한 2번방법쓰되 안되면 1번쓰는 방향으로

learn
1. 제발 for문의 i 부분 헷갈리지말고 제대로 쓰자
'''

n, k = map(int, input().split())
count = 0  # 총 계산 횟수

for n in range(n, 0, -1):  # 1번째 계산. 2번째가 안되면 자동적으로 -1
    # 2번째 계산. 되면 될 때까지 2번째 계산
    while True:
        if n % k == 0:
            n //= k
            count += 1
        else:
            break
    # 1되면 탈출
    if n == 1:
        break
    # 1번째 계산 되면서 카운트 up
    count += 1

print(count)  # 카운트 출력

'''
실전3
=>1중 반복문 이용, 차감반복회수(-1)줄임
learn
1. 몫*? 으로 나누어떨어지는 수 표현 가능
2. 기능의 구현도 좋다.
하지만 더 줄여야 할 경우
기능의 구현에 더해서,
기능의 흐름(1쫙 빼내며 나누다가->나중에 빼기)도 잘 파악할 것

'''

n, k = map(int, input().split())
count = 0  # 총 계산 횟수

while True:
    # 1+2계산!나누어 떨어지는 수로 만들기.떨거지 1더하기
    tmp = (n // k) * k
    count += n - tmp
    n = tmp
    # 2계산되나? 나누고 남은 수가 k보다 작으면 break
    if n < k:
        break

    # 2계산! 또 나눌 수 있으면 count up
    count += 1
    n //= k

# 1계산! 이제 더 나누지 못해서 떨어져 나온수에 1들을 더함
count += (n - 1)

print(count)
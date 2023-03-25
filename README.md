Baekjoon
========
#### 2023-03-21
---------------
## **Greedy**
* 2839 (설탕 배달)
* 11047 (동전 0)
* 11399 (ATM)

#### 2023-03-22
---------------
## **Implement** 
* 2920 (음계)
* 7287 (다이얼)
  + ###### 아스키 코드를 사용하여 접근했지만 문자의 개수가 균일하지 않은 문제 때문에, 오히려 코드가 맛이 없어짐
  ```
  if(ord(word[i]) < 80) :
        sum += (ord(word[i]) % ord('A')) // 3 + 3
    elif word[i] in ['P','Q','R','S'] :
        sum += 8
    elif word[i] in ['T','U','V'] :
        sum += 9
    else : 
        sum += 10
  ```
  ###### **아스키 코드를 사용하거나 배열을 사용하거나, 한 가지 방식으로 푸는 것이 코드를 이해하기 좋아보임**
* 25304 (영수증)

#### 2023-03-23
---------------
## **DFS**
* 2667 (단지번호 붙이기)
* 4963 (섬의 개수)
    + ##### 만일 RecursionError가 발생한다면, 파이썬은 재귀 깊이가 정해져 있어서 의도적으로 늘려줘야한다.
    ``` 
    import sys
    sys.setrecursionlimit(10**4)
    ```
* 10026 (적록색약)
    + ##### **2차원 배열을 새롭게 copy 할 때**
    ##### 1. copy 모듈의 deepcopy() 사용

    ```
    import copy
    board2 = copy.deepcopy(board1)
    ```
    
    ##### 2. list slicing

    ```
    board2 = [arr[:] for arr in board1]
    ```
    ##### slicing이 deepcopy보다 간단하고 시간도 더 빠르다고 한다.
    #####  **slicing을 사용하도록 하자....**

#### 2023-03-24
---------------
## **BFS**
#### **최단경로를 찾는 문제에서 BFS를 사용하도록 하자**
#### 방문한 노드들을 차례대로 관리할 수 있는 **큐(Queue)** 를 사용. 즉, 선입선출(FIFO)을 원칙으로 탐색한다.

* 2178 (미로 탐색)
* 2644 (촌수계산)
* 7562 (나이트의 이동) <br>
#### 간혹 문제를 풀고 숏코딩을 보면 2차원 배열을 선언할때 **eval()** 함수를 사용하는 걸 볼 수 있다. 보기에는 간편할지라도
    __import__('os').system('ls /')
#### 다음과 같은 입력을 했을 때, 서버의 root 디렉토리의 정보가 그대로 노출되는 취약점을 가지고 있다. 

#### 2023-03-25
---------------
## **Sorting**
##### 1. 문제를 풀다가 시간 초과가 나는 경우는 **input()** 이 너무 느려서 그런거니 
    import sys
    input = sys.stdin.readline
##### **sys 모듈** 을 이용해서 입력을 받으면 시간 제한에 걸리지 않는다.
##### 2. 내장메소드인 **sort()** 는 merge sort와 insertion sort를 조합한 **Tim sort 알고리즘** 을 사용하며 최악의 경우에도 O(n log n)의 시간 복잡도를 가진다. 

* 1764 (듣보잡) <br>

    ##### 제너레이터와 컴프리헨션을 사용하여 정답만 담아 올 수 있다.
    ```
    (str(input()) for _ in range(M))
    ```
    ###### M 개의 문자열을 입력받는 제너레이터
* 5635 (생일)
    ##### 년 월 일 순으로 정렬할 때 이런 방법도 있다.
    ```
    info.sort(key = lambda x : (int(x[3]), int(x[2]), int(x[1])))
    ```
* 11650 (좌표 정렬하기)

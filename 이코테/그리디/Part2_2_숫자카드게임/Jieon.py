import sys
#data 받기
N,M=map(int,sys.stdin.readline().split())
data=[] #카드정보 수집
for i in range(N):
    data.append(min(map(int,sys.stdin.readline().split()))) #행 중 가장 작은 수만 저장

print(max(data)) #가장 큰 수 선택


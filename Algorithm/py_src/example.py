from collections import deque
import sys
import os

file_path = os.path.join(os.path.dirname(__file__), "example.txt")
sys.stdin = open(file_path, "r")

# 백준 입력값 처리
N, M, K = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]


def solution(N, M, K, board):
    print(N, M, K, board)
    return -1


print(solution(N, M, K, board))

def solution(number: int) -> int:
    return sum({x for x in range(3, number) if x % 3 == 0 or x % 5 == 0})

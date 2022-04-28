from typing import List
import math

Vector = List[float]


def add(v: Vector, w: Vector) -> Vector:
    """sum of vectors"""
    assert len(v) == len(w), "vectors should have same len!"

    return [v_i + w_i for v_i, w_i in zip(v, w)]


def substract(v: Vector, w: Vector) -> Vector:
    """substract elements"""
    assert len(v) == len(w), "vectors should have same len"

    return [v_i - w_i for v_i, w_i in zip(v, w)]


def vector_sum(vectors: List[Vector]) -> Vector:
    """sum elements of vectors"""
    assert vectors, "vectors are not exist!"

    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "vectors should have same len!"

    return [sum(vector[i] for vector in vectors) for i in range(num_elements)]


def scalar_multiply(c: float, v: Vector) -> Vector:
    """Multiply vector with float"""
    return [c * v_i for v_i in v]


def vector_mean(vectors: List[Vector]) -> Vector:
    """calculates the arithmetic mean"""
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))


def dot(v: Vector, w: Vector) -> float:
    """v[1] * w[1] + ... +v[i] * w[i]"""
    assert len(v) == len(w), "vectors should have same len!"

    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def sum_of_squares(v: Vector) -> float:
    return dot(v, v)


def magnitude(v: Vector) -> float:
    return math.sqrt(sum_of_squares(v))


def distance(v: Vector, w: Vector) -> float:
    return magnitude(substract(v, w))


assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]

assert substract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]

assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]

assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]

assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]

assert dot([1, 2, 3], [4, 5, 6]) == 32

assert sum_of_squares([1, 2, 3]) == 14

assert magnitude([1, 2, 2]) == 3

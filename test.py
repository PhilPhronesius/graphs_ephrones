import pytest
from graphs_ephrones.sp import dijkstra

@pytest.fixture
def graph():
    return {
        0: {1: 4, 7: 8},
        1: {0: 4, 2: 8, 7: 11},
        2: {1: 8, 3: 7, 5: 4},
        3: {2: 7, 4: 9},
        4: {3: 9, 5: 10},
        5: {2: 4, 4: 10, 6: 2},
        6: {5: 2, 7: 1, 8: 6},
        7: {0: 8, 1: 11, 6: 1, 8: 7},
        8: {6: 6, 7: 7}
    }

def test_dijkstra(graph):
    distances, path = dijkstra(graph, 0)
    assert distances[0] == 0
    assert distances[1] == 4
    assert distances[2] == 12
    assert distances[3] == 19
    assert distances[4] == 21
    assert distances[5] == 11
    assert distances[6] == 9
    assert distances[7] == 8
    assert distances[8] == 15
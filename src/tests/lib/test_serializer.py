import pytest
from lib.serializer import serialize

class Setup:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def test_serializing_an_object_with_ints():
    newObject = Setup(3, 4)
    assert serialize(newObject) == '{"x": 3, "y": 4}'

def test_serializing_an_object_with_strings():
    newObject = Setup("string1", "string2")
    assert serialize(newObject) == '{"x": "string1", "y": "string2"}'

def test_serializing_a_list_of_objects():
    objectList = []
    newObject1 = Setup(3, "cats")
    newObject2 = Setup(5, "dogs")
    objectList.append(newObject1)
    objectList.append(newObject2)
    assert serialize(objectList) == '[{"x": 3, "y": "cats"}, {"x": 5, "y": "dogs"}]'
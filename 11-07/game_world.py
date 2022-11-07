# objects[0] : 바닥 계층
# objects[1] : 상위 계층
objects = [[], []]

def add_object(o, depth):
    objects[depth].append(o)

def remove_object(o):
    for layer in objects:
        if o in layer: # o 객체, layer 계충 == depth
            layer.remove(o)
            del o
            break
    # objects.remove(o) # 리스트에서 뺀다.
    # del o # 메모리에서 날려준다.

def all_objects():
    for layer in objects:
        for o in layer:
            # Genertator, 호출한 사람에게 모든 object를 하나씩 넘겨준다
            # for문과 연동해서 쓴다.
            yield o # 제너레이터, 모든 객체들을 하나씩 넘겨준다

def clear():
    for o in all_objects():
        del o
    for layer in objects:
        layer.clear()


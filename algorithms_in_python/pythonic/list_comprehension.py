
import json

# https://www.tutorialspoint.com/gensim/index.htm
# https://www.tutorialspoint.com/gensim/gensim_quick_guide.htm

# topic distribution converted to  json.
# The problem is that json can not comvert float32.

td = [
    [(0, 1.0)],
    [(0, 0.8734379353188121), (1, 0.4869354917707381)],
    [(2, 0.5773502691896257), (3, 0.5773502691896257), (4, 0.5773502691896257)],
    [(1, 0.3667400603126873), (5, 0.657838022678017), (6, 0.657838022678017)],
    [(1, 0.19338287240886842), (2, 0.34687949360312714), (3, 0.6937589872062543),
    (4, 0.34687949360312714), (5, 0.34687949360312714), (6, 0.34687949360312714)
    ]]
# This converts the float32 arrays to string

z = [ [ {j[0]: str(j[1])} for j in i ] for i in td ]
print(json.dumps(z))
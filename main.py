# import pandas as pd
# data = [10, 20, 30, 40]
# s = pd.Series(data, index=['a', 'b', 'c', 'd'], name='numbers')
# print(s)
import pandas as pd

data = {'animals': ['cat', 'dog', 'snake'],
        'age': [2, 3, 4],
        'visits': [1, 5, 2],
        'priority': ['yes', 'yes', 'no']}
labels = ['a', 'b', 'c']

df = pd.DataFrame(data, index=labels)
print(df)
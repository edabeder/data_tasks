import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)
obj = pd.read_pickle('data.pkl')
obj.to_pickle("data.pkl")

my_dictionary = {
    1: "split squat",
    2: "SL squat",
    3: "SL BW Decel",
    4: "SL prone curls",
    5: "SL glute bridge",
    6: "SL elevated glue bridge",
    7: "45deg adductor squeeze",
    8: "0deg adductor squeeze",
    9: "copenhagen",
    10: "SL straight knee calf raise"
}

cnt = 0

for i in range(len(obj) - 1):
    if obj.iloc[i]['task'] == 0 and obj.iloc[i + 1]['task'] == 1:
        cnt += 1
    elif obj.iloc[i]['task'] == 1:
        obj.at[i, "task"] = my_dictionary[cnt]

a = obj['task'].str.split(expand=True).stack().value_counts().reset_index(name='count') \
    .sort_values(['count'], ascending=False)

print('Edited table:')
print(obj)

print()
print('Word count: ')
print(a)

ax = a.plot.bar(x='index', y='count', rot=0)
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

students=[('Alice', 85), ('Bob', 90), ('Charlie', 78)]
ranked = sorted(students,key=lambda x: x[1])
print(ranked)

str1=['apple','banana','cherry','date','elderberry']
res=sorted(str1,key=lambda x: len(x))
print(res)
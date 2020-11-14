# a = [{
#     "uid": node["uid"],
#     "group": 1
# } for (node, i) in enumerate([{
#     "uid": 1
# }, {
#     "uid": 2
# }])]
# pip freeze > requirements.txt
a = [{
    "uid": node["1id"],
    "group": 1
} for (node, i) in enumerate([{
    "uid": 1
}, {
    "uid": 2
}])]
print(a)
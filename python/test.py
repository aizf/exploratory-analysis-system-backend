# a = [{
#     "uid": node["uid"],
#     "group": 1
# } for (node, i) in enumerate([{
#     "uid": 1
# }, {
#     "uid": 2
# }])]

a = [{
    "uid": node["1id"],
    "group": 1
} for (node, i) in enumerate([{
    "uid": 1
}, {
    "uid": 2
}])]
print(a)
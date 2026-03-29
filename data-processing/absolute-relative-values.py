def covtoabsolute (sym):
    div = []
    for i in sym:
        x = i / 100
        div.append(x)
    return div
    

def abs_to_rel(list, div):
    list_abs = []
    j = 0
    for i in list:
        x = i * div[j]
        list_abs.append(x)
        j += 1
    return list_abs


nv = [7.6, 7.6, 24.5, 26.6, 9.0, 5.2, 2.6, 1.8, 1.4, 1.4]

fatigue = [52, 52, 65, 64, 47, 47, 35, 30, 62, 62]
headache = [7, 7, 8, 12, 15, 17, 17, 18, 17, 17]
sleep = [0.08, 0.08, 9, 12, 16, 17, 17, 17, 17, 17]
depress = [1.41, 1.41, 0.79, 0.65, 3.78, 3.77, 5.18, 6.52, 5.55, 5.55]

print(covtoabsolute(fatigue))
print(abs_to_rel(nv, covtoabsolute(fatigue)))
print(abs_to_rel(nv, covtoabsolute(headache)))
print(abs_to_rel(nv, covtoabsolute(sleep)))
print(abs_to_rel(nv, covtoabsolute(depress)))





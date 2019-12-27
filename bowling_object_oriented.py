import random
list = []

for i in range(9):
    class Frame:
        number = i + 1
        pin1 = random.randint(0, 10)
        pin2 = random.randint(0, (10-pin1))
        summ = pin1 + pin2
    list.append(Frame())


class Frame:
    number = 10
    pin1 = random.randint(0, 10)
    if pin1 == 10:
        pin2 = random.randint(0, 10)
        pin3 = random.randint(0, (10-pin2))
    else:
        pin2 = random.randint(0, (10-pin1))
        if pin1 + pin2 == 10:
            pin3 = random.randint(0, 10)
        else:
            pin3 = 0
    summ = pin1 + pin2 + pin3
list.append(Frame)

# Frame1
if list[0].pin1 == 10:
    if list[1].pin1 == 10:
        score = list[0].summ + 10 + list[2].pin1
    else:
        score = list[0].summ + list[1].summ
elif list[0].summ == 10:
    score = list[0].summ + list[1].pin1
else:
    score = list[0].summ
a1 = list[0]
a1.score = score


# Frame2-8
for k in range(1, 9):
    if list[k].pin1 == 10:
        if list[k+1].pin1 == 10:
            score = list[k-1].score + list[k].summ + 10 + list[k+1].pin1
        else:
            score = list[k-1].score + list[k].summ + list[k+1].summ
    elif list[k].summ == 10:
        score = list[k-1].score + list[k].summ + list[k+1].pin1
    else:
        score = list[k-1].score + list[k].summ
    a = list[k]
    a.score = score
# Frame9
if list[8].pin1 == 10:
    score = list[7].score + list[8].summ + list[9].pin1 + list[9].pin2
elif list[8].summ == 10:
    score = list[7].score + list[8].summ + list[9].pin1
else:
    score = list[7].score + list[8].summ
a9 = list[8]
a9.score = score

# Frame10
score = list[8].score + list[9].summ
a10 = list[9]
a10.score = score

for j in range(9):
    print(list[j].pin1)
    print(list[j].pin2)
    print(list[j].score)
print(list[9].pin1)
print(list[9].pin2)
print(list[9].pin3)
print(list[9].score)

# strike -> 'X', spare -> '/'
for l in range(9):
    if list[l].pin1 == 10:
        list[l].pin1 = 'X'
    elif list[l].pin1 + list[l].pin2 == 10:
        list[l].pin2 = '/'
# Frame10
if list[9].pin1 == 10:
    list[9].pin1 = 'X'
    if list[9].pin2 == 10:
        list[9].pin2 = 'X'
    elif list[9].pin2 + list[9].pin3 == 10:
        list[9].pin3 = '/'
elif list[9].pin1 + list[9].pin2 == 10:
    list[9].pin2 = '/'

f = open('score.html', 'w')
f.write('<table>')
f.write('<table border="1" cellpadding="10" cellspacing="0">')

f.write("<tr>")
for i in range(9):
    f.write('<td colspan="2", align=center>{}</td>'.format(list[i].number))
f.write('<td colspan="3", align=center>{0}</td>'.format(10))
f.write("</tr>")
f.write("<tr>")
for i in range(10):
    f.write('<td align=center>{}</td>'.format(list[i].pin1))
    f.write('<td align=center>{}</td>'.format(list[i].pin2))
f.write('<td align=center>{}</td>'.format(list[9].pin3))
f.write("</tr>")
f.write("<tr>")
for i in range(9):
    f.write('<td colspan="2", align=center>{}</td>'.format(list[i].score))
f.write('<td colspan="3", align=center>{}</td>'.format(list[9].score))
f.write("</tr>")
f.write("</table>")
f.close()

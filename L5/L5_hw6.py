subj = {}
with open('text_6.txt', 'r', encoding="UTF-8") as f:
    for line in f:
        splitted_line = line.split()
        subject = splitted_line[0]
        sum_lessons = sum([int(x[:x.find('(')]) for x in splitted_line[1:] if '(' in x])
        subj[subject] = sum_lessons
    print(subj)

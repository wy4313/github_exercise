#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def ListOperate():
    students = ["hello", "world", "python"]
    print(students, 'len is:', len(students))
    for x in students:
        print(x, 'len is:', len(x))

    for i in range(len(students)):
        print(students[i], end=' ')
        print(students[-i - 1])

    students.append("someday")
    print(students, 'len:', len(students))
    students.insert(1, 'joureny')
    print(students, 'len:', len(students))
    students.insert(len(students), 'joureny')
    print(students, 'len:', len(students))
    print("insert at out of list range.")
    students.insert(len(students) + 1, 'joureny')
    print(students, 'len:', len(students))
    students.remove('joureny')
    print(students, 'len:', len(students))
    joureny_count = students.count('joureny')
    print('joureny count is:', joureny_count)

    print(students.pop())
    print('after pop() students', students)
    print(students.pop(1))
    print('after pop(1) students', students)

    while 'joureny' in students:
        students.remove('joureny')
    print('students', students)

    samelist = students
    copylist = list(students)
    students.clear()
    print("samelist=students after students.clear()", samelist)
    print("copylist=list(students) after student.clear()", copylist)

    students.append(copylist)
    print(students)
    students.extend(range(3))
    print(students)

    for x in students[0]:
        print(x)


def TupleOperate():
    classmates = ('hello', 'python', 'world', 'python')
    print(classmates)

    print('tuple.count:', classmates.count('python'))
    print('tuple.index(\'python\'):', classmates.index('python'))


if __name__ == "__main__":
    # ListOperate()
    TupleOperate()

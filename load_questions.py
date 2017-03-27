# -*- coding: utf-8 -*-

import sqlite3
import xlrd

con = sqlite3.connect('db.sqlite3')
cur = con.cursor()

rb = xlrd.open_workbook('data.xls', formatting_info=True)
sheet = rb.sheet_by_index(0)
for rownum in range(2, sheet.nrows):
    row = sheet.row_values(rownum)
    print u'Гружу --->', row[0], row[1], row[2], row[3]
    insert_q = (row[0], row[1], row[2])
    sql = "INSERT INTO polls_question(title,text,category) VALUES(?,?,?)"
    cur.execute(sql, insert_q)
    con.commit()
    sql = "select MAX(id), * FROM polls_question"
    cur.execute(sql)
    d = cur.fetchone()
    question_id_id = d[0]
    answer = row[3].split(',')
    if len(answer) < 2:
        insert_a = (row[3], 0, question_id_id)
        sql = "INSERT INTO polls_answer(answer,answer_true,question_id_id) VALUES(?,?,?)"
        cur.execute(sql, insert_a)
        con.commit()
    else:
        for ans in answer:
            insert_a = (ans, 0, question_id_id)
            sql = "INSERT INTO polls_answer(answer,answer_true,question_id_id) VALUES(?,?,?)"
            cur.execute(sql, insert_a)
            con.commit()

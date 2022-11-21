import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('education.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

# 5 студентов с наибольшим средним баллом по всем предметам.
sql_1 = """
select d.name , s.fullname , avg(g.grade) as avg_grade
from grades g
left join students s 
on g.student_id  = s.id 
left join disciplines d 
on d.id = g.discipline_id 
group by d.name , s.fullname 
order by avg(g.grade)  DESC 
limit 5;
"""

# 1 студент с наивысшим средним баллом по одному предмету.
sql_2 = """
select d.name , s.fullname , avg(g.grade) as avg_grade
from grades g
left join students s 
on g.student_id  = s.id 
left join disciplines d 
on d.id = g.discipline_id 
where d.id  = 1 
group by d.name , s.fullname 
order by avg(g.grade)  DESC 
limit 1
"""

# средний балл в группе по одному предмету.
sql_3 = """
select gg.name ,d.name ,avg(g.grade) as grade_avg
from grades g
left join students s 
on s.id = g.student_id 
left join groups gg 
on gg.id = s.group_id 
left join disciplines d 
on d.id =g.discipline_id 
group by gg.name ,d.name
"""

# Средний балл в потоке.
sql_4 = """
select avg(g.grade) as grade_avg
from grades g
"""

# Какие курсы читает преподаватель.
sql_5 = """
select t.fullname ,d.name 
from teachers t 
left join disciplines d 
on t.id = d.teacher_id 
group by t.fullname ,d.name 
order by 1
"""

# Список студентов в группе.
sql_6 = """
select g.name ,s.fullname 
from students s 
left join groups g 
on s.group_id  = g.id 
group by g.name ,s.fullname 
order by 1
"""

# Оценки студентов в группе по предмету.
sql_7 = """
select g2.name as name_grp ,
d.name as name_disc,s.fullname  ,g.grade 
FROM grades g 
left join students s 
on s.id =g.student_id 
left join disciplines d 
on d.id =g.discipline_id 
left join  groups g2 
on g2.id =s.group_id 
order by 1,2
"""

# Оценки студентов в группе по предмету на последнем занятии.
sql_8 = """
select *
FROM (
select g2.name as grp,
       d.name as name_disc,
       s.fullname as student_name,
        g.date_of,
       DENSE_RANK() over (PARTITION  by g2.name,d.name,s.fullname order by g.date_of  DESC  ) as rn
from grades g 
left join students s 
on s.id =g.student_id 
left join disciplines d 
on d.id  = g.discipline_id 
left join groups g2 
on g2.id = s.group_id 
)
where rn=1
"""

# Список курсів, які відвідує студент.
sql_9 = """
select distinct d.name  as discipline, s.fullname 
from grades g 
left join students s 
on g.student_id  =s.id 
left join disciplines d 
on d.id =g.discipline_id 
order by 1
"""

# Список курсів, які студенту читає викладач.
sql_10 = """
select distinct d.name  as discipline,t.fullname as teacher_name, s.fullname 
from grades g 
left join students s 
on g.student_id  =s.id 
left join disciplines d 
on d.id =g.discipline_id 
left join teachers t 
on t.id  = d.teacher_id 
order by 1,2
"""

# Средний балл, который преподаватель ставит студенту.
sql_11 = """
select t.fullname  as teacher_name, s.fullname  as stydent_name,
avg(g.grade) as avg_grade
from grades g 
left join students s 
on g.student_id  =s.id 
left join disciplines d 
on d.id =g.discipline_id 
left join teachers t 
on t.id  = d.teacher_id 
group by t.fullname , s.fullname
"""

# Средний балл, который ставит преподаватель.
sql_12 = """
select t.fullname  as teacher_name, 
avg(g.grade) as avg_grade
from grades g 
left join disciplines d 
on d.id =g.discipline_id 
left join teachers t 
on t.id  = d.teacher_id 
group by t.fullname 
"""

print(execute_query(sql_1))
print(execute_query(sql_2))
print(execute_query(sql_3))
print(execute_query(sql_4))
print(execute_query(sql_5))
print(execute_query(sql_6))
print(execute_query(sql_7))
print(execute_query(sql_8))
print(execute_query(sql_9))
print(execute_query(sql_10))
print(execute_query(sql_11))
print(execute_query(sql_12))
## 数据表如如下
1,Alex Li,22,13651054608,IT,2013-04-01
## 现需要对这个员工信息文件，实现增删改查操作

1. 可进行模糊查询，语法至少支持下面3种:
```sql
select name,age from staff_table where age > 22
select  * from staff_table where dept = "IT"
select  * from staff_table where enroll_date like "2013"
``` 

 2. 查到的信息，打印后，最后面还要显示查到的条数 
 3. 可创建新员工纪录，以phone做唯一键，staff_id需自增
 4. 可删除指定员工信息纪录，输入员工id，即可删除
 5. 可修改员工信息，语法如下:
```sql
  UPDATE staff_table SET dept="Market" WHERE where dept = "IT"
```
 - 注意：以上需求，要充分使用函数，请尽你的最大限度来减少重复代码！
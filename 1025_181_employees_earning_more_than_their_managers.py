"""
181. Employees Earning More Than Their Managers
Easy

SQL Schema
The Employee table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.

+----+-------+--------+-----------+
| Id | Name  | Salary | ManagerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | NULL      |
| 4  | Max   | 90000  | NULL      |
+----+-------+--------+-----------+
Given the Employee table, write a SQL query that finds out employees who earn more than their managers. For the above table, Joe is the only employee who earns more than his manager.

+----------+
| Employee |
+----------+
| Joe      |
+----------+
"""

"""
SELECT name AS Employee FROM Employee WHERE salary > SELECT Salary from Employee Id=ManagerId 

select E1.name as Employee from Employee as E1, Employee as E2 where E1.ManagerId=E2.Id and E1.Salary > E2.Salary
"""
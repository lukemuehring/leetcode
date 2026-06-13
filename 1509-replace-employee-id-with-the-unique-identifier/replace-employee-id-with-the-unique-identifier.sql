# Write your MySQL query statement below
select e.unique_id, a.name
from employees a
left join employeeuni e on e.id = a.id 
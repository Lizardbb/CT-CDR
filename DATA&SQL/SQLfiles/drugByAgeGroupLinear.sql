use MMUCC_SeniorProgram
select Drug,Age_Group,count(Drug) as Count from PositiveStateLabToxData
group by Drug,Age_Group
order by Drug,Age_Group asc
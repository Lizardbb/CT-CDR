use MMUCC_SeniorProgram

select 
pivoted.Town,
isnull([1],0) as 'M',
isnull([2],0) as 'F'

from (SELECT  c.CrashTownName as Town
			  ,p.Gender as Gender
			  ,count(p.Gender) as Count

	  FROM (select CrashID,Gender from Persons) as p

	  inner join

	  (select CrashID,CrashTownName from Crashes) as c
	  on c.CrashID = p.CrashID

	  where p.Gender is not Null and p.Gender is not null
	  group by c.CrashTownName,p.Gender

) as source

pivot

(MAX(Count)
for Gender
in ([1],[2])) as pivoted
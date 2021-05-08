use MMUCC_SeniorProgram
SELECT  c.CrashTownName
			  ,a.AgeRange as Age_Group
			  ,count(c.CrashTownName) as Count

	  FROM (select CrashID,Age from Persons) as p

	  left join

	  (select Age,AgeRange from AgeRanges) as a
	  on a.Age = p.Age

	  inner join

	  (select CrashID,CrashTownName from Crashes) as c
	  on c.CrashID = p.CrashID

	  where p.Age is not Null and p.Age is not null and AgeRange is not null
	  group by c.CrashTownName,a.AgeRange
	  order by CrashTownName,Age_Group
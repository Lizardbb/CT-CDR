use MMUCC_SeniorProgram
select 
pivoted.CrashTownName as 'Town',
isnull([0-18],0) as '0-18',
isnull([19-24],0) as '19-25',
isnull([25-34],0) as '26-34',
isnull([35-54],0) as '35-54',
isnull([55-64],0) as '55-64',
isnull([65+],0) as '65+'


from (SELECT  c.CrashTownName
			  ,p.Age_Group
			  ,count(p.Age_Group) as Count

	  FROM (select CrashID,Age_Group from Persons) as p

	  inner join

	  (select CrashID,CrashTownName from Crashes) as c
	  on c.CrashID = p.CrashID

	  where p.Age_Group is not Null and p.Age_Group is not null
	  group by c.CrashTownName,p.Age_Group
) as source

pivot

(MAX(Count)
for Age_Group
in ([0-18],[19-24],[25-34],[35-54],[55-64],[65+])) as pivoted

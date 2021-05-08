use MMUCC_SeniorProgram

select 
pivoted.Injury as Injury,
isnull([0-18],0) as '0-18',
isnull([19-24],0) as '19-25',
isnull([25-34],0) as '26-34',
isnull([35-54],0) as '35-54',
isnull([55-64],0) as '55-64',
isnull([65+],0) as '65+'

from (SELECT  i.Description as Injury
			  ,a.AgeRange as Age_Group
			  ,count(i.Description) as Count
	  FROM Persons as p

	  left join

	  (select Age,AgeRange from AgeRanges) as a
	  on a.Age = p.Age

	  inner join

	  (select Value,Description from injurystatus) as i
	  on i.Value = p.InjuryStatus

	  where p.Age is not Null and p.InjuryStatus is not null and AgeRange is not null
	  group by i.Description,a.AgeRange

) as source

pivot

(MAX(Count)
for Age_Group
in ([0-18],[19-24],[25-34],[35-54],[55-64],[65+])) as pivoted
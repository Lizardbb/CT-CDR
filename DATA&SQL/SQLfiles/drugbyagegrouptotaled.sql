select 
pivoted.Drug as Drug,
isnull([0-18],0) as '0-18',
isnull([19-24],0) as '19-25',
isnull([25-34],0) as '26-34',
isnull([35-54],0) as '35-54',
isnull([55-64],0) as '55-64',
isnull([65+],0) as '65+',
Total

from (SELECT Drug,Age_Group,count(Drug) as Count
	  FROM [MMUCC_SeniorProgram].[dbo].[PositiveStateLabToxData] as data
	  group by Drug,Age_Group
) as source

pivot

(MAX(Count)
for Age_Group
in ([0-18],[19-24],[25-34],[35-54],[55-64],[65+])) as pivoted

inner join (select Drug,count(Drug) as Total from [MMUCC_SeniorProgram].[dbo].[PositiveStateLabToxData] group by Drug)
as t on pivoted.Drug = t.Drug

order by Total desc
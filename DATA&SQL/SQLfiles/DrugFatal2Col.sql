select top 30
pivoted.Drug as Drug,
isnull([True],0) as 'Fatal',
isnull([False],0) as 'Non-Fatal',
t.Total

from (SELECT Drug,Fatal,count(Fatal) as Count
	  FROM [MMUCC_SeniorProgram].[dbo].[PositiveStateLabToxData] as data
	  group by Drug,Fatal
) as source

pivot

(MAX(Count)
for Fatal
in ([True],[False])) as pivoted

inner join (SELECT Drug,count(Drug) as Total
		    FROM [MMUCC_SeniorProgram].[dbo].[PositiveStateLabToxData] as data
		    group by Drug) as t
			on pivoted.Drug = t.Drug

order by Total Desc

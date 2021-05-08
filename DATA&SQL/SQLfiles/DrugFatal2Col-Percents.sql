select top 30
pivoted.Drug as Drug,
cast(round(isnull([True],0) * 100.0 / t.Total,2) as decimal (4,2)) as'Fatal',
cast(round(isnull([False],0) * 100.0 / t.Total,2)as decimal (5,2)) as'Non-Fatal'


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

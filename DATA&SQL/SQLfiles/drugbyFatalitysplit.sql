use MMUCC_SeniorProgram



select top 20
	   Count,
	   case Fatal when 'True' then 'Fatal' when 'False' then 'Non-Fatal' end as Severity,
	   Drug
from 
	(select count(Fatal) as Count, Fatal, a.Drug,b.total from [PositiveStateLabToxData] as a
	 left join
	 (select Drug, count(Drug) as total from [PositiveStateLabToxData]
	 group by Drug) as b
	 on a.Drug = b.Drug
	 group by a.Drug,a.Fatal,b.total) as c
	 where Drug != 'Negative'
	 order by total desc

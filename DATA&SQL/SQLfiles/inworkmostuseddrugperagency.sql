/****** Script for SelectTopNRows command from SSMS  ******/



select totaled.Submitting_Agency,maxed2.Drug, num_used
from
	(select maxed.Submitting_Agency, max(maxed.count) as num_used
	 from(
		SELECT [Submitting_Agency]
		 ,Drug
		 ,count(Drug) as count
		 FROM [MMUCC_SeniorProgram].[dbo].[PositiveStateLabToxData]
	     group by Submitting_Agency,Drug
	     )as maxed
	  group by Submitting_Agency) as totaled

left join 

 (SELECT [Submitting_Agency],
	  Drug
	  ,count(Drug) as count
  FROM [MMUCC_SeniorProgram].[dbo].[PositiveStateLabToxData]
  group by Submitting_Agency,Drug
  ) as maxed2

  on (totaled.num_used = maxed2.count) and (totaled.Submitting_Agency = maxed2.Submitting_Agency)
  
  order by Submitting_Agency asc

 
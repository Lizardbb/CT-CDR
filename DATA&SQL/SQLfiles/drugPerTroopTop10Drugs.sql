/****** Script for SelectTopNRows command from SSMS  ******/
SELECT [Submitting_Agency]
	  ,Drug
      ,count(Drug) as Count
  FROM [MMUCC_SeniorProgram].[dbo].[PositiveStateLabToxData]
  where Drug in (select top 10 Drug
				 from MMUCC_SeniorProgram.dbo.PositiveStateLabToxData
				 group by Drug
				 order by count(drug) desc)
  group by Submitting_Agency,Drug
  order by Submitting_Agency
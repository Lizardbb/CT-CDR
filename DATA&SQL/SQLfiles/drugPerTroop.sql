/****** Script for SelectTopNRows command from SSMS  ******/
SELECT [Submitting_Agency]
	  ,Drug
      ,count(Drug) as Count
  FROM [MMUCC_SeniorProgram].[dbo].[PositiveStateLabToxData]
  group by Submitting_Agency,Drug
  order by Submitting_Agency
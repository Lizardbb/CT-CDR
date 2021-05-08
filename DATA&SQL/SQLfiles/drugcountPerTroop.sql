/****** Script for SelectTopNRows command from SSMS  ******/
SELECT [Submitting_Agency]
      ,count(Submitting_Agency) as Count
  FROM [MMUCC_SeniorProgram].[dbo].[PositiveStateLabToxData]
  group by Submitting_Agency
  order by Submitting_Agency
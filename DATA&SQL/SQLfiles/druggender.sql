/****** Script for SelectTopNRows command from SSMS  ******/
SELECT 
	  [Drug]
	  ,Gender as Sex
	  ,count(drug) as DrugByGender
  FROM [MMUCC_SeniorProgram].[dbo].[PositiveStateLabToxData] where gender is not Null
  group by Gender,Drug
  order by Drug,Gender
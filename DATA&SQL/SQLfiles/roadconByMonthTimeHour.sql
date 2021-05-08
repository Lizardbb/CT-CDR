/****** Script for SelectTopNRows command from SSMS  ******/
SELECT 
	   CrashDateMonth
	  ,CrashTimeHour
	  ,Description
	  ,count(Description) as Count
  FROM [MMUCC_SeniorProgram].[dbo].[Crashes] as crashes

  inner join

  (select * from MMUCC_SeniorProgram.dbo.Codes
  where CodeName = 'TrafficSurfaceCondition') as codes on crashes.TrafficSurfaceCondition = codes.Value

  where TrafficSurfaceCondition is not null and TrafficSurfaceCondition != '99' and CrashDateYear is not null and CrashDateMonth is not null
    and CrashDateYear >= 2018

  group by CrashDateMonth,CrashTimeHour,Description

  order by CrashDateMonth,CrashTimeHour,Description
SELECT 
      crashes.CrashTownName
	  ,codes.Description
	  ,count(codes.Description) as Count
  FROM [MMUCC_SeniorProgram].[dbo].[Crashes] as crashes

  inner join

  (select * from MMUCC_SeniorProgram.dbo.Codes
  where CodeName = 'TrafficSurfaceCondition') as codes on crashes.TrafficSurfaceCondition = codes.Value

  where TrafficSurfaceCondition is not null and TrafficSurfaceCondition != '99'

  group by CrashTownName,Description

  order by CrashTownName,Description
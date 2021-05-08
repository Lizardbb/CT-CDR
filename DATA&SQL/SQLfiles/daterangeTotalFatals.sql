/****** Script for SelectTopNRows command from SSMS  ******/
SELECT 'March 1st-22nd 2019' as date
	  ,count(CrashID) as Total
	  ,sum(case FatalCaseStatus when 0 then 1 else 0 end) as  Fatal
  FROM [MMUCC_SeniorProgram].[dbo].[Crashes]
  where CrashDate between '2019-03-01' and '2019-03-22'

  union

SELECT 'March 23rd-May 19th 2019'
	  ,count(CrashID) as Total
	  ,sum(case FatalCaseStatus when 0 then 1 else 0 end) as  Fatal
  FROM [MMUCC_SeniorProgram].[dbo].[Crashes]
  where CrashDate between '2019-03-23' and '2019-05-19'

  union

SELECT 'May 20th-June 16th 2019'
	  ,count(CrashID) as Total
	  ,sum(case FatalCaseStatus when 0 then 1 else 0 end) as  Fatal
  FROM [MMUCC_SeniorProgram].[dbo].[Crashes]
  where CrashDate between '2019-05-20' and '2019-06-16'

  union

SELECT 'June 17th-October 7th 2019'
	  ,count(CrashID) as Total
	  ,sum(case FatalCaseStatus when 0 then 1 else 0 end) as  Fatal
  FROM [MMUCC_SeniorProgram].[dbo].[Crashes]
  where CrashDate between '2019-06-17' and '2019-10-07'

  union

SELECT 'October 8th 2019-February 28th 2020'
	  ,count(CrashID) as Total
	  ,sum(case FatalCaseStatus when 0 then 1 else 0 end) as  Fatal
  FROM [MMUCC_SeniorProgram].[dbo].[Crashes]
  where CrashDate between '2019-10-08' and '2020-02-28'

  union

  SELECT 'March 1st-22nd 2020'
  	  ,count(CrashID) as Total
	  ,sum(case FatalCaseStatus when 0 then 1 else 0 end) as  Fatal
  FROM [MMUCC_SeniorProgram].[dbo].[Crashes]
  where CrashDate between '2020-03-01' and '2020-03-22'

  union

SELECT 'March 23rd-May 19th 2020'
	  ,count(CrashID) as Total
	  ,sum(case FatalCaseStatus when 0 then 1 else 0 end) as  Fatal
  FROM [MMUCC_SeniorProgram].[dbo].[Crashes]
  where CrashDate between '2020-03-23' and '2020-05-19'

  union

SELECT 'May 20th-June 16th 2020'
	  ,count(CrashID) as Total
	  ,sum(case FatalCaseStatus when 0 then 1 else 0 end) as  Fatal
  FROM [MMUCC_SeniorProgram].[dbo].[Crashes]
  where CrashDate between '2020-05-20' and '2020-06-16'

  union

SELECT 'June 17th-October 7th 220'
	  ,count(CrashID) as Total
	  ,sum(case FatalCaseStatus when 0 then 1 else 0 end) as  Fatal
  FROM [MMUCC_SeniorProgram].[dbo].[Crashes]
  where CrashDate between '2020-06-17' and '2020-10-07'

    union

SELECT 'October 8th 2020-February 28th 2021'
	  ,count(CrashID) as Total
	  ,sum(case FatalCaseStatus when 0 then 1 else 0 end) as  Fatal
  FROM [MMUCC_SeniorProgram].[dbo].[Crashes]
  where CrashDate between '2020-10-08' and '2021-02-28'
select towns.CrashTownName,towns.total_count as Total,ISNULL(fatal.fatal_count ,0) as Fatals
from

(SELECT CrashTownName,count(CrashTownName) as total_count
FROM [MMUCC_SeniorProgram].[dbo].[Crashes]
group by CrashTownName) as towns

left join (SELECT [CrashTownName],count([CrashTownName]) as fatal_count
  FROM [MMUCC_SeniorProgram].[dbo].[Crashes] as towns
  where FatalCaseStatus = 0
  group by CrashTownName) as fatal on fatal.CrashTownName = towns.CrashTownName

order by CrashTownName asc
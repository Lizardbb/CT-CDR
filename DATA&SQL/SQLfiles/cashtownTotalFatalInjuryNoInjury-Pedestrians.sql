select	towns.CrashTownName,
		towns.total_count as Total,
		ISNULL(fatal.fatal_count ,0) as Fatals,
		ISNULL(injury.injury_count,0) as Injury,
		ISNULL(noinjury.noinjury_count,0) as No_Injury

from

(SELECT CrashTownName,count(CrashTownName) as total_count
FROM [MMUCC_SeniorProgram].[dbo].[Crashes]
where CountOfNonMotorists != 0
group by CrashTownName) as towns

  left join (SELECT [CrashTownName],count([CrashTownName]) as fatal_count
			 FROM [MMUCC_SeniorProgram].[dbo].[Crashes] as towns
			 where (MostSevereInjury = 'K' or FatalCaseStatus = '0') and CountOfNonMotorists != 0
			 group by CrashTownName) as fatal on fatal.CrashTownName = towns.CrashTownName

  left join (SELECT CrashTownName,count(CrashTownName) as injury_count
		FROM [MMUCC_SeniorProgram].[dbo].[Crashes] where (MostSevereInjury = 'A' or MostSevereInjury = 'B' or MostSevereInjury = 'C') and CountOfNonMotorists != 0
		group by CrashTownName) as injury on injury.CrashTownName = towns.CrashTownName

  left join (SELECT CrashTownName,count(CrashTownName) as noinjury_count
		FROM [MMUCC_SeniorProgram].[dbo].[Crashes] where MostSevereInjury = 'O' and CountOfNonMotorists != 0
		group by CrashTownName) as noinjury on noinjury.CrashTownName = towns.CrashTownName

order by CrashTownName asc
select	code.Description as School_Bus_Relation,
		crash.total_count as Total,
		ISNULL(fatal.fatal_count ,0) as Fatals,
		ISNULL(injury.injury_count,0) as Injury,
		ISNULL(noinjury.noinjury_count,0) as No_Injury

from

(SELECT SchoolBusRelated,count(SchoolBusRelated) as total_count
FROM [MMUCC_SeniorProgram].[dbo].[Crashes]
group by SchoolBusRelated) as crash

  left join (SELECT SchoolBusRelated,count(SchoolBusRelated) as fatal_count
			 FROM [MMUCC_SeniorProgram].[dbo].[Crashes] as towns
			 where MostSevereInjury = 'K' or FatalCaseStatus = '0'
			 group by SchoolBusRelated) as fatal on fatal.SchoolBusRelated = crash.SchoolBusRelated

  left join (SELECT SchoolBusRelated,count(SchoolBusRelated) as injury_count
		FROM [MMUCC_SeniorProgram].[dbo].[Crashes] where MostSevereInjury = 'A' or MostSevereInjury = 'B' or MostSevereInjury = 'C'
		group by SchoolBusRelated) as injury on injury.SchoolBusRelated = crash.SchoolBusRelated

  left join (SELECT SchoolBusRelated,count(SchoolBusRelated) as noinjury_count
		FROM [MMUCC_SeniorProgram].[dbo].[Crashes] where MostSevereInjury = 'O'
		group by SchoolBusRelated) as noinjury on noinjury.SchoolBusRelated = crash.SchoolBusRelated

  join (select value, description from [MMUCC_SeniorProgram].[dbo].[Codes] where CodeName = 'SchoolBusRelated') as code
	    on code.Value = crash.SchoolBusRelated

where crash.SchoolBusRelated is not null and crash.SchoolBusRelated != '99'
order by Total desc
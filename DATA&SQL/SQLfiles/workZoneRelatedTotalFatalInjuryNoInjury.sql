select	CASE when crash.IsCrashRelatedToAWorkZone = 1 then 'No' when crash.IsCrashRelatedToAWorkZone = 2 then 'Yes' END as Work_Zone_Relation,
		crash.total_count as Total,
		ISNULL(fatal.fatal_count ,0) as Fatals,
		ISNULL(injury.injury_count,0) as Injury,
		ISNULL(noinjury.noinjury_count,0) as No_Injury

from

(SELECT IsCrashRelatedToAWorkZone,count(IsCrashRelatedToAWorkZone) as total_count
FROM [MMUCC_SeniorProgram].[dbo].[Crashes]
where IsCrashRelatedToAWorkZone is not null
group by IsCrashRelatedToAWorkZone) as crash

  left join (SELECT IsCrashRelatedToAWorkZone,count(IsCrashRelatedToAWorkZone) as fatal_count
			 FROM [MMUCC_SeniorProgram].[dbo].[Crashes] as towns
			 where MostSevereInjury = 'K' or FatalCaseStatus = '0'
			 group by IsCrashRelatedToAWorkZone) as fatal on fatal.IsCrashRelatedToAWorkZone = crash.IsCrashRelatedToAWorkZone

  left join (SELECT IsCrashRelatedToAWorkZone,count(IsCrashRelatedToAWorkZone) as injury_count
		FROM [MMUCC_SeniorProgram].[dbo].[Crashes] where MostSevereInjury = 'A' or MostSevereInjury = 'B' or MostSevereInjury = 'C'
		group by IsCrashRelatedToAWorkZone) as injury on injury.IsCrashRelatedToAWorkZone = crash.IsCrashRelatedToAWorkZone

  left join (SELECT IsCrashRelatedToAWorkZone,count(IsCrashRelatedToAWorkZone) as noinjury_count
		FROM [MMUCC_SeniorProgram].[dbo].[Crashes] where MostSevereInjury = 'O'
		group by IsCrashRelatedToAWorkZone) as noinjury on noinjury.IsCrashRelatedToAWorkZone = crash.IsCrashRelatedToAWorkZone

where crash.IsCrashRelatedToAWorkZone is not null and crash.IsCrashRelatedToAWorkZone != '99'
order by Total desc
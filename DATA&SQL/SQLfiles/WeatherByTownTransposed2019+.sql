select 
Town_Name as TownName,
ISNULL(Clear,0) as Clear,
ISNULL([Blowing Sand, Soil, Dirt],0) as Blowing_Sand_Soil_Dirt,
ISNULL(Cloudy,0) as Cloudy,
ISNULL([Fog, Smog, Smoke],0) as Fog_Smog_Smoke,
ISNULL(Rain,0) as Rain,
ISNULL([Sleet or Hail],0) as Sleet_or_Hail,
ISNULL([Freezing Rain or Freezing Drizzle],0) as Freezing_Rain_or_Freezing_Drizzle,
ISNULL(Snow,0) as Snow,
ISNULL([Blowing Snow],0) as Blowing_Snow,
ISNULL([Not Applicable],0) as Not_Applicable,
ISNULL([Severe Crosswinds],0) as Severe_Crosswinds,
ISNULL([Other],0) as Other,	
ISNULL([Unknown],0) as Unknown

from (SELECT CrashTownName as Town_Name,code.Description as WeatherCondition1,count(code.Description) as Count
	  FROM [MMUCC_SeniorProgram].[dbo].[Crashes] as crash
	  inner join (select * from [MMUCC_SeniorProgram].[dbo].[Codes] where CodeName = 'WeatherCondition') as code
	  on code.Value = WeatherCondition1
	  where CrashDateYear >= 2019
	  group by code.Description,CrashTownName
) as source

pivot

(MAX(Count)
for WeatherCondition1
in (Clear,[Blowing Sand, Soil, Dirt],[Cloudy],[Fog, Smog, Smoke],Rain,[Sleet or Hail],
[Freezing Rain or Freezing Drizzle],Snow,[Blowing Snow],[Not Applicable],[Severe Crosswinds],[Other],[Unknown])) as pivoted


select 
Town_Name as TownName,
ISNULL(Daylight,0) as Daylight,
ISNULL(Dawn,0) as Dawn,
ISNULL(Dusk,0) as Dusk,
ISNULL([Dark-Lighted],0) as Dark_Lighted,
ISNULL([Dark-Not Lighted],0) as Dark_Not_Lighted,
ISNULL([Dark-Unknown Lighting],0) as Dark_Unknown_Lighting,
ISNULL([Other],0) as Other,	
ISNULL([Unknown],0) as Unknown

from (SELECT CrashTownName as Town_Name,code.Description as LightCondition,count(code.Description) as Count
	  FROM [MMUCC_SeniorProgram].[dbo].[Crashes] as crash 
	  inner join (select * from [MMUCC_SeniorProgram].[dbo].[Codes] where CodeName = 'LightCondition') as code
	  on code.Value = LightCondition
	  group by code.Description,CrashTownName
) as source

pivot

(MAX(Count)
for LightCondition
in (Daylight,Dawn,Dusk,[Dark-Lighted],[Dark-Not Lighted],[Dark-Unknown Lighting],[Other],[Unknown])) as pivoted


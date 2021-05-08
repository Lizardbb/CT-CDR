select 
Town_Name as TownName,
ISNULL(Dry,0) as Dry,
ISNULL([Standing Water],0) as 'Standing Water',
ISNULL(Wet,0) as Wet,
ISNULL(Snow,0) as Snow,
ISNULL(Slush,0) as Slush,
ISNULL([Ice / Frost],0) as 'Ice / Frost',
ISNULL([Moving Water],0) as 'Moving Water',
ISNULL([Sand],0) as Sand,

ISNULL([Mud, Dirt, Gravel],0) as 'Mud, Dirt, Gravel',
ISNULL(Oil,0) as Oil,
ISNULL([Other],0) as Other,	
ISNULL([Unknown],0) as Unknown

from (SELECT CrashTownName as Town_Name,code.Description as TrafficSurfaceCondition,count(code.Description) as Count
	  FROM [MMUCC_SeniorProgram].[dbo].[Crashes] as crash
	  inner join (select * from [MMUCC_SeniorProgram].[dbo].[Codes] where CodeName = 'TrafficSurfaceCondition') as code
	  on code.Value = TrafficSurfaceCondition
	  where CrashDateYear >= 2019
	  group by code.Description,CrashTownName
) as source

pivot

(MAX(Count)
for TrafficSurfaceCondition
in (Clear,[Dry],[Standing Water],[Wet],Snow,Slush,[Ice / Frost],
[Moving Water],[Sand],[Mud, Dirt, Gravel],Oil,[Other],[Unknown])) as pivoted


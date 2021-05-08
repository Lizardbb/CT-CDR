use MMUCC_SeniorProgram
DECLARE @Columns as VARCHAR(MAX)
DECLARE @NColumns as VARCHAR(MAX)
DECLARE @SQL as VARCHAR(MAX)

SELECT @Columns =
ISNULL(@Columns + ', ','') + QUOTENAME(OwnerState)
FROM
   (select Distinct OwnerState 
    from Vehicles
	where OwnerState is not null and OwnerState != ''
   ) AS B
ORDER BY B.OwnerState

SELECT @NColumns =
ISNULL(@NColumns + ', ','') + 'ISNULL(' + QUOTENAME(OwnerState) + ',0) AS ' + QUOTENAME(OwnerState)
FROM
   (select Distinct OwnerState 
    from Vehicles
	where OwnerState is not null and OwnerState != ''
   ) AS B

SET @SQL = 'SELECT Town, ' + @NColumns + '
FROM
(
 SELECT  c.CrashTownName as Town
			  ,v.OwnerState
			  ,ISNULL(count(v.OwnerState),0) as Count

	  FROM (select CrashID,OwnerState from Vehicles) as v

	  inner join

	  (select CrashID,CrashTownName from Crashes) as c
	  on c.CrashID = v.CrashID

	  where v.OwnerState is not Null
	  group by c.CrashTownName,v.OwnerState
) as PivotData
PIVOT
(
   MAX(Count)
   FOR OwnerState IN (' + @Columns + ')
) AS PivotResult'

EXEC(@SQL);
use MMUCC_SeniorProgram
DECLARE @Columns as VARCHAR(MAX)
DECLARE @SQL as VARCHAR(MAX)

SELECT @Columns =
COALESCE(@Columns + ', ','') + QUOTENAME(Gender)
FROM
   (select Distinct Gender 
    from Persons
	where Gender is not null and Gender not in(99,'')
   ) AS B
ORDER BY B.Gender

SET @SQL = 'SELECT CrashTownName, ' + @Columns + '
FROM
(
 SELECT  c.CrashTownName
			  ,p.Gender as Gender
			  ,count(p.Gender) as Count

	  FROM (select CrashID,Gender from Persons) as p

	  inner join

	  (select CrashID,CrashTownName from Crashes) as c
	  on c.CrashID = p.CrashID

	  where p.Gender is not Null and p.Gender is not null
	  group by c.CrashTownName,p.Gender
) as PivotData
PIVOT
(
   MAX(Count)
   FOR Gender IN (' + @Columns + ')
) AS PivotResult'

EXEC(@SQL);
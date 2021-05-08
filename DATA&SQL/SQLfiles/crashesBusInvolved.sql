use MMUCC_SeniorProgram
select code.Description,count(code.Description) as Count from Crashes as crash


left join (select value, description from Codes where CodeName = 'SchoolBusRelated') as code
on code.Value = crash.SchoolBusRelated

where SchoolBusRelated != '99' and SchoolBusRelated is not Null
group by code.Description
order by Count Desc

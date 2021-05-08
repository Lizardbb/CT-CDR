use MMUCC_SeniorProgram
select code.Description,count(code.Description) as Count from Crashes as crash


left join (select value, description from Codes where CodeName = 'IsCrashRelatedToAWorkZone') as code
on code.Value = crash.IsCrashRelatedToAWorkZone

where IsCrashRelatedToAWorkZone != '99' and IsCrashRelatedToAWorkZone is not Null
group by code.Description
order by Count Desc

use MMUCC_SeniorProgram

select v.OwnerState, count(v.OwnerState) as Count
from Crashes as c
left join
Vehicles as v on c.CrashID = v.CrashID
group by OwnerState
order by OwnerState asc

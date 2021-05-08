use MMUCC_SeniorProgram
select Latitude,Longitude from Crashes
where MostSevereInjury = 'K' or FatalCaseStatus = '0'
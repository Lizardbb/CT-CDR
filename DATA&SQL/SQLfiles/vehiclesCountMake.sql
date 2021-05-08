/****** Script for SelectTopNRows command from SSMS  ******/
SELECT
      LOWER(REPLACE([VehicleMake], ' ', '')) as 'Vehicle Make'
	  ,count(LOWER(REPLACE([VehicleModel], ' ', ''))) as Count
  FROM [MMUCC_SeniorProgram].[dbo].[Vehicles]
  where VehicleMake != ''and VehicleMake not like '%unknown%'
  group by LOWER(REPLACE([VehicleMake], ' ', ''))
  order by count desc
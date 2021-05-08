/****** Script for SelectTopNRows command from SSMS  ******/
SELECT
      LOWER(REPLACE([VehicleMake], ' ', '')) as 'Vehcile Make'
      ,LOWER(REPLACE([VehicleModel], ' ', '')) as 'Vehicle Model'
	  ,count(LOWER(REPLACE([VehicleModel], ' ', ''))) as Count
  FROM [MMUCC_SeniorProgram].[dbo].[Vehicles]
  where VehicleMake != '' and VehicleModel != '' and VehicleMake not like '%unknown%' and VehicleModel not like '%unknown%'
  group by LOWER(REPLACE([VehicleMake], ' ', '')),LOWER(REPLACE([VehicleModel], ' ', ''))
  order by count desc
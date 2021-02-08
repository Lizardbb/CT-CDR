This example shows a choropleth map of Connecticut, showing the town
subdivisions. The example resizes the map to use the space available,
while still keeping the correct aspect ratio. 

This visualization is part of a series focused on [Run
169](http://www.debticonn.org). I'm trying to run a road race in each of
Connecticut's 169 towns. Hover over a town to see its name, driving time from my town, and races in
the next two weeks.

To experience the resize behavior, [run this example
full-screen](https://bl.ocks.org/jpasini/raw/dca25b76efe015ef42433c5ca019e27b/)
and resize the browser.

Notes:

* forked from <a href='http://bl.ocks.org/curran/'>curran</a>'s block:
    <a
    href='http://bl.ocks.org/curran/3a68b0c81991e2e94b19'>Responding
    to Resize</a>
* Choropleth map code based on [this
    video](https://www.youtube.com/watch?v=lJgEx_yb4u0)
* Other data
  * [Shapefiles for CT Towns](http://magic.lib.uconn.edu/connecticut_data.html)
  * [Converter from shapefiles to geojson](https://mygeodata.cloud/converter/shp-to-geojson)
  * Used topojson to convert large GeoJSON to TopoJSON and then
      simplify the shapes. Note that TopoJSON includes *topology*
      information, so when the shapes in the map are simplified (for
      speed) common boundaries between towns remain as common
      boundaries. In contrast, simplifying GeoJSON files creates gaps.



forked from <a href='http://bl.ocks.org/jpasini/'>jpasini</a>'s block: <a href='http://bl.ocks.org/jpasini/dca25b76efe015ef42433c5ca019e27b'>Resizable choropleth map</a>
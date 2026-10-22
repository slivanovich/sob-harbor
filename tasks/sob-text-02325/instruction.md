Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Dowsby: Dowsby is a village and civil parish in the South Kesteven district of Lincolnshire, England.  It is situated on the western edge of The Fens at the junction of the east-west B1397 road and the north-south B1177.  It is 1 mi north-east from Rippingale and just south of Pointon.  The civil parish includes the hamlet of Graby.  Nearby to the east, along the B1397 at Dowsby Fen, is Car Dyke.  The civil parish population taken at the 2011 census was 204.

Colsterworth: Colsterworth is a village and civil parish in the South Kesteven district of Lincolnshire, England.  It lies less than half a mile (0.8 km) west of the A1, about 7 mi south of Grantham, and 12 mi north-west of Stamford.  The village, with the hamlet of Woolsthorpe-by-Colsterworth, had a population of 1,713 at the time of the 2011 Census in an area of 1465 ha .

Ancaster, Lincolnshire: Ancaster is a village and civil parish in the South Kesteven district of Lincolnshire, England, on the site of a Roman town.  The population of the civil parish was 1,317 at the 2001 census increasing to 1,647 at the 2011 census.  The civil parish includes the settlements of Sudbrook and West Willoughby.

Abbeytown: Abbeytown, also known as Holme Abbey, is a village and civil parish in Cumbria, England.  The population of the civil parish as of the 2011 census was 819.  It is located five-and-a-half miles south-east of Silloth, and six-and-a-half miles north-west of Wigton.  The civil parish borders Holme Low to the north, Holme East Waver and Dundraw to the east, Bromfield to the south, and Holme St Cuthbert to the west.  The county town of Carlisle is eighteen miles to the north-east.  Other nearby settlements include Highlaws, Kelsick, Mawbray, Pelutho, and Wheyrigg.  The B5302 road runs through the village.

Scopwick: Scopwick is small village and civil parish in the district of North Kesteven, Lincolnshire, England, situated 6 mi south from Lincoln.  The population of the civil parish at the 2011 census was 815.  The parish includes Kirkby Green, a hamlet to the east of Scopwick.  The village main road runs parallel to a narrow stream.

Blythburgh: Blythburgh is a village and civil parish in the Suffolk Coastal district of the English county of Suffolk.  It is 4 mi west of Southwold and 5 mi south-east of Halesworth and lies on the River Blyth.  The A12 road runs through the village which is split either side of the road.  At the 2011 census the population of the parish was 297.  The parish includes the hamlets of Bulcamp and Hinton.

High Dyke (road): High Dyke is a minor road following a length of the Roman Road Ermine Street in the English county of Lincolnshire, between Woolsthorpe-by-Colsterworth and Ancaster, and onwards nearly to Bracebridge Heath.  It is also the name of a small settlement on that road, 1 mi south-east from Great Ponton, near to the mouth of Stoke Tunnel on the East Coast Main Line.  High Dyke is also a name for the general area between Easton and Great Ponton.  On the Ordnance Survey 1:25000 sheets it is spelled "High Dike".

Hayton and Mealo: Hayton and Mealo is a civil parish in Allerdale district, Cumbria.  In the 2011 census it had a population of 237.  The western boundary of the parish is a short stretch of coastline south of Allonby; working clockwise it is then bordered by Allonby parish to the north, Westnewton to the north east, Aspatria to the east and Oughterside and Allerby to the south.  The B5300 road runs along the western edge of the parish, on the coast, and the A596 road from Aspatria to Maryport runs just outside the parish's south eastern boundary.  The only settlement is Hayton, a village in the centre of the parish.

North Wingfield: North Wingfield is a large village and civil parish in the English county of Derbyshire, located approximately 4½ miles south-east of Chesterfield, and 1 mile north-east of Clay Cross.  The population of the civil parish as of the 2011 census was 6,505.  It is in the North East Derbyshire district.  The A6175 road from the M1 motorway to the A61 road runs through the village.

Worston: Worston is a small linear village and civil parish in Lancashire, England.  The village is north-west of Pendle Hill, east of Clitheroe, and is in the Ribble Valley district.  As it is only a small village, with a population of 76 at the 2001 census, it has no parish council, but instead has a parish meeting.  The parish meeting is shared with Mearley, a small parish south of Worston with no villages or hamlets and a population of 25, the second smallest in Lancashire.  From the 2011 Census population information for both Mearley and Worston is included within the civil parish of Pendleton.

Question: What is the 2011 census population of this village and civil parish in Lincolnshire, England, where High Dyke road runs between it and Colsterworth?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "village_name": {
      "type": "string",
      "description": "The name of the village and civil parish identified."
    },
    "county": {
      "type": "string",
      "description": "The county where the village is located."
    },
    "district": {
      "type": "string",
      "description": "The district where the village is located."
    },
    "census_details": {
      "type": "object",
      "properties": {
        "year": {
          "type": "integer",
          "description": "The year of the census."
        },
        "population": {
          "type": "integer",
          "description": "The population figure from the specified census year."
        }
      },
      "required": [
        "year",
        "population"
      ],
      "additionalProperties": false
    },
    "connecting_road_information": {
      "type": "object",
      "properties": {
        "road_name": {
          "type": "string",
          "description": "The name of the road that connects the identified village to another place."
        },
        "connected_places": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of places connected by the specified road, including the identified village and the other village mentioned in the question."
        }
      },
      "required": [
        "road_name",
        "connected_places"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "village_name",
    "county",
    "district",
    "census_details",
    "connecting_road_information"
  ],
  "additionalProperties": false
}

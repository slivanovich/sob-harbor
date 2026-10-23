{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBlackburn with Darwen: Blackburn with Darwen is a unitary authority area in Lancashire, North West England.  It consists of Blackburn, the small town of Darwen to the south of it, and the surrounding countryside.  The population of the Unitary Authority taken at the 2011 census was 147,489.\n\nBorough of Darlington: Darlington is a unitary authority area in the ceremonial county of County Durham, north-east England.  It borders the non-metropolitan county of County Durham to the north and west, Stockton-on-Tees to the east and North Yorkshire to the south along the line of the River Tees.  The urban centre and the base of the borough is the town of Darlington.  In 2011 it had a resident population of 106,000.  The borough is a member of the Tees Valley combined authority area.\n\nNorth East Lincolnshire: North East Lincolnshire is a unitary authority area in the Yorkshire and the Humber region of England, bordering the unitary authority of North Lincolnshire and the non-metropolitan county of Lincolnshire.  The population of the Unitary Authority at the 2011 Census was 159,616.  These three administrative units make up the ceremonial county of Lincolnshire.\n\nListed buildings in Warrington (unparished area): Warrington is a town, borough and unitary authority area of Cheshire, England.  The unitary authority contains 18 civil parishes, which are distributed around its periphery.  Its central area, including the town, is unparished.  This list contains the 141 structures in the unparished area that are designated by English Heritage as listed buildings and included in the National Heritage List for England.  Of these, three buildings are listed at Grade I, and ten at Grade II*.  The remaining buildings are listed at Grade II.  The listed buildings in the civil parishes are included in separate lists.\n\nEastoft: Eastoft is a village and civil parish in North Lincolnshire, England.  It is situated within the Isle of Axholme, 3 mi north-east from Crowle, and on the A161 road.\n\nCantref Reservoir: Cantref Reservoir is the middle of the three reservoirs in the Taff Fawr valley in Wales.  It is owned by Welsh Water.  It is located in the Brecon Beacons National Park, mostly in the Powys unitary authority area and within the historic county boundaries of Breconshire.  Part of the south west corner is in the Rhondda Cynon Taff unitary authority area.\n\nLlwyn-on Reservoir: Llwyn-on Reservoir is the largest and southernmost of the three reservoirs in the Taff Fawr valley in South Wales.  It is owned by Welsh Water.  It is located in the Brecon Beacons National Park.  The eastern half is in the Merthyr Tydfil unitary authority area and the western half is in the Rhondda Cynon Taff unitary authority area.  The reservoir is within the historic county boundaries of Breconshire.  The dam is adjacent to Llwyn-On village.\n\nBorough of Halton: Halton is a local government district in the ceremonial county of Cheshire in North West England, with borough status and administered by a unitary authority.  It was created in 1974 as a district of the non-metropolitan county of Cheshire, and became a unitary authority area on 1 April 1998.  Since 2014 it has been a member of the Liverpool City Region Combined Authority.  The borough consists of the towns of Runcorn and Widnes and the civil parishes of Hale, Daresbury, Moore, Preston Brook, Halebank and Sandymoor.  The district borders Merseyside, Warrington and Cheshire West and Chester.  The borough straddles the River Mersey – the area to the north (including Widnes) is historically part of Lancashire, that to the south (including Runcorn) part of Cheshire.\n\nNorth Lincolnshire: North Lincolnshire is a unitary authority area in the region of Yorkshire and the Humber in England.  The population of the Unitary Authority at the 2011 census was 167,446.  For ceremonial purposes it is part of Lincolnshire.  There are three significant towns: Scunthorpe (the administrative centre), Brigg and Barton-upon-Humber.\n\nList of towns and cities in Devon by population: This list is of towns and cities in Devon in order of their population, according to the 2011 census data from the Office for National Statistics.  It comprises the Key Statistics for local authorities, civil parishes and wards that attempt to show their populations.  The largest settlement in Devon is the city and unitary authority of Plymouth with a population of 256,720, whereas the smallest settlement was the town and civil parish of Beer with a population of 1,317.  The city of Exeter, which is home to Exeter Cathedral, is the county town and headquarters of Devon County Council.  The ceremonial county of Devon includes unitary authority areas such as Plymouth and Torbay, but the non-metropolitan county of Devon excludes such unitary authority areas.  It is governed by Devon County Council, whereas Plymouth and Torbay can govern themselves on matters such as transport and education.\n\nQuestion: What was the 2011 population of the unitary authority area that includes the village Eastoft?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"unitary_authority_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the unitary authority area.\"\n    },\n    \"village_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the village located within the unitary authority.\"\n    },\n    \"census_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the population census was conducted.\"\n    },\n    \"population\": {\n      \"type\": \"integer\",\n      \"description\": \"The population of the unitary authority area according to the specified census.\"\n    }\n  },\n  \"required\": [\n    \"unitary_authority_name\",\n    \"village_name\",\n    \"census_year\",\n    \"population\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "unitary_authority_name": {
        "type": "string",
        "description": "The name of the unitary authority area."
      },
      "village_name": {
        "type": "string",
        "description": "The name of the village located within the unitary authority."
      },
      "census_year": {
        "type": "integer",
        "description": "The year the population census was conducted."
      },
      "population": {
        "type": "integer",
        "description": "The population of the unitary authority area according to the specified census."
      }
    },
    "required": [
      "unitary_authority_name",
      "village_name",
      "census_year",
      "population"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

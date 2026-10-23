{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nListed buildings in Appleby-in-Westmorland: Appleby-in-Westmorland is a civil parish in the Eden District, Cumbria, England.  It contains 140 buildings that are recorded in the National Heritage List for England.  Of these, six are listed at Grade I, the highest of the three grades, nine are at Grade II*, the middle grade, and the others are at Grade II, the lowest grade.  The parish contains the market town of Appleby (renamed Appleby-in-Westmorland in 1974) and surrounding countryside.  There is a great variety of types of listed building in the parish.  The most important building is Appleby Castle; this and a number of associated structures are listed.  Most of the listed buildings are houses and associated structures, shops and public buildings.  Other listed buildings include churches, public houses, hotels, two crosses and a lamp post, farmhouses and farm buildings, former industrial buildings, schools, banks, a bridge, railway station buildings, and a milestone.\n\nListed buildings in Odd Rode: Odd Rode is a civil parish in Cheshire East, England.  It contains 35 buildings that are recorded in the National Heritage List for England as designated listed buildings. Of these, one is listed at Grade I, the highest grade, five are listed at Grade II*, the middle grade, and the others are at Grade II.  The most important listed building in the parish is Little Moreton Hall; other notable country houses include Rode Hall and Ramsdell Hall.  Most of the other listed buildings are houses, farmhouses, and associated structures.  The Macclesfield and the Trent and Mersey Canals run through the parish, and the listed buildings associated with these are bridges, milestones, and distance markers.  The other listed buildings are a church.  a folly, wellheads, and a public house.\n\nCongleton United Reformed Church: Congleton United Reformed Church is in Antrobus Street, Congleton, Cheshire, England.  It is recorded in the National Heritage List for England as a designated Grade II listed building.\n\nChurch of St Thomas à Becket, Capel: The Church of St Thomas à Becket is a redundant Anglican church in the village of Capel, Kent, England.  It is recorded in the National Heritage List for England as a designated Grade I listed building, and is under the care of the Churches Conservation Trust.  Capel is located 4 mi east of Tonbridge, off the B2017 road.  It is said that Thomas Becket preached either in the church, or under a yew tree in the churchyard.\n\nListed buildings in Congleton: Congleton is a civil parish in Cheshire East, England.  It contains 133 buildings that are recorded in the National Heritage List for England as designated listed buildings. Of these, one is listed at Grade I, the highest grade, four are listed at Grade II*, the middle grade, and the others are at Grade II.  The parish contains the town of Congleton, and surrounding countryside.  Passing through the parish are the Macclesfield Canal and the River Dane, and a number of listed structures are associated with these waterways.  The silk and cotton weaving industries came to the town from the 18th century, and there are listed buildings associated with these, including mills and weavers' cottages.  Otherwise the listed buildings include houses and cottages in the town and the country, churches and associated structures, shops, schools, a town hall, offices, and public houses.  Some of the buildings date from the 16th and 17th centuries, and are timber-framed.  The great majority of houses are from the late 18th and early 19th centuries, reflecting the industrial growth and prosperity in the town at this time.\n\nListed buildings in Edge, Cheshire: Edge is a civil parish in Cheshire West and Chester, England.  It contains 18 buildings that are recorded in the National Heritage List for England as designated listed buildings.  One of these is listed at Grade II*, the middle grade, and the rest at the lowest grade, Grade II.  The parish is entirely rural, and most of the listed buildings are domestic, or related to farming.  The most important building is the country house, Edge Hall, which dates from about 1600.  Many of the other listed buildings are houses and cottages, either timber-framed or with a timber-framed core, dating from the 17th century.  Other structures in the list include a former corn mill, former stables, and a bridge near Edge Hall.\n\nAll Saints Chapel, Somerford: All Saints Chapel, Somerford is in an isolated position near the hamlet of Brereton Heath, between Congleton and Holmes Chapel, Cheshire, England.  It is recorded in the National Heritage List for England as a designated Grade II* listed building.  The chapel is in the Anglican benefice of Astbury and Smallwood in the deanery of Congleton, the archdeaconry of Macclesfield and the diocese of Chester.\n\nNether Alderley Mill: Nether Alderley Mill is a 16th-century watermill located in Congleton Road (the A34), to the south of the village of Nether Alderley, Cheshire, England.  It is owned by the National Trust, and is recorded in the National Heritage List for England as a designated Grade II* listed building.  It is a unique example of a triple overshot waterwheel system, two of which are in working order.  It is one of only four virtually complete corn mills in Cheshire.\n\nSt Peter's Church, Congleton: St Peter's Church is in Chapel Street, Congleton, Cheshire, England.  It is recorded in the National Heritage List for England as a designated Grade I listed building.  It is an active Anglican parish church in the Diocese of Chester, the archdeaconry of Macclesfield and the deanery of Congleton.  Its benefice is combined with those of St Stephen, Congleton, St John the Evangelist, Buglawton, and Holy Trinity, Mossley.  Alec Clifton-Taylor includes it in his list of 'best' English parish churches.\n\nLittle Moreton Hall: Little Moreton Hall, also known as Old Moreton Hall, is a moated half-timbered manor house 4 mi southwest of Congleton in Cheshire, England.  The earliest parts of the house were built for the prosperous Cheshire landowner William Moreton in about 1504–08, and the remainder was constructed in stages by successive generations of the family until about 1610.  The building is highly irregular, with three asymmetrical ranges forming a small, rectangular cobbled courtyard.  A National Trust guidebook describes Little Moreton Hall as being \"lifted straight from a fairy story, a gingerbread house\".  The house's top-heavy appearance, \"like a stranded Noah's Ark\", is due to the Long Gallery that runs the length of the south range's upper floor.\n\nQuestion: What is the most important building in the National Heritage for England located 4 mi southwest of Congleton in Cheshire?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"building_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the most important building.\"\n    },\n    \"importance_reason\": {\n      \"type\": \"string\",\n      \"description\": \"The reason why the building is considered most important, as stated in the context.\"\n    },\n    \"location_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"distance_miles\": {\n          \"type\": \"integer\",\n          \"description\": \"The distance from the reference town in miles.\"\n        },\n        \"direction\": {\n          \"type\": \"string\",\n          \"description\": \"The cardinal direction from the reference town.\"\n        },\n        \"reference_town\": {\n          \"type\": \"string\",\n          \"description\": \"The town used as a reference point for the building's location.\"\n        },\n        \"county\": {\n          \"type\": \"string\",\n          \"description\": \"The county where the building is located.\"\n        }\n      },\n      \"required\": [\n        \"distance_miles\",\n        \"direction\",\n        \"reference_town\",\n        \"county\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"building_name\",\n    \"importance_reason\",\n    \"location_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "building_name": {
        "type": "string",
        "description": "The name of the most important building."
      },
      "importance_reason": {
        "type": "string",
        "description": "The reason why the building is considered most important, as stated in the context."
      },
      "location_details": {
        "type": "object",
        "properties": {
          "distance_miles": {
            "type": "integer",
            "description": "The distance from the reference town in miles."
          },
          "direction": {
            "type": "string",
            "description": "The cardinal direction from the reference town."
          },
          "reference_town": {
            "type": "string",
            "description": "The town used as a reference point for the building's location."
          },
          "county": {
            "type": "string",
            "description": "The county where the building is located."
          }
        },
        "required": [
          "distance_miles",
          "direction",
          "reference_town",
          "county"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "building_name",
      "importance_reason",
      "location_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

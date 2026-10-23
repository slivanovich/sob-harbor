{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGreentown, Indiana: Greentown is a town in Liberty Township, Howard County, Indiana, United States.  Located approximately 9 miles east of Kokomo on State Road 22 / US 35, it is home to the Howard County Fair Grounds.  The town was platted in 1848, and incorporated as a town in 1873.  Known for its collectible glassware made for only a few years by a local factory destroyed in 1903, it is home to the Greentown Glass Museum.  As of the 2010 census, the town's population was 2,415.\n\nNexø: Nexø, sometimes spelled Neksø, is a town on the east coast of the Baltic island of Bornholm, Denmark.  With a population of 3,642 (as of 1 January 2015), it is the second largest town, as well as the largest fishing port on the island.  Fishing is the mainstay of the town's economy.  Nexø is also the site of a distillery (Bornholmske Spiritfabrik ApS) and a mustard factory (Bornholmersennep ApS).  The town is also a port of call for the passenger ferries linking Bornholm with Kołobrzeg, Darłowo, and Ustka in Poland.  Dueodde, the largest beach on Bornholm, is located south of Nexø, in the southeastern corner of the island.\n\nNawabganj, North 24 Parganas: Nawabganj is a small residential town under Barrackpore subdivision located 25 kilometers north of Kolkata, and in the district of North 24 Parganas, West Bengal, India.  This small town is situated beside the Hooghly River and it is surrounded by Palta Water Works, Barrackpore Air Force Station and Ishapore Rifle Factory.  The town is densely populated where the majority of the population are Bengalis and is well connected with Kolkata and nearby cities by highways and railroads with adequate public transportation facility.\n\nHudson, Massachusetts: Hudson is a town in Middlesex County, Massachusetts, United States, with a total population of 19,063 as of the 2010 census.  Before its incorporation as a town in 1866, Hudson was a neighborhood and unincorporated village within the town of Marlborough, Massachusetts, and was known as Feltonville, and before that, known as Eastborough.  From around 1850 until the last shoe factory burned down in 1968, Hudson was known as a \"shoe town\".  At one point, the town had 17 shoe factories, many of them powered by the Assabet River, which runs through town.  Because of the many factories in Hudson, immigrants were attracted to the town.  Today, most people are of either Portuguese or Irish descent, with a smaller percentage of people being of French, Italian, English, or Scots-Irish descent.  Hudson is served by the Hudson Public Schools district.\n\nWeatherly, Pennsylvania: Weatherly a borough in Carbon County, Pennsylvania, United States, located 12 mi northwest of Jim Thorpe and 28 mi south of Wilkes Barre.  Early in the twentieth century, there were silk mills, foundries, a candy factory, a fabricating plant, and a cigar factory.  In 1900 2,471 people lived there, and in 1910, the population was 2,501.  The population was 2,525 at the 2010 census.\n\nRoman, Bulgaria: Roman (Роман) is a town in northwestern Bulgaria near the city of Pravets and about 90 km northeast of the capital of Bulgaria, Sofia.  It is located in Vratsa Province and is known for the big steel factory, producing 100,000 tons of steel a year.  The raw materials come from the Kremikovtsi factory near Sofia.  As of December 2009, the town has a population of 3,157 inhabitants.\n\nGreentown Glass Museum: The Greentown Glass Museum features locally-made glass items and is located at 112 N Meridian Street in Greentown City Hall, Greentown, Indiana.  Items include vases, mugs, pitchers, salt cellars, toothpick holders, covered dishes topped by hens, cats, and rabbits, and other decorative items.  There is also an exhibit with examples of all the patterns and colors of glass made by the local factory.  The items were created beginning in 1894 by the Indiana Tumbler and Goblet Factory, which was sold in 1899 to the National Glass Company, and then shut down the factory in 1903 when a fire destroyed the building.\n\nStratham, New Hampshire: Stratham is a town in Rockingham County, New Hampshire, United States.  The town had a population of 7,255 at the 2010 census, and an estimated population of 7,280 in 2013.  It is bounded on the west by the Squamscott River.  The town is the home of the only U.S. Lindt & Sprüngli factory and the headquarters of the Timberland Corporation.\n\nChetwynd, British Columbia: Chetwynd is a district municipality located on the foothills of the Rocky Mountains in northeastern British Columbia, Canada.  Situated on an ancient floodplain, it is the first town eastbound travellers encounter after emerging from the Rockies along Highway 97 and acts as the gateway to the Peace River Country.  The town developed during the construction of infrastructure through the Rocky Mountains in the 1950s, and was used as a transshipment point during the construction of hydroelectric dams in the 1960s and 1970s and the new town of Tumbler Ridge in the early 1980s.  Home to approximately 2,600 residents, the population has increased little if at all since the 1980s but is significantly younger than the provincial average.\n\nIndian Head, Maryland: Indian Head is a town in Charles County, Maryland, United States.  The population was 3,844 at the 2010 U.S. Census.  It has been the site of a naval base specializing in gun and rocket propellants since 1890.  Production of nitrocellulose and smokeless powder began at the Indian Head Powder Factory in 1900.  The name of the base has varied over the years from Indian Head Proving Ground, to Naval Powder Factory, to Naval Propellant Plant, to Naval Ordnance Station, to the present Naval Support Facility Indian Head.  The facility's main tenant activity is the Indian Head Naval Surface Warfare Center (NSWC/IH).  Advanced research in energetic systems takes place at NSWC/IH.  NSWC/IH absorbed the function of the closed Naval Ordnance Laboratory, formerly in White Oak, Maryland.  The base currently employs 3,700.\n\nQuestion: What was the town's population where the Tumbler and Goblet Factory was located in 2010?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"town_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the town where the factory was located.\"\n    },\n    \"location_details\": {\n      \"type\": \"string\",\n      \"description\": \"Additional geographical details for the town (e.g., state, county, country).\"\n    },\n    \"factory_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the factory in question.\"\n    },\n    \"population_census_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year of the census for the reported population.\"\n    },\n    \"population_count\": {\n      \"type\": \"integer\",\n      \"description\": \"The population count of the town in the specified year.\"\n    }\n  },\n  \"required\": [\n    \"town_name\",\n    \"location_details\",\n    \"factory_name\",\n    \"population_census_year\",\n    \"population_count\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "town_name": {
        "type": "string",
        "description": "The name of the town where the factory was located."
      },
      "location_details": {
        "type": "string",
        "description": "Additional geographical details for the town (e.g., state, county, country)."
      },
      "factory_name": {
        "type": "string",
        "description": "The name of the factory in question."
      },
      "population_census_year": {
        "type": "integer",
        "description": "The year of the census for the reported population."
      },
      "population_count": {
        "type": "integer",
        "description": "The population count of the town in the specified year."
      }
    },
    "required": [
      "town_name",
      "location_details",
      "factory_name",
      "population_census_year",
      "population_count"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

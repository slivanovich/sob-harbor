{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nLinda Berglin: Linda Lee Berglin (born October 19, 1944) is a Minnesota politician and a former member of the Minnesota Senate who represented District 61, which includes portions of the city of Minneapolis in Hennepin County, which is in the Twin Cities metropolitan area.  A Democrat, she was first elected to the Senate in 1980, and was re-elected in each election until she resigned on August 15, 2011, to take a position with Hennepin County.  Prior to the 1982 and 1992 redistricting, the area was known as District 59 and District 60, respectively.\n\nMinneapolis: Minneapolis ( ) is the county seat of Hennepin County, and the larger of the Twin Cities, the 16th-largest metropolitan area in the United States.  As of 2016, Minneapolis is the largest city in the state of Minnesota and 46th-largest in the United States, with an estimated population of 413,651.  The Twin Cities metropolitan area is the third largest in the Midwest with about 3.5 million people.  Minneapolis and Saint Paul anchor the second-largest economic center in the Midwest, after Chicago.\n\nCounty Road 61 (Hennepin County, Minnesota): Hennepin County Road 61 or County State-Aid Highway 61 (CR 61, CSAH 61) is a major route along the east side of Interstate 494 (I-494) in Hennepin County, Minnesota.  The route travels through the west suburbs of the Twin Cities through Maple Grove, Plymouth, Minnetonka, Hopkins and Eden Prairie.\n\nRandy Johnson (Minnesota elected official): Randy Johnson represented the 5th District of Hennepin County government in Minnesota from 1979-2017.  Hennepin County is the largest of Minnesota's 87 counties in population, budget and estimated value.  Hennepin County's population is 1.1 million, which is 21 percent of the state's total population, and about one third of the population of the Twin Cities metropolitan area.  Minneapolis is the county seat.\n\nMinnesota State Highway 62 (Hennepin County): Minnesota State Highway 62 (MN 62) is a highway in the Twin Cities region of Minnesota.  The route was part of \"Hennepin County Road 62\" until 1988, when a portion of the route was inherited by the state.  The western terminus of the route is at Interstate Highway 494 in Eden Prairie, where the roadway continues west as \"Hennepin County Road 62\" to \"Hennepin County Road 101\".  The eastern terminus of the route is at State Highway 55 near the Minneapolis-Saint Paul International Airport in Minneapolis.  Locally, the route is known as \"the \"Crosstown\",\" though signage with this name does not appear on the highway itself, but only on local streets adjacent to the road.  It is also used as an alternate name, even by the Minnesota Department of Transportation.  Though it does follow the 62nd Street plane for most of its route, that name is less frequently used.  Highway 62 is 12 mi in length.\n\nSlave Raider: Slave Raider was an American heavy metal band formed in 1985 that was known for its over-the-top antics, heavy make-up and glam song lyrics.  In the 1980s, the Minneapolis music scene was primarily known for The Replacements, Soul Asylum, Hüsker Dü and Prince among others.  In the Twin Cities, Slave Raider had a sizeable following that were known as \"The Raid\".  They opened for such 1980s bands as Ratt and Poison with the original lineup.\n\nMike Opat: Michael Joseph Opat (born March 25, 1961) is an American politician from the U.S. state of Minnesota.  He serves on the Hennepin County Board of Commissioners, the governing body for the largest county in Minnesota, with more than 1.1 million residents and an annual budget of $1.7 billion.  Opat represents District 1 (out of 7 districts), an area that includes more than 160,000 residents and encompasses six suburban cities: Brooklyn Center, Brooklyn Park, Crystal, New Hope, Osseo, and Robbinsdale, as well as North Minneapolis.  In his time on the County Board, Opat has led, among other initiatives, policy and governance changes at Hennepin County Medical Center, numerous advancements in public infrastructure including the revitalization of the Humboldt Greenway, reconstruction of Highway 100 in the northern suburbs, construction of the new Brookdale library, the construction of Target Field and expansion of the Twin Cities area transit network, including the Bottineau line along County Road 81 through the northern part of the county.\n\nLinda Higgins: Linda Higgins (born November 11, 1950) is a Minnesota politician and former member of the Minnesota Senate who represents District 59, which included portions of the city of Minneapolis in Hennepin County, which is in the Twin Cities metropolitan area.  A Democrat, she was first elected to the Senate in 1996, and was re-elected in 2000, 2002, 2006 and 2010.  She served as a majority whip from 2001 to 2006.  In the fall of 2011, she announced that she would not be seeking reelection after the current term ends in 2012.  However, when Hennepin County District 2 Commissioner Mark Stenglein announced in June 2012 that he would resign, Higgins decided to run for that position.  On May 20, 2012, she was endorsed by the DFL party for the position, and won the election in November.  In 2014, she ran unopposed and was reelected.  She currently is the Vice-Chair of the County Board, and Chair of the Housing and Redevelopment Authority.\n\nTake the World by Storm: Take the World by Storm is the debut studio album by the American glam metal band Slave Raider, released independently in 1986.  In December 1987, the album was remixed and released to the public in 1988 through the Jive record label, suffering poor sales.  The band did have a cult following in Minneapolis.  The remixed \"Make Some Noise\" was released as a single and a promotional video was shot in The Twin Cities.  In the remix, \"Make Some Noise\" was cut by around a minute and \"The Black Hole\" has a longer introduction.  It was available scarcely on CD, cassette, and vinyl and was out of print until Divebomb Records reissued it and the band's sophomore release \"What Do You Know About Rock 'N Roll?\"  in April 2015.\n\nHennepin County Library: Hennepin County Library is a public library system serving the entire population of Hennepin County, Minnesota, USA.  The current iteration of Hennepin County Library was formed by the merger of urban Minneapolis Public Library and suburban Hennepin County Library on January 1, 2008.  The system has 41 library locations, deposit collections at nursing homes and correctional facilities, mail service to the homebound and extensive outreach services.  The Library is a department of Hennepin County Government.  The library headquarters are in the Ridgedale Library in suburban Minnetonka.  The library system has an eleven-member advisory Library Board appointed by the Hennepin County Board of Commissioners.  It is a member of the Metropolitan Library Service Agency, a consortium of eight Twin Cities library systems.\n\nQuestion: Slave Raider was an American heavy metal band formed in 1985, in the 1980s, which county seat of Hennepin County, and the larger of the Twin Cities? \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"city_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the city that is the county seat of Hennepin County and the larger of the Twin Cities.\"\n    },\n    \"city_attributes\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"is_county_seat\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the city is the county seat of Hennepin County.\"\n        },\n        \"is_larger_twin_city\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the city is the larger of the Twin Cities.\"\n        },\n        \"county_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the county the city is the seat of.\"\n        },\n        \"metropolitan_area\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the metropolitan area the city belongs to.\"\n        }\n      },\n      \"required\": [\n        \"is_county_seat\",\n        \"is_larger_twin_city\",\n        \"county_name\",\n        \"metropolitan_area\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"band_context\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"band_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the band mentioned in the context.\"\n        },\n        \"formation_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the band was formed.\"\n        },\n        \"music_scene_relevance\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the city's music scene was relevant to the band's era.\"\n        }\n      },\n      \"required\": [\n        \"band_name\",\n        \"formation_year\",\n        \"music_scene_relevance\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"city_name\",\n    \"city_attributes\",\n    \"band_context\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "city_name": {
        "type": "string",
        "description": "The name of the city that is the county seat of Hennepin County and the larger of the Twin Cities."
      },
      "city_attributes": {
        "type": "object",
        "properties": {
          "is_county_seat": {
            "type": "boolean",
            "description": "Indicates if the city is the county seat of Hennepin County."
          },
          "is_larger_twin_city": {
            "type": "boolean",
            "description": "Indicates if the city is the larger of the Twin Cities."
          },
          "county_name": {
            "type": "string",
            "description": "The name of the county the city is the seat of."
          },
          "metropolitan_area": {
            "type": "string",
            "description": "The name of the metropolitan area the city belongs to."
          }
        },
        "required": [
          "is_county_seat",
          "is_larger_twin_city",
          "county_name",
          "metropolitan_area"
        ],
        "additionalProperties": false
      },
      "band_context": {
        "type": "object",
        "properties": {
          "band_name": {
            "type": "string",
            "description": "The name of the band mentioned in the context."
          },
          "formation_year": {
            "type": "integer",
            "description": "The year the band was formed."
          },
          "music_scene_relevance": {
            "type": "boolean",
            "description": "Indicates if the city's music scene was relevant to the band's era."
          }
        },
        "required": [
          "band_name",
          "formation_year",
          "music_scene_relevance"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "city_name",
      "city_attributes",
      "band_context"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

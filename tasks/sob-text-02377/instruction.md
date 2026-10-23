{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAddison, Texas: Addison is an incorporated town in Dallas County, Texas, in the United States.  Addison is situated to the immediate north of the city of Dallas.  The town's population was 13,056 at the 2010 census.  Addison and Flower Mound were the only two Texas towns with a population greater than 10,000 in the 2010 census; since then the towns of Prosper and Trophy Club have also exceeded 10,000 in population estimates.  Addison is best-known within the Dallas-Fort Worth Metroplex region for its abundance of restaurants and nightlife.\n\nKTCK (AM): KTCK (1310 AM; \"SportsRadio 1310 The Ticket\") is a commercial sports talk radio station licensed to Dallas, Texas, which serves the Dallas-Fort Worth Metroplex (DFW).  Its daytime power is 25,000 watts, which is reduced to 5,000 watts at night.  The station's studios are located in the Victory Park district in Dallas, just north of downtown, and the transmitter site is in Coppell.  The station is currently owned by Cumulus Media.  KTCK's programs are simulcast at 96.7 MHz over KTCK-FM, licensed to Flower Mound, Texas.\n\nFlower Mound High School: Flower Mound High School (FMHS) is part of Lewisville Independent School District and is located in Flower Mound, Texas, United States.  The school rests on 52 acre of land that were purchased in 1993.  FMHS was the second high school built in Flower Mound, after Edward S. Marcus High School.  With the expansion of the town in the 1980s and 1990s (from 1980 to 2000, it grew from 4,402 to 50,702 residents), a second high school was built to accommodate the growth.  Flower Mound High School has been called one of the top ten best public high schools in the Dallas area\n\nVanilla Ice: Robert Matthew Van Winkle (born October 31, 1967), known professionally as Vanilla Ice, is an American rapper, actor, and television host.  Born in South Dallas, and raised in Texas and South Florida, Ice released his debut album, \"Hooked\", in 1989 on Ichiban Records, before signing a contract with SBK Records, a record label of the EMI Group which released a reformatted version of the album under the title \"To the Extreme\".  Ice's 1990 single \"Ice Ice Baby\" was the first hip hop single to top the \"Billboard\" charts.\n\nLouis J. Cabri: Louis Jean-Pierre Cabri (born February 23, 1934, Cairo) is an eminent Canadian scientist in the field of platinum group elements (PGE) mineralogy with expertise in precious metal mineralogy and base metals at the Canada Centre for Mineral and Energy Technology (CANMET).  First as Research Scientist and later as Principal Scientist (1996–1999).  In the 1970s he discovered two new Cu–Fe sulfide minerals, \"mooihoekite\" and \"haycockite\".  In 1983 he discovered another new mineral, named after him: cabriite (PdSnCu).\n\nMarcos Hernandez (singer): Marcos Hernandez was born in Phoenix, Arizona in 1982 and raised in Dallas, Texas.  He worked at the Lewisville YMCA in Flower Mound, Texas as a lifeguard.  Hernandez was discovered by Vanilla Ice manager Tommy Quon.  He is a Mexican American pop singer whose debut single, \"If You Were Mine\", was released in August 2005.  The single got a good amount of airplay on Pop and Rhythmic stations and slowly crept up to the Top 25 on Top 40 radio.  The single also went to #1 in South Africa and France.  The video for the single was shot in Echo Park, California.  He joined the U.S. Marines in 2009.\n\nSecond Guangzhou Uprising: The Second Guangzhou Uprising, known in Chinese as the Yellow Flower Mound Uprising or the Guangzhou Xinhai Uprising, was a failed uprising led by Huang Xing and his fellow revolutionaries against the Qing Dynasty in Guangzhou.  It is honored in Guangzhou's Yellow Flower Mound or Huanghuagang Park.\n\nGlorious Day (Living He Loved Me): \"Glorious Day (Living He Loved Me)\" is a song performed by contemporary Christian band Casting Crowns from their 2009 album \"Until the Whole World Hears\".  While the music was composed by the band, the lyrics come from the hymn \"One Day\", written in 1910 by John Wilbur Chapman, and the song's verse melody was set by Michael Bleecker at The Village Church in Flower Mound, Texas.  The single has been successful on Christian radio, reaching the top spot on the Hot Christian Songs (for a total of nine non-consecutive weeks), Soft AC/Inspirational, and Christian AC charts.  The song has also achieved some inroads on secular charts, peaked at #2 on the Bubbling Under Hot 100 Singles chart.\n\nFlower Mound, Texas: Flower Mound is an incorporated town located in Denton and Tarrant counties in the U.S. state of Texas.  Located northwest of Dallas and northeast of Fort Worth adjacent to Grapevine Lake, the town derives its name from a prominent 12.5 acre mound located in the center of town.\n\nKTCK-FM: KTCK-FM (96.7 FM) is a commercial radio station licensed to serve the community of Flower Mound, Texas.  KTCK-FM, established in 1967 as KDSQ, is managed locally at 2221 East Lamar Blvd., Suite 300 in Arlington, and is currently owned by Cumulus Media.  As of October 21, 2013, the station broadcasts a sports/talk radio format to the Dallas/Fort Worth Metroplex area as a simulcast of sister station KTCK \"The Ticket\" (1310 AM).\n\nQuestion: The person who managed the artist that had an album named Hooked discovered another artist who worked where in Flower Mound, Texas?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"discovered_artist_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the artist who was discovered.\"\n    },\n    \"discoverer_role\": {\n      \"type\": \"string\",\n      \"description\": \"The role of the person who discovered the artist.\"\n    },\n    \"discoverer_of_artist_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the artist that the discoverer managed.\"\n    },\n    \"work_location\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the place where the discovered artist worked.\"\n        },\n        \"city\": {\n          \"type\": \"string\",\n          \"description\": \"The city where the work location is situated.\"\n        },\n        \"state\": {\n          \"type\": \"string\",\n          \"description\": \"The state where the work location is situated.\"\n        },\n        \"type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of establishment (e.g., YMCA).\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"city\",\n        \"state\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"discovered_artist_name\",\n    \"discoverer_role\",\n    \"discoverer_of_artist_name\",\n    \"work_location\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "discovered_artist_name": {
        "type": "string",
        "description": "The name of the artist who was discovered."
      },
      "discoverer_role": {
        "type": "string",
        "description": "The role of the person who discovered the artist."
      },
      "discoverer_of_artist_name": {
        "type": "string",
        "description": "The name of the artist that the discoverer managed."
      },
      "work_location": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the place where the discovered artist worked."
          },
          "city": {
            "type": "string",
            "description": "The city where the work location is situated."
          },
          "state": {
            "type": "string",
            "description": "The state where the work location is situated."
          },
          "type": {
            "type": "string",
            "description": "The type of establishment (e.g., YMCA)."
          }
        },
        "required": [
          "name",
          "city",
          "state"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "discovered_artist_name",
      "discoverer_role",
      "discoverer_of_artist_name",
      "work_location"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

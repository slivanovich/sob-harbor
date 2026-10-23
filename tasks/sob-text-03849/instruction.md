{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nComanche Nation Casino: Comanche Nation Casino, originally known as Comanche Nation Games, is a Native American casino geographically situated in the Southwest Great Plains Country of the United States.  The American Indian casino is located in Lawton, Comanche County, Oklahoma with East Cache Creek serving as a picturesque.  The gaming establishment, opening in 2007, is operated and owned by the tribal sovereignty of the Comanche Nation of Oklahoma with the governing powers in Lawton.\n\nBlack Horse (Comanche): Black Horse or Tu-ukumah (unknown–\"circa\" 1900), was a Comanche war chief.  After Bull Bear died in 1874, Black Horse was promoted to second chief in the Quahadi band of Comanche.  That is Quanah Parker's band.\n\nCache, Oklahoma: Cache is a city in Comanche County, Oklahoma, United States.  The population was 2,796 at the 2010 census.  It is an exurb included in the Lawton, Oklahoma Metropolitan Statistical Area.  It is the location of Star House, the home of the Comanche chief Quanah Parker, the major leader of the Quahadi Comanche in the years of Indian Wars and transition to reservation life.\n\nQuanah Parker: Quanah Parker (Comanche \"kwana\", \"smell, odor\") (  1845 or 1852 – February 23, 1911) was a Comanche war leader of the Quahadi (\"Antelope\") band of the Comanche people.  He was born into the Nokoni (\"Wanderers\") band, the son of Comanche chief Peta Nocona and Cynthia Ann Parker, an Anglo-American, who had been kidnapped as a child and assimilated into the tribe.  Following the apprehension of several Kiowa chiefs in 1871, Quanah emerged as a dominant figure in the Red River War, clashing repeatedly with Colonel Ranald S. Mackenzie.  With whites deliberately hunting American bison, the Comanche's primary livelihood, into extinction, Quanah finally surrendered and peaceably led the Quahadi to the reservation at Fort Sill, Oklahoma.\n\nRide the Wind: Ride the Wind (1982) by Lucia St. Clair Robson is the story of Cynthia Ann Parker's life after she was captured during the Comanche raid on her family's fort.  In 1836, when she was nine years old, Cynthia was kidnapped by Comanche Indians.  This is the story of how she grew up with them, mastered their ways, married one of their leaders, and became, in every way, a Comanche woman.  Her son Quanah Parker was the last Comanche leader to surrender.  It is also an account of a people who were happiest when they were moving, and a depiction of a way of life that is gone forever.\n\nCynthia Ann Parker: Cynthia Ann Parker, or Naduah (Comanche \"Narua\") (  1825 – March 1871) was an Anglo-American who was kidnapped in 1836, at the age of about ten (possibly as young as 8 or already over 11 – her birth year is uncertain), by a Comanche war band, who had massacred her family's settlement.  Her Comanche name means \"someone found.\"  She was adopted by the Comanche and lived with them for 24 years, completely forgetting her white ways.  She married a Comanche chieftain, Peta Nocona, and had three children with him, including the last free Comanche chief, Quanah Parker.  At approximately age 34, she was relocated by the Texas Rangers, but spent the remaining ten years of her life refusing to adjust to life in white society.  At least once, she escaped and tried to return to her Comanche family and children, but was again brought back to Texas.  She found it difficult to understand her iconic status to the nation, which saw her as having been redeemed from the Comanches.  Heartbroken over the loss of her family, she stopped eating and died of influenza in 1871.\n\nCherry Springs Dance Hall: Cherry Springs Dance Hall, is one of the oldest and most historic dance halls in Texas.  It is located at 17662 North U.S. Highway 87, Cherry Springs, TX 78624.  The Texas farming community of Cherry Spring is 16 mi NW of Fredericksburg, Texas, in Gillespie County's portion of the Texas Hill Country.  The dance hall was established along the old Pinta Trail in 1889 as a stop for cattle drives.  It was originally run by Herman Lehmann, son of German immigrants, Apache captive and adopted son of Comanche chief Quanah Parker.\n\nQuanah Parker Star House: The Quanah Parker Star House, with stars painted on its roof, is located in the city of Cache, county of Comanche, in the U.S. state of Oklahoma.  It was added to the National Register of Historic Places listings in Comanche County, Oklahoma, in 1970.\n\nComanche County–City Airport: Comanche County–City Airport (ICAO: KMKN, FAA LID: MKN) is a public use airport located two nautical miles (2.3 mi, 3.7 km) northeast of the central business district of Comanche, a city in Comanche County, Texas, United States.  It is owned by the City of Comanche and Comanche County.  The airport is included in the FAA's National Plan of Integrated Airport Systems for 2011–2015, which categorized it as a \"general aviation\" facility.\n\nJohn Richard Parker: John T. Parker (1834–1915) was the brother of Cynthia Ann Parker and the uncle of Comanche chief Quanah Parker.  An Anglo-Texas man of Scots-Irish descent who was kidnapped from his natural family at the age of five by a Native American raiding party, he returned to the Native American people of his own free will after being ransomed back from the Comanche.  He was a member of the large Parker frontier family that settled in east Texas in the 1830s.  He was captured in 1836 by Comanches during the raid of Fort Parker near present-day Groesbeck, Texas.\n\nQuestion: Cache is a city in Comanche County, Oklahoma, it is the location of Star House, the home of the Comanche chief Quanah Parker, was a Comanche war leader of the Quahadi (\"Antelope\") band of which people?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"city_info\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"county\": {\n          \"type\": \"string\"\n        },\n        \"state\": {\n          \"type\": \"string\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"county\",\n        \"state\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"landmark_info\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"owner_chief\": {\n          \"type\": \"string\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"owner_chief\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"chief_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"role\": {\n          \"type\": \"string\"\n        },\n        \"band\": {\n          \"type\": \"string\"\n        },\n        \"people\": {\n          \"type\": \"string\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"role\",\n        \"band\",\n        \"people\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"city_info\",\n    \"landmark_info\",\n    \"chief_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "city_info": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "county": {
            "type": "string"
          },
          "state": {
            "type": "string"
          }
        },
        "required": [
          "name",
          "county",
          "state"
        ],
        "additionalProperties": false
      },
      "landmark_info": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "owner_chief": {
            "type": "string"
          }
        },
        "required": [
          "name",
          "owner_chief"
        ],
        "additionalProperties": false
      },
      "chief_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "role": {
            "type": "string"
          },
          "band": {
            "type": "string"
          },
          "people": {
            "type": "string"
          }
        },
        "required": [
          "name",
          "role",
          "band",
          "people"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "city_info",
      "landmark_info",
      "chief_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

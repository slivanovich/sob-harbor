{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nScott Isaacs: Scott Isaacs is a software architect who is best known for the development of Dynamic HTML (DHTML), which is at the core of what is commonly termed Ajax.  Scott was a partner software architect at Microsoft Corporation for over 20 years before leaving for Amazon.com in September 2013.  One of his first projects at Amazon was to help establish the Amazon Prime Air vision and team.\n\nABX Air: ABX Air, Inc., formerly Airborne Express, is a cargo airline headquartered at Wilmington Air Park near the City of Wilmington, Ohio, USA.  ABX Air operates scheduled, ad hoc charter and ACMI (Aircraft, Crew, Maintenance and Insurance) freight services.  It also provides flight support services and training.  ABX Air is owned by Air Transport Services Group.\n\nWilmington Air Park: Wilmington Air Park (IATA: ILN, ICAO: KILN, FAA LID: ILN) is a public-use airport located two nautical miles (3.7 km) southeast of the central business district of Wilmington, a city in Clinton County, Ohio, United States.  While DHL had privately owned the property while operating from the facility, the company agreed to donate the property to the Clinton County Port Authority.\n\nLondon Air Park: London Air Park, also known as Hanworth Air Park, was a grass airfield in the grounds of Hanworth Park House, operational 1917–1919 and 1929–1947.  It was on the southeastern edge of Feltham, now part of the London Borough of Hounslow.  In the 1930s, it was best known as a centre for private flying, society events, visits by the Graf Zeppelin airship, and for aircraft manufacture by General Aircraft Limited (GAL) 1934–1949.\n\nAmazon Prime Pantry: Amazon Prime Pantry is a service of Amazon.com available only to Amazon Prime members that packages everyday (non-bulk) non-perishable grocery store items into a single box for delivery for a flat fee.  The service is available in the United States, the United Kingdom, Germany, Austria, India, Japan, Italy, Spain, and France.\n\nList of Ripper Street episodes: \"Ripper Street\" is a BBC fictional drama based in Whitechapel following on from the infamous murders of Jack the Ripper.  The first episode was broadcast on 30 December 2012.  A second series was confirmed in January 2013, with the first episode being broadcast on 28 October 2013.  The third series was produced by Amazon Prime Instant Video and uploaded weekly onto the Amazon UK site from November 2014.  A fourth series, again produced by Amazon Prime Instant Video, began airing weekly on the service, beginning 15 January 2016.  This series was originally expected to consist of eight episodes, but ended up consisting of six, including a feature-length (130 min.)  premiere, that was split into two episodes for television broadcast.  The concluding Series 5 premiered in full on Amazon Prime UK on 12 October 2016.  It includes six episodes featuring a runtime of 60 to 75 minutes.\n\nAmazon Prime Air: Amazon Prime Air is a cargo airline that contracts through Air Transport International, ABX Air, and Atlas Air, as well as a conceptual drone-based delivery system currently in development by Amazon.com.  The cargo side is based at Cincinnati/Northern Kentucky International Airport in Hebron, Kentucky, near Cincinnati, Ohio.  The hub began operations on April 30, 2017 and will quickly expand under a $1.49-billion expansion plan with 40 Boeing 767-300F's and 200 daily takeoff and landings.\n\nSt. Johns Industrial Air Park: St. Johns Industrial Air Park (IATA: SJN, ICAO: KSJN, FAA LID: SJN) is a city-owned public-use airport located one nautical mile (1.85 km) north of the central business district of St. Johns, a city in Apache County, Arizona, United States.  The airport is included in the FAA's National Plan of Integrated Airport Systems for 2009–2013, which categorizes it as a \"general aviation\" facility.  The NPIAS report for 2015-2019 classified the Air Park again as General Aviation, in the \"Basic\" asset category, for airports with the lowest levels of activity.\n\nWycombe Air Park: Wycombe Air Park, also known as Booker Airfield (IATA: HYC, ICAO: EGTB) , is an operational general aviation aerodrome located in Booker, Buckinghamshire, 2.4 NM south-west of High Wycombe, England.  Wycombe air park celebrate its 50th year of opening on 25 April 2015.  The airfield opened in 1941 as RAF Booker and was primarily involved in training during World War II, remaining a military establishment until 1965.\n\nBritannia (TV series): Britannia is an upcoming historical period drama written by Jez Butterworth that is scheduled to air on Sky Atlantic in the UK and Ireland, and be available on Amazon Prime Video in the US in 2018.  The ten-part series stars Kelly Reilly, David Morrissey, Zoë Wanamaker, Liana Cornell and Stanley Weber.  The series is the first co-production between Sky and Amazon Prime Video.\n\nQuestion: A airline headquartered in Wilmington Air Park does what for Amazon Prime Air?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"airline_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the airline.\"\n    },\n    \"headquarters_location\": {\n      \"type\": \"string\",\n      \"description\": \"The location where the airline is headquartered.\"\n    },\n    \"related_entity\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the entity with which the airline has a relationship.\"\n    },\n    \"relationship_type\": {\n      \"type\": \"string\",\n      \"description\": \"Describes the nature of the relationship between the airline and the related entity.\"\n    }\n  },\n  \"required\": [\n    \"airline_name\",\n    \"headquarters_location\",\n    \"related_entity\",\n    \"relationship_type\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "airline_name": {
        "type": "string",
        "description": "The name of the airline."
      },
      "headquarters_location": {
        "type": "string",
        "description": "The location where the airline is headquartered."
      },
      "related_entity": {
        "type": "string",
        "description": "The name of the entity with which the airline has a relationship."
      },
      "relationship_type": {
        "type": "string",
        "description": "Describes the nature of the relationship between the airline and the related entity."
      }
    },
    "required": [
      "airline_name",
      "headquarters_location",
      "related_entity",
      "relationship_type"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

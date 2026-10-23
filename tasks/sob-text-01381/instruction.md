{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMaersk: A.P. Moller–Maersk Group (Danish: \"A.P. Møller–Mærsk A/S\", ] ), also known as Maersk, is a Danish business conglomerate with activities in the transport and logistics and energy sectors.  Maersk has been the largest container ship and supply vessel operator in the world since 1996.  The company is based in Copenhagen, Denmark with subsidiaries and offices across 130 countries and around 88,000 employees.\n\nOdense Steel Shipyard: Odense Steel Shipyard (Danish: \"Odense Staalskibsværft\" ) was a Danish shipbuilding company located in Odense.  It was best known for building container ships for its parent group, A.P. Moller – Maersk Group, including the Mærsk E-class in 2006 which at the time were the biggest container ships in the world.  The global financial crisis led to Maersk announcing its closure in 2009 and the last new ship was delivered in January 2012.\n\nClementine Maersk: Clementine Maersk is a container ship property of the largest company for maritime transport and logistics in the world - Maersk Line.  The ship was built in 2002 in the ship-yard of Odense Steel.  The container ship is large and has capacity for 6,600 TEUs according to company statistics and calculations.  The ship is designed with modern and new technologies and large cargo capacity for the year of building.  More than 7 years later we see ships, which has larger cargo capacity and smaller length and beam, which is great sign for the shipbuilding development.\n\nEmma Mærsk: Emma Mærsk is the first container ship in the E-class of eight owned by the A. P. Moller-Maersk Group.  When launched in 2006 she was the largest container ship ever built, and in 2010 she and her seven sister ships were among the longest container ships.  Officially, she is able to carry around 11,000 twenty-foot equivalent units (TEU) or 14,770 TEU depending on definition.  In May 2010, her sister ship \"Ebba Mærsk\" set a record of 15,011 TEU in Tanger-Med, Tangiers.\n\nEleonora Mærsk: Eleonora Mærsk is one of the world's largest container ships operated by A.P. Moller and registered to Svendborg Denmark.  It was constructed in 2006 at the Odense Steel Shipyard and its maiden voyage was the Suez Canal.  There are 7 other identical sister ships in the A.P. Moller fleet.  The Eleonora Maersk and the other seven ships in her class are among the biggest ever built.\n\nPeter Mærsk Møller: Peter Mærsk Møller (22 September 1836 – 9 February 1927) was a sea captain who perhaps is best known as the father of Arnold Peter Møller, founder of the Maersk corporation, and grandfather of Mærsk Mc-Kinney Møller, who made Maersk the largest container ship operator and supply vessel operator in the world.\n\nMærsk E-class container ship: The Maersk E Series comprises eight 14,770 twenty-foot equivalent unit (TEU) container ships.  Each sister ship bear names beginning with the letter \"E\".  Until 2012, they were the largest container ship ever constructed, and are among the longest ships currently in use at 399 metres (1,302 ft) long and 56 metres (184 ft) wide.  They are owned by the Danish A. P. Moller-Maersk Group.  The first in the class built was \"Emma Maersk\" by Odense Steel Shipyard Ltd., Denmark.  The E-class was followed by the Triple-E class, which is even larger and more fuel-efficient.\n\nSovereign Maersk: Sovereign Maersk is container ship, which is part of the fleet of Maersk Line.  The container vessel is operated by AP Moller Maersk Denmark and built in 1997 in the shipyard of Odense Steel Shipyard.  This cargo ship is one of the most discussed ships as a result of a crankcase explosion.  On January 20, 2000, whilst sailing from Hong Kong to Long Beach, an oil mist detector alarm sounded.  The on duty engineer entered the engine room to investigate.  Shortly afterward, a crank case explosion caused by a main engine bearing overheating occurred, causing serious injury to the engineer (who required months of recuperation).  The vessel was towed into Kobe, Japan for repairs.  The problem with the main engine of \"Sovereign Maersk\" was later fixed and in spite of this incident the ship is among the most environmental and most economical ships of Maersk Line built before year 2000.\n\nMarchen Maersk: The Marchen Maersk is owned and operated by the A.P. Moller Maersk.  \"Marchen Maersk\" is one of the largest container ships in the world.  The \"Marchen Maersk\" was christened on 10 May 2008 at Maersk Odense Steel Shipyard in Denmark.  This ship is the first of 12 M-Class vessels.\n\nMV Barzan: Barzan is an ultra large container ship.  It is the first of a series of six 18,800 TEU container ships built for United Arab Shipping Company (UASC) in South Korea.  As of 2015, it stood among the largest container ships in the world.  According to the builder, it has carbon emissions far lower than the Maersk EEE class container ships.\n\nQuestion: Odense Steel Shipyard was best known for building container ships for its parent group the largest container ship and supply vessel operator in the world since what year?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"company_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the company that holds the status.\"\n    },\n    \"status_description\": {\n      \"type\": \"string\",\n      \"description\": \"The description of the status held by the company.\"\n    },\n    \"status_start_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year since which the company has held this status.\"\n    },\n    \"related_entity\": {\n      \"type\": \"string\",\n      \"description\": \"The entity related to the company's parent group mentioned in the question.\"\n    }\n  },\n  \"required\": [\n    \"company_name\",\n    \"status_description\",\n    \"status_start_year\",\n    \"related_entity\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "company_name": {
        "type": "string",
        "description": "The name of the company that holds the status."
      },
      "status_description": {
        "type": "string",
        "description": "The description of the status held by the company."
      },
      "status_start_year": {
        "type": "integer",
        "description": "The year since which the company has held this status."
      },
      "related_entity": {
        "type": "string",
        "description": "The entity related to the company's parent group mentioned in the question."
      }
    },
    "required": [
      "company_name",
      "status_description",
      "status_start_year",
      "related_entity"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

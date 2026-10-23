{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nList of aircraft of the Royal Air Force: Many aircraft types have served in the British Royal Air Force since its formation in April 1918 from the merger of the Royal Flying Corps and Royal Naval Air Service.  This is a list of RAF aircraft, including all currently active and retired types listed in alphabetic order by their RAF type name.  For just those aircraft currently in service, see List of active United Kingdom military aircraft.  Aircraft operated with the Fleet Air Arm from 1924 until 1939 were operated by the Royal Air Force on behalf of the Navy and are included but not those operated by the Royal Navy after it re-acquired control of the aircraft used to support its operations in 1939 are not, but all aircraft operated in conjunction with the Navy are listed at List of aircraft of the Fleet Air Arm.  Army Air Corps aircraft are not included but can be found at List of aircraft of the Army Air Corps.\n\nList of Nepalese List A cricketers: This is a list of Nepalese List A cricketers.  List A cricket matches are those between international teams or the highest standard of domestic teams.  Matches played in the tournament of World Cricket League division 2 and above also qualify as List A.  This list is not limited to those who have played List A cricket for Nepal and may include Nepalese players who played their List A cricket elsewhere.  The players are listed alphabetically by their last name.\n\nList of National Trust properties in Wales: Below is a list of the stately homes, historic houses, castles, abbeys, museums, estates, coastline and open country in the care of the National Trust in Wales, grouped into the unitary authority areas.  Many areas of land owned by the trust, both open-access and closed to the public, are not listed here.  This is a list of the more notable sites, generally defined as those having either an entry in the National Trust handbook, or a page on their website.  There are many other areas of moorland and open country, agricultural holdings and coastline belonging to the National Trust, that are not listed here.\n\nTianjin Port Holdings: Tianjin Port Holdings Company Limited (), formerly Tianjin Port Storage and Transportation Holdings Limited, is engaged in the operations of Tianjin Port, the warehousing and storage of cargo and the provision of freight forwarding and shipping brokerage services.  It is parented by Tianjin Port (Group).  Its A shares were listed on the Shanghai Stock Exchange in 1996.  Its name was changed to Tianjin Port Holdings Company Limited in 1998.\n\nT&amp;D Holdings: T&D Holdings is a Japanese insurance company.  It is listed on the Nikkei 225.  It is based in Tokyo, Japan.\n\nKatakura Kojūrō: Katakura Kojūrō (片倉 小十郎 ) was the common name of the head of the Japanese Katakura clan, who served as senior retainers to the Date clan.  Following the Date clan's move into Sendai han, they were granted holdings at Shiroishi Castle (12,000 \"koku\" in total), which they held through the start of the Meiji Era.  A chronologically arranged list of the generations of Edo-era Katakura Kojūrō (listed by their formal name) follows:\n\nList of jungle and drum and bass artists: This is a list of jungle and drum and bass artists.  This includes notable artists who have either been very important to the genre or have had a considerable amount of exposure (such as those who have been on a major label).  This list does not include little-known local artists.  Artists are listed by the first letter in their name (not including the words \"a\", \"an\", or \"the\"), and individuals are listed by last name.  For a list specific to jungle and drum and bass emcees, see List of jungle and dnb emcees.\n\nNikkei 225: The Nikkei 225 (日経平均株価 , Nikkei heikin kabuka , 日経225) , more commonly called the Nikkei, the Nikkei index, or the Nikkei Stock Average ( , , or ), is a stock market index for the Tokyo Stock Exchange (TSE).  It has been calculated daily by the \"Nihon Keizai Shinbun\" (\"Nikkei\") newspaper since 1950.  It is a price-weighted index (the unit is yen), and the components are reviewed once a year.  Currently, the Nikkei is the most widely quoted average of Japanese equities, similar to the Dow Jones Industrial Average.  In fact, it was known as the \"Nikkei Dow Jones Stock Average\" from 1975 to 1985.\n\nAdvanced Card Systems Holdings: Advanced Card Systems Ltd (ACS) is a Hong Kong-based company founded by Denny Wong in 1995.  It is a fully owned subsidiary of Advanced Card Systems Holdings Ltd., a publicly listed company on the Hong Kong Stock Exchange.  ACS develops smart cards, smart card readers and related products, and distributes them to over one hundred countries.  It was ranked by Frost & Sullivan as one of the world's top 3 suppliers and Asia Pacific's top supplier of PC-linked Smart Card Readers.  In 2010, 2014, and 2015, it was listed among \"Forbes Asia\"' s \"Best Under a Billion\", a prestigious list of 200 top-performing companies with sales between US$5 million and US$1 billion, selected from publicly listed enterprises in Asia Pacific.\n\nDavid Consunji: David M. Consunji (October 18, 1921 – September 4, 2017) was the chairman of a publicly listed holding firm, DMCI Holdings, Incorporated ().  He was a former secretary of the Department of Public Works, Transportation and Communications from 1970 to 1975, during the Marcos administration.  In 2014, Forbes listed him as the 6th richest Filipino, with a net worth of US$3.9 billion.\n\nQuestion: What was the name, from 1975 to 1985, of the list T&D Holdings is listed on?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"company_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the company listed on the index.\"\n    },\n    \"index_name_current\": {\n      \"type\": \"string\",\n      \"description\": \"The current name of the stock market index.\"\n    },\n    \"index_name_historical\": {\n      \"type\": \"string\",\n      \"description\": \"The historical name of the stock market index during a specific period.\"\n    },\n    \"historical_period_start_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The start year of the historical period for the index name.\"\n    },\n    \"historical_period_end_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The end year of the historical period for the index name.\"\n    }\n  },\n  \"required\": [\n    \"company_name\",\n    \"index_name_current\",\n    \"index_name_historical\",\n    \"historical_period_start_year\",\n    \"historical_period_end_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "company_name": {
        "type": "string",
        "description": "The name of the company listed on the index."
      },
      "index_name_current": {
        "type": "string",
        "description": "The current name of the stock market index."
      },
      "index_name_historical": {
        "type": "string",
        "description": "The historical name of the stock market index during a specific period."
      },
      "historical_period_start_year": {
        "type": "integer",
        "description": "The start year of the historical period for the index name."
      },
      "historical_period_end_year": {
        "type": "integer",
        "description": "The end year of the historical period for the index name."
      }
    },
    "required": [
      "company_name",
      "index_name_current",
      "index_name_historical",
      "historical_period_start_year",
      "historical_period_end_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

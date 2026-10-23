{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCopp's Hill: Copp's Hill is an elevation in the historic North End of Boston, Massachusetts.  It is bordered by Hull Street, Charter Street and Snow Hill Street.  The hill takes its name from William Copp, a shoemaker who once owned the land.  Copp's Hill Burying Ground is a stop on the Freedom Trail.\n\nSamuel Corning House: The Samuel Corning House is a historic First Period house at 87 Hull Street in Beverly, Massachusetts.  It is a 2.5 story five bay house with a central chimney that was apparently built in stages, and is also notable for early 20th century preservation actions.  The first portion, to the right of the chimney, was built c. 1700 as a typical First Period two story single cell structure.  Around 1720 the left side was built, and a leanto section was added to the back at a somewhat later date.\n\nEast Chicago Street Historic District: The East Chicago Street Historic District is a mixed residential and commercial historic district located in Coldwater, Michigan.  The original portion of the district, running along Chicago Street from Wright Street to Division Street, was listed on the National Register of Historic Places in 1975.  Two boundary increases were added in 1990, one running roughly along Pearl Street between Hudson and Lincoln Streets, and the other roughly along Church Street from Jefferson to Daugherty Streets, along with the block of Park Place north of Church and the block of Hull Street west of Park Place.\n\nBeverly, Massachusetts: Beverly is a city in Essex County, Massachusetts, United States.  The population was 39,502 at the 2010 census.\n\nWalter Rathbone Bacon: Walter Rathbone Bacon (February 22nd, 1845 - November 14th, 1917) was an American capitalist who organised a system of tramways in Europe.  Over his career, Bacon acted as director of Imperial Tramways Company, London Street Tramways Company, Corris Railway Company, Bell Punch Company Ltd., Hull Street Tramways Company, North Metropolitan Tramway Company and Belfast Street Tramways Company.\n\nHull High: Hull High (also known as Hull Street High) is an American musical teen drama series which aired on the NBC television network in 1990.  The series was created and executive produced by Gil Grant.\n\nOld School of Mines, Kimberley: The Old School of Mines building in Hull Street, Kimberley, is where the South African School of Mines was established in 1896, later evolving into the Transvaal University College, and eventually into both the University of the Witwatersrand and the University of Pretoria.  In 1904 the school was moved to Johannesburg, becoming the Transvaal Technical Institute which, in turn, was renamed the Transvaal University College in 1906.  The separation of Johannesburg and Pretoria campuses in 1910 paved the way for establishment of the Universities of the Witwatersrand (1922) and of Pretoria (1930).\n\nSkinny House (Boston): The Skinny House at 44 Hull Street in the North End of Boston, Massachusetts, USA, is an extremely narrow four-story house reported by the \"Boston Globe\" as having the \"uncontested distinction of being the narrowest house in Boston.\"  According to the executive director of the Boston Landmarks Commission, \"In a city where there are many narrow lots, this far exceeds the norm.  ... As far as we know, it is the narrowest house in Boston.\"  It was originally built as a spite house.\n\nLevi S. Gould: Levi Swanton Gould (March 27, 1831 – March 22, 1917) was an American businessman and politician who served as a member, and chairman of the Middlesex County, Massachusetts county commission, and as the first mayor of Melrose, Massachusetts.\n\nHull Street Station: Hull Street Station was a railroad station in the city of Richmond, Virginia.  It was built by the Southern Railway to replace Mill Street Station across the river in Richmond.  The station, which had been closed, was damaged in several floods of the James River before Richmond's flood wall was completed in 1995.  Since 2011, it has been the site of the Richmond Railroad Museum.\n\nQuestion: In what Massachusetts county does the house at 87 Hull Street, Beverly, Massachusetts reside?   \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"house_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the historic house.\"\n    },\n    \"house_address\": {\n      \"type\": \"string\",\n      \"description\": \"The street address of the house.\"\n    },\n    \"city\": {\n      \"type\": \"string\",\n      \"description\": \"The city where the house is located.\"\n    },\n    \"state\": {\n      \"type\": \"string\",\n      \"description\": \"The state where the house is located.\"\n    },\n    \"county\": {\n      \"type\": \"string\",\n      \"description\": \"The county where the house is located.\"\n    }\n  },\n  \"required\": [\n    \"house_name\",\n    \"house_address\",\n    \"city\",\n    \"state\",\n    \"county\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "house_name": {
        "type": "string",
        "description": "The name of the historic house."
      },
      "house_address": {
        "type": "string",
        "description": "The street address of the house."
      },
      "city": {
        "type": "string",
        "description": "The city where the house is located."
      },
      "state": {
        "type": "string",
        "description": "The state where the house is located."
      },
      "county": {
        "type": "string",
        "description": "The county where the house is located."
      }
    },
    "required": [
      "house_name",
      "house_address",
      "city",
      "state",
      "county"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPete V. Domenici United States Courthouse: The Pete V. Domenici United States Courthouse is a federal courthouse located in downtown Albuquerque, New Mexico.  The building was completed in 1998 and named in honor of Senator Pete Domenici at a ceremony in 2004.  Since its completion it has been joined at the intersection of Fourth and Lomas by two additional courthouses, the Bernalillo County Courthouse on the southwest corner and the Metropolitan Courthouse on the northwest corner.  The seven-story courthouse is 176 ft tall, placing it tenth on the list of Albuquerque's tallest buildings.\n\nAl D'Amato: Alfonse Marcello D'Amato (born August 1, 1937) is an American lawyer and former New York politician.  A Republican, he served as United States Senator from New York from 1981 to 1999.  He subsequently founded a lobbying firm, Park Strategies.\n\nUnited States Courthouse (Austin, Texas, 1936): The Austin United States Courthouse is a historic former federal courthouse in downtown Austin, Texas.  Built between 1935 and 1936, the building exemplifies Depression-era Moderne architecture, while Art Moderne and Art Deco finishes characterize the interior.  It housed Austin's United States district court and other judicial offices until 2012, when a new federal courthouse building was completed.  The structure was added to the National Register of Historic Places in 2001.\n\nAlfonse M. D'Amato United States Courthouse: The Alfonse M. D'Amato United States Courthouse is a federal courthouse for the United States District Court for the Eastern District of New York.  It is located at 100 Federal Plaza in Central Islip on Long Island in New York.  It is named after former U.S. Senator Al D'Amato of New York, a native of Long Island.\n\nJames A. Redden Federal Courthouse: The James A. Redden Federal Courthouse, formerly the United States Post Office and Courthouse, is federal courthouse located in Medford, Oregon, United States.  Completed in 1916 under the supervision of architect Oscar Wenderoth, it houses the United States District Court for the District of Oregon.  A substantial extension was completed in 1940, under the supervision of architect, Louis A. Simon.  In September 1996, the United States Senate enacted a bill introduced by Oregon Senator Mark Hatfield to rename the building for long-serving District Court judge James A. Redden.\n\nRoman L. Hruska Federal Courthouse: The Roman L. Hruska Federal Courthouse is a 350000 sqft Federal Courthouse located at 111 S. 18th Plz.  in Downtown Omaha, Nebraska.  Completed in 2000, the six story courthouse serves the United States District Court for the District of Nebraska, and features nine courtrooms and a central atrium; built at a cost of $70 million.  It was dedicated October 24, 2000, in front of an audience of over 400 people.  The courthouse is built on the former site of several historic buildings, including the Hotel Fontenelle, razed in 1983.  and the Omaha Athletic Club, razed in 1992.  It was the first courthouse in the country to be built under the GSA’s Design Excellence Program.\n\nGus J. Solomon United States Courthouse: The Gus J. Solomon United States Courthouse is a federal courthouse located in downtown Portland, Oregon, United States.  Completed in 1933, it previously housed the United States District Court for the District of Oregon until the Mark O. Hatfield United States Courthouse opened in 1997.  The Renaissance Revival courthouse currently is used by commercial tenants and formerly housed a U.S. Postal Service branch.  In 1979, the building was added to the National Register of Historic Places as U.S. Courthouse.\n\nWayne Lyman Morse United States Courthouse: The Wayne Lyman Morse United States Courthouse is a federal courthouse located in Eugene, Oregon.  Completed in 2006, it serves the District of Oregon as part of the Ninth Judicial Circuit.  The courthouse is named in honor of former U.S. Senator Wayne Morse who represented Oregon for 24 years in the Senate and was a Eugene area resident.  Located in downtown Eugene, the building overlooks the Willamette River.\n\nLee County Courthouse (Fort Madison, Iowa): The Lee County Courthouse in Fort Madison, Iowa, United States was built in 1842.  It was listed on the National Register of Historic Places in 1976 as a part of the County Courthouses in Iowa Thematic Resource.  The courthouse serves the court functions and county administration for the northern part of Lee County, and is the county’s first courthouse.  Southern Lee County is served from a courthouse in Keokuk in a former Federal Courthouse building.  It is listed on the National Register of Historic Places as the U.S. Post Office and Courthouse.\n\nErie Federal Courthouse: The Erie Federal Courthouse and Post Office, also known as Erie Federal Courthouse, in Erie, Pennsylvania, is a complex of buildings that serve as a courthouse of the United States District Court for the Western District of Pennsylvania, and house other federal functions.  The main courthouse building was built in 1937 in Moderne architecture style.  It served historically as a courthouse, as a post office, and as a government office building.  It was listed on the National Register of Historic Places in 1993.  By the late 1980s, the federal courts needed more space to effectively serve the public.  To resolve the space shortage, the General Services Administration undertook a bold plan to purchase, restore, and adaptively use two adjacent historic buildings: the Main Library and the Isaac Baker & Son Clothing Store.  The existing courthouse was rehabilitated and two additions were constructed.  Each of the buildings in the complex is of a different architectural style.\n\nQuestion: The Senator and founder of lobbying firm, Park Strategies, has a federal courthouse named after him located where? \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_named\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person after whom the courthouse is named.\"\n    },\n    \"person_role\": {\n      \"type\": \"string\",\n      \"description\": \"The primary role or title of the person.\"\n    },\n    \"courthouse_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the federal courthouse.\"\n    },\n    \"courthouse_location\": {\n      \"type\": \"string\",\n      \"description\": \"The specific city or area where the courthouse is located.\"\n    },\n    \"state\": {\n      \"type\": \"string\",\n      \"description\": \"The state where the courthouse is located.\"\n    }\n  },\n  \"required\": [\n    \"person_named\",\n    \"person_role\",\n    \"courthouse_name\",\n    \"courthouse_location\",\n    \"state\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_named": {
        "type": "string",
        "description": "The name of the person after whom the courthouse is named."
      },
      "person_role": {
        "type": "string",
        "description": "The primary role or title of the person."
      },
      "courthouse_name": {
        "type": "string",
        "description": "The full name of the federal courthouse."
      },
      "courthouse_location": {
        "type": "string",
        "description": "The specific city or area where the courthouse is located."
      },
      "state": {
        "type": "string",
        "description": "The state where the courthouse is located."
      }
    },
    "required": [
      "person_named",
      "person_role",
      "courthouse_name",
      "courthouse_location",
      "state"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

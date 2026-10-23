{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nNew York State Route 434: New York State Route 434 (NY 434) is a state highway located in the Southern Tier of New York in the United States.  The route extends for 20.89 mi from an intersection with NY 96 in the village of Owego to an intersection with U.S. Route 11 (US 11) in the city of Binghamton.  In between, NY 434 passes through the towns of Owego and Vestal.  The portion of NY 434 from the Tioga–Broome county line to downtown Binghamton is known as Vestal Parkway.\n\nBinghamton Bearcats baseball: The Binghamton Bearcats baseball team is a varsity intercollegiate athletic team of Binghamton University in Vestal, New York, United States.  The team is a member of the America East Conference, which is part of the National Collegiate Athletic Association's Division I.  The team plays its home games at Varsity Field in Vestal, New York.  The Bearcats are coached by Tim Sinicki.\n\nDonna Lupardo: Donna A. Lupardo (born August 17, 1954) is a member of the New York State Assembly representing the 123rd Assembly District, which includes the city of Binghamton, New York, as well as the towns of Vestal, New York and Union, New York.  The villages of Johnson City, New York and Endicott, New York are contained within the Town of Union and also make up part of the district.\n\nBinghamton Bearcats wrestling: The Binghamton Bearcats wrestling team represents Binghamton University of Vestal, New York.  The squad was coached by Pat Popolizio, a former wrestler for the Oklahoma State Cowboys, who left in 2012 to take the head wrestling coach position at North Carolina State University.  Popolizio was succeeded by Matt Dernlan who had been the head coach of the Clarion Golden Eagles.  Binghamton has fielded a college wrestling team since 1969.  The team competed on the Division III level until 1998.  The Bearcats moved to Division II in 1999 and Division I in 2002.  The wrestling team joined the Eastern Intercollegiate Wrestling Association in July 2013.  Previously, it had been an associate member of the Colonial Athletic Association, but conference realignment led the CAA to drop the sport.  The rest of Binghamton's intercollegiate teams, excepting golf, are members of the America East Conference.  The Bearcats have had four All-American wrestlers (Josh Patterson 7th, Justin Lister 4th, Nick Gwiazdowski 8th, Donald Vinson 3rd) since joining Division I and had 25 All-Americans in Divisions II and III.\n\nWLTB: WLTB is the callsign of a top 40/CHR radio station licensed to Johnson City, New York and serves the Greater Binghamton Market .  The station is owned by GM Broadcasting and broadcasts on 101.7 MHz from Ingraham Hill in Binghamton.  It also has a translator @ 102.5 on Bornt Hill in Endicott, NY.  It is only one of two locally owned radio stations in the Binghamton market.  Studios for WLTB were originally located on McMaster Street in Owego N.Y.  It was relocated to the Executive Inn in Endicott N.Y. in 1993, next to the Vestal Parkway in 1998, then in December 2009 to 3215 E. Main Street in Endwell N.Y.  The station is currently located at 2801 East Main Street in the Endwell Plaza.  Moved a few blocks down in October 2015.\n\nSihamir Osmanov: Sihamir Osmanov (Macedonian: Шихамир Османов ; born May 25, 1975 in Makhachkala, Russian SFSR) is a retired amateur Macedonian freestyle wrestler, who competed in the men's middleweight category.  He finished fifth in the 74-kg division at the 2003 World Wrestling Championships in New York City, New York, United States, and later represented the Republic of Macedonia at the 2004 Summer Olympics.  Osmanov also trained full-time as a member of the wrestling squad for Varda Makedonia Sports Club in Skopje under his personal coach and 2000 Olympian Nasir Gadzhikhanov.\n\nJohnson City High School (New York): Johnson City High School is a public high school located in Johnson City, New York, a village in Broome County adjacent to Binghamton.  The school, originally situated on Main Street in downtown Johnson City, was relocated to where it currently stands on Reynolds Road.\n\nJohnson City Historic District: Johnson City Historic District is a national historic district located at Johnson City, Broome County, New York.  It encompasses 183 contributing buildings and 1 contributing site in a mixed, residential, commercial, and industrial core of Johnson City.  It developed between about 1888 and 1966, and includes notable examples of Romanesque Revival, Gothic Revival, Colonial Revival, and Streamline Moderne style architecture.  Located in the district are the previously listed Goodwill Theatre, United States Post Office, and Your Home Library.  Other notable contributing resources include the Endicott-Johnson Athletic Association East Branch Recreational Center (1947), St. James Roman Catholic Church Complex (1914-1950), Ash Block (c. 1901), Tacoma Block (1892, 1945), Rich Block, Dawson Block (1898-1899), Woolworths (c. 1937), Men's Quality Shop (1966), Red Robin Diner (1950, 1959), Thompson Hall (1951), Sarah Jane Johnson Methodist Church (1927), Charles F. Johnson, Jr., House (1919), Endicott-Johnson's Pioneer Annex (1916), Endicott-Johnson's Jigger Factory (1926), Endicott-Johnson's Sunrise Building (1929), Eagle Felt Mill (1898), Ansco Factory and Gate House (1947), Endicott-Johnson's Medical Facility (1918), Endicott-Johnson's Victory Factory (1919-1920), Endicott-Johnson's New Toe Box Factory (1914), Endicott-Johnson's Firehouse (1916), and the Village Hall and Fire Station (1899).\n\nNew York State Route 201: New York State Route 201 (NY 201) is a north–south state highway located west of the city of Binghamton in Broome County, New York.  The southern terminus of the route is at NY 434 in Vestal while the northern terminus is at an interchange with NY 17 (future Interstate 86) in Johnson City.\n\nBinghamton University: The State University of New York at Binghamton, commonly referred to as Binghamton University or SUNY Binghamton, is a public research university with campuses in Binghamton, Vestal, and Johnson City, New York, United States.  Since its establishment as Triple Cities College in 1946, the school has evolved from a small liberal arts college to a large doctoral-granting institution.  Presently consisting of eight colleges and schools, it is now home to more than 17,000 undergraduate and graduate students.  Binghamton is one of the four university centers in the State University of New York (SUNY) system.\n\nQuestion: What  is a public research university with campuses in Binghamton, Vestal, and Johnson City, New York, United States, who's wrestling squad was coached by Pat Popolizio?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"university_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the university.\"\n    },\n    \"university_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of institution the university is (e.g., public research university).\"\n    },\n    \"campus_locations\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of cities where the university has campuses.\"\n    },\n    \"wrestling_team_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the university's wrestling team.\"\n    },\n    \"former_wrestling_coach\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the former wrestling coach for the university's team.\"\n    }\n  },\n  \"required\": [\n    \"university_name\",\n    \"university_type\",\n    \"campus_locations\",\n    \"wrestling_team_name\",\n    \"former_wrestling_coach\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "university_name": {
        "type": "string",
        "description": "The name of the university."
      },
      "university_type": {
        "type": "string",
        "description": "The type of institution the university is (e.g., public research university)."
      },
      "campus_locations": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of cities where the university has campuses."
      },
      "wrestling_team_name": {
        "type": "string",
        "description": "The name of the university's wrestling team."
      },
      "former_wrestling_coach": {
        "type": "string",
        "description": "The name of the former wrestling coach for the university's team."
      }
    },
    "required": [
      "university_name",
      "university_type",
      "campus_locations",
      "wrestling_team_name",
      "former_wrestling_coach"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

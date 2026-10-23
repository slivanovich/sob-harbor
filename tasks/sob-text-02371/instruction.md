{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nHasanpur Lodha: Hasanpur Lodha is a village panchayat located in the Hapur district of Uttar Pradesh state, India.  The latitude 28.6354392 and longitude 77.559076 are the geocoordinate of the Hasanpur Lodha.  The other nearest state capital from Hasanpur Lodha is Delhi and its distance is 34.1 km.  The other surrounding state capitals are Delhi 34.1 km., Dehradun 179.0 km., Chandigarh 246.9 km.  Hasanpur Lodha is a Village in Dhaulana Tehsil in Hapur District of Uttar Pradesh State, India.  It belongs to Meerut Division.  It is located 17 km towards East from District headquarters Ghaziabad.  9 km from Dhaulana.  453 km from State capital Lucknow.\n\nUniversidad Autónoma del Estado de México: The Universidad Autónoma del Estado de México (UAEM) (Autonomous University of Mexico State) is a public university in the State of Mexico, Mexico.  It is the largest university institution in the state with over 84,500 students, with its central campus located in the state capital of Toluca.  Formalised as a university under the UAEM name in 1956, the institution traces its origins back to 1828 with the foundation Instituto Literario del Estado de México, in the former state capital of Tlalpan.  In 1943 the institution was augmented to become the Instituto Científico y Literario de Toluca (ICLA), and thirteen years later obtaining its present name and institutional status.  The UAEM has graduated many notable alumni, the best-known is the artist Mariana Galán.\n\nMünchen-Nürnberg-Express: The München-Nürnberg-Express (literally: \"Munich-Nuremberg Express\") is a RegionalExpress train service in the southern German state of Bavaria, connecting the two main cities of the state, Munich and Nuremberg.  With its maximum speed of 200 km/h (125 mph), the train is currently (as of 2011 ) the fastest regional train service in Germany.  The train was formerly known under the project name FRESH, expanding to FRanken-Express über die Schnellfahrstrecke in die LandesHauptstadt (\"FRanconia Express via the High speed line to the state Capital\").\n\nBahari, Sidhi: Bahari is a Tehsil and a village Panchayat in Sidhi district in the Indian state of Madhya Pradesh.  Bhopal is the state capital for Bahari village.  It is located around 587 km from Bahari.  The other nearest state capital from Bahari is Lucknow and its distance is 385.1 km.  The other surrouning state capitals are Patna 442.7 km and Ranchi 416.6 km\n\nMuzaffarpur: Muzaffarpur (   ) is a sub-metropolitan city located in Muzaffarpur district in the Tirhut region of Bihar.  It serves as the headquarters of Tirhut division, Muzaffarpur district and the Muzaffarpur Railway District.  It is the second bigggest and important city in Bihar after Capital Patna.  It is also amongst the few cities in Bihar other than state capital Patna which fulfill nearly all the criteria to be called a Sub Metropolitan City.  It is located at a distance of 68 kilometres from state capital Patna.\n\nPhoenix, Arizona: Phoenix ( ) is the capital and most populous city of the U.S. state of Arizona.  With 1,615,017 people (as of 2016 ), Phoenix is the fifth most populous city nationwide, the most populous state capital in the United States, and the only state capital with a population of more than one million residents.\n\nGovernor's Mansion (Shawnee, Oklahoma): The Governor's Mansion in Shawnee, Oklahoma was built in 1903, on the speculation that Shawnee would be selected as the state capital and that this structure would become the Governor's official residence when Oklahoma became a state.  However, Oklahoma did not attain statehood until 1907, and the Legislature chose Guthrie as the first capital, before naming Oklahoma City as the permanent state capital in 1910.\n\nConcord, New Hampshire: Concord is the capital city of the U.S. state of New Hampshire and the county seat of Merrimack County.  As of the 2010 census, its population was 42,695.\n\nAustin, Texas: Austin ( , ) is the capital of the U.S. state of Texas and the seat of Travis County, with portions extending into Hays and Williamson counties.  It is the 11th-most populous city in the United States and the 4th most populous city in Texas.  It is the fastest growing large city in the United States and the second most populous state capital in the U.S after Phoenix, Arizona.  As of the U.S. Census Bureau's July 1, 2016 estimate, Austin has a population of 947,890.  Located in Central Texas in the foothills of Texas Hill Country, the city is home to numerous lakes, rivers, and waterways including Lady Bird Lake, Barton Springs, McKinney Falls, the Colorado River, Lake Travis, and Lake Walter E. Long.  It is the cultural and economic center of the Austin–Round Rock metropolitan area, which had an estimated population of 2,056,405 as of July 1, 2016.  It is the most populous state capital in the U.S that isn't the most populous city in a state.\n\nSamuel Adams Holyoke: Samuel Holyoke (October 15, 1762 - February 7, 1820) was an American composer and teacher of vocal and instrumental music, was the son of Rev. Elizur Holyoke and Hannah Peabody.  He was born October 15, 1762 in Boxford, Massachusetts, and died February 7, 1820 in Concord, New Hampshire.  He was a Congregationalist and a Mason, and never married.\n\nQuestion: What state capital did Samuel Holyoke die in?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person.\"\n    },\n    \"death_location_city\": {\n      \"type\": \"string\",\n      \"description\": \"The city where the person died.\"\n    },\n    \"death_location_state\": {\n      \"type\": \"string\",\n      \"description\": \"The state where the person died.\"\n    },\n    \"is_state_capital\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the death location city is a state capital.\"\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"death_location_city\",\n    \"death_location_state\",\n    \"is_state_capital\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The name of the person."
      },
      "death_location_city": {
        "type": "string",
        "description": "The city where the person died."
      },
      "death_location_state": {
        "type": "string",
        "description": "The state where the person died."
      },
      "is_state_capital": {
        "type": "boolean",
        "description": "Indicates if the death location city is a state capital."
      }
    },
    "required": [
      "person_name",
      "death_location_city",
      "death_location_state",
      "is_state_capital"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

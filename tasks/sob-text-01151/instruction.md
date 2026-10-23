{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAlbuquerque Convention Center: Albuquerque Convention Center is a multipurpose convention and performing arts center in Albuquerque, New Mexico.  It is New Mexico's largest convention center.\n\nOrange County Convention Center: The Orange County Convention Center (OCCC) is the primary public convention center for the Central Florida region.  The center currently ranks as the second largest convention center in the United States (the biggest is McCormick Place in Chicago).  The OCCC offers 7000000 sqft of total space, 2100000 sqft of which is exhibit space.  The large complex is located on the south end of International Drive, a major tourist area in Orlando, Florida.  Solar panels on the roof of the South Concourse provide 1 MW of power.  On April 18, 2012, the American Institute of Architects's Florida Chapter placed the building on its list of \"Florida Architecture: 100 Years.  100 Places\".\n\nPuerto Rico Convention Center: The Puerto Rico Convention Center Dr. Pedro Rosselló González\" (PRCC) (or \"Centro de Convenciones de Puerto Rico Dr. Pedro Rosselló González\" \"' in Spanish) is a convention center located in Isla Grande (recently named the Convention Center District), in San Juan, Puerto Rico owned by the Puerto Rico Convention District Authority, a government agency of Puerto Rico, and managed by AEG (property management).  Designed by tvsdesign, it is the largest convention center in the Caribbean and one of the most technologically advanced in The Americas.\n\nLansing Center: Lansing Center, officially the Lansing Convention Center, is the primary and largest convention center in Lansing, Michigan.  The center is located along Michigan Avenue, with its western facade fronting the Grand River.  The center's location includes a riverfront plaza that has been home to outdoor events.  It is also directly connected to the Lansing Radisson Hotel by an enclosed, climate-controlled skybridge spanning the Grand River.  Since 1996, Lansing Center has been managed by the non-profit Lansing Entertainment & Public Facilities Authority (LEPFA).\n\nSands Expo: The Sands Expo and Convention Center is a large convention center.  It opened in 1990 across the street from the original Sands Hotel, was the second largest convention center in the world when it opened.\n\nSuburban Collection Showplace: Suburban Collection Showplace is a convention center and exposition center in Novi, Michigan, which forms part of Metro Detroit.  Suburban Collection Showplace is owned by TBON, LLC., a corporation located in Novi.  The center is in proximity to Interstate 96, and is about 20 mi west-northwest of Detroit.  it is the second largest convention center facility in Metro Detroit, after the Cobo Center in Downtown Detroit.  The complex hosts the Michigan State Fair and has done so since 2012.\n\nInternational Convention Center (Jerusalem): The International Convention Center (Hebrew: מרכז הקונגרסים הבינלאומי‎ ‎ , \"Merkaz HaKongresim HaBeinLeumi\"), commonly known as Binyenei HaUma (Hebrew: בנייני האומה‎ ‎ , lit.  \"Buildings of the nation\"), is a concert hall and convention center in Giv'at Ram in Jerusalem.  It is the largest convention center in the Middle East.\n\nGeorgia International Convention Center: The Georgia International Convention Center or GICC, opened in April 2009, is the second largest convention center in the U.S. state of Georgia, second only to the Georgia World Congress Center.  It is located at 2000 Convention Center Concourse, just off Camp Creek Parkway (S.R. 6) and Roosevelt Highway (U.S. 29) in College Park.  The Convention Center is accessible from the Airport MARTA station (via a connection to the ATL Skytrain), Interstate 285, and Interstate 85.\n\nThe Palazzo: The Palazzo is a luxury hotel and casino resort located on the Las Vegas Strip in Paradise, Nevada.  It is the tallest completed building in Nevada.  Designed by the Dallas based HKS, Inc., the hotel offers luxury in an Italian Renaissance ambiance.  The hotel and casino are part of a larger complex (operated as one hotel) comprising the adjoining Venetian Resort and Casino and the Sands Convention Center, all of which are owned and operated by the Las Vegas Sands Corporation.\n\nJaffa Shrine Center: The Jaffa Shrine Center is a 3,200-seat multipurpose arena located in Altoona, Pennsylvania.  The current Shrine Center, headquarters to the Jaffa Shriners, was built in 1930, opening on September 25 of that year.  It was the largest convention center in Blair County until the Blair County Convention Center was built.\n\nQuestion: The second largest convention center on its opening in 1990 is owned by what company?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"convention_center_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the convention center.\"\n    },\n    \"opening_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The year the convention center opened.\"\n    },\n    \"ranking_at_opening\": {\n      \"type\": \"string\",\n      \"description\": \"The ranking of the convention center at the time of its opening.\"\n    },\n    \"owner_company\": {\n      \"type\": \"string\",\n      \"description\": \"The company that owns the convention center.\"\n    },\n    \"associated_properties\": {\n      \"type\": \"array\",\n      \"description\": \"Other properties associated with the convention center under the same ownership.\",\n      \"items\": {\n        \"type\": \"string\"\n      }\n    }\n  },\n  \"required\": [\n    \"convention_center_name\",\n    \"opening_year\",\n    \"ranking_at_opening\",\n    \"owner_company\",\n    \"associated_properties\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "convention_center_name": {
        "type": "string",
        "description": "The name of the convention center."
      },
      "opening_year": {
        "type": "integer",
        "description": "The year the convention center opened."
      },
      "ranking_at_opening": {
        "type": "string",
        "description": "The ranking of the convention center at the time of its opening."
      },
      "owner_company": {
        "type": "string",
        "description": "The company that owns the convention center."
      },
      "associated_properties": {
        "type": "array",
        "description": "Other properties associated with the convention center under the same ownership.",
        "items": {
          "type": "string"
        }
      }
    },
    "required": [
      "convention_center_name",
      "opening_year",
      "ranking_at_opening",
      "owner_company",
      "associated_properties"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

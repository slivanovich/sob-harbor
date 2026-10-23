{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nLion's mane jellyfish: The lion's mane jellyfish (\"Cyanea capillata\"), also known as the giant jellyfish or the hair jelly, is the largest known species of jellyfish.  Its range is confined to cold, boreal waters of the Arctic, northern Atlantic, and northern Pacific Oceans.  It is common in the English Channel, Irish Sea, North Sea and in western Scandinavian waters south to Kattegat and Øresund.  It may also drift in to the south-western part of the Baltic Sea (where it cannot breed due to the low salinity).\n\nEntranceway at Main Street at Roycroft Boulevard: Entranceway at Main Street at Roycroft Boulevard is a suburban residential subdivision entranceway built in 1918.  It is on Main Street (New York State Route 5) in the hamlet of Snyder, New York, in the town of Amherst within Erie County.  The entranceway is a marker that represents the American suburbanization of rural areas, suburbanization that occurred through transportation-related land development on the edges of urban areas.  It consists of a variety of half-height wall formations, featuring a semicircular wall on the Roycroft Boulevard median's intersection with Main Street.  The entranceway was added to the National Register of Historic Places on December 7, 2005.\n\nMiddelgrundsfortet: Middelgrundsfortet or Fort Middelgrund is a sea fort located on an artificial island in the Øresund between Copenhagen and Malmö.  The fortress is constructed at a point where the seabed is 7 meters below the water surface, and at the northern meeting point of the straits Kongedybet and Hollænderdybet.\n\nFortress of Miolans: The Fortress of Miolans (French: \"Château de Miolans\" ) is a former fortress prison located in a remote area of Savoy between Italy and France.  The site, which has been occupied since the fourth century AD, strategically controlled the route across the junction of the Isere and Arc rivers.  The fortress was converted into a prison by the Counts of Savoy in the mid-16th century.  Its notoriety led it to be compared to the Bastille in Paris.\n\nVan Fortress: The Fortress of Van (Armenian: Վանի Բերդ, also known as Van Citadel, Turkish: Van Kalesi or Kurdish: Kela Wanê‎ ) is a massive stone fortification built by the ancient Armenian kingdom of Urartu during the 9th to 7th centuries BC, and is the largest example of its kind.  It overlooks the ruins of Tushpa the ancient Urartian capital during the 9th century which was centered upon the steep-sided bluff where the fortress now sits.  A number of similar fortifications were built throughout the Urartian kingdom, usually cut into hillsides and outcrops in places where modern-day Armenia, Turkey and Iran meet.  Successive groups such as the Medes, Achaemenids, Armenians, Parthians, Romans, Sassanid Persians, Byzantines, Arabs, Seljuks, Safavids, Afsharids, Ottomans and Russians each controlled the fortress at one time or another.  The ancient fortress is located just west of Van and east of Lake Van in the Van Province of Turkey.\n\nKronborg: Kronborg is a castle and stronghold in the town of Helsingør, Denmark.  Immortalized as Elsinore in William Shakespeare's play \"Hamlet\", Kronborg is one of the most important Renaissance castles in Northern Europe and has been added to UNESCO's World Heritage Sites list (2000).\n\nFlakfortet: Flakfortet, meaning sand-shoal fortress, is a sea fort located on the artificially built island of \"Saltholmrev\", in the Øresund between Copenhagen and Saltholm.  The island and fort are simply known as \"Flakfortet\"; the name of the island; \"Saltholmrev\", meaning the reef near Saltholm, is seldom used.\n\nKärnan: Kärnan (] ; Danish: \"Kernen\" , both literally \"The Core\") is a medieval tower in Helsingborg, Scania, in southern Sweden.  It is the only part remaining of a larger Danish fortress which, along with the fortress Kronborg on the opposite of Øresund, controlled the entranceway between Kattegat and Øresund and further south the Baltic Sea.\n\nÅs Abbey: Ås Abbey (Danish: \"Ås Kloster\" ; Latin: \"Asylum\" ) was a Cistercian monastery situated near the mouth of the River Viskan into the Kattegat in Halland, formerly part of Denmark but now in Sweden, near the present hamlet of Åskloster about 14 km north of Varberg, in Varberg Municipality.\n\nBaltic Sea: The Baltic Sea is a sea of the Atlantic Ocean, enclosed by Scandinavia, Finland, the Baltic countries, and the North and Central European Plain.  It includes the Gulf of Bothnia, the Bay of Bothnia, the Gulf of Finland, the Gulf of Riga, and the Bay of Gdańsk.  The sea stretches from 53°N to 66°N latitude and from 10°E to 30°E longitude.  A mediterranean sea of the Atlantic, with limited water exchange between the two bodies, the Baltic Sea drains through the Danish islands into the Kattegat by way of the straits of Øresund, the Great Belt, and the Little Belt.\n\nQuestion: Which fortress that controlled the entranceway between Kattegat and Øresund was in \"Hamlet\"?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"fortress_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the fortress.\"\n    },\n    \"location_city\": {\n      \"type\": \"string\",\n      \"description\": \"The city where the fortress is located.\"\n    },\n    \"location_country\": {\n      \"type\": \"string\",\n      \"description\": \"The country where the fortress is located.\"\n    },\n    \"controlled_waterways\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of waterways whose entranceway was controlled by the fortress.\"\n    },\n    \"is_featured_in_hamlet\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the fortress is featured in Shakespeare's play 'Hamlet'.\"\n    },\n    \"hamlet_name_in_play\": {\n      \"type\": \"string\",\n      \"description\": \"The name by which the fortress is known in 'Hamlet'.\"\n    }\n  },\n  \"required\": [\n    \"fortress_name\",\n    \"location_city\",\n    \"location_country\",\n    \"controlled_waterways\",\n    \"is_featured_in_hamlet\",\n    \"hamlet_name_in_play\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "fortress_name": {
        "type": "string",
        "description": "The name of the fortress."
      },
      "location_city": {
        "type": "string",
        "description": "The city where the fortress is located."
      },
      "location_country": {
        "type": "string",
        "description": "The country where the fortress is located."
      },
      "controlled_waterways": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of waterways whose entranceway was controlled by the fortress."
      },
      "is_featured_in_hamlet": {
        "type": "boolean",
        "description": "Indicates if the fortress is featured in Shakespeare's play 'Hamlet'."
      },
      "hamlet_name_in_play": {
        "type": "string",
        "description": "The name by which the fortress is known in 'Hamlet'."
      }
    },
    "required": [
      "fortress_name",
      "location_city",
      "location_country",
      "controlled_waterways",
      "is_featured_in_hamlet",
      "hamlet_name_in_play"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

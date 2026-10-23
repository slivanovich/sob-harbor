{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nLowell Cemetery: Lowell Cemetery is a cemetery located in Lowell, Massachusetts.  Founded in 1841 and located on the banks of the Concord River, the cemetery is one of the oldest garden cemeteries in the nation, inspired by Mount Auburn Cemetery in Cambridge, Massachusetts.  Many of Lowell's wealthy industrialists are buried here, under ornate Victorian tombstones.  A 73 acre portion of the 84 acre cemetery was listed on the National Register of Historic Places in 1998.\n\nSaint Raymond's Cemetery (Bronx): Saint Raymond's Cemetery is a Roman Catholic cemetery at 2600 Lafayette Avenue in the Throggs Neck and Schuylerville sections of the Bronx, New York City, United States.  The cemetery is composed of two separate locations: the older section (main entrance is located at 1201 Balcom Avenue), and the newer section (where most present-day burials now take place), both east of the Hutchinson River Parkway.  The Bronx–Whitestone Bridge is located adjacent to the cemetery's newer section, while the neighboring Throgs Neck Bridge can be seen from a distance.\n\nMetairie Cemetery: Metairie Cemetery is a cemetery in New Orleans, Louisiana, United States.  The name has caused some people to mistakenly presume that the cemetery is located in Metairie, Louisiana; but it is located within the New Orleans city limits, on Metairie Road (and formerly on the banks of the since filled-in Bayou Metairie).\n\nJefferson Barracks National Cemetery: Jefferson Barracks National Cemetery is an American military cemetery located in St. Louis County, Missouri, just on the banks of the Mississippi River.  The cemetery was established after the American Civil War in an attempt to put together a formal network of military cemeteries.  It started as the Jefferson Barracks Military Post Cemetery in 1826 and became a United States National Cemetery in 1866.\n\nMound Cemetery (Arkansas City, Arkansas): The Mound Cemetery is a historic cemetery, located just outside Arkansas City, Arkansas in Desha County.  The oldest portion of the cemetery, dating to the 1860s, is located on top of a Mississippian culture mound, one of the few places the early American settlers of the area found to be safe from periodic flooding by the Mississippi River.  It is located off County Road 351, about one-half mile outside Arkansas City, and about 3 mi from the river.\n\nOak Grove Cemetery (Fall River, Massachusetts): Oak Grove Cemetery is a historic cemetery located at 765 Prospect Street in Fall River, Massachusetts.  It was established in 1855 and greatly improved upon in the years that followed.  It features Gothic Revival elements, including an elaborate entrance arch constructed of locally quarried Fall River granite.  The cemetery originally contained 47 acres, but has since been expanded to roughly 100 acres.  The cemetery is the city's most significant, built in the planned rural-garden style of Mount Auburn Cemetery in Cambridge, Massachusetts.  It was designed and laid out by local architect Josiah Brown, who is also known for his designs of early mills including the Union, Border City, and others.\n\nPerm: Perm (Russian: Пермь ; ] ;) is a city and the administrative center of Perm Krai, Russia, located on the banks of the Kama River in the European part of Russia near the Ural Mountains.\n\nIndian Mound Cemetery: Indian Mound Cemetery is a cemetery located along the Northwestern Turnpike (U.S. Route 50) on a promontory of the \"Yellow Banks\" overlooking the South Branch Potomac River and Mill Creek Mountain in Romney, West Virginia, United States.  The cemetery is centered on a Hopewellian mound, known as the Romney Indian Mound.  Indian Mound Cemetery is also the site of Fort Pearsall, the Confederate Memorial, Parsons Bell Tower, and reinterments from Romney's Old Presbyterian Cemetery.  The cemetery is currently owned and maintained by the Indian Mound Cemetery Association, Inc.\n\nYegoshikha River: Yegoshikha (Russian: Егоши́ха , ] ), formerly Yagoshikha (Russian: Ягоши́ха ), is a river in Perm Krai, Russia, being the left tributary of the Kama.  In spite of its relatively small size it is famous for its historical significance.  It mainly flows along the east and west borders of the city of Perm.  The source of the Yegoshikha river is in the forest area close to Lipovaya Gora and Vladimirskiy microdistricts.  The river flows along the \"Yegoshikha ravine\", which divides the left-bank (relatively to Kama) part of Perm city and is crossed by two dams and a bridge (which is also called a dam by the general population).  On the banks of Yegoshikha there are a lot of country cottages, \"The South Cemetery\" and \"The Yegoshikha (Old) Cemetery\".  The Yegoshikha flows into the Kama close to Perm's river port.\n\nYegoshikha Cemetery: Yegoshikha Cemetery (Russian: Егошихинское кладбище) is the principal cemetery of the Russian city of Perm.  It takes its name from the Yegoshikha River which borders it and was founded in the second half of the 18th century.\n\nQuestion: Yegoshikha Cemetery is located in a city that is located on the banks ofr what river?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"cemetery_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the cemetery in question.\"\n    },\n    \"city_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the city where the cemetery is located.\"\n    },\n    \"city_location_description\": {\n      \"type\": \"string\",\n      \"description\": \"Describes the city's relationship to the river.\"\n    },\n    \"river_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the river on whose banks the city is located.\"\n    }\n  },\n  \"required\": [\n    \"cemetery_name\",\n    \"city_name\",\n    \"city_location_description\",\n    \"river_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "cemetery_name": {
        "type": "string",
        "description": "The name of the cemetery in question."
      },
      "city_name": {
        "type": "string",
        "description": "The name of the city where the cemetery is located."
      },
      "city_location_description": {
        "type": "string",
        "description": "Describes the city's relationship to the river."
      },
      "river_name": {
        "type": "string",
        "description": "The name of the river on whose banks the city is located."
      }
    },
    "required": [
      "cemetery_name",
      "city_name",
      "city_location_description",
      "river_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

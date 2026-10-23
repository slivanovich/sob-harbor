{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nWoolsthorpe-by-Belvoir: Woolsthorpe, also known as Woolsthorpe-by-Belvoir, is a village and civil parish in the South Kesteven district of Lincolnshire, England.  The population of the civil parish at the 2011 census was 415.  It is situated approximately 5 mi west from Grantham, and adjoins the county border with Leicestershire.  The neighbouring village of Belvoir lies on the other side of the border.  Grantham Canal is situated 1 mi to the north-east at its closest point.\n\nBrandsnutene: Brandsnutene or Brandsnutane is a 1496 m tall mountain on the border of Aust-Agder and Telemark counties in southern Norway.  Is the second highest mountain in Aust-Agder of the mountains with a prominence of at least 50 m .  The mountain is located on the border of the municipalities of Bykle (in Aust-Agder) and Tokke (in Telemark).  The mountain has a secondary peak of 1480 m located about 1 km east of the municipal/county border inside Tokke.\n\nKnockmealdown: Knockmealdown (Irish: \"Cnoc Mhaoldomhnaigh\" ) is the highest peak of the Knockmealdown Range of mountains, located on the border between Co Tipperary and Co Waterford.  The peak itself is located in County Waterford and is the highest point in that county.  However, since the county border generally follows the summit line the main peaks are actually in both county Tipperary and in county Waterford (OSI Discovery Map 75).  Of the more prominent peaks to the east of the 'Vee' road — Sugarloaf, Knockmealdown, Knocknagnauv and Knockmeal sit on the border, Knocknafallia and Knocknanask are in County Waterford and Knockshane, Crohan West and Knocknasculloge are in County Tipperary.  The same situation is true for part of the nearby Galty mountains where the highest peaks are shared between Tipperary and Limerick.\n\nStony River (West Virginia): The Stony River is a 26.7 mi tributary of the North Branch Potomac River in Grant County in West Virginia's Eastern Panhandle.  The Stony River joins with the North Branch at the Mineral County border.  Its source lies north of the Dolly Sods Wilderness on the Tucker County border in the Allegheny Front.\n\nBakke, Norway: Bakke is a former municipality in Vest-Agder county, Norway.  The municipality existed from 1838 until its dissolution in 1965.  It was located in the present-day municipalities of Sirdal and Flekkefjord.  It included the whole Sirdalen valley along the Rogaland county border, stretching from the Aust-Agder county border in the north to Sirnes and the lake Lundevatnet in the south.  The administrative center was the village of Sira where Bakke Church is located.\n\nWoodsburgh, New York: Woodsburgh is a village in Nassau County, New York in the United States.  The population was 778 at the 2010 census.\n\nNew Sharon, New Jersey: New Sharon is an unincorporated community located along the border of Robbinsville Township in Mercer County and Upper Freehold Township in Monmouth County, New Jersey, United States.  Old York Road (County Route 539) passes through the center of the community and its center line the county border.\n\nHewlett-Woodmere School District: The Hewlett-Woodmere Public School District, Union Free School District 14, is located in the southwest section of Nassau County, New York and borders the New York City borough of Queens.  Communities in the district include, in full or in part, Hewlett, Woodmere, Woodsburgh, North Woodmere an unincorporated area of Valley Stream, the Gibson section of Valley Stream, Hewlett Harbor, Hewlett Neck, and Hewlett Bay Park, as well as parts of Lynbrook, all comprise the geographical boundaries for the school district.  There are approximately 3,200 students enrolled in pre-K through 12th grade.  The district is operated under the supervision of a seven-member Board of Education.\n\nSira, Norway: Sira is a village in Flekkefjord municipality in Vest-Agder county, Norway.  The village is located immediately east of the county border of Vest-Agder and Rogaland.  The European route E39 highway passes by the village and the Sørlandet Line runs right through the village, stopping at Sira Station.  The 0.66 km2 village has a population (2015) of 630, giving the village a population density of 955 PD/km2 .\n\nJonesborough, County Armagh: Jonesborough or Jonesboro (Irish: \"Baile an Chláir\") is a small village and civil parish in the Ring of Gullion in County Armagh, Northern Ireland.  It is about 8 km south of Newry and lies 1 km from the border with County Louth in the Republic of Ireland.  In the 2001 Census it had a population of 273 people.  In 1837 it had 174 inhabitants.  The Catholic parish includes the neighbouring area of Dromintee and crosses the county border into Louth.\n\nQuestion: Population of 778, what is Nassu County border to?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"entity_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the village or community with the specified population.\"\n    },\n    \"population\": {\n      \"type\": \"integer\",\n      \"description\": \"The population of the entity.\"\n    },\n    \"county\": {\n      \"type\": \"string\",\n      \"description\": \"The county where the entity is located.\"\n    },\n    \"bordering_entity\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the entity that borders the specified county.\"\n    },\n    \"border_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of the bordering entity (e.g., borough, county).\"\n    }\n  },\n  \"required\": [\n    \"entity_name\",\n    \"population\",\n    \"county\",\n    \"bordering_entity\",\n    \"border_type\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "entity_name": {
        "type": "string",
        "description": "The name of the village or community with the specified population."
      },
      "population": {
        "type": "integer",
        "description": "The population of the entity."
      },
      "county": {
        "type": "string",
        "description": "The county where the entity is located."
      },
      "bordering_entity": {
        "type": "string",
        "description": "The name of the entity that borders the specified county."
      },
      "border_type": {
        "type": "string",
        "description": "The type of the bordering entity (e.g., borough, county)."
      }
    },
    "required": [
      "entity_name",
      "population",
      "county",
      "bordering_entity",
      "border_type"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

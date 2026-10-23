{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nEye 2 Eye: Live in Madrid: Eye 2 Eye: Live In Madrid is a live concert performance by Alan Parsons released on both DVD-Video and Audio CD on April 6, 2010 on the \"Frontiers\" label.  The show was performed with his band \"Alan Parsons Live Project\", and was recorded live at the Plaza Mayor, Madrid, Spain, on May 14, 2004.\n\nMerrimack County Courthouse: The Merrimack County Courthouse stands at 163 North Main Street in Concord, New Hampshire, the state capital and county seat of Merrimack County.  The oldest part of the courthouse building is a brick and granite two story structure, completed in 1857 to serve as a town hall and court building.  The city and county used the building for town offices and county courts until 1904, when the city sold its interest in the building to the county.  Between 1905 and 1907 the building was extensively remodeled to plans by local architect George S. Forrest.  A modern addition has been made to the rear of the building.\n\nFrank Nesmith Parsons: Frank Nesmith Parsons (September 3, 1854 in Dover, New Hampshire – 1934 in Franklin, New Hampshire) was a lawyer, politician, and Chief Justice of the New Hampshire Supreme Court from 1902 to 1924.  Some sources spell his middle name \"Naismith\".\n\nJeffrey Kollman: Jeffrey \"Jeff\" Kollman is an American guitar player from Toledo, Ohio, best known for his work with Chad Smith's Bombastic Meatbats, Glenn Hughes, UFO offshoot Mogg/Way, progressive rock trio, Cosmosquad, and his 90's progressive metal band, Edwin Dare.  He has worked extensively with contemporary jazz keyboardist Lao Tizer, toured with Japanese superstar Eikichi Yazawa, the Alan Parsons Live Project, former Skid Row vocalist Sebastian Bach, the Michael Schenker Group and UFO, gigged with bassist/vocalist Marco Mendoza and the Danny Seraphine led CTA (California Transit Authority), and is currently a member of Asia feat.  John Payne and blues rockers Bleeding Harp.\n\nP. J. Olsson: Paul Josef Olsson is an American singer, most notable as being the lead singer for the Alan Parsons Live Project.  He has toured with various artists over his lifetime, including Rufus Wainright, Beth Orton, and Placebo.\n\nMerrimack County Bank: The Merrimack County Bank building is a historic commercial building at 214 North Main Street in Concord, New Hampshire.  The three story brick Federal style building was built in 1826 to house the offices of the Merrimack County Bank on the first floor, law offices on the second floor, and a public meeting space above.  In 1840 the upper floor was taken over by the New Hampshire Historical Society for use as a library.  The Society significantly altered the interior in the early 20th century to convert this space for display purposes.  In 1952 the building was acquired by the Christian Mutual Life Insurance Company, which restored the interior to its original Federal appearance, and sold the building to a law firm in the 1970s.  The building also housed the law offices of future president Franklin Pierce.\n\nDowntown Concord Historic District: The Downtown Concord Historic District encompasses most of the commercial heart of downtown Concord, New Hampshire, United States.  Incorporated in 1734, Concord became the state capital in 1808 and the seat of Merrimack County in 1823.  Economic growth followed, due in part to these government institutions and also to the rise of industry along the Merrimack River, which flows through the city east of the downtown area, and the arrival in the 1840s of the railroad.  The New Hampshire State House was built in 1819 south of the traditional center of the city (now the Concord Historic District), and the commercial heart of the city began to take shape along the First New Hampshire Turnpike south of the State House (now Main Street).  The district was listed on the National Register of Historic Places in 2000.\n\nFranklin, New Hampshire: Franklin is a city in Merrimack County, New Hampshire, United States.  At the 2010 census, the population was 8,477, the lowest of any of New Hampshire's 13 cities.  Franklin includes the village of West Franklin.\n\nKevin Chalfant: Kevin Chalfant is an American singer-songwriter and a native of Streator, Illinois.  He obtained a BMI award for co-writing and singing on one of the most frequently aired rock radio hits of 1992 and 1993, \"I’ve Got A Lot To Learn About Love\"', by The Storm.  In October 1993 he very briefly sat in for Steve Perry in Journey, singing lead at a roast for Journey's manager, Herbie Herbert, and in 2003, he toured as lead vocalist for the Alan Parsons Live Project.\n\nMerrimack County, New Hampshire: Merrimack County is a county in the U.S. state of New Hampshire.  As of the 2010 census, the population was 146,445, making it the third-most populous county in New Hampshire.  Its county seat is Concord, the state capital.  The county was organized in 1823 from parts of Hillsborough and Rockingham counties, and is named for the Merrimack River.\n\nQuestion: Which city in Merrimack County did Frank Nesmith Parsons live in? \n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the person in question.\"\n    },\n    \"county_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the county relevant to the question.\"\n    },\n    \"city_of_residence\": {\n      \"type\": \"string\",\n      \"description\": \"The city where the person lived or died.\"\n    },\n    \"is_city_in_county\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates whether the identified city is located within the specified county.\"\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"county_name\",\n    \"city_of_residence\",\n    \"is_city_in_county\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The full name of the person in question."
      },
      "county_name": {
        "type": "string",
        "description": "The name of the county relevant to the question."
      },
      "city_of_residence": {
        "type": "string",
        "description": "The city where the person lived or died."
      },
      "is_city_in_county": {
        "type": "boolean",
        "description": "Indicates whether the identified city is located within the specified county."
      }
    },
    "required": [
      "person_name",
      "county_name",
      "city_of_residence",
      "is_city_in_county"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

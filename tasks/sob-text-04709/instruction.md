{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAllenstown Meeting House: The Allenstown Meeting House (also known as Old Allenstown Meeting House; Church of Christ; Christian Church) is a historic meeting house on Deerfield Road in Allenstown, New Hampshire.  It is a single-story wood-frame structure with a gable roof, resting on a granite foundation.  It has a heavy timber frame and is sheathed in wooden clapboards.  The main facade faces the road to the south, and is five bays wide, with a central door flanked by two windows on either side.  The interior has retained its original box pews and pulpit.  The northwest corner of the building was damaged by arson fire in 1985, but has been sensitively restored.  The meeting house was built in 1815, and served as the town's main civic and religious building from then until 1886, when it was abandoned for both purposes.  It is the only surviving single-story meeting house of the period in New Hampshire.\n\nCreek Meeting House and Friends' Cemetery: Creek Meeting House and Friends' Cemetery is a historic Society of Friends meeting house and cemetery on Salt Point Turnpike/Main Street in Clinton Corners, Dutchess County, New York.  It was built between 1777 and 1782.  The meeting house is a two story, squarish building constructed of fieldstone.  Land for the building was given by Able Peters whose substantial brick house is the next building on the same side of the road north of the meeting house.  In 1828 the Friends Creek Meeting split into Hicksite and Orthodox meetings (Orthodox referring to mainstream Protestant practices).  The Orthodox meeting moved about a mile north of Clinton Corners to the Shingle Meeting House] located on the grounds of the current Friends Upton Lake Cemetery.  The Creek Meeting sold the building to the Upton Lake Grange in 1927 and joined the Bulls Head Meeting in 1936.  The Grange transferred the building to the Town of Clinton Historical Society in 1995.  The original slate covered, moderately pitched gable roof was replaced with metal in the early 21st century by the Historical Society.\n\nNew Hampton Town House: The New Hampton Town House (also known as New Hampton Meeting House; Center Meeting House) is a historic meeting house at the junction of Town House Road and Dana Hill Road in New Hampton, New Hampshire.\n\nSanbornton, New Hampshire: Sanbornton is a town in Belknap County, New Hampshire, United States.  The population was 2,966 at the 2010 census.  It includes the villages of North Sanbornton and Gaza.\n\nRockingham Meeting House: The Rockingham Meeting House, also known as Old North Meeting House and First Church in Rockingham, is a historic civic and religious building on Meeting House Road in Rockingham, Vermont, United States.  The Meeting House was built between 1787 and 1801 and was originally used for both Congregational church meetings as well as civic and governmental meetings.  Church services ceased in 1839 but town meetings continued to be held in it until 1869.  It was designated a National Historic Landmark in 2000 as an exceptionally well-preserved \"second period\" colonial-style meeting house.  The building, owned by the town, is available for weddings and other events under rules established by the town.\n\nNorth Sandwich Meeting House: The North Sandwich Meeting House is a historic Quaker meeting house at the northwest junction of Quaker-Whiteface Road and Brown Hill Road in Sandwich, New Hampshire.  Built in 1881, it is the best-preserved 19th-century Quaker meeting house in the county.  The building was listed on the National Register of Historic Places in 1986, at which time it was the only active Quaker meeting house in Carroll County.\n\nJones Hall (Marlow, New Hampshire): Jones Hall, also known as The Meetinghouse at Marlow Hill or The Christian Church, is a historic church and municipal building on Church Street in Marlow, New Hampshire.  Built between 1792 and 1800, it is a rare 18th century meeting house in New Hampshire, although it has been altered somewhat and moved (in 1845) from its original location; it was said to originally be a near duplicate of the Rockingham Meeting House in Vermont.  Construction of the timber frame building was repeatedly delayed due to a shortage of funding.  It first served as a combined religious and civic meeting house, with ownership residing with the society of pew owners.\n\nFremont Meeting House: The Fremont Meeting House (also known as Poplin Meeting House) is a historic meeting house at 464 Main Street (New Hampshire Route 107) in Fremont, New Hampshire.  Built in 1800, it is a well-preserved example of a Federal-period meeting house, and is the only surviving example in the state with two porches, a once-common variant of the building type.  The building was listed on the National Register of Historic Places in 1993.\n\nBay Meeting House and Vestry: The Bay Meeting House and Vestry is a historic church complex on Upper Bay and Steele Roads in Sanbornton, New Hampshire.  The wood frame church was built in 1836 for a Baptist congregation, on a site which had held a church since 1808, and exhibits well-preserved transitional Federal-Gothic Revival style.  It is a rectangular structure with a gable roof and a two-stage belfry tower above its main (eastern) facade.  The main facade has three bays and is two stories in height, with doorways occupying the outer bays on the first floor, and rectangular sash windows in the other positions.  The doorways are slightly recessed in molded frames with corner blocks.  The gable pediment is flushboarded, with a semi-elliptical in its center.  The long sides of the church are lined with Gothic pointed-arch windows.  The vestry is a relatively modest rectangular structure, built in 1841 with enlargements in the early 20th century and again in the 1980s.\n\nOld Webster Meeting House: The Old Webster Meeting House is an historic meeting house on Battle Street in Webster, New Hampshire.  Built in 1791, and altered in the 1840s, the meeting house is one of a small number of meeting houses to survive in northern New England.  The building was moved from its original site in 1942 to make way for a flood control project and was given modern footings for the granite foundation in 1979.  The building, owned by the Society for the Preservation of the Old Meeting House, now serves as a local museum.\n\nQuestion: Which town in New Hampshire includes the villages of North Sanbornton and Gaza and is also home to the Bay Meeting House and Vestry?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"town_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the town.\"\n    },\n    \"state\": {\n      \"type\": \"string\",\n      \"description\": \"The state where the town is located.\"\n    },\n    \"villages_included\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of villages included within the town.\"\n    },\n    \"meeting_house_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the meeting house located in the town.\"\n        },\n        \"description\": {\n          \"type\": \"string\",\n          \"description\": \"A brief description of the meeting house type.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"description\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"town_name\",\n    \"state\",\n    \"villages_included\",\n    \"meeting_house_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "town_name": {
        "type": "string",
        "description": "The name of the town."
      },
      "state": {
        "type": "string",
        "description": "The state where the town is located."
      },
      "villages_included": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of villages included within the town."
      },
      "meeting_house_details": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the meeting house located in the town."
          },
          "description": {
            "type": "string",
            "description": "A brief description of the meeting house type."
          }
        },
        "required": [
          "name",
          "description"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "town_name",
      "state",
      "villages_included",
      "meeting_house_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

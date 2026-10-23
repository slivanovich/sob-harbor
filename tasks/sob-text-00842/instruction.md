{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nKings Langley Palace: Kings Langley Palace was a 13th-century Royal Palace which was located to the west of the Hertfordshire village of Kings Langley in England.  During the Middle Ages, the palace served as a residence of the Plantagenet kings of England.  It fell into disuse sometime during the 16th century and became a ruin.  Today, nothing remains of the building except for some archaeological remains.  The site is a scheduled ancient monument.\n\nCraven in the Domesday Book: The extent of the medieval district of Craven, in the north of England is a matter of debate.  The name Craven is either pre-Celtic Britain, Britonnic or Romano-British in origin.  However, its usage continued following the ascendancy of the Anglo-Saxons and the Normans – as was demonstrated by its many appearances in the Domesday Book of 1086.  Places described as being \"In Craven\" in the Domesday Book fell later within the modern county of North Yorkshire, as well as neighbouring areas of West Yorkshire, Lancashire and Cumbria.  Usage of Craven in the Domesday Book is, therefore, circumstantial evidence of an extinct, British or Anglo-Saxon kingdom or subnational entity (such as a shire or earldom).\n\nKings Langley School: Kings Langley School is a coeducational secondary school and sixth form with academy status, located in the village of Kings Langley in Hertfordshire, England.  It is situated on Love Lane about 0.75 miles from Junction 20 on the M25 and about 0.5 miles from Kings Langley railway station.\n\nKings Langley F.C.: Kings Langley Football Club are a semi-professional association football club in the village and civil parish of Kings Langley, Hertfordshire, England.  The club have spent the majority of their history in the Hertfordshire County League, they joined the Spartan South Midlands Football League in 2001, winning the Premier Division in the 2015-16 season and are currently members of the Southern League Premier Division - the seventh tier of the English football league system, following a third consecutive promotion in 2016 when they became champions of the Southern League Division One South.  In doing so, Kings Langley join Truro F.C., Chester F.C., F.C. United of Manchester and Gretna F.C. as the only clubs in the United Kingdom with three or more successive promotions.  They are also unofficially the highest-ranked village football club in England.\n\nKingskerswell: Kingskerswell (formerly Kings Carswell, or Kings Kerswell) is a village and civil parish within Teignbridge local government district in the south of Devon, England.  The village grew up where an ancient track took the narrowest point across a marshy valley and it is of ancient foundation, being mentioned in the Domesday Book.  It has a church dating back to the 14th century and the ruins of a manor house of similar date.  The coming of the railway in the 1840s had a large effect on the village, starting its conversion into a commuter town.  The village is a major part of the electoral ward called Kerswell-with-Combe.  This ward had a population of 5,679 at the 2011 census.\n\nHanging Heaton: Hanging Heaton is a large village in West Yorkshire, England.  Partly in both Batley and Dewsbury it is a historic village mentioned in the Domesday Book under the name 'Etun'.  The prefix 'Hanging' refers to a steep hillside hanging above lower ground.  Heaton means 'High Farm' therefore Hanging Heaton was a lonely hillside farmstead.\n\nLangley railway station: Langley railway station is a railway station in Langley, a suburb of Slough, Berkshire, England.  It is 16.25 mi west of Paddington towards Reading .\n\nWorle: Worle ( ) is a large village in North Somerset which is joined to the seaside town of Weston-super-Mare on its western edge.  It, however, maintains a very separate identity, and may now be bigger than its more famous neighbour.  Worle pre-dates Weston and was mentioned in the Domesday Book of 1086.  In the book, it is said that Worle was owned by Walter of Douai, and consisted of 750 acre and valued at 6.5 hides.  \"Walter de Dowai holds of the King, Worle.  Edgar held it in the time of King Edward, and gelded for six hides and a half.\"  The parish church of St Martin's sits on the side of Worlebury Hill and overlooks the village.  In 2017, Bunnings Warhouse moved into the old Homebase building and is a popular diy shop within Worle.\n\nKings Langley railway station: Kings Langley railway station is just under the M25 motorway at Junction 20.  It serves the village of Kings Langley, and the nearby villages of Abbots Langley and Hunton Bridge.  The station is 21 miles (34 km) north west of London Euston on the West Coast Main Line.  The station and all services calling at the station are operated by London Midland.\n\nAbbots Langley: Abbots Langley is a large village and civil parish in the English county of Hertfordshire.  It is an old settlement and is mentioned (under the name of Langelai) in the Domesday Book.  Economically the village is closely linked to Watford and was formerly part of the Watford Rural District.  Since 1974 it has been included in the Three Rivers district.\n\nQuestion: What large village is serviced by the Kings Langley railway station and was mentioned in the Domesday Book under the name of Langelai?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"village_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the village that meets the criteria.\"\n    },\n    \"is_large_village\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the village is described as a 'large village'.\"\n    },\n    \"domesday_book_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"mentioned_in_domesday_book\": {\n          \"type\": \"boolean\",\n          \"description\": \"True if the village is mentioned in the Domesday Book.\"\n        },\n        \"name_in_domesday_book\": {\n          \"type\": \"string\",\n          \"description\": \"The specific name under which the village was mentioned in the Domesday Book.\"\n        }\n      },\n      \"required\": [\n        \"mentioned_in_domesday_book\",\n        \"name_in_domesday_book\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"servicing_railway_station\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the railway station that services the village.\"\n    }\n  },\n  \"required\": [\n    \"village_name\",\n    \"is_large_village\",\n    \"domesday_book_details\",\n    \"servicing_railway_station\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "village_name": {
        "type": "string",
        "description": "The name of the village that meets the criteria."
      },
      "is_large_village": {
        "type": "boolean",
        "description": "Indicates if the village is described as a 'large village'."
      },
      "domesday_book_details": {
        "type": "object",
        "properties": {
          "mentioned_in_domesday_book": {
            "type": "boolean",
            "description": "True if the village is mentioned in the Domesday Book."
          },
          "name_in_domesday_book": {
            "type": "string",
            "description": "The specific name under which the village was mentioned in the Domesday Book."
          }
        },
        "required": [
          "mentioned_in_domesday_book",
          "name_in_domesday_book"
        ],
        "additionalProperties": false
      },
      "servicing_railway_station": {
        "type": "string",
        "description": "The name of the railway station that services the village."
      }
    },
    "required": [
      "village_name",
      "is_large_village",
      "domesday_book_details",
      "servicing_railway_station"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

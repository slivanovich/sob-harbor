{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCharles I of England: Charles I (19 November 1600 – 30 January 1649 ) was monarch of the three kingdoms of England, Scotland, and Ireland from 27 March 1625 until his execution in 1649.\n\nHMS Carisbrooke Castle (K379): HMS \"Carisbrooke Castle\" (K379) was a Royal Navy Castle-class corvette.  She was named after Carisbrooke Castle on the Isle of Wight.\n\nRecords of the Three Kingdoms: The Records of the Three Kingdoms is a Chinese historical text which covers the history of the late Eastern Han dynasty (c. 184–220 AD) and the Three Kingdoms period (220–280 AD).  It is widely regarded as the official and authoritative historical text for that period.  Written by Chen Shou in the third century, the work combines the smaller histories of the rival states of Cao Wei, Shu Han and Eastern Wu in the Three Kingdoms period into a single text.  The \"Records of the Three Kingdoms\" provided the basis for the historical novel \"Romance of the Three Kingdoms\" written by Luo Guanzhong in the 14th century.\n\nRomance of the Three Kingdoms IV: Wall of Fire: Romance of the Three Kingdoms IV: Wall of Fire (released as Sangokushi IV in Japan) is the fourth in the \"Romance of the Three Kingdoms\" series of turn-based strategy games produced by Koei and based on the historical novel \"Romance of the Three Kingdoms\".  \"Romance of the Three Kingdoms IV: Wall of Fire\" was the last game in the series to be released on the PC in the United States until \"Romance of the Three Kingdoms XI\".\n\nCarisbrooke: Carisbrooke is a village on the south western outskirts of Newport, Isle of Wight and is best known as the site of Carisbrooke Castle.  It also has a medieval parish church.  St. Mary's Church (overlooking Carisbrooke High Street with views to the castle), began life as part of a Benedictine priory, established by French monks about 1150.  The priory was dissolved by King Henry V of England in 1415 during the French Wars.  Neglect over the centuries took its toll, but in 1907 the church was restored to its full glory.  Its most striking feature is the 14th century tower, rising in five stages with a turret at one corner and a battlemented and pinnacled crown.\n\nSilius Titus: Silius Titus (1623–1704), of Bushey, was an English politician, Captain of Deal Castle, and Groom of the Bedchamber to King Charles II.  Colonel Titus was an organiser in the attempted escape of King Charles I from Carisbrooke Castle.\n\nThree Kingdoms (TV series): Three Kingdoms (Chinese: 三国) is a 2010 Chinese television series based on the events in the late Eastern Han dynasty and the Three Kingdoms period.  The plot is adapted from the 14th century historical novel \"Romance of the Three Kingdoms\" and other stories about the Three Kingdoms period.  Directed by Gao Xixi, the series had a budget of over 160 million RMB (30 million USD) and took five years of pre-production work.  Shooting of the series commenced in October 2008, and was released in China in May 2010.\n\nList of people of the Three Kingdoms: The following are lists of people significant to the Three Kingdoms period (220–280) of Chinese history.  Their names are sorted in alphabetical order.  Fictional characters in Luo Guanzhong's historical novel \"Romance of the Three Kingdoms\" and those found in other cultural references to the Three Kingdoms are listed separately in List of fictional people of the Three Kingdoms.\n\nCarisbrooke Castle: Carisbrooke Castle is a historic motte-and-bailey castle located in the village of Carisbrooke (near Newport), Isle of Wight, England.  Charles I was imprisoned at the castle in the months prior to his trial.\n\nWilliam Levett (courtier): William Levett, Esq., (sometimes spelled William Levet) was a long serving courtier to King Charles I of England.  Levett accompanied the King during his flight from Parliamentary forces, including his escape from Hampton Court palace, and eventually to his imprisonment in Carisbrooke Castle on the Isle of Wight, and finally to the scaffold on which he was executed.  Following the King's death, Levett wrote a letter claiming that he had witnessed the King writing the so-called Eikon Basilike during his imprisonment, an allegation that produced a flurry of new claims about the disputed manuscript and flamed a growing movement to rehabilitate the image of the executed monarch.\n\nQuestion: What is the birthdate of this monarch of three kingdoms of England, Scottland, and Ireland, who attempted to escape from Carisbrooke Castle?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"monarch_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the monarch.\"\n    },\n    \"birth_date\": {\n      \"type\": \"string\",\n      \"description\": \"The birth date of the monarch.\"\n    },\n    \"kingdoms_ruled\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of kingdoms ruled by the monarch.\"\n    },\n    \"imprisonment_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"location\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the castle where the monarch was imprisoned.\"\n        },\n        \"attempted_escape\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if an escape was attempted from the imprisonment location.\"\n        }\n      },\n      \"required\": [\n        \"location\",\n        \"attempted_escape\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"monarch_name\",\n    \"birth_date\",\n    \"kingdoms_ruled\",\n    \"imprisonment_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "monarch_name": {
        "type": "string",
        "description": "The name of the monarch."
      },
      "birth_date": {
        "type": "string",
        "description": "The birth date of the monarch."
      },
      "kingdoms_ruled": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of kingdoms ruled by the monarch."
      },
      "imprisonment_details": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "The name of the castle where the monarch was imprisoned."
          },
          "attempted_escape": {
            "type": "boolean",
            "description": "Indicates if an escape was attempted from the imprisonment location."
          }
        },
        "required": [
          "location",
          "attempted_escape"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "monarch_name",
      "birth_date",
      "kingdoms_ruled",
      "imprisonment_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

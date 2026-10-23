{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBBC Radio Stoke: Both of the English counties the station covers have no BBC local radio station for their whole area.  In Staffordshire, the south is covered by BBC WM, east by BBC Radio Derby and the west by BBC Radio Shropshire.  In Cheshire, north-western areas are served by BBC Radio Merseyside and the north-east by BBC Radio Manchester.\n\nAndy Crane: Howard Andrew \"Andy\" Crane (born 24 February 1964) is an English television and radio presenter, best known for presenting Children's BBC between 1987 and 1990 and for his current work as presenter on BBC Radio Manchester, BBC Radio Sheffield, BBC Radio 5 Live and Granada Reports.\n\nJames H. Reeve: James Hengist Reeve, born 25 June 1950, is a cult English broadcaster, journalist, raconteur and radio phone-in host based in the Manchester area.  James has hosted shows on Piccadilly Radio, BBC GMR (now BBC Radio Manchester), BBC Radio Five Live, The New Hallam FM, talkSPORT, TEAMtalk 252 stations and, up until July 2006, presented the late night phone-in show at Key 103.\n\nBBC Radio Manchester: BBC Radio Manchester is a BBC Local Radio station broadcasting to Greater Manchester and north east Cheshire in North West England from MediaCityUK in Salford Quays on FM via a transmitter at Holme Moss, with a small repeater at Saddleworth that covers Tameside and Saddleworth.  It can be heard on DAB radio and via internet streaming.\n\nNaomi (singer-songwriter): Naomi (born 29 June 1996) is a female British singer-songwriter born and raised in Manchester, England, formerly known as Caleidra, who first came to prominence after a song she wrote at school in her music class, led to her being signed to a record label and the release of her first single 'With You' on 24 August 2012.  This received national media coverage and Naomi appeared on television programmes such as ITV Daybreak, ITV Granada Reports, radio including BBC Radio Manchester and Salford City Radio, in the national press, The Times, The Independent and The Guardian, teen magazines Mizz and Shout.  Her second single was produced by John McLaughlin who previously worked with Busted, 911 (UK band) and Westlife and led to further appearances in the media, including ITV Granada Reports, further live performances on BBC Radio Manchester, BBC Radio Sheffield, Salford City Radio and during the Manchester International Festival and received impressive media reviews including Music Week.\n\nPhil Trow: Phil Trow (born 9 September 1966 in Manchester) is a broadcaster at BBC Radio Manchester and has worked in radio for over 20 years.\n\nSalford Quays: Salford Quays is an area of Salford, Greater Manchester, England, near the end of the Manchester Ship Canal.  Previously the site of Manchester Docks, it became one of the first and largest urban regeneration projects in the United Kingdom following the closure of the dockyards in 1982.\n\nBBC Local Radio: BBC Local Radio is the BBC's local and regional radio service for England and the Channel Islands, consisting of forty (40) stations.  They cover a variety of areas; with some serving a city and surrounding areas, for example BBC Radio Manchester; a county, for example BBC Radio Norfolk; a conurbation, for example BBC WM; or a region, for example BBC Radio Solent.\n\nCaroline Woodruff: Caroline Woodruff is an English voice-over artist and actor based in Stockport.  She is a professional broadcaster and trained with the BBC in London going on to present music and arts programmes for BBC Radio Leeds, BBC GMR, and BBC Radio Manchester where she met presenter and producer Jeff Cooper, Editor of radio2XS.  In 2008 Woodruff began broadcasting with Radio2XS.\n\nAllan Beswick: Allan Beswick (born 8 October 1948) is a radio broadcaster who presents the late night phone-in on BBC Radio Manchester and BBC Radio Lancashire.\n\nQuestion: Which canal is found near this area where BBC Radio Manchester is based?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"radio_station_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the BBC local radio station.\"\n    },\n    \"base_location\": {\n      \"type\": \"string\",\n      \"description\": \"The specific area where the radio station is based.\"\n    },\n    \"nearby_canal\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the canal found near the radio station's base location.\"\n    }\n  },\n  \"required\": [\n    \"radio_station_name\",\n    \"base_location\",\n    \"nearby_canal\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "radio_station_name": {
        "type": "string",
        "description": "The name of the BBC local radio station."
      },
      "base_location": {
        "type": "string",
        "description": "The specific area where the radio station is based."
      },
      "nearby_canal": {
        "type": "string",
        "description": "The name of the canal found near the radio station's base location."
      }
    },
    "required": [
      "radio_station_name",
      "base_location",
      "nearby_canal"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

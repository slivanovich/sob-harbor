{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nUniversity College Cork A.F.C.: University College Cork Association Football Club is an Irish association football club based in Cork.  It was founded in 1952 by students at University College Cork.  It's senior men's team currently play in the Munster Senior League Senior Premier Division.  They also regularly compete in the Munster Senior Cup and the Collingwood Cup.  They have also played in the FAI Cup and the FAI Intermediate Cup.  In 2013–14 they were Munster Senior League champions and as a result were invited to play in the 2015 League of Ireland Cup.  In 2015 they completed an Intervarsity treble – winning the Collingwood Cup, the Crowley Cup and the Harding Cup.  UCC A.F.C. currently fields teams in the Munster Senior League, the Cork Athletic Union League, the College & Universities Football League and the Women's Soccer Colleges Association of Ireland League.\n\nNordring Berlin: SG Nordring Berlin is a German association football club based in the capital city of Berlin.  The club traces its roots back to 22 November 1893 establishment of \"Berliner Fussball Club vom Jahre 1893\".  \"BFC 93\" became one of the founding clubs of the DFB (Deutscher Fussball Bund, en:German Football Association) at Leipzig in 1900.  They played top flight city football in the Märkischer Fussball Bund from 1904–07 before slipping to lower tier competition.\n\nAviron Bayonnais FC: Aviron Bayonnais Football Club (] ; commonly referred to as simply Bayonne) is a French association football club based in Bayonne.  The club is a part of a sports club that was formed in 1904 that is also known for its rugby union club.  The football club was founded in 1935 and currently play in the Championnat National 3, the fifth level of French football.  Bayonne plays its home matches at the Stade Didier Deschamps located in the city.  It is named after Bayonne native, former youth player and the 1998 FIFA World Cup and UEFA Euro 2000 winning captain Didier Deschamps, who also played for Marseille and Juventus.\n\nAkademischer BC 1897 Charlottenburg: Akademischer Ballspiel-Club 1897 Charlottenburg was a German association football club based in the Charlottenburg district of Berlin.  Founded on 31 May 1897, it is notable as one of the founding clubs of the German Football Association (Deutscher Fussball Bund or German Football Association) in Leipzig in 1900.\n\nHertha BSC in European football: Hertha, Berliner Sport-Club e.V., commonly known as Hertha BSC (] ), Hertha Berlin or simply Hertha, is a German association football club based in the Charlottenburg locality of Berlin.\n\nLlandudno Ladies F.C.: Llandudno Ladies Football Club, currently known as MBi Llandudno Ladies Football Club due to sponsorship, are a Welsh women's association football club based in Llandudno Junction, Conwy County Borough.  They currently play their home games at Maes Du and play in the Welsh Premier Women's Football League.\n\nHertha BSC: Hertha, Berliner Sport-Club e.V., commonly known as Hertha BSC (] ), Hertha Berlin or simply Hertha, is a German association football club based in the Charlottenburg locality of Berlin.  Hertha BSC plays in the Bundesliga, the top-tier division of German football, after finishing at the top of the 2.  Bundesliga table at the end of the 2012–13 season.\n\nCFC Hertha 06: CFC Hertha 06 is a German association football club from the Charlottenburg district of Berlin.  The club's greatest success has been promotion to the tier five NOFV-Oberliga Nord in 2015.\n\nSteve von Bergen: Steve von Bergen (born 10 June 1983) is a Swiss professional footballer who plays as defender for Young Boys.  He played for FC Zürich for two full seasons, winning the Swiss Super League in both campaigns and then moved to Hertha BSC, playing there for three years.  He managed to establish himself as a regular on the Switzerland national football team, earning over 40 caps since his debut in 2006 and playing at two World Cups.\n\nSukhothai F.C.: Sukhothai Football Club (Thai สโมสรฟุตบอลจังหวัดสุโขทัย) is a Thai professional association football club based in Sukhothai province.  They currently play in the Thai League 1.  Sukhothai FC represents the Sukhothai Province mainly known for being the first Kingdom of Thailand.  Their main team colors are red and white and their away colors are black and green.  Sukhothai FC currently play all their home matches at the Thalay Luang Stadium which has a maximum capacity of 9,500.\n\nQuestion: Which club does the Swiss professional footballer and former member of the German association football club based in the Charlottenburg locality of Berlin currently play for?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"footballer\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the professional footballer.\"\n        },\n        \"nationality\": {\n          \"type\": \"string\",\n          \"description\": \"The nationality of the footballer.\"\n        },\n        \"position\": {\n          \"type\": \"string\",\n          \"description\": \"The playing position of the footballer.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"nationality\",\n        \"position\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"former_club\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the former club.\"\n        },\n        \"country\": {\n          \"type\": \"string\",\n          \"description\": \"The country where the former club is based.\"\n        },\n        \"location\": {\n          \"type\": \"string\",\n          \"description\": \"The specific locality or district of the former club.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"country\",\n        \"location\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"current_club_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the club the footballer currently plays for.\"\n    }\n  },\n  \"required\": [\n    \"footballer\",\n    \"former_club\",\n    \"current_club_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "footballer": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the professional footballer."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the footballer."
          },
          "position": {
            "type": "string",
            "description": "The playing position of the footballer."
          }
        },
        "required": [
          "name",
          "nationality",
          "position"
        ],
        "additionalProperties": false
      },
      "former_club": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the former club."
          },
          "country": {
            "type": "string",
            "description": "The country where the former club is based."
          },
          "location": {
            "type": "string",
            "description": "The specific locality or district of the former club."
          }
        },
        "required": [
          "name",
          "country",
          "location"
        ],
        "additionalProperties": false
      },
      "current_club_name": {
        "type": "string",
        "description": "The name of the club the footballer currently plays for."
      }
    },
    "required": [
      "footballer",
      "former_club",
      "current_club_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

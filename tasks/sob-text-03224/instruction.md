{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nRafael Márquez (boxer): Rafael Márquez Méndez (born 25 March 1975) is a Mexican former professional boxer who competed from 1995 to 2013.  He is a two-time world champion in two weight classes, having held the IBF bantamweight title from 2003 to 2007; and the WBC, \"Ring\" magazine, and lineal super bantamweight titles in 2007.  He also held the IBO bantamweight title from 2005 to 2007, and challenged once for WBO featherweight title in 2011.  Márquez was known for his formidable knockout power and relentless pressure fighting style.  His older brother Juan Manuel Márquez is also a professional boxer and multiple-time world champion.\n\nJuan Manuel Márquez: Juan Manuel Márquez Méndez (born August 23, 1973) is a Mexican former professional boxer who competed from 1993 to 2014.  He is the third Mexican boxer (after Érik Morales and Jorge Arce) to become a four-weight world champion, having formerly held nine world championships including the WBA (Super), IBF, and WBO featherweight titles between 2003 and 2007; the WBC super featherweight title from 2007 to 2008; the WBA (Super), WBO, \"Ring\" magazine, and lineal lightweight titles between 2008 and 2012; and the WBO junior welterweight title from 2012 to 2013.\n\nJermall Charlo: Jermall Charlo (born May 19, 1990) is an American professional boxer who held the IBF light middleweight title from 2015 to 2017.  His identical twin brother, Jermell Charlo, is also a professional boxer and is younger by one minute.  Both brothers are graduates of Hastings High School.  They began boxing when they started following their father, himself a former boxer, into the gym.  In 2016, both brothers became world champions when Jermell won the WBC light middleweight title.\n\nLiam Smith (boxer): Liam Smith (born 27 July 1988) is a British professional boxer.  He held the WBO light-middleweight title from 2015 to 2016, having previously held the Commonwealth light-middleweight title from 2012 to 2013, and the British light-middleweight title from 2013 to 2015.  Liam is the younger brother of Paul Smith and Stephen Smith, and the older brother of Callum Smith; all of whom are also professional boxers.\n\nAnthony Dirrell: Anthony Dirrell (born October 14, 1984) is an American professional boxer who held the WBC super middleweight title from 2014 to 2015.  He is the younger brother of 2004 Olympic bronze medalist Andre Dirrell, who is also a professional boxer.\n\nRatanachai Sor Vorapin: Ratanachai Sor Vorapin is a professional boxer and a former WBO bantamweight champion.  He is the younger brother of Ratanapol Sor Vorapin, a former IBF strawweight champion.\n\nCallum Smith: Callum Smith (born 23 April 1990) is a British professional boxer who competes in the super-middleweight division, and held the European, the British, and the WBC Silver titles between 2015 and 2017.  He is the youngest of the Smith brothers—Paul, Stephen, and Liam—all of whom are professional boxers.\n\nTyson Fury: Tyson Luke Fury (born 12 August 1988) is a British professional boxer.  He has held the \"Ring\" magazine heavyweight title since 2015, after defeating long-reigning world champion Wladimir Klitschko.  In the same fight, Fury also won the unified WBA (Super), IBF, WBO, IBO and lineal titles, with the victory earning him Fighter of the Year and Upset of the Year awards by \"The Ring\".  Fury was subsequently stripped of the IBF title later that year for being unable to grant a fight against their mandatory challenger, Vyacheslav Glazkov, due to agreeing to a rematch with Klitschko.  In 2016, Fury vacated the WBA, WBO, IBO, and lineal titles following an ongoing medical investigation and personal issues and two cancellations of the Klitschko rematch.  In August 2016, Fury was ranked by BoxRec as the world's sixth best active boxer, pound for pound.\n\nDrian Francisco: Drian Francisco (born November 10, 1982 in Sablayan, Occidental Mindoro, Philippines), nicknamed Gintong Kamao (Golden Fist), is a Filipino professional boxer.  Born in the province of Mindoro, Francisco currently resides in Agoncillo, Batangas.  His younger brother Lloyd Francisco, like him, is also a professional boxer.\n\nJorge Arce: Jorge Armando Arce Armenta ( ; born July 27, 1979), best known as Jorge Arce, is a Mexican former professional boxer who competed from 1996 to 2014.  He is a five-time world champion, and the second boxer from Mexico to win world titles in four weight divisions (after Érik Morales, who first achieved the feat two months prior).  In a storied career, Arce held the WBO light flyweight title from 1998 to 1999; the WBC and lineal light flyweight titles from 2002 to 2004; the WBO super flyweight title in 2010; the WBO junior featherweight title in 2011; and the WBO bantamweight title from 2011 to 2012.  Additionally he held the WBC interim flyweight title from 2005 to 2006, the WBA interim super flyweight title from 2008 to 2009, and challenged once for the WBC featherweight title in his final fight in 2014.\n\nQuestion: The professional boxer, who held the WBO ligh-middleweight from 2015-2016, has a younger brother who is also a professional boxer; what is this brother's name?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"main_boxer\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"title_held\": {\n          \"type\": \"string\"\n        },\n        \"title_reign_years\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"start_year\": {\n              \"type\": \"integer\"\n            },\n            \"end_year\": {\n              \"type\": \"integer\"\n            }\n          },\n          \"required\": [\n            \"start_year\",\n            \"end_year\"\n          ],\n          \"additionalProperties\": false\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"title_held\",\n        \"title_reign_years\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"related_boxer\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"relationship_to_main_boxer\": {\n          \"type\": \"string\"\n        },\n        \"is_professional_boxer\": {\n          \"type\": \"boolean\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"relationship_to_main_boxer\",\n        \"is_professional_boxer\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"answer\": {\n      \"type\": \"string\"\n    }\n  },\n  \"required\": [\n    \"main_boxer\",\n    \"related_boxer\",\n    \"answer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "main_boxer": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "title_held": {
            "type": "string"
          },
          "title_reign_years": {
            "type": "object",
            "properties": {
              "start_year": {
                "type": "integer"
              },
              "end_year": {
                "type": "integer"
              }
            },
            "required": [
              "start_year",
              "end_year"
            ],
            "additionalProperties": false
          }
        },
        "required": [
          "name",
          "title_held",
          "title_reign_years"
        ],
        "additionalProperties": false
      },
      "related_boxer": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "relationship_to_main_boxer": {
            "type": "string"
          },
          "is_professional_boxer": {
            "type": "boolean"
          }
        },
        "required": [
          "name",
          "relationship_to_main_boxer",
          "is_professional_boxer"
        ],
        "additionalProperties": false
      },
      "answer": {
        "type": "string"
      }
    },
    "required": [
      "main_boxer",
      "related_boxer",
      "answer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

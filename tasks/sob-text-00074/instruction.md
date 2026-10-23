{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nHemel Hempstead Town F.C.: Hemel Hempstead Town Football Club is a semi-professional football club based in Hemel Hempstead, Hertfordshire, England.  Affiliated to the Hertfordshire County Football Association, they are currently members of the National League South, the sixth tier of English football, and play at Vauxhall Road.\n\nJordan Parkes: Jordan David Parkes (born 26 July 1989) is an English semi professional association footballer, who plays as an attacking midfielder for Hemel Hempstead Town and has also played as a full back.\n\n2015 Rakhine United F.C. season: Rakhine United FC (Burmese: ရခိုင်ယူနိုက်တက် ဘောလုံးအသင်း ) Football Club is a professional football club, based in Rakhine State, that plays in the Myanmar National League.  Rakhine United Football Club in 2009, the club changed its name to Rakhapura United in December,2010.  Home Stadium to use Waytharli Yinpyin in Sittwe Township, Rakhine State.  Now they use to play in Thuwanna YTC Stadium as home.  Last season Rakhapura United FC stand 10th position.  Rakhine United FC biggest won (7-2) in General Aung San Cup against Manaw Myay.\n\nRakhine United F.C.: Rakhine United Football Club (Burmese: ရခိုင်ယူနိုက်တက် ဘောလုံးအသင်း ) is a professional football club, based in Rakhine State, that plays in the Myanmar National League.  Rakhine United Football Club in 2009, the club changed its name to Rakhapura United in December,2010.  Home Stadium to use Waytharli Yinpyin in Sittwe Township, Rakhine State.  Now they use to play in Thuwanna YTC Stadium as home.  Last season Rakhapura United FC stand 10th position.  Rakhapura United Football Club drawn with Yadanabon FC, that time Yadanarbon FC is the Champion of MNL.  That match is the first ever professional match in Myanmar National League.  In December 2012, the club has used its origin name Rakhine United F.C..\n\n2016 Rakhine United F.C. season: Rakhine United FC (Burmese: ရခိုင်ယူနိုက်တက် ဘောလုံးအသင်း ) Football Club is a professional football club, based in Rakhine State, that plays in the Myanmar National League.  Rakhine United Football Club in 2009, the club changed its name to Rakhapura United in December,2010.  Home Stadium to use Waytharli Yinpyin in Sittwe Township, Rakhine State.  Now they use to play in Thuwanna YTC Stadium as home.  Last season Rakhapura United FC stand 10th position.  Rakhine United FC biggest won (7-2) in General Aung San Cup against Manaw Myay.\n\nReza Bahmaei: Mohammad Hassan Fakori Far (Persian: محمد حسن فکوری فر‎ ‎ ) is an Iranian Football Forward who currently plays for English football club Esteghlal Ahvaz.  Fakori plays as a forward but is also able to play as a winger or attacking midfielder.\n\nJosue Dos Santos: Josue Dos Santos or simply Valmir (born 11 April 1979) is a Brazilian football player.  He currently plays for Brusque Futebol Clube.  Valmir is a central midfielder who plays in the holding midfield role or as an attacking midfielder.  Despite often being used in a defensive position, he is mainly an attacking player.\n\n2017 Rakhine United FC season: Rakhine United FC (Burmese: ရခိုင်ယူနိုက်တက် ဘောလုံးအသင်း ) Football Club is a professional football club, based in Rakhine State, that plays in the Myanmar National League.  Rakhine United Football Club in 2009, the club changed its name to Rakhapura United in December,2010.  Home Stadium to use Waytharli Yinpyin in Sittwe Township, Rakhine State.  Now they use to play in Thuwanna YTC Stadium as home.  Last season Rakhapura United FC stand 10th position.  Rakhine United FC biggest won (7-2) in General Aung San Cup against Manaw Myay.\n\nLim Shiya: Lim Shiya (born 26 June 1986) is a Singaporean footballer who plays as a midfielder for Australian W-League team Perth Glory.  She made her debut for the Singapore Women's National Team on 18 April 2004, coming off the bench against Hong Kong in the AFC Beijing Olympics Qualifiers 2004 held at Hiroshima Big Arch Stadium in Osaka, Japan.  She made her team debut for Home United FC (Women’s Team) in the FAS Women’s Challenge Cup 2001 at the age of 15 and played for FAS Young Women in 2003 before moving to Arion Women's Football Club, the Singapore’s first all-women football club in 2006.  A left-footed attacking midfielder who possesses good pace and dribbling skills, Shiya is known for her vision, technique and passing.  She is also a regular goal scorer for her club.\n\nQi Hong: Qi Hong (; born June 3, 1976 in Shanghai) is a former Chinese international footballer who played as an attacking midfielder or shadow striker throughout his career.  He is predominately remembered for his time at Shanghai Shenhua where he won the league and Chinese FA Cup with them before controversially moving to then local neighbours Shanghai Zhongyuan Huili.  While internationally he is remembered for being part of the Chinese squad that came fourth within the 2000 AFC Asian Cup as well as also being part of the squad that took part in the 2002 FIFA World Cup.  Since retiring he would help form a local football club called Shanghai Lucky Star Youth Football Club, however on October 12, 2010 he was detained by police for his involvement in fixing a league game against Tianjin Teda F.C. on November 30, 2003 and was sentenced to five and a half years imprisonment on June 13, 2012.\n\nQuestion: What is the home stadium of this football club where Jordan Parkes plays as an attacking midfielder?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"football_club\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the football club.\"\n        },\n        \"home_stadium\": {\n          \"type\": \"string\",\n          \"description\": \"The home stadium of the football club.\"\n        },\n        \"league_tier\": {\n          \"type\": \"string\",\n          \"description\": \"The league or tier the club is currently a member of.\"\n        },\n        \"affiliation\": {\n          \"type\": \"string\",\n          \"description\": \"The football association the club is affiliated with.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"home_stadium\",\n        \"league_tier\",\n        \"affiliation\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"player\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the player.\"\n        },\n        \"position\": {\n          \"type\": \"string\",\n          \"description\": \"The primary playing position of the player.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"position\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"answer\": {\n      \"type\": \"string\",\n      \"description\": \"The home stadium of the football club where the player plays.\"\n    }\n  },\n  \"required\": [\n    \"football_club\",\n    \"player\",\n    \"answer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "football_club": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the football club."
          },
          "home_stadium": {
            "type": "string",
            "description": "The home stadium of the football club."
          },
          "league_tier": {
            "type": "string",
            "description": "The league or tier the club is currently a member of."
          },
          "affiliation": {
            "type": "string",
            "description": "The football association the club is affiliated with."
          }
        },
        "required": [
          "name",
          "home_stadium",
          "league_tier",
          "affiliation"
        ],
        "additionalProperties": false
      },
      "player": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the player."
          },
          "position": {
            "type": "string",
            "description": "The primary playing position of the player."
          }
        },
        "required": [
          "name",
          "position"
        ],
        "additionalProperties": false
      },
      "answer": {
        "type": "string",
        "description": "The home stadium of the football club where the player plays."
      }
    },
    "required": [
      "football_club",
      "player",
      "answer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJohn Lindsay (Paralympian): John Lindsay, OAM (born 29 January 1970) is an Australian Paralympic athlete from Melbourne.  He competed in the 1988 Seoul games in distances ranging from 100 m to 800 m, but did not win any medals.  At the 1992 Barcelona Games, he won a gold medal in the Men's 200 m TW3 event, for which he received a Medal of the Order of Australia, a silver medal in the Men's 100 m TW3 event and a bronze medal in the Men's 400 m TW3 event.  That year, he had a Victorian Institute of Sport scholarship.  He was also working as a fitness instructor in 1992, held world records in the 100 m and 200 m events, and was ranked 6th in the world in the 400 m.  He won a gold medal in the men's athletics 100 m T52 event at the 1996 Summer Paralympics with a time of 15.22, a silver medal in the 200 m T52 event with a time of 27.38, and a bronze medal in the 400 m T52 event with a time of 52.93.  At the 2000 Sydney Games, he won a gold medal in the Men's 100 m T53 event, a silver medal as part of the Men's 4x100 m Relay T54 team, and a bronze medal in the Men's 200 m T53 event; he was also part of the Men's 4x400 m Relay T54 team, which was the only one to qualify in its heat, but it did not make it to the finals.  At the 2004 Athens Games, he came seventh in the first round of the Men's 100 m T53 event and sixth in the third round of the Men's 200 m T53 event.  He was an Australian Institute of Sport scholarship holder in 1995 and 2000.\n\nAlfredo Rota: Alfredo Rota (born 21 July 1975) is an Italian fencer.  He won the bronze medal in the men's team épée event at the 2008 Summer Olympics.  He also won the Olympic gold medal in Men's Team Épée at the 2000 Sydney Olympics.\n\nIstván Görgényi: István Görgényi (born 2 November 1946) is a Hungarian former water polo player won won a silver medal at the 1972 Summer Olympics and coached the Australian women's national water polo team to the gold medal at the 2000 Sydney Olympics.\n\nSébastien Flute: Sébastien Flute (born 25 March 1972 in Brest, Finistère) is a gold medal winning French archer.  He currently has the 25th best ranking in the world among archers.  He won the gold medal in the Men's Individual competition in the 1992 Summer Olympics, the 20-year-old European champion defeated all three South Korean archers on his way to the Olympic Title; and also competed in the 1996 Olympic Games and the 2000 Olympic Games.  He retired from International competition after the 2000 Sydney Olympics.\n\nFeroze Khan (field hockey): Feroze Khan (Urdu: فیروز خان) (September 9, 1904 – April 21, 2005) was, at the time of his death, the world's oldest Olympic gold medal winner, following the death of U.S. athlete James Rockefeller in 2004.  He was part of British India's Olympic hockey team at the 1928 Summer Olympics in Amsterdam, the Netherlands, who won the gold medal for the event.  After his death, Roger Beaufrand of France became the oldest living Olympic gold medal winner.\n\nCamp Orange (UK &amp; Ireland): The UK & Irish version of Camp Orange is a children's reality television show broadcast on Nickelodeon (UK & Ireland).  The first season premiered on 22 July 2011.  It is currently in its second season which premiered on 12 August 2012.  The series is hosted by Anna Williamson, Jamie Rickers and Denise Lewis.\n\nCalvin Harrison: Calvin Harrison (born January 20, 1974) is an American athlete.  He won a gold medal in the men's 4 × 400 metres relay at the 2000 Summer Olympics in Sydney, Australia.  He is the identical twin brother of fellow Olympic medalist Alvin Harrison.  At the 2000 Olympics, Alvin Harrison and Calvin Harrison made history by becoming the first twins ever to compete and win Olympic gold medals together on the same relay team since the inception of the modern Olympic Games.  In the 4 × 400 m relay, Alvin ran the first leg and Calvin ran the third leg.  In 2008, the 2000 Sydney Olympics 4×400 metres relay US team was stripped of their medals after teammate Antonio Pettigrew admitted that he had used performance-enhancing drugs.\n\nDenise Lewis: Denise Lewis OBE (born 27 August 1972, in West Bromwich) is a retired English track and field athlete, who specialised in the heptathlon.  She won the gold medal in the heptathlon at the 2000 Sydney Olympics.\n\nHeavy Seas Beer: Heavy Seas Beer is brewed by Clipper City Brewing Company, in Baltimore, Maryland.  The brewery was established by Hugh Sisson in 1995.  Previously, Sisson operated Maryland's first brewpub, Sisson's.  In 2010, the brewery rebranded.  While the name of the company remains Clipper City Brewing Company, all of its beer falls under the Heavy Seas brand.  Heavy Seas hosts tours on most weekends.  It is located at 4615 Hollins Ferry Road, Suite B, in the Halethorpe section of Baltimore.  Heavy Seas currently offers a variety of beer styles in approx. 18 states within the United States.  Several Heavy Seas beers have been awarded and include the following: Cutlass Amber Lager (a repeat medal winner at the Great American Beer Festival from 2006-2010, bronze medal winner at the 2010 World Beer Cup and silver medal winner at the 2012 World Beer Cup as Heavy Seas Märzen), Powder Monkey Pale Ale (silver medal winner at the 2008 Great American Beer Festival and bronze medal winner at the 2010 World Beer Cup as Heavy Seas Pale Ale), Small Craft Warning Uber Pils (bronze medal winner at the 2004 Great American Beer Festival), Gold Ale (gold medal winner at the 2010 World Beer Cup, bronze medal winner at the 2010 Great American Beer Festival and bronze medal winner at the 2014 Great American Beer Festival as Heavy Seas Gold Ale) and Winter Storm Imperial ESB (gold medal winner at the 2008 World Beer Cup).\n\nNick Porzig: Nicholas Weston Porzig (born 1 July 1972 in Cape Town) is a South African-born rower who competed for Australia from 1993 to 2000.  He rowed in the 1996 Atlanta and 2000 Sydney Olympics in the men's VIII.  He won a silver medal at the Sydney Olympics.\n\nQuestion: The gold medal winner in the heptathlon at the 2000 Sydney Olympics co-hosts a children's tv show that premiered in what year?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"olympic_athlete\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"olympic_games\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"year\": {\n              \"type\": \"integer\"\n            },\n            \"city\": {\n              \"type\": \"string\"\n            },\n            \"event\": {\n              \"type\": \"string\"\n            },\n            \"medal\": {\n              \"type\": \"string\"\n            }\n          },\n          \"required\": [\n            \"year\",\n            \"city\",\n            \"event\",\n            \"medal\"\n          ],\n          \"additionalProperties\": false\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"olympic_games\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"childrens_tv_show\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\"\n        },\n        \"role\": {\n          \"type\": \"string\"\n        },\n        \"premiere_year\": {\n          \"type\": \"integer\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"role\",\n        \"premiere_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"answer_year\": {\n      \"type\": \"integer\"\n    }\n  },\n  \"required\": [\n    \"olympic_athlete\",\n    \"childrens_tv_show\",\n    \"answer_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "olympic_athlete": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "olympic_games": {
            "type": "object",
            "properties": {
              "year": {
                "type": "integer"
              },
              "city": {
                "type": "string"
              },
              "event": {
                "type": "string"
              },
              "medal": {
                "type": "string"
              }
            },
            "required": [
              "year",
              "city",
              "event",
              "medal"
            ],
            "additionalProperties": false
          }
        },
        "required": [
          "name",
          "olympic_games"
        ],
        "additionalProperties": false
      },
      "childrens_tv_show": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string"
          },
          "role": {
            "type": "string"
          },
          "premiere_year": {
            "type": "integer"
          }
        },
        "required": [
          "title",
          "role",
          "premiere_year"
        ],
        "additionalProperties": false
      },
      "answer_year": {
        "type": "integer"
      }
    },
    "required": [
      "olympic_athlete",
      "childrens_tv_show",
      "answer_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

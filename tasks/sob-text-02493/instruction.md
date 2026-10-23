{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nRobyn Ah Mow-Santos: Robyn Mokihana Ah Mow-Santos (perf, born September 15, 1975) is the head coach of the Hawaii Rainbow Wahine volleyball team and a former American indoor volleyball player.  She is a setter on the USA national team and played at the 2000 Sydney Olympics, the 2004 Athens Olympics, and also played at the 2008 Beijing Olympics, helping Team USA to a silver medal.  She worked as an assistant coach at the University of Hawaii Rainbow Wahine volleyball team until 2016.\n\nSteve Jefferys: Steve Jefferys (born in Australia) was the lone rider in the Sydney Olympics Opening Ceremony.  He galloped into the stadium on his 7-year-old Australian Stock Horse \"Ammo\", which reared, and then Jefferys cracked his whip to signal the beginning of the Opening Ceremony.  This was followed by the entrance of a further 120 riders (which included Steve Jefferys' wife, Sandra Langsford) and their Stock Horses.\n\n2014 Winter Olympics torch relay: The 2014 Winter Olympics torch relay was run from October 7, 2013, 123 days prior to the Sochi 2014 Winter Olympics, until February 7, 2014, the day of the opening ceremony at Sochi.  In Russia the relay traveled from Moscow to Sochi through 2,900 towns and villages across all 83 federal subjects of Russia by foot, car, train, plane, and \"troika\" for over 65,000 km of journey.  The event became the longest relay in Winter Olympics history.\n\nSydney Blue Sox: The Sydney Blue Sox are a professional baseball team, and one of six foundation teams in the re-formed Australian Baseball League (ABL).  The team plays their home games at Blacktown International Sportspark (BISS), one of the two venues used for baseball at the 2000 Sydney Olympics, when it was known as Blacktown Olympic Park.  The Blue Sox hosted the league's Opening Day for the inaugural season on 6 November 2010, when they played against the Canberra Cavalry, and won the game 1–0.  The Blue Sox are the only team in the Australian Baseball League to implement sabermetrics as a way to run their team with volunteer statistician, Anthony Rescan.\n\nRoy Heiner: Roy Heiner (born 22 November 1960, in Virginia, Free State, South Africa) is a sailor from the Netherlands, who represented his country at the 1988 Summer Olympics in Pusan.  Heiner took 7th place in the Finn.  In 1992 Summer Olympics, Barcelona Heiner helmed the Dutch Soling.  With crew members Peter Burggraaff and Han Bergsma Heiner took 18th place.  Heiner switched back to the Finn for the 1996 Summer Olympics, Savannah and took the Bronze medal.  His last Olympic appearance was in the 2000 Sydney Olympics.  With crew members Peter van Niekerk and Dirk de Ridder Heiner took 4th place in the Soling.\n\nJulie Anthony (singer): Julie Moncrief Anthony (née Lush) AM OBE (born 24 August 1949 in Lameroo, South Australia), better known as Julie Anthony, is an Australian soprano and entertainer.  She sang the Australian National Anthem at the Opening Ceremony of the 2000 Sydney Olympics with Human Nature.\n\nOn a Night Like This (concert tour): On a Night Like This was the sixth concert tour by Australian recording artist, Kylie Minogue.  The tour supports her seventh studio album \"Light Years\" that began in March 2001.  Having hit the headlines around the globe for her hugely successful performance at the Sydney Olympics in 2000, and having subsequently performed again at the opening ceremony of Sydney's Paralympics soon after, Minogue seized the opportunity to announce details of her new tour.  It became the fastest-selling concert tour of her career when tickets went on sale that November, and with dozens of sell-out shows, she had succeeded in establishing herself as one of the most in-demand live entertainers.  The tour began with a bumpy start, however, when the first show in Dublin, Ireland, scheduled for 1 March, had to be cancelled due to treacherous storms preventing air travel into the country.\n\nNick Porzig: Nicholas Weston Porzig (born 1 July 1972 in Cape Town) is a South African-born rower who competed for Australia from 1993 to 2000.  He rowed in the 1996 Atlanta and 2000 Sydney Olympics in the men's VIII.  He won a silver medal at the Sydney Olympics.\n\nCalvin Harrison: Calvin Harrison (born January 20, 1974) is an American athlete.  He won a gold medal in the men's 4 × 400 metres relay at the 2000 Summer Olympics in Sydney, Australia.  He is the identical twin brother of fellow Olympic medalist Alvin Harrison.  At the 2000 Olympics, Alvin Harrison and Calvin Harrison made history by becoming the first twins ever to compete and win Olympic gold medals together on the same relay team since the inception of the modern Olympic Games.  In the 4 × 400 m relay, Alvin ran the first leg and Calvin ran the third leg.  In 2008, the 2000 Sydney Olympics 4×400 metres relay US team was stripped of their medals after teammate Antonio Pettigrew admitted that he had used performance-enhancing drugs.\n\nAdvance Australia Fair: \"Advance Australia Fair\" is the national anthem of Australia.  Created by the Scottish-born composer Peter Dodds McCormick, the song was first performed in 1878 and sung in Australia as a patriotic song.  It replaced \"God Save the Queen\" as the official national anthem in 1984, following a plebiscite to choose the national song in 1977.  Other songs and marches have been influenced by \"Advance Australia Fair\", such as the Australian vice-regal salute.\n\nQuestion: At the Opening Ceremony of the 2000 Sydney Olympics Julie Moncrief Anthony sang an anthem created by what composer?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"olympic_event\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"year\": {\n          \"type\": \"integer\"\n        },\n        \"city\": {\n          \"type\": \"string\"\n        },\n        \"ceremony_type\": {\n          \"type\": \"string\"\n        }\n      },\n      \"required\": [\n        \"year\",\n        \"city\",\n        \"ceremony_type\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"performer\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"role\": {\n          \"type\": \"string\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"role\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"anthem\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\"\n        },\n        \"type\": {\n          \"type\": \"string\"\n        },\n        \"composer\": {\n          \"type\": \"object\",\n          \"properties\": {\n            \"name\": {\n              \"type\": \"string\"\n            },\n            \"origin\": {\n              \"type\": \"string\"\n            }\n          },\n          \"required\": [\n            \"name\",\n            \"origin\"\n          ],\n          \"additionalProperties\": false\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"type\",\n        \"composer\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"olympic_event\",\n    \"performer\",\n    \"anthem\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "olympic_event": {
        "type": "object",
        "properties": {
          "year": {
            "type": "integer"
          },
          "city": {
            "type": "string"
          },
          "ceremony_type": {
            "type": "string"
          }
        },
        "required": [
          "year",
          "city",
          "ceremony_type"
        ],
        "additionalProperties": false
      },
      "performer": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "role": {
            "type": "string"
          }
        },
        "required": [
          "name",
          "role"
        ],
        "additionalProperties": false
      },
      "anthem": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string"
          },
          "type": {
            "type": "string"
          },
          "composer": {
            "type": "object",
            "properties": {
              "name": {
                "type": "string"
              },
              "origin": {
                "type": "string"
              }
            },
            "required": [
              "name",
              "origin"
            ],
            "additionalProperties": false
          }
        },
        "required": [
          "title",
          "type",
          "composer"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "olympic_event",
      "performer",
      "anthem"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

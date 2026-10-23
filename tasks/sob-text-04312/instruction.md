{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nGaro Special: Byakuya no Maju: Garo Special: Byakuya no Maju (牙狼〈GARO〉スペシャル 白夜の魔獣 , GARO Supesharu Byakuya no Majū , subtitle literally \"Demon Beast of the Midnight Sun\") is a two-part made-for-TV movie of the Japanese tokusatsu series \"Garo\" that aired at the end of 2006.\n\nGaro Hills Autonomous District Council: Garo Hills Autonomous District Council (GHADC) is seated at Tura and covers East Garo Hills district, West Garo Hills district, South Garo Hills District, North Garo Hills District and South West Garo Hills District is one of the three Autonomous District Councils within Meghalaya state, and one of fourteen autonomous regions of India.\n\nAmpati: Ampati is a district headquarters of South West Garo Hills of Meghalaya state in north-eastern India.  South West Garo Hills is curved of present West Garo Hills on 7 August 2012.  It is located at the latitude of 25º27.505 and longitude of 089º56.456 and is 52 km away from the district headquarters Tura of West Garo Hills district, Meghalaya.  The hill region is mostly inhabited by the Garos, while in the foothills there are Hajongs and Kochs.The second largest ethnicity after Garos is Hajongs.  The district is surrounded by Dhubri district of Assam and Kurigram District of Bangladesh.  South West Garo Hills has approximately 35 kilometres of international boundary with Bangladesh on the south and western side.  Nearly one third of the total number of villages of the district is declared as border villages by the Border Area Development Department.\n\nGaro: The Animation: Garo: The Animation is a Japanese anime series based on the \"Garo\" tokusatsu drama.  The anime is set in the distant past compared to the contemporary settings of the live action series.  The first series, titled in Japan as Garo: The Carved Seal of Flames (Japanese: 牙狼〈GARO〉-炎の刻印- , Hepburn: GARO -Honō no Kokuin- ) , premiered in October 2014.  It was licensed for streaming in North America by Funimation.\n\nPa Togan Sangma: Pa Togan Sangma also known as Togan Sangma or Pa Togan Nengminja Sangma was a Garo tribe leader from Garo hills in North East India.  In 1872, during the British occupation of Garo Hills in present Indian state of Meghalaya, the local Garo tribe warriors were led by a young man called Togan Sangma.  His troops met the British troops at Rongrenggiri.\n\nReuben Nakian: Reuben Nakian (born August 10, 1897, College Point, New York – died December 4, 1986, Stamford, Connecticut) was an American sculptor and teacher of Armenian extraction.  His recurring themes are from Greek and Roman mythology.  Noted works include \"Leda and the Swan\", \"The Rape of Lucrece\", \"Hecuba\", and \"The Birth of Venus\".  He was also commissioned to create portraits of Roosevelt's cabinet in the 1930s.\n\nBill Capece: William George Capece (born April 1, 1959 in Miami, Florida) is a former professional American football player who played placekicker for three seasons for the Tampa Bay Buccaneers.  He attended Chaminade-Madonna College Preparatory School in Hollywood, Florida along with David Shula, and was invited by Shula's father, Miami Dolphins coach Don Shula, to attend Dolphin practices and work out with placekicker Garo Yepremian.  It was Yepremian who provided Capece with the encouragement to consider a career in professional football.  Capece attended Florida State University, where he graduated as the holder of FSU's records for single-season scoring (104 points), most field goals in a game (five, against Pittsburgh), and field goal percentage (100%).  His 104 points in 1980 were the most by a kicker in national collegiate history.  He was signed to a professional contract with the Buccaneers in 1981, during a week in which the Buccaneers cut both their placekicker and their punter.  Ironically, Capece's signing marked the end of his former mentor's career, as Yepremian was the player he was signed to replace.  After a late-1983 loss to the Green Bay Packers in which missed kicks provided the margin of defeat, coach John McKay made his famous announcement that \"Capece is kaput\".  Capece returned as the team's placekicker the following season, but was waived following a poor performance in a preseason game against the Dolphins.  His 41 field goals stood as the Buccaneers' career record until broken in 1987 by Donald Igwebuike.\n\nGaro Yepremian: Garabed Sarkis \"Garo\" Yepremian (June 2, 1944 – May 15, 2015) was an American football placekicker in the National Football League for the Detroit Lions, Miami Dolphins, New Orleans Saints, and Tampa Bay Buccaneers, during a career that spanned from 1966 to 1981.\n\nGaro: Gold Storm Sho: Garo: Gold Storm Sho (牙狼〈GARO〉－GOLD STORM－翔 , Garo -GOLD STORM- Shō , lit.  \"Garo: Gold Storm Flight\") is both a film and the fifth television series in the \"Garo\" continuity that serve as sequels to \"\".  Wataru Kuriyama and Miki Nanri reprise their roles and are joined by new cast members (among them is Masahiro Inoue as the series antagonist Zinga).  The film adaptation was released in theatres on March 28, 2015, while the television series began broadcast on April 3, 2015.\n\nGaro: Makai no Hana: Garo: Makai no Hana (牙狼〈GARO〉-魔戒ノ花- , \"Garo: The Makai Flower\") is a 2014 Japanese tokusatsu television drama.  It is the fourth television series set in the \"Garo\" universe, this time focusing on the character of Raiga Saezima, the son of the original protagonist Kouga, who takes on the mantle of the Golden Knight Garo.  The series began broadcast on April 4, 2014, on TV Tokyo and its sister stations in the TX Network.\n\nQuestion: Are Reuben Nakian and Garo Yepremian of the same nationality?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_1\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"nationality\": {\n          \"type\": \"string\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"nationality\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"person_2\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"nationality\": {\n          \"type\": \"string\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"nationality\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"nationalities_are_same\": {\n      \"type\": \"boolean\",\n      \"description\": \"True if both individuals share the same nationality, false otherwise.\"\n    },\n    \"answer\": {\n      \"type\": \"boolean\",\n      \"description\": \"The direct answer to the question: Are Reuben Nakian and Garo Yepremian of the same nationality?\"\n    }\n  },\n  \"required\": [\n    \"person_1\",\n    \"person_2\",\n    \"nationalities_are_same\",\n    \"answer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_1": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "nationality": {
            "type": "string"
          }
        },
        "required": [
          "name",
          "nationality"
        ],
        "additionalProperties": false
      },
      "person_2": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "nationality": {
            "type": "string"
          }
        },
        "required": [
          "name",
          "nationality"
        ],
        "additionalProperties": false
      },
      "nationalities_are_same": {
        "type": "boolean",
        "description": "True if both individuals share the same nationality, false otherwise."
      },
      "answer": {
        "type": "boolean",
        "description": "The direct answer to the question: Are Reuben Nakian and Garo Yepremian of the same nationality?"
      }
    },
    "required": [
      "person_1",
      "person_2",
      "nationalities_are_same",
      "answer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

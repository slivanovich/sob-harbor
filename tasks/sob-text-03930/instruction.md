{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nTomoko Matsunashi: Tomoko Matsunashi (松梨 智子 , Matsunashi Tomoko ) is a Japanese film director and actress.  She was described in 2007 as one of the female Japanese directors who \"have brought some needed originality and talent to contemporary Japanese cinema.\"\n\nList of Dallas Vigilantes seasons: The Dallas Vigilantes were an Arena Football League team based in Dallas, Texas.  Like its AFL predecessor, the Dallas Desperados, the Vigilantes played at the American Airlines Center.  The Vigilantes and the Jacksonville Sharks began play in the 2010 season, the first after the league's restructuring.  The franchise was owned by former Tampa Bay Storm owner Peter C. Kern and managed by original Buffalo Destroyers head coach Dave Whinham.  The team's last head coach was former Desperados quarterback Clint Dolezel.\n\nAntti Niemi (ice hockey): Antti Niemi (] ; born 29 August 1983) is a Finnish professional ice hockey goaltender currently playing for the Pittsburgh Penguins of the National Hockey League (NHL).  During the 2009–10 season as a member of the Chicago Blackhawks, he became the first Finnish goaltender to win the Stanley Cup.  Niemi left the Blackhawks and played with the San Jose Sharks from 2011 to 2014.  He signed a contract to play for Pelicans in the SM-liiga in Finland during the 2012–13 NHL lockout.  On 27 June 2015, the Sharks traded his negotiation rights to the Dallas Stars, who signed him to a three-year deal on 29 June.  He was bought-out from the final year of his contract with the Stars on June 27, 2017.\n\nTed Sharks: Ted Sharks (born January 25) is a Japanese film director, producer, screenwriter and editor.  He is best known for writing and directing \"Hard to Say\", \"Save the Underprivileged\" and \"An Ideal Marriage\".\n\nDallas M. Fitzgerald: Dallas M. Fitzgerald (born August 13, 1876 in La Grange, Kentucky, US; died: May 9, 1940 (age 63) in Los Angeles) was an American motion picture director and producer, primarily in the silent era.  He is also known as the writer of the Frank Buck film serial \"Jungle Menace\".\n\nGary Ewing: Garrison \"Gary\" Arthur Ewing is a fictional character from the CBS soap opera, \"Knots Landing\", a spin-off of \"Dallas\".  The character of Gary Ewing was first played by actor David Ackroyd, in a 2-part \"Dallas\" episode entitled \"Reunion\", which broadcast in September 1978.  Gary Ewing was the second son of oil baron Jock Ewing and Miss Ellie Ewing, the father of Lucy Ewing and the ex-husband of Valene Ewing.  Over a year later, the part of Gary Ewing was recast for the spin-off \"Knots Landing\" with actor Ted Shackelford in the role, and Gary became one of the main stars of the series in December 1979.  Ted Shackelford played Gary Ewing in \"Knots Landing\" for its entire fourteen seasons (1979–1993), while continuing to make occasional appearances in \"Dallas\" during that time.  The character of Gary made his last \"Knots Landing\" appearance in 1997, in the reunion series \"\".  Shackelford reprised his character for the new, updated version of \"Dallas\" in 2013.\n\nJapanese School of Dallas: The Japanese School of Dallas (ダラス補習授業校 \"Darasu Hoshū Jugyō Kō\") is a part-time Japanese educational program for Japanese citizens and Japanese Americans located in the Dallas-Fort Worth metroplex.  The school office in Dallas, and it conducts its classes at Ted Polk Middle School in Carrollton.  As of 2015 Munetake Yamamura (山村 宗武 \"Yamamura Munetake\") is the principal.\n\nKillers (2003 film): Killers (キラーズ , Kirāzu ) is a 2003 theatrical compilation of five short film thrillers by five different Japanese directors.  This compilation concept's official name is \"Omnibus Action Movie\".\n\nTokihiko Okada: Tokihiko Okada (岡田 時彦 ) (February 18, 1903 – January 16, 1934) was a Japanese silent film star in Japan during the 1920s and early 1930s.  A Tokyo native, he first started at the Taikatsu studio and later he was a leading player for such legendary Japanese directors as Yasujirō Ozu and Kenji Mizoguchi.  Film critic Tadao Sato recounts that Okada was among the handsomest and favorite Japanese actors of the era.  Throughout his career, Okada played the role of the quintessential nimaime (translated as \"second line\") which were romantic, sensitive men as opposed to the rugged and hard-boiled leading men known as tateyaku.  He was the father of film actress Mariko Okada.  Tokihiko Okada died of tuberculosis a month and two days before turning 31 years of age.\n\nJerry Brown (gridiron football): Jerome \"Jerry\" Brown, Jr., (October 20, 1987 – December 8, 2012) was an American football linebacker who played for five different teams combined in the National Football League, Arena Football League and Canadian Football League.  In college, he played on the defensive line for the University of Illinois.  In his professional career, he was a member of the Hamilton Tiger-Cats of the Canadian Football League, the Jacksonville Sharks and San Antonio Talons of the Arena Football League and the Indianapolis Colts and Dallas Cowboys of the National Football League.  He was signed as a free agent by the Jacksonville Sharks in 2011 and was a contributor to the Sharks victory in ArenaBowl XXIV by having one tackle assist, a forced fumble and a fumble recovery.\n\nQuestion: Were Ted Sharks and Dallas M. Fitzgerald both Japanese directors?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"question_asked\": {\n      \"type\": \"string\",\n      \"description\": \"The original question asked by the user.\"\n    },\n    \"directors_compared\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the director.\"\n          },\n          \"is_japanese\": {\n            \"type\": \"boolean\",\n            \"description\": \"True if the director is Japanese, false otherwise.\"\n          },\n          \"nationality\": {\n            \"type\": \"string\",\n            \"description\": \"The stated nationality of the director.\"\n          },\n          \"profession\": {\n            \"type\": \"string\",\n            \"description\": \"The primary profession of the individual.\"\n          }\n        },\n        \"required\": [\n          \"name\",\n          \"is_japanese\",\n          \"nationality\",\n          \"profession\"\n        ],\n        \"additionalProperties\": false\n      },\n      \"minItems\": 2,\n      \"maxItems\": 2\n    },\n    \"both_are_japanese_directors\": {\n      \"type\": \"boolean\",\n      \"description\": \"True if both individuals are Japanese directors, false otherwise.\"\n    }\n  },\n  \"required\": [\n    \"question_asked\",\n    \"directors_compared\",\n    \"both_are_japanese_directors\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "question_asked": {
        "type": "string",
        "description": "The original question asked by the user."
      },
      "directors_compared": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string",
              "description": "The name of the director."
            },
            "is_japanese": {
              "type": "boolean",
              "description": "True if the director is Japanese, false otherwise."
            },
            "nationality": {
              "type": "string",
              "description": "The stated nationality of the director."
            },
            "profession": {
              "type": "string",
              "description": "The primary profession of the individual."
            }
          },
          "required": [
            "name",
            "is_japanese",
            "nationality",
            "profession"
          ],
          "additionalProperties": false
        },
        "minItems": 2,
        "maxItems": 2
      },
      "both_are_japanese_directors": {
        "type": "boolean",
        "description": "True if both individuals are Japanese directors, false otherwise."
      }
    },
    "required": [
      "question_asked",
      "directors_compared",
      "both_are_japanese_directors"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

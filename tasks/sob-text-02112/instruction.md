{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nShannon Ritch: Shannon Grey Ritch (born September 27, 1970) is an American professional mixed martial artist, boxer, professional wrestler and kickboxer, known for being the former Gladiators Challenge Heavyweight Champion and KOTC Middleweight Champion also current RUF Interim Heavyweight Champion and IFC Middleweight Champion.  A professional competitor since 1998, Ritch has competed for the MFC, Pancrase, K-1, PRIDE, Rebel Fighting Championship, King of the Cage and the WEC.  Ritch has also has been featured in two episodes of Walker, Texas Ranger as a Biker Gang Member and a character named Knight, Choke in 2011 as an extra, CSI Las Vegas as Thug #2, an episode of iCarly as a MMA Fighter, an episode of Numbers in 2010, an episode of Ultimate Soldier Challenge on the History Channel representing a military contracting company and most recently in 2017 the direct to DVD film, directed by Robert Parham, Bullets, Blades and Blood and upcoming in 2018 No Way Out directed by Jeffrey D. Parker.  Shannon claims he has over 200 professional MMA fights 112 wins, 88 losses and 2 draws, some fights going undocumented and dating back as far as 1991.  His documented record of fights goes back to 1998 with a record of 56 wins, 81 loses, and 4 draws.  Shannon also holds a 2-1 record in professional boxing and a 25-2 record in bare knuckle boxing with all of his wins coming by way of knockout, in 2017 he was inducted into the Bare Knuckle Boxing Hall of Fame and also plans to round out his boxing career in 2018 against boxing superstar Bobby Gunn.  Ritch is also an occasional professional wrestler, recently in mid 2017 main eventing a card in Guyana.  Shannon has also found success as a grappler winning multiple NAGA, Grapplers Quest and Abu Dhabi Combat Club competitions, most recently winning a gold medal in the super heavyweight division at the Grand Canyon 2017 BJJ Open in Arizona and a silver medal at the '17 Arizona State BJJ Championships.  Ritch is also an avid golf player, winning 1st place in many state and pro am competitions held within his native Arizona as recent as 2017.\n\nJorge Rubio (boxing trainer): Jorge Enrique Rubio is a Cuban trainer in the sport of boxing.  Rubio was a trainer of the Cuban national amateur boxing team.  Rubio trains numerous professional fighters in Miami, Florida, including Gil Reyes, Juan Arroyo, and Stacey Reile.  Rubio was announced as Amir Khan's trainer on July 26, 2008.  After Khan's disastrous first-round KO defeat at the hands of relatively unknown Colombian Breidis Prescott, Khan and Rubio parted ways.\n\n2012 in Super Fight League: The year 2012 was the inaugural year for Super Fight League, an Indian-based mixed martial arts (MMA) league.  Its first event was held in March and featured a bout between the two MMA veterans Bob Sapp and James Thompson.  The league has scheduled several events to occur throughout India in 2012.  On August 5, the Super Fight League will air their reality show SFL Challengers.  Similar to the Ultimate Fighter, the show will take young up-and-coming Indian mixed martial artists, place them in the same house as each other.  On October 12, the Super Fight League changed their organisational structure from one event a month in arenas to one event every Friday in a specially designed mini-arena in Mumbai in front of an exclusive invitation only audience.  Programming will last for three hours each week with weigh-ins, live fights, and interviews from Bollywood cage side guests.  There will be 7 fights in total each event, with 1 of them being a female bout.  It will air live on Neo Prime in India and on their YouTube page for the rest of the world.\n\nSuper Fight League: Super Fight League Is a mixed martial arts promotion, based in India.  The organisation was formed in 2012 by actor Sanjay Dutt and British Indian businessman Raj Kundra.  Super Fight League has produced close to 50 live televised events broadcast on Colors, Neo Prime, ESPN Star Sports and on YouTube live worldwide.\n\nSuper Boxing League: The Super Boxing League is proposed professional boxing league of India.  Bill Dosanjh and Amir Khan founded Super Boxing League in 2017 after Super Fight League first season.  The league will be organised with the support of World Boxing Council and Professional Boxing Organisation India.  The first season will have 8 teams comprising both men and women pugilist.\n\nJimmy Ambriz: Jimmy \"The Titan\" Ambriz (born March 20, 1977) is an American professional mixed martial artist currently competing in the Super Heavyweight division.  A professional competitor since 2001, He is also a veteran of the WEC, Tachi Palace Fights, K-1 Hero's, Pancrase, the MFC, DREAM, the Super Fight League, and King of the Cage.  He is the former KOTC Super Heavyweight Champion.\n\nAmir Khan vs. Lamont Peterson: Amir Khan vs Lamont Peterson, billed as Capital Showdown, was a boxing match for Khan's WBA (Super) & IBF light welterweight titles.  The fight took place in the Convention Center in Washington, D.C., United States, on 10 December 2011.  Khan was making the first defense of his IBF belt against his mandatory challenger.\n\nAmir Khan (boxer): Amir Iqbal Khan (born 8 December 1986) is a British professional boxer.  He is a former unified light-welterweight world champion, having held the WBA (later Super) title from 2009 to 2012, and the IBF title in 2011.  Additionally he held the Commonwealth lightweight title from 2007 to 2008, the WBC Silver welterweight title from 2014 to 2016, and has challenged once for a middleweight world title in 2016.\n\nAmir Khan vs. Paul McCloskey: Amir Khan vs. Paul McCloskey was a 140-pound world title fight, that was aired on HBO's \"Boxing After Dark\", as part of an HBO-televised split-site double-header, which also included WBC Welterweight Championship fight, Andre Berto vs. Victor Ortiz.  Following on from Khan's successful title defense against Marcos Maidana, Champion Amir returned to Manchester to continue his title defense against EBU Super Lightweight Champion Paul McCloskey at the Manchester Evening News Arena.\n\nCanelo Álvarez vs. Amir Khan: Canelo Álvarez vs. Amir Khan, billed as \"Power vs. Speed\" and also known as \"Canelo vs. Khan\" or by the portmanteau \"Khanelo\", was a professional boxing fight which took place on May 7, 2016, and was contested for the WBC, \"Ring\" magazine and lineal middleweight titles.  It was the first major sporting event to be held at the T-Mobile Arena in Las Vegas.\n\nQuestion: The Super Boxing League is proposed professional boxing league of which country, Amir Khan co-founded Super Boxing League in 2017 after Super Fight League first season?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"league_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the professional boxing league.\"\n    },\n    \"country_of_origin\": {\n      \"type\": \"string\",\n      \"description\": \"The country where the boxing league is proposed.\"\n    },\n    \"founding_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"co_founder_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of one of the co-founders of the league.\"\n        },\n        \"founding_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the league was founded.\"\n        },\n        \"founded_after_super_fight_league_season\": {\n          \"type\": \"boolean\",\n          \"description\": \"Indicates if the league was founded after the Super Fight League's first season.\"\n        }\n      },\n      \"required\": [\n        \"co_founder_name\",\n        \"founding_year\",\n        \"founded_after_super_fight_league_season\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"league_name\",\n    \"country_of_origin\",\n    \"founding_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "league_name": {
        "type": "string",
        "description": "The name of the professional boxing league."
      },
      "country_of_origin": {
        "type": "string",
        "description": "The country where the boxing league is proposed."
      },
      "founding_details": {
        "type": "object",
        "properties": {
          "co_founder_name": {
            "type": "string",
            "description": "The name of one of the co-founders of the league."
          },
          "founding_year": {
            "type": "integer",
            "description": "The year the league was founded."
          },
          "founded_after_super_fight_league_season": {
            "type": "boolean",
            "description": "Indicates if the league was founded after the Super Fight League's first season."
          }
        },
        "required": [
          "co_founder_name",
          "founding_year",
          "founded_after_super_fight_league_season"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "league_name",
      "country_of_origin",
      "founding_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

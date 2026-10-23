{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAl Iaquinta: Alexander Jay Iaquinta ( ; born April 30, 1987) is an American mixed martial artist.  A professional MMA competitor since 2009, Iaquinta has made a name for himself fighting for the Ring of Combat promotion and his stint on FX's .  He is currently signed with the Ultimate Fighting Championship (UFC).  He is currently #12 in official UFC Lightweight rankings and the #8 Lightweight fighter in the world by Sherdog.  Outside the ring, he is a licensed real estate agent.\n\nTony Ferguson: Anthony Armand \"Tony\" Ferguson (born February 12, 1984) is an American professional mixed martial artist currently competing in the Lightweight division of the Ultimate Fighting Championship (UFC).  A professional competitor since 2008, Ferguson was the winner of .  He is currently #2 in official UFC Lightweight rankings.\n\nBobby Green (fighter): Bobby Ray Green (born September 9, 1986) is an American professional mixed martial artist who is currently under contract with the UFC, competing in their Lightweight division.  A professional competitor since 2008, Green is the former King of the Cage Lightweight Champion and has also competed in Tachi Palace Fights, Strikeforce, and Affliction.  Green also made an appearance on the MTV/MTV2 reality show Bully Beatdown.  As of August 17, 2015, he is #12 in the official UFC lightweight rankings.\n\nJonathan Brookins: Jonathan Quinn Brookins (born August 13, 1985) is an American mixed martial artist who competed as a featherweight for the Ultimate Fighting Championship.  A professional MMA competitor since 2006, Brookins has mostly fought in Florida, as well as competing in .  On December 4, 2010, Brookins defeated Michael Johnson to become the \"Ultimate Fighter\" and earn a contract with the UFC.  During his time at Lindenwood University he was also the college roommate of former fellow UFC fighter Mike Rio.\n\nMichael Johnson (fighter): Michael Julian Johnson (born June 4, 1986) is an American mixed martial artist who competes in the lightweight division of the Ultimate Fighting Championship.  A professional MMA competitor since 2008, Johnson mostly competed in his regional circuit, before signing onto the Ultimate Fighting Championship to appear on \"\".  As of July 2017, he is #9 in the official UFC lightweight rankings.\n\nCaol Uno: Kaoru \"Caol\" Uno (宇野薫 , Uno Kaoru ) (born May 8, 1975) is a Japanese mixed martial artist.  He is the Co-Champion of the UFC 41 Lightweight Tournament and a former Shooto Lightweight Champion.  As one of the early Ultimate Fighting Championship's elite Lightweight competitors, Uno competed for the UFC Lightweight Championship on two separate occasions.  Despite falling short in both championship bouts; losing a five-round decision against Jens Pulver at UFC 30, to determine the inaugural UFC Lightweight Champion as well as a draw against B.J. Penn at UFC 41 (in a bout which would have determined the new UFC Lightweight Champion and UFC 41 Lightweight Tournament Winner), Uno is acknowledged as a pioneer for his impact and influence during the early era of the UFC Lightweight Division.\n\nB.J. Penn: Jay Dee \"B.J.\" Penn (born December 13, 1978) is an American professional mixed martial artist and Brazilian Jiu-Jitsu practitioner.  Penn debuted and competed in the Ultimate Fighting Championship (UFC), and later in K-1.  Prior to fighting for the UFC, he became the first American Gold medalist of the World Jiu-Jitsu Championship.  In mixed martial arts, Penn has competed in the Featherweight, Lightweight, Welterweight, and Middleweight divisions.  As a former UFC Lightweight Champion and UFC Welterweight Champion, he is one of only three fighters in UFC history to win titles in multiple weight classes.  Penn was also a Co-champion in the UFC 41 Lightweight Tournament, due to an eventual draw opposite Caol Uno in the tournament finale.  Through his tenures as champion, Penn unofficially unified the UFC Lightweight Championship (against Sean Sherk) and broke the all-time lightweight title defense record.  Penn was inducted into the UFC Hall of Fame, as the inaugural inductee in the Modern-Era Wing by career-long rival Matt Hughes, during \"International Fight Week\" in July 2015.\n\nJustin Gaethje: Justin Ray Gaethje ( ; born November 14, 1988) is an American professional mixed martial artist who fights in the lightweight division of the Ultimate Fighting Championship (UFC).  He is a former WSOF Lightweight Champion.  He has an undefeated record of 18–0 and is #5 in the UFC lightweight rankings as of September 2017.\n\nAnthony Pettis: Anthony Paul Pettis (born January 27, 1987) is an American mixed martial artist currently competing as a Lightweight in the Ultimate Fighting Championship (UFC), where he is the former UFC Lightweight Champion.  Pettis was also the final WEC Lightweight Champion prior to the promotion being merged into the UFC.  At one point, he was ranked as a top-ten pound for pound fighter.  He is currently ranked #13 in the official UFC lightweight rankings.\n\nJens Pulver: Jens Johnnie Pulver (born December 6, 1974) is an American professional mixed martial artist and undefeated boxer and kickboxer.  Pulver was the inaugural UFC Lightweight Champion in addition to serving as the head coach on \"The Ultimate Fighter 5\" reality show against long-time rival B.J. Penn.  In mixed martial arts, Pulver competed at the Lightweight, Featherweight, Bantamweight and Flyweight divisions in addition to competing at the Middleweight, Light Middleweight, and Welterweight divisions as a professional boxer.  While perhaps best known for competing in the UFC, Pulver has also competed in Pride Fighting Championships, for the PRIDE 2005 Lightweight Grand Prix.  He is to-date the youngest UFC Lightweight Champion in the UFC history, eventually relinquishing his title, after two defenses, due to a contract dispute.  Pulver officially retired from combat sports in 2014.  Pulver is considered the founder of the UFC lightweight division.\n\nQuestion: What ranking does the man who Jonathan Brookins defeated on December 4, 2010 have in UFC lightweight rankings?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"fighter_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the fighter who was defeated by Jonathan Brookins.\"\n    },\n    \"defeat_date\": {\n      \"type\": \"string\",\n      \"format\": \"date\",\n      \"description\": \"The date of the defeat.\"\n    },\n    \"ranking_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"division\": {\n          \"type\": \"string\",\n          \"description\": \"The weight division for the ranking.\"\n        },\n        \"organization\": {\n          \"type\": \"string\",\n          \"description\": \"The organization providing the ranking.\"\n        },\n        \"rank\": {\n          \"type\": \"integer\",\n          \"description\": \"The numerical rank of the fighter.\"\n        },\n        \"ranking_as_of_date\": {\n          \"type\": \"string\",\n          \"format\": \"date\",\n          \"description\": \"The date as of which the ranking is valid.\"\n        }\n      },\n      \"required\": [\n        \"division\",\n        \"organization\",\n        \"rank\",\n        \"ranking_as_of_date\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"fighter_name\",\n    \"defeat_date\",\n    \"ranking_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "fighter_name": {
        "type": "string",
        "description": "The name of the fighter who was defeated by Jonathan Brookins."
      },
      "defeat_date": {
        "type": "string",
        "format": "date",
        "description": "The date of the defeat."
      },
      "ranking_details": {
        "type": "object",
        "properties": {
          "division": {
            "type": "string",
            "description": "The weight division for the ranking."
          },
          "organization": {
            "type": "string",
            "description": "The organization providing the ranking."
          },
          "rank": {
            "type": "integer",
            "description": "The numerical rank of the fighter."
          },
          "ranking_as_of_date": {
            "type": "string",
            "format": "date",
            "description": "The date as of which the ranking is valid."
          }
        },
        "required": [
          "division",
          "organization",
          "rank",
          "ranking_as_of_date"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "fighter_name",
      "defeat_date",
      "ranking_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

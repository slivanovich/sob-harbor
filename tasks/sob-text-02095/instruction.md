{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBertrand Amoussou-Guenou: Bertrand Amoussou-Guenou (born May 29, 1966) is a retired French mixed martial artist and judoka.  He is a trainer for his younger brother Karl of \"Team Amoussou\" and, following official recognition of mixed martial arts in France, became the president of the national sanctioning body, the Commission National de Mixed Martial Arts, in January 2008.  On 1 October 2013, Amoussou assumed the position of president of the International Mixed Martial Arts Federation (IMMAF).\n\nUFC on Fox: Weidman vs. Gastelum: UFC on Fox: Weidman vs. Gastelum (also known as UFC on Fox 25) was a mixed martial arts event produced by the Ultimate Fighting Championship held at the Nassau Veterans Memorial Coliseum in Uniondale, New York.\n\nShooto: Shooto is a combat sport/mixed martial arts system and mixed martial arts organization that is governed by the \"Shooto Association\" and the \"International Shooto Commission\".  Shooto was originally formed in 1985, as an organization and as a particular fighting system derived from shoot wrestling.  Practitioners are referred to as shooters, similarly to practitioners of shoot wrestling.  Shooto rules have evolved such that their events are now true mixed martial arts competitions.\n\nCV Productions, Inc.: CV Productions, Inc., is a Pittsburgh, Pennsylvania-based mixed martial arts company, founded in 1979.  It is considered the first MMA based company in the United States and responsible for creating the blueprint for modern mixed martial arts competition.  The company promoted the first regulated league of mixed martial arts style competitions beginning in 1980 with the intention of creating a new mainstream sport.  The league events pitted combatants from all fighting disciplines including boxers, kick boxers, martial artists, wrestlers, grapplers, and all around “tough guys.”  Competitors could win by opponent’s submission, knockout or judges' decision (based on the 10 point “must” system).  The competitions were promoted as “Anything Goes - striking, throwing, grappling, punching, kicking, ground fighting, and more.”  The shows were immediately dubbed by the media as “Organized, Legalized, Street Fighting,” a phrase coined by KDKA TV's Dave Durian.\n\nMohammed &quot;The Hawk&quot; Shahid: Mohammed Shahid (born July 8, 1989) is an entrepreneur and a mixed martial artist from Bahrain.  He is the CEO of KHK MMA and the President of the Bahrain based mixed martial arts organisation, Brave Combat Federation owned and supported by His Highness Sheikh Khalid bin Hamad Al Khalifa.  Mohammed Shahid was the first mixed martial artist from Bahrain to compete in global MMA events.  He was assigned a managerial role to develop mixed martial arts in Bahrain as the CEO of KHK MMA.  Bahrain established a national team alongside bringing global talent to facilitate the growth of MMA in Bahrain.\n\nDerrick Lewis (fighter): Born and raised as one of seven siblings, the second oldest, by a single mother in New Orleans, Louisiana, Lewis was troubled growing up and was often involved in street fighting.  In 1999, Lewis and his family relocated to Houston, Texas due to his mother being in an abusive relationship.  At the age of 17, Lewis began training in boxing and was preparing for his first amateur fight when the gym unexpectedly shut down.  Two weeks after graduating from high school, Lewis was charged with aggravated assault, and was placed on probation.  Two years later, while attending Kilgore College on a full scholarship for football, Lewis violated his probation and was sentenced to five years in prison, but ended up serving three and a half.  A week after being released, Lewis was introduced to mixed martial arts by a friend and, while working as a tow-truck driver, continued with boxing under the tutelage of George Foreman.  However, after dominating in his first professional mixed martial arts fight, Lewis decided to focus on mixed martial arts.\n\nTeam Hammer House: Team Hammer House is a mixed martial arts team operating out of Columbus, Ohio, made up of mostly former NCAA wrestlers.  While Hammer House focuses on amateur wrestling they do have cross training deals with notable fighters and camps such as Matt Serra, Pat Miletich and Xtreme Couture Mixed Martial Arts.  Founded by former UFC champion Mark Coleman, Team Hammer House has attracted such mixed martial arts fighters as Kevin Randleman and Phil Baroni.\n\nNassau Veterans Memorial Coliseum: Nassau Veterans Memorial Coliseum (branded as NYCB Live, home of the Nassau Veterans Memorial Coliseum for naming rights reasons), commonly known as just Nassau Coliseum, is a multi-purpose indoor arena in Uniondale, New York.  The Coliseum is approximately 19 mi east of New York City on Long Island.\n\nZenQuest Martial Arts Center: ZenQuest Martial Arts Center, formerly called the Okinawan Karate School, is a martial arts school located in Lenox, Massachusetts.  The oldest martial arts school in Berkshire County, it was founded in 1972 as a dojo for Uechi-ryu karate.  The school since expanded to include other martial arts, and currently provides instruction in Shohei-ryu karate (a spin-off of Uechi-ryu), Brazilian jiu-jitsu, mixed martial arts, Muay Thai, boxing, wrestling, kobudo, and self-defense, and is the fastest growing martial arts community in Berkshire County.  The school also contains a store which provides equipment, gear, and instructional media.  It is affiliated with the Okinawan Karatedo Association, Demian Maia Jiu-Jitsu Association, and Team Sityodtong Boston, and is accredited by the North American Grappling Association.  ZenQuest has received significant coverage by regional and local media in Berkshire County, including \"The Berkshire Eagle\", \"Berkshires' Best Buys, Business, and Beyond\", and Pittsfield Cable Television, for its regular youth tournaments and seminars with high-ranking officials from the school's parent organizations.\n\nMixed Martial Arts Pakistan: Mixed Martial Arts Pakistan (or PAK MMA) is the premiere mixed martial arts (MMA) and martial arts promotion based in Pakistan that was created in December 2007 by Bashir Ahmad to promote martial arts (and martial sports such as boxing and wrestling) styles in Pakistan with a particular focus on mixed martial arts competition.\n\nQuestion: Where is this mixed martial arts even taking place?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"event_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the mixed martial arts event.\"\n    },\n    \"event_type\": {\n      \"type\": \"string\",\n      \"description\": \"The type of event, e.g., mixed martial arts.\"\n    },\n    \"location_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"venue_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the venue where the event was held.\"\n        },\n        \"city\": {\n          \"type\": \"string\",\n          \"description\": \"The city where the event was held.\"\n        },\n        \"state\": {\n          \"type\": \"string\",\n          \"description\": \"The state where the event was held.\"\n        }\n      },\n      \"required\": [\n        \"venue_name\",\n        \"city\",\n        \"state\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"event_name\",\n    \"event_type\",\n    \"location_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "event_name": {
        "type": "string",
        "description": "The name of the mixed martial arts event."
      },
      "event_type": {
        "type": "string",
        "description": "The type of event, e.g., mixed martial arts."
      },
      "location_details": {
        "type": "object",
        "properties": {
          "venue_name": {
            "type": "string",
            "description": "The name of the venue where the event was held."
          },
          "city": {
            "type": "string",
            "description": "The city where the event was held."
          },
          "state": {
            "type": "string",
            "description": "The state where the event was held."
          }
        },
        "required": [
          "venue_name",
          "city",
          "state"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "event_name",
      "event_type",
      "location_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
David Bédard: David Peter Bédard (born October 23, 1965) is a retired diver from Canada, who represented his native country at four consecutive Summer Olympics, starting in 1984.  He twice won a medal at the Pan American Games (1987 and 1995).  He won a silver medal at the 1986 Commonwealth Games and two silver medals at the 1990 Commonwealth Games.

Andrew Baildon: Andrew James Baildon (born 25 August 1971) is a former freestyle and butterfly swimming champion, who represented Australia in the 1988 Summer Olympics in Seoul and the 1992 Summer Olympics in Barcelona.  Andrew was a medalist at the 1990 Commonwealth Games in Auckland, New Zealand where he became the first swimmer in the Commonwealth to break the 50 second barrier for the 100m freestyle, when he smashed his own Commonwealth record to win gold (49.80s), and the 1994 Commonwealth Games in Victoria, Canada.  He was a medalist in 4 Pan Pacific Swimming Championships.

Nauru at the 1990 Commonwealth Games: Nauru was represented at the 1990 Commonwealth Games in Auckland by a single athlete, weightlifter Marcus Stephen, who would later become his country's President in 2007.  The 1990 Games marked Nauru's first participation in the Commonwealth Games.  Stephen competed in three events only, and won medals in all three, including one gold.

Joanne Deakins: Joanne Cara Deakins (born 20 November 1972) is an English former competitive swimmer who specialised in the backstroke.  She represented Great Britain at the 1992 Olympic Games in Barcelona and the 1996 Olympic Games in Atlanta.  She also represented England at three Commonwealth Games.  She won a 1990 Commonwealth silver medal in the 4 x 100 metres medley relay, and a 1995 Universiade bronze medal in the 200 metres backstroke.

Australia at the 1990 Commonwealth Games: Australia at the 1990 Commonwealth Games was abbreviated AUS.  This was their fourteenth of 14 Commonwealth Games having participated in all Games meets up to these Games.

Sharon Stewart (athlete): Sharon Lee Stewart (born 17 August 1965) is a retired Australian middle-distance runner who specialised in the 800 metres.  She represented her country at one outdoor and one indoor World Championships.  In addition, she won the bronze medal at the 1990 Commonwealth Games.

Peter Elliott (athlete): Peter Elliott (born 9 October 1962 in Rotherham, Yorkshire) is a former middle-distance runner from the United Kingdom.  During his career, he won the gold medal in the 1500 metres at the 1990 Commonwealth Games, the silver medal in the 1500 metres at the 1988 Olympic Games, and the silver medal in the 800 metres at the 1987 World Championships.

Abrar Hussain (boxer): Abrar Hussain (February 9, 1961 – June 16, 2011) was professional Pakistani welterweight and Light-middleweight boxer.  Hussain represented Pakistan at the 1984, 1988, and 1992 Summer Olympics.  In 1985 South Asian Games, he won a Gold medal for Pakistan in Dhaka.  In 1990 Asian Games, Hussain secured Gold medal in boxing for Pakistan.  He also represented his country at the 1990 Commonwealth Games.

Karen van Wirdum: Karen Tracey van Wirdum (born 9 April 1971) is a former freestyle swimmer from Australia, who competed in three consecutive Summer Olympics for her native country, starting in 1988.  She won the gold medal in the 100-metre freestyle at the 1990 Commonwealth Games and in the 50-metre freestyle at the 1994 Commonwealth Games.

1990 Commonwealth Games: The 1990 Commonwealth Games were held in Auckland, New Zealand from 24 January – 3 February 1990.  It was the 14th Commonwealth Games, and part of New Zealand's 1990 sesquicentennial celebrations.  Participants competed in ten sports: athletics, aquatics, badminton, boxing, cycling, gymnastics, judo, lawn bowls, shooting and weightlifting.  The Triathlon was a demonstration event.

Question: What medal did Sharon Steward win at the 1990 Commonwealth Games?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "athlete_name": {
      "type": "string",
      "description": "The name of the athlete."
    },
    "event_details": {
      "type": "object",
      "properties": {
        "event_name": {
          "type": "string",
          "description": "The name of the games where the medal was won."
        },
        "year": {
          "type": "integer",
          "description": "The year the event took place."
        },
        "medal_type": {
          "type": "string",
          "description": "The type of medal won (e.g., gold, silver, bronze)."
        }
      },
      "required": [
        "event_name",
        "year",
        "medal_type"
      ],
      "additionalProperties": false
    },
    "athlete_nationality": {
      "type": "string",
      "description": "The nationality of the athlete."
    }
  },
  "required": [
    "athlete_name",
    "event_details",
    "athlete_nationality"
  ],
  "additionalProperties": false
}

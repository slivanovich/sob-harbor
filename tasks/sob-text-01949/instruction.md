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
Andre Fili: Andre Fili (born June 25, 1990) is an American mixed martial artist who competes in the Featherweight division.  Fili is of Samoan and Native Hawaiian descent and is currently signed with the Ultimate Fighting Championship (UFC).

Brian Ortega: Brian Ortega (born February 21, 1991) is an American mixed martial artist currently competing in the Featherweight division of the Ultimate Fighting Championship.  A professional competitor since 2010, he has also formerly competed for the RFA, where he was the Featherweight Champion.  He currently fights in the UFC featherweight division.

Buffalo Bulls wrestling: The Buffalo Bulls wrestling team is a varsity intercollegiate athletic team of the University at Buffalo in Amherst, New York, United States.  The team is a member of the Mid-American Conference (MAC), which is part of the National Collegiate Athletic Association's Division I.  The team plays their home matches at Alumni Arena in Amherst, New York.  The Bulls are coached by John Stutzman.  Former Bull Wrestler Desmond Green was a MAC Champion and 3-time Division 1 NCAA Qualifier and is currently a Mixed Martial Artist fighting for Bellator.

Melvin Guillard: Melvin Paul Guillard, Jr. (born March 30, 1983) is an American mixed martial artist who competes in the Welterweight division.  Guillard most notably competed in the Lightweight division of the Ultimate Fighting Championship (UFC) where he went (12–9), Bellator MMA (Bellator) where is went (0–3 (1)) and World Series of Fighting (WSOF) where he went (1–1).  He debuted in the company on "The Ultimate Fighter 2" television series, losing to Josh Burkman by decision in the first Welterweight elimination bout.  Guillard currently holds the UFC record for most TKO/KO victories (eight) in the Lightweight division, surpassing the previous record held by Multi-Divisional Champion B.J. Penn with his knockout of Shane Roller at "UFC 132".  He again extended this record in his knockout victory over Mac Danzig at "".

Renato Moicano: Renato Carneiro (born May 21, 1989), professionally known as Renato Moicano, is a Brazilian mixed martial artist who competes in the Featherweight division of the Ultimate Fighting Championship.  A professional MMA competitor since 2010, Moicano made a name for himself fighting all over his home country of Brazil, and is the former interim Jungle Fight Featherweight Champion.

Mike Wilkinson (fighter): Mike Wilkinson (born September 15, 1987) is an English mixed martial artist who formerly competed in the Featherweight division of the Ultimate Fighting Championship.  He competed on .  Wilkinson competes in the featherweight division of the Absolute Championship Berkut

Rick Glenn: Rick "The Gladiator" Glenn (born April 12, 1989) is an American mixed martial artist.  He was the Professional Fighters League (formerly known as World Series of Fighting (WSOF) ) featherweight champion and Midwest Cage Fight featherweight champion.  Glenn currently fights in Featherweight division in the Ultimate Fighting Championship (UFC).

Júnior Assunção: Cleuder F. "Júnior" Assunção (born June 24, 1981) is a Brazilian mixed martial artist, who is perhaps best known for his 2–3 stint with the Ultimate Fighting Championship.  He competes in the featherweight division, and is the current Premium FC Featherweight Champion.

Desmond Green: Desmond Green (born October 11, 1989) is an American mixed martial artist who competes in the featherweight division for Ultimate Fighting Championship.

Chas Skelly: Chas Lucas Skelly (born May 11, 1985) is an American mixed martial artist currently competing in the featherweight division of the Ultimate Fighting Championship.  A professional since 2009, he has also competed for Bellator MMA and Legacy Fighting Championship.

Question: Who was a MAC Champion and 3-time Division 1 NCAA Qualifier and is an American mixed martial artist who competes in the featherweight division for Ultimate Fighting Championship?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "fighter_name": {
      "type": "string"
    },
    "nationality": {
      "type": "string"
    },
    "current_promotion": {
      "type": "string"
    },
    "fighting_division": {
      "type": "string"
    },
    "wrestling_achievements": {
      "type": "object",
      "properties": {
        "mac_champion": {
          "type": "boolean"
        },
        "ncaa_division_1_qualifier_count": {
          "type": "integer"
        }
      },
      "required": [
        "mac_champion",
        "ncaa_division_1_qualifier_count"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "fighter_name",
    "nationality",
    "current_promotion",
    "fighting_division",
    "wrestling_achievements"
  ],
  "additionalProperties": false
}

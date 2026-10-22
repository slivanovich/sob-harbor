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
Jonathan Joss: Jonathan Joss (born November 24, 1965) is an American actor.  He is best known for portraying the voice of John Redcorn from season 2 to 13 of the animated series "King of the Hill", and for his recurring role as Chief Ken Hotate in "Parks and Recreation".

John Redcorn: John Redcorn III (voiced by Victor Aaron Season 1, Jonathan Joss Season 2–13) is a character in the Fox animated series "King of the Hill".  He is addressed or referred to as "John Redcorn" or "Mr. Redcorn" by every character in the series, and very rarely just "John" or "Johnny".

Catt family: The Catt family, Ronald "Scott" Catt, and eventually his two children, Hayden and Abigail Catt, were responsible for a number of bank robberies in the Portland, Oregon, and Houston, Texas, areas.  After the death of his wife, Catt was facing financial difficulties due in part to his drug and alcohol addictions and unstable employment history.  Catt decided to bolster the family income by robbing banks.  Catt and his family committed several robberies, all occurring while the family lived a seemingly typical middle-class American life.

King of the Hill: King of the Hill is an American animated sitcom created by Mike Judge and Greg Daniels that ran from January 12, 1997 to September 13, 2009 on Fox.  It centers on the Hills, a middle-class American family in the fictional city of Arlen, Texas.  It attempts to maintain a realistic approach, seeking humor in the conventional and mundane aspects of everyday life.

Family Guy: Family Guy is an American animated sitcom created by Seth MacFarlane for the Fox Broadcasting Company.  The series centers on the Griffins, a family consisting of parents Peter and Lois; their children, Meg, Chris, and Stewie; and their anthropomorphic pet dog, Brian.  The show is set in the fictional city of Quahog, Rhode Island, and exhibits much of its humor in the form of cutaway gags that often lampoon American culture.

List of King of the Hill episodes: "King of the Hill" is an American animated television series created by Mike Judge and Greg Daniels.  The series focuses on the Hills, a middle-class American family in the fictional city of Arlen, Texas.  It originally aired on Fox from January 12, 1997 to September 13, 2009; with four episodes from the final season premiering in syndication from May 3 to May 6, 2010.  A total of 259 episodes aired over the course of 13 seasons.

List of Family Guy guest stars: "Family Guy" is an American adult animated sitcom created by Seth MacFarlane for the Fox Broadcasting Company.  Along with its core voice actors, the show has had its history of guest stars.  The series centers on the Griffins, a family consisting of parents Peter and Lois; their children Meg, Chris, and Stewie; and their anthropomorphic pet dog Brian.  The show is set in the fictional city of Quahog, Rhode Island, and exhibits much of its humor in the form of cutaway gags that often lampoon American culture.

Victor Aaron: Victor Aaron Ramirez (September 11, 1956 – September 4, 1996) was a Native American actor of the Yaqui tribe.  He was the original voice of John Redcorn on "King of the Hill", which was taken over by Jonathan Joss in the show's second season following Aaron's death.  He died in a road accident in 1996, 7 days before his 40th birthday.  The "King of the Hill" episode "The Order of the Straight Arrow" is dedicated to his memory.

The Sleeping Father: The Sleeping Father is a novel by Matthew Sharpe first published in 2003 about an average middle-class American family struck by betrayal, separation, and illness.  In particular, it is about the coming of age of the two teenage members of the family despite, or rather through, the troubles that befall them.

The Adventures of Noko Mashaba: The Adventures of Noko Mashaba is a South Africa animated sociopolitical satire created by a self-taught animator and university dropout Jonas Lekganyane for Soweto TV, Ekurhuleni TV & YouTube.  Intended for any audience, the show is inspired by the American adult animated sitcom South Park and centers around a fictional character – Noko Mashaba – an ordinary guy hailing from the calm streets of Limpopo, who occasionally ventures on extraordinary adventures to unravel mysteries and relive urban legends.  On the show Mashaba always finds himself in informative, controversial and attention-grabbing situations.

Question: The American actor "Jonathan Joss" participated in which American animated sitcom that centers around the middle-class American family in the fictional city in Texas?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the American actor."
    },
    "animated_sitcom_name": {
      "type": "string",
      "description": "The name of the American animated sitcom."
    },
    "character_voiced": {
      "type": "string",
      "description": "The character voiced by the actor in the sitcom."
    },
    "setting_details": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The fictional city where the sitcom is set."
        },
        "state": {
          "type": "string",
          "description": "The state where the fictional city is located."
        }
      },
      "required": [
        "city",
        "state"
      ],
      "additionalProperties": false
    },
    "family_description": {
      "type": "string",
      "description": "A description of the family type central to the sitcom."
    },
    "seasons_of_participation": {
      "type": "array",
      "items": {
        "type": "integer"
      },
      "description": "A list of seasons the actor participated in for the sitcom."
    }
  },
  "required": [
    "actor_name",
    "animated_sitcom_name",
    "character_voiced",
    "setting_details",
    "family_description",
    "seasons_of_participation"
  ],
  "additionalProperties": false
}

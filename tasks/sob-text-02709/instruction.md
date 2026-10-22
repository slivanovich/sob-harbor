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
2017 Hawaii Rainbow Warriors football team: The 2017 Hawaii Rainbow Warriors football team represents the University of Hawaii at Manoa in the 2017 NCAA Division I FBS football season.  The Rainbow Warriors play their home games at Aloha Stadium in Honolulu.  They compete in the West Division of the Mountain West Conference, and are led by second-year head coach Nick Rolovich.

2013 Hawaii Rainbow Warriors football team: The 2013 Hawaii Rainbow Warriors football team represented the University of Hawaii at Mānoa in the 2013 NCAA Division I FBS football season.  The team was led by second-year head coach Norm Chow and played their home games at Aloha Stadium.  They were members of the Mountain West Conference in the West Division.  They finished the season 1–11, 0–8 in Mountain West play to finish in last place in the West Division.

1999 Hawaii Rainbow Warriors football team: The 1999 Hawaii Rainbow Warriors football team represented the University of Hawaii at Manoa in the 1999 NCAA Division I-A football season.  Hawaii finished the 1999 season with a 9–4 record, going 5–2 in Western Athletic Conference (WAC) play.  The Warriors capped the best single season turnaround in NCAA history with a win in the Oahu Bowl after going 0–12 the year before.  New head coach June Jones led the Warriors to their first conference championship and bowl victory since the 1992 season.

2015–16 Hawaii Rainbow Warriors basketball team: The 2015–16 Hawaii Rainbow Warriors basketball team represented the University of Hawaii at Manoa during the 2015–16 NCAA Division I men's basketball season.  The Rainbow Warriors, led by first year head coach Eran Ganot, played their home games at the Stan Sheriff Center, and were members of the Big West Conference.  They finished the season 28–6, 13–3 in Big West play to tie for the Big West regular season championship.  They beat Cal State Fullerton, UC Santa Barbara, and Long Beach State to become champions of the Big West Tournament and earn the conference's automatic bid to the NCAA Tournament.  As a #13 seed, they defeated #4 seeded California in the first round for the school's first ever victory in the NCAA Tournament.  They fell to Maryland in the second round.

2014 Hawaii Rainbow Warriors football team: The 2014 Hawaii Rainbow Warriors football team represented the University of Hawaiʻi at Mānoa in the 2014 NCAA Division I FBS football season.  The team was led by third-year head coach Norm Chow and played their home games at Aloha Stadium.  They were members of the Mountain West Conference in the West Division.  They finished the season 4–9, 3–5 in Mountain West play to finish in fourth place in the West Division.

Hawaii Rainbow Warriors football: The Hawaii Rainbow Warriors football team represents the University of Hawaii at Manoa in NCAA Division I FBS college football.  On November 27, 2015, Nick Rolovich was hired as the new head football coach at the University of Hawaii replacing Norm Chow.  It was part of the Western Athletic Conference until July 2012, when the team joined the Mountain West Conference.

Norm Chow: Norman Yew Heen "Norm" Chow (, born May 3, 1946) is an American football coach and former player.  He was the previous head football coach at the University of Hawaiʻi at Mānoa, a position he assumed in December 2011 until November 1, 2015.  Chow previously held the offensive coordinator position for the Utah Utes, UCLA Bruins, the NFL's Tennessee Titans, USC Trojans, NC State Wolfpack, and BYU Cougars.

2012 Hawaii Warriors football team: The 2012 Hawaii Warriors football team represented the University of Hawaii at Manoa in the 2012 NCAA Division I FBS football season.  They were led by first-year head coach Norm Chow and played their home games at Aloha Stadium.  They were first year members of the Mountain West Conference.  They finished the season 3–9, 1–7 in Mountain West play to finish in a tie for ninth place.

2015 Hawaii Rainbow Warriors football team: The 2015 Hawaii Rainbow Warriors football team represented the University of Hawaii at Mānoa in the 2015 NCAA Division I FBS football season.  The team was led by head coach Norm Chow, who was fired after week 10 and replaced by Chris Naeole on an interim basis.  They played their home games at Aloha Stadium.  They were members of the Mountain West Conference in the West Division.  They finished the season 3–10, 0–8 in Mountain West play to finish in last place in the West Division.

2016 Hawaii Rainbow Warriors football team: The 2016 Hawaii Rainbow Warriors football team represented the University of Hawaii at Mānoa in the 2016 NCAA Division I FBS football season.  The team was led by first year head coach Nick Rolovich, who replaced Norm Chow.  They played their home games at Aloha Stadium.  They were members of the Mountain West Conference in the West Division.

Question: The 2016 Hawaii Rainbow Warriors football team represented the University of Hawaii at Mānoa in the 2016 NCAA Division I FBS football season, the team was led by which first year head coach, who replaced Norm Chow?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "team_information": {
      "type": "object",
      "properties": {
        "year": {
          "type": "integer",
          "description": "The year of the football season."
        },
        "university": {
          "type": "string",
          "description": "The university the team represents."
        },
        "sport": {
          "type": "string",
          "description": "The sport of the team."
        }
      },
      "required": [
        "year",
        "university",
        "sport"
      ],
      "additionalProperties": false
    },
    "coach_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the head coach."
        },
        "tenure_description": {
          "type": "string",
          "description": "Description of the coach's tenure (e.g., 'first year')."
        },
        "replaced_coach_name": {
          "type": "string",
          "description": "The name of the coach who was replaced."
        }
      },
      "required": [
        "name",
        "tenure_description",
        "replaced_coach_name"
      ],
      "additionalProperties": false
    },
    "final_answer": {
      "type": "string",
      "description": "The name of the head coach who led the team."
    }
  },
  "required": [
    "team_information",
    "coach_details",
    "final_answer"
  ],
  "additionalProperties": false
}

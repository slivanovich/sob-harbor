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
1971 Miami Redskins football team: The 1971 Miami Redskins football team was an American football team that represented Miami University in the Mid-American Conference (MAC) during the 1971 college football season.  In their third season under head coach Bill Mallory, Miami compiled a 7–3 record (2–3 against MAC opponents), finished in a tie for third place in the MAC, and outscored all opponents by a combined total of 207 to 117.  The team's defense allowed only 11.7 points per game, which ranked 12th among 128 NCAA University Division football teams.

1975 Miami Redskins football team: The 1975 Miami Redskins football team was an American football team that represented Miami University during the 1975 NCAA Division I football season.  In their second season under head coach Dick Crum, the Redskins won the Mid-American Conference (MAC) championship, compiled an 11–1 record (6–0 against MAC opponents), outscored all opponents by a combined total of 306 to 141, defeated South Carolina, 20–7, in the Tangerine Bowl, and were ranked #12 in the final AP Poll.  The team's sole loss was to Michigan State by a 14–13 score in the second game of the season.

1955 Miami Redskins football team: The 1955 Miami Redskins football team was an American football team that represented Miami University in the Mid-American Conference (MAC) during the 1955 college football season.  In their fifth and final season under head coach Ara Parseghian, the Redskins compiled a perfect 9–0 record (5–0 against MAC opponents), won the MAC championshipn, and outscored opponents by a combined total of 226 to 47.  The defense led the way for the 1955 Miami team, allowing an average of 5.2 points per game, which remains a Miami school record.  Bo Schembechler was an assistant coach on the team.

Mid-American Conference: The Mid-American Conference (MAC) is a National Collegiate Athletic Association (NCAA) Division I collegiate athletic conference with a membership base in the Great Lakes region that stretches from Western New York to Illinois.  Nine of the twelve full member schools are in Ohio and Michigan, with single members located in Illinois, Indiana, and New York.  For football, the MAC participates in the NCAA's Football Bowl Subdivision.

1962 Miami Redskins football team: The 1962 Miami Redskins football team was an American football team that represented Miami University in the Mid-American Conference (MAC) during the 1962 college football season.  In its seventh and final season under head coach John Pont, Miami compiled an 8–2–1 record (3–1–1 against MAC opponents), finished in third place in the MAC, lost to Houston in the 1962 Tangerine Bowl, and outscored all opponents by a combined total of 241 to 175.  The season included a 10-7 victory over No. 9 ranked Purdue a victory ranked among the greatest victories in program history.

1977 Miami Redskins football team: The 1977 Miami Redskins football team was an American football team that represented Miami University during the 1977 NCAA Division I football season.  In their fourth season under head coach Dick Crum, the Redskins tied for the Mid-American Conference (MAC) championship, compiled a 10–1 record (5–0 against MAC opponents) and outscored all opponents by a combined total of 262 to 173.  The team's sole loss came against South Carolina by a 42–19 score in the second week of the season.

1964 Miami Redskins football team: The 1964 Miami Redskins football team was an American football team that represented Miami University in the Mid-American Conference (MAC) during the 1964 college football season.  In their second season under Schembechler, the Redskins compiled a 6–3–1 record (4–2 against MAC opponents), finished in a tie for second place in the MAC, and outscored all opponents by a combined total of 210 to 142.  On October 17, 1964, in what is regarded as one of the great victories in Miami football history, Miami defeated Northwestern, coached by former Miami mentor Ara Parseghian, by a 28 to 27 score.

1972 Miami Redskins football team: The 1972 Miami Redskins football team was an American football team that represented Miami University in the Mid-American Conference (MAC) during the 1972 college football season.  In their fourth season under head coach Bill Mallory, Miami compiled a 7–3 record (2–3 against MAC opponents), finished in a tie for fourth place in the MAC, and outscored all opponents by a combined total of 207 to 117.  The team's defense allowed only 11.7 points per game, which ranked 12th among 128 NCAA University Division football teams.

1967 Miami Redskins football team: The 1967 Miami Redskins football team was an American football team that represented Miami University in the Mid-American Conference (MAC) during the 1967 college football season.  In their fifth season under Bo Schembechler, Miami compiled a 6–4 record (4–2 against MAC opponents), finished in a tie for third place in the MAC, and outscored all opponents by a combined total of 181 to 113.  Gary Moeller, Larry Smith, and Chuck Stobart all joined Schembechler's staff as assistant coaches in 1967.  The team's 14–3 victory over Tulane on September 23, 1967, is regarded as one of the Miami football program's greatest victories.

1888 Miami Redskins football team: The 1888 Miami Redskins football team was an American football team that represented Miami University during the 1888 college football season.  The 1888 team was Miami's first football team to compete in intercollegiate football.  The team played only one game, a scoreless tie with the University of Cincinnati football team at Oxford, Ohio, on December 8, 1888.  The team did not have a paid coach from 1888 to 1894.  The 1888 game between Cincinnati and Miami was the first in what later became the Victory Bell series that has been included more than 110 games and is one of the oldest rivalries in college football.  It was also the first college football game played in the State of Ohio.

Question: The 1962 Miami Redskins football team represented Miami University in a conference with how many full member schools?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "conference_name": {
      "type": "string",
      "description": "The name of the athletic conference."
    },
    "team_year": {
      "type": "integer",
      "description": "The year of the football team being discussed."
    },
    "full_member_schools_count": {
      "type": "integer",
      "description": "The total number of full member schools in the conference."
    },
    "membership_details": {
      "type": "object",
      "properties": {
        "schools_in_ohio_and_michigan": {
          "type": "integer",
          "description": "The number of full member schools located in Ohio and Michigan."
        },
        "single_member_states": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of states that have a single full member school in the conference."
        }
      },
      "required": [
        "schools_in_ohio_and_michigan",
        "single_member_states"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "conference_name",
    "team_year",
    "full_member_schools_count",
    "membership_details"
  ],
  "additionalProperties": false
}

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
1986–87 Indiana Hoosiers men's basketball team: The 1986–87 Indiana Hoosiers men's basketball team represented Indiana University.  Their head coach was Bobby Knight, who was in his 16th year.  The team played its home games in Assembly Hall in Bloomington, Indiana, and was a member of the Big Ten Conference.  The team is noted for having achieved much success without much NBA talent.

1991–92 Indiana Hoosiers men's basketball team: The 1991–92 Indiana Hoosiers men's basketball team represented Indiana University.  Their head coach was Bobby Knight, who was in his 21st year.  The team played its home games in Assembly Hall in Bloomington, Indiana, and was a member of the Big Ten Conference.

1978–79 Indiana Hoosiers men's basketball team: The 1978–79 Indiana Hoosiers men's basketball team represented Indiana University.  Their head coach was Bobby Knight, who was in his 8th year.  The team played its home games in Assembly Hall in Bloomington, Indiana, and was a member of the Big Ten Conference.

1980–81 Indiana Hoosiers men's basketball team: The 1980–81 Indiana Hoosiers men's basketball team represented Indiana University.  Their head coach was Bobby Knight, who was in his 10th year.  The team played its home games in Assembly Hall in Bloomington, Indiana, and was a member of the Big Ten Conference.

1996–97 Indiana Hoosiers men's basketball team: The 1996–97 Indiana Hoosiers men's basketball team represented Indiana University.  Their head coach was Bobby Knight, who was in his 26th year.  The team played its home games in Assembly Hall in Bloomington, Indiana, and was a member of the Big Ten Conference.  The Hoosiers finished the regular season with an overall record of 22–11 and a conference record of 9–9, finishing in a tie for sixth in the Big Ten.  The Hoosiers received an at-large bid to the NCAA Tournament as a No. 8 seed.  However, IU made a quick exit with a loss in the First Round to Colorado.

1971–72 Indiana Hoosiers men's basketball team: The 1971–72 Indiana Hoosiers men's basketball team represented Indiana University.  Their head coach was Bobby Knight, who was in his 1st year.  The team played its home games in the newly constructed Assembly Hall in Bloomington, Indiana, and was a member of the Big Ten Conference.

Bob Knight: Robert Montgomery Knight (born October 25, 1940) is a retired American basketball coach.  Nicknamed "The General", Knight won 902 NCAA Division I men's college basketball games, the most all-time at the time of his retirement and currently second all-time, behind his former player and assistant coach Mike Krzyzewski of Duke University.  Knight is best known as the head coach of the Indiana Hoosiers from 1971 to 2000.  He also coached at Texas Tech (2001–2008) and at Army (1965–1971).

2000–01 Indiana Hoosiers men's basketball team: The 2000–01 Indiana Hoosiers men's basketball team represented Indiana University.  At beginning of the season, the head coach was Bobby Knight; however, Knight was fired early September 2000, and Mike Davis was named interim head coach.  The team played its home games in the Assembly Hall in Bloomington, Indiana, and was a member of the Big Ten Conference.

1999–2000 Indiana Hoosiers men's basketball team: The 1999–2000 Indiana Hoosiers men's basketball team represented Indiana University.  Their head coach was Bobby Knight, who (unbeknownst to Knight) was coaching his last full season.  The team played its home games in Assembly Hall in Bloomington, Indiana, and was a member of the Big Ten Conference.

1992–93 Indiana Hoosiers men's basketball team: The 1992–93 Indiana Hoosiers men's basketball team represented Indiana University.  Their head coach was Bobby Knight, who was in his 22nd year.  The team played its home games in Assembly Hall in Bloomington, Indiana, and was a member of the Big Ten Conference.

Question: The 1991–92 Indiana Hoosiers men's basketball team represented Indiana University, their head coach was Bobby Knight, Robert Montgomery Knight, a retired American basketball coach, who was in his which year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "team_season": {
      "type": "string",
      "description": "The season of the Indiana Hoosiers men's basketball team."
    },
    "coach": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the head coach."
        },
        "year_number": {
          "type": "integer",
          "description": "The numerical year of the coach's tenure for that season."
        },
        "year_ordinal": {
          "type": "string",
          "description": "The ordinal representation of the coach's tenure year (e.g., '1st', '21st')."
        }
      },
      "required": [
        "name",
        "year_number",
        "year_ordinal"
      ],
      "additionalProperties": false
    },
    "university": {
      "type": "string",
      "description": "The university the team represented."
    }
  },
  "required": [
    "team_season",
    "coach",
    "university"
  ],
  "additionalProperties": false
}

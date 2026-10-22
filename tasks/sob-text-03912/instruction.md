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
Fath Tehran F.C.: Fath Tehran F.C. was an Iranian Football club based in Tehran, Iran.  It was the first club of former Bayern Munich midfielder Ali Karimi, and former VfL Bochum striker Vahid Hashemian.

Sajjad Shahbazzadeh: Sajjad Shahbazzadeh (Persian: سجاد شهباززاده‎ ‎ , born 23 January 1990 in Ardabil, Iran) is an Iranian footballer who plays for Esteghlal Tehran in the Iranian Persian Gulf Pro League.

Hadi Tavoosi: Hadi Tavoosi (هادی طاووسی in Persian, born 7 October 1938 in Tehran, Iran) is a retired Iranian footballer and administrator.  He was a Goalkeeper and has played most of his playing careers in Shahin and Persepolis.  He was also played one season at Paykan on loan.  He was retired in 1974 and became a vice president at Iranian Football Federation.  After resignation of Naser Noamooz in 1980, Tavoosi was appointed as president of the football federation.  He was president of Iranian FA from 6 October 1980 until 8 August 1981.

Kargaran Stadium: Kargaran Stadium is a sporting stadium (mainly used for football/soccer) in Tehran.  The teams houses Parseh Tehran F.C..  It has capacity of 5,000.

Mohammad Panjali: Seyed Mohammad Panjali Qomi (born July 26, 1955 in Tehran, Iran) is a retired Iranian footballer and a football coach.  He played for Bargh Tehran, Fath Tehran, F.C. Aboomoslem, Persepolis FC, Al-Ittihad and the Iran national football team, where he made 45 appearances.  He usually played in the defender position.  He was also team manager of Persepolis from 1993 until 1994.

Ali Karimi: Ali Karimi (Persian: علی کریمی‎ ‎ ] (born 8 November 1978) is an Iranian coach and retired footballer.  He has played for Fath Tehran, Persepolis, Al-Ahli Dubai, Bayern Munich, Qatar SC, Steel Azin, Schalke 04, Tractor Sazi, and the Iran national team for which he scored 38 goals in 127 appearances.  In 2004, he became the fourth Iranian player to win the Asian Footballer of the Year.  He announced his retirement at the end of the 2013–14 season and, on 11 April 2014, played the final game of his 18-year career.  He is currently manager of Naft Tehran.

Iranian missile boat Paykan (2003): "For the Automobile see Paykan." <br>"For the Iranian football club based in Tehran, see Paykan Tehran F.C."

Mohammad Ranjbar: Mohammad Ranjbar (1 January 1935 – 29 June 2004) was an Iranian footballer and coach.  Ranjbar played for Taj Tehran and Pas Tehran.  He was a member and captain of Iran national football team.  He was also head coach of national team in 1972.

Reza Rezaeimanesh: Reza Rezaeimanesh (Persian: رضا رضائی منش‎ ‎ , born 1969 in Tehran) is a retired Iranian football Right Wingback.  He played for Esteghlal Jonub Tehran F.C., Pas F.C., Bahman F.C. and the Iranian national football team.  He also had a stint with Singaporean side Geylang in 1997.

Vahid Hashemian: Vahid Hashemian (Persian: وحيد هاشميان‎ ‎ , born 21 July 1976) is a retired Iranian footballer and current coach.

Question: What 1976 born Iranian footballer got his start on Fath Tehran F.C.?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "footballer_name": {
      "type": "string",
      "description": "The name of the Iranian footballer."
    },
    "birth_year": {
      "type": "integer",
      "description": "The birth year of the footballer."
    },
    "first_club": {
      "type": "string",
      "description": "The name of the first club the footballer played for."
    }
  },
  "required": [
    "footballer_name",
    "birth_year",
    "first_club"
  ],
  "additionalProperties": false
}

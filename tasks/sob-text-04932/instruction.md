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
John Walmsley: John William Walmsley (22 April 1903 – 1970) was an English professional association footballer who played predominantly as a wing half.  Born in Accrington, Lancashire, he initially played Sunday league football for St Paul's and Accrington St Peter's.  Walmsley started his senior playing career in non-league football with Bacup Borough before joining Football League Third Division North side Nelson in 1921.  He played just one match for Nelson, appearing at centre-half in the 2–4 defeat to Wrexham on 26 November 1921.

Accrington F.C.: Accrington Football Club was an English football club from Accrington, Lancashire, who were one of the founder members of The Football League.

Accrington Stanley F.C. (1891): Accrington Stanley was an English football club based in Accrington, Lancashire.  Established in 1891, the club played in the Football League between 1921 and 1962, when the club became the second to resign from the League mid-season.  The club went into liquidation in 1966.  They played at Peel Park.

Blackcraig Castle: Blackcraig Castle is a tower house located at Blairgowrie, Perth, Scotland.  Patrick Allan Fraser built the Bridge House this very unique building.  The Bridge House is close to Blackcraig Castle which took almost 40 years to complete, from 1856 to late 1880s.  Fraser bought the land in 1847 from trustees of Robert Rattray.  The Castle became part of Hospitalfield Arts Trust after the death of Fraser in 1890.  The Bridge House is run as a guest house.  It is three storeys tall and it was built with lime-mortared rubble.

List of Accrington Stanley F.C. seasons: Accrington Stanley Football Club is an English football club based in Accrington, Lancashire.  The club participates in Football League Two, the fourth tier of the English football league system.

List of Nelson F.C. seasons: Nelson F.C. is an English semi-professional association football club based in the town of Nelson, Lancashire.  Founded in 1881, the club played friendly matches for its first eight years, before becoming one of the founder members of the Lancashire League in 1889.  The team won the Lancashire League title in 1896, but disbanded in late 1898 and was suspended by the Lancashire Football Association following incidents involving fans at an FA Cup defeat at Southport Central.  Nelson was accepted back into the Lancashire League the following season and in 1901, they joined the Lancashire Combination.  Between 1915 and 1918, the team ceased play for the First World War.  When competitive football restarted in England in 1919, they joined the Central League.  Two seasons later, the club was invited to be one of the founder teams of the Football League Third Division North.  They won the league in 1923, gaining promotion to the Football League Second Division.  However, they stayed there for just one season, finishing second-bottom of the league and being relegated back to the Third Division.

Accrington Stanley F.C.: Accrington Stanley Football Club is an association football club based in Accrington, Lancashire.  The team play in League Two, the fourth tier of the English football league system.

Charlie Jackson (defensive back): Charles Robert Jackson (born March 3, 1936) is a former American football defensive back who played one season with the Chicago Cardinals of the National Football League (NFL).  He was drafted by the Chicago Cardinals in the 13th round of the 1958 NFL Draft.  He played college football at Southern Methodist University and attended Paris High School in Paris, Texas.  Jackson was also a member of the Dallas Texans of the American Football League.

Charlie Rattray: Charles Robert Rattray (11 May 1911 – 1 October 1995) was an English footballer who scored 16 goals in 150 league games in a nine-year career in the Football League with Blackpool, Watford, Mansfield Town, Port Vale, and Accrington Stanley.

Crown Ground: The Crown Ground is a multi-use stadium in Accrington, Lancashire, England.  It is currently called the Wham Stadium as part of a three-year £200,000 sponsorship deal with What More UK Ltd.  It is currently used mostly for football matches and is the home ground of Accrington Stanley.  The stadium holds 5,057 and was built in 1968.  It is currently the smallest stadium in the Football League.

Question: Who was Charles Robert Rattray in a Football League with that was located in Accrington, Lancashire?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The full name of the footballer."
    },
    "club_name": {
      "type": "string",
      "description": "The name of the football club."
    },
    "club_location": {
      "type": "string",
      "description": "The location of the football club."
    },
    "league_affiliation": {
      "type": "string",
      "description": "The league the club was affiliated with."
    }
  },
  "required": [
    "player_name",
    "club_name",
    "club_location",
    "league_affiliation"
  ],
  "additionalProperties": false
}

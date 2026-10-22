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
Kyle Jarvis: Kyle Malcolm Jarvis (born 16 February 1989) is a Zimbabwean cricketer who represents Zimbabwe and played for Lancashire.  The son of another former Zimbabwean international cricketer Malcolm Jarvis, he was educated at St Johns College, Harare, where he excelled at rugby and cricket.  Kyle was a key bowler for Zimbabwe in the 2008 Under-19 World Cup and he also played for the Zimbabwe U-19 Rugby Team.

Tudor architecture: The Tudor architectural style is the final development of Medieval architecture in England, during the Tudor period (1485–1603) and even beyond, and also the tentative introduction of Renaissance architecture to England.  It is generally not used to refer to the whole period of the Tudor dynasty (1485-1603), but in prestige buildings to the period roughly between 1500 and 1560.  It followed the Late Gothic Perpendicular style and was superseded by Elizabethan architecture from about 1560 in domestic building of any pretensions to fashion.  In the much more slow-moving styles of vernacular architecture "Tudor" has become a designation for styles like half-timbering that characterise the few buildings surviving from before 1485 and others from the Stuart period.  In this form the Tudor style long retained its hold on English taste.  Nevertheless, 'Tudor style' is an awkward style-designation, with its implied suggestions of continuity through the period of the Tudor dynasty and the misleading impression that there was a style break at the accession of Stuart James I in 1603.

Stu Roberts: Stuart James Roberts (born 22 March 1965 in Christchurch) is a former New Zealand cricketer who played two One Day Internationals in 1990.

Stuart Karppinen: Stuart James Karppinen (born 13 June 1973) is a former Australian cricketer who is the current strength and conditioning coach of the Australian national cricket team.  Born in Townsville, Karppinen moved to Canberra with his family at a young age.  He played for the Australian Capital Territory Under-19s at the 1991–92 Barclays Bank Australian Under-19 Championships, taking one wicket in his only match.  He was first selected for the Australian Capital Territory senior side during the 1993–94 season, although the ACT did not at the time have either first-class or List A status, and thus only played state teams' Second XIs and other sides touring Canberra.  Karppinen was also the recipient of an Australian Institute of Sport scholarship in 1997.  The Australian Capital Territory was admitted to the Australian domestic limited-overs competition for the 1997–98 season, playing as the "Canberra Comets".  Karppinen played six matches for the team in their inaugural season, taking nine wickets with a best of 2/35.  Karppinen did not play any matches the following season, and transferred to Western Australia for the 1999–2000 season.

Stuart Davidson (cricketer): Stuart James Davidson (born 8 March 1972) is a Zimbabwean-born former Scottish cricketer.  Davidson was a right-handed batsman who bowled right-arm medium pace.

Devika Palshikar: Devika Palshikar (Devanagari:देविका पळशीकर, born 20 June 1979 in Malvan, Maharashtra, India) is a Test and One Day International cricketer who represents India.  She has played one Test and 15 ODIs and represents Maharashtra and West Zone in India's domestic league.

Stuart Airey: Stuart James Airey (born 18 March 1983) is an English cricketer.  Airey is right-handed batsman who bowled right-arm medium-fast.  He was born in Cleethorpes, Lincolnshire.

Stuart McCullum: Stuart James McCullum (born 6 December 1956) is a former cricketer who played for Otago throughout his career.  A left-handed opening batsman who occasionally kept-wicket, he is the father of New Zealand international players Brendon and Nathan McCullum.

Nathan McCullum: Nathan Leslie McCullum (born 1 September 1980) is a former New Zealand international cricketer, who represented New Zealand in Twenty20 Internationals and One Day Internationals.

Brendon McCullum: Brendon Barrie McCullum {'1': ", '2': ", '3': ", '4': "} (born 27 September 1981), popularly Brendon "Baz" McCullum is a former New Zealand international cricketer, who played all formats and also a former captain in all forms.  A big hitting legend in limited over cricket, McCullum took quick scoring to Test matches as well, notably recording the fastest test century of all time.  He is considered as one of the most successful captains of New Zealand cricket.

Question: The son of Stuart James McCullum is an international cricketer who represents which country? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "father_name": {
      "type": "string",
      "description": "The full name of the father mentioned in the question."
    },
    "sons_details": {
      "type": "array",
      "description": "Details about the sons who are international cricketers.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the son."
          },
          "is_international_cricketer": {
            "type": "boolean",
            "description": "Indicates if the son is an international cricketer."
          },
          "represented_country": {
            "type": "string",
            "description": "The country the son represents as an international cricketer."
          }
        },
        "required": [
          "name",
          "is_international_cricketer",
          "represented_country"
        ],
        "additionalProperties": false
      }
    },
    "final_answer_country": {
      "type": "string",
      "description": "The country that the son of Stuart James McCullum represents as an international cricketer."
    }
  },
  "required": [
    "father_name",
    "sons_details",
    "final_answer_country"
  ],
  "additionalProperties": false
}

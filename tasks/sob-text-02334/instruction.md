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
Stefan Mihajlović: Stefan Mihajlović (; born 24 June 1994) is a Serbian footballer, who plays for Vojvodina.  He is a son of former Bosnian Serb footballer Radmilo Mihajlović.

Momčilo Krajišnik: Momčilo Krajišnik (Serbian Cyrillic: ; born 20 January 1945) is a former Bosnian Serb political leader, who along with Radovan Karadžić co-founded the Bosnian Serb nationalist Serb Democratic Party (SDS).  Between 1990-92, he was Speaker of the People's Assembly of Republika Srpska.  Between June and December 1992, he also served as member of the expanded Presidency of Republika Srpska.

Tihomir Ognjanov: Tihomir "Bata" Ognjanov (Serbian Cyrillic: Тихомир Огњанов; 2 March 1927 – 2 July 2006) was a Serbian footballer who was part of Yugoslavia national football team at the 1950 and 1954 FIFA World Cup.  He later became a manager.  He played for Spartak Subotica (in three different periods), Partizan (when he was in the Yugoslav Army although he only played in friendly matches) and Red Star.  With Red Star he won 2 national championships (1951, 1953) and 2 Yugoslav cups (1949, 1950).

Haris Smajić: Haris Smajić (born 8 March 1960) is a former Bosnian footballer.  He played for Yugoslavia national under-20 football team at the 1979 FIFA World Youth Championship, but was never capped for Yugoslavia at full international level.

Stojan Malbašić: Stojan Malbašić (, born 15 September 1959) is a former Bosnian Serb footballer and now a coach at FK Borac Banja Luka.

Radmilo Mihajlović: Radmilo Mihajlović (born 19 November 1964) is a former Bosnian Serb footballer who played for the Yugoslavia national football team.

Ranko Golijanin: Ranko Golijanin (Serbian Cyrillic: ; born January 18, 1975) is a Bosnian Serb footballer who played in the First League of FR Yugoslavia, Segunda División, USL A-League, and the Canadian Soccer League.

Boško Antić: Božidar "Boško" Antić (Serbian Cyrillic: Божидар "Бошко" Антић; born January 7, 1944 in Sarajevo, Vrhbosna County, Independent State of Croatia, now Bosnia and Herzegovina) was a Bosnian Serb footballer who played for SFR Yugoslavia.

Yugoslavia national football team: The Yugoslavia national football team represented the Kingdom of Yugoslavia (1918–1941, "until 1929 as Kingdom of Serbs, Croats and Slovenes"), and the Socialist Federal Republic of Yugoslavia (1943–1992, "until November 29, 1945 as Democratic Federal Yugoslavia", "29 November 1945–1963 as Federal People's Republic of Yugoslavia") in association football.  It enjoyed success in international competition.  In 1992, during the Yugoslav wars, the team was suspended from international competition as part of a United Nations sanction.  In 1994, when the boycott was lifted, it was succeeded by the Federal Republic of Yugoslavia national football team.

Mitar Lukić: Mitar Lukić (born 22 October 1957) is a former Bosnian Serb footballer and current manager of FK Sloga Doboj.

Question: Stefan Mihajlović ( born 24 June 1994) is a Serbian footballer, who plays for which team, he is a son of Radmilo Mihajlovi, a former Bosnian Serb footballer, who played for the Yugoslavia national football team?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_name": {
      "type": "string",
      "description": "The name of the footballer."
    },
    "player_nationality": {
      "type": "string",
      "description": "The nationality of the footballer."
    },
    "player_birth_date": {
      "type": "string",
      "description": "The birth date of the footballer."
    },
    "current_team": {
      "type": "string",
      "description": "The current team the footballer plays for."
    },
    "parent_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the parent."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the parent."
        },
        "former_profession": {
          "type": "string",
          "description": "The former profession of the parent."
        },
        "played_for_national_team": {
          "type": "string",
          "description": "The national team the parent played for."
        }
      },
      "required": [
        "name",
        "nationality",
        "former_profession",
        "played_for_national_team"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "player_name",
    "player_nationality",
    "player_birth_date",
    "current_team",
    "parent_details"
  ],
  "additionalProperties": false
}

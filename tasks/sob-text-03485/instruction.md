{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\n1987–88 U.C. Sampdoria season: U.C. Sampdoria won its second cup trophy in just three years, defeating Torino in the final, thanks to a 3-2 aggregate victory.  Gianluca Vialli scored ten goals to become club top scorer, as Sampdoria finished fourth in the domestic league.\n\n1986–87 U.C. Sampdoria season: U.C. Sampdoria started its march towards an eventual Serie A championship and European Cup final with its appointment of Yugoslav coach Vujadin Boškov.  With Britons Graeme Souness and Trevor Francis leaving the squad, Boškov built his team around young Italian players, with Roberto Mancini, Gianluca Vialli, Pietro Vierchowod and Moreno Mannini among the bulwark of the squad as Sampdoria finished 6th in a tight battle involving several teams for 3rd in the championship.\n\n1985–86 U.C. Sampdoria season: U.C. Sampdoria fell short of repeating its successful 1984-85 season, ending up in 12th position in the league.  It did almost defend its cup title successfully, but despite a 2-1 victory in the first leg, it lost to Roma in the return leg.  Sampdoria's European adventure did not live up to expectations, it not even reaching the quarter finals of the Cup Winners' Cup.\n\n1994–95 U.C. Sampdoria season: Unione Calcio Sampdoria spent the 1994-95 season mired in the midfield, since its remarkable offensive play from the 1993-94 season failed to occur.  Despite this, it came close to another European final, but stumbled at Arsenal following penalties in the semi finals.  Following the end of the season, creative midfielders David Platt, Attilio Lombardo and Vladimir Jugović all left the club, bringing further uncertainty of the future direction of the club.\n\nDavid Platt (footballer): David Andrew Platt (born 10 June 1966) is an English former professional footballer who played as a midfielder.\n\n1984–85 U.C. Sampdoria season: U.C. Sampdoria recorded its best league season since 1960-61, thanks to a fourth place-finish.  President Mantovani had surprised the football world by signing Liverpool stalwart Graeme Souness to the squad, and it paid off, with Souness adapting quickly to Italian football, also helping the team to win the 1985 edition of Coppa Italia, which was the first ever title for the club.  The defensive line, with Moreno Mannini, Pietro Vierchowod and Antonio Paganin among the crew, was the main reason for the success, Sampdoria conceding just 23 goals in 30 league matches played.  Quite a few of the players were still with the club when it finally won the league title in 1991.\n\n2004–05 U.C. Sampdoria season: U.C. Sampdoria enjoyed its best season since 1993–94, when the club finished third in Serie A and won Coppa Italia.  In 2004-05 Sampdoria was able to finish fifth in the standings, thanks to a robust defence and a goalscoring ace in secondary striker Francesco Flachi, who played the football of his life.  With only 29 goals conceded, the defence of Sampdoria was fully comparable with those of top sides Juventus and Milan, and coach Walter Novellino was hailed for the strong performance in the clubs' second season since its return to Serie A.\n\n1992–93 U.C. Sampdoria season: U.C. Sampdoria continued its decline and finished in seventh position in Serie A, once again missing out on international competitions.  New coach Sven-Göran Eriksson came to a squad that had lost its main striker Gianluca Vialli, but despite his absence Sampdoria scored 50 goals in 34 matches, but the defence leaked in an uncharacteristic manner for Eriksson's teams.\n\n1990–91 U.C. Sampdoria season: U.C. Sampdoria won their first ever Serie A title, thanks to a remarkable season for a team playing on its absolute peak.  Gianluca Vialli was the league top scorer on 19 goals, and Roberto Mancini, Attilio Lombardo, goalkeeper Gianluca Pagliuca plus centre half Pietro Vierchowod were also instrumental in Sampdoria's success story.\n\n2007–08 U.C. Sampdoria season: U.C. Sampdoria had a successful season in the domestic league, finishing in sixth place.  The club also captured Antonio Cassano from Real Madrid, with the notorious troublemaker settling in well at Sampdoria, helping the club to European qualification.  The season also saw the first Serie A derbies between Sampdoria and Genoa C.F.C. since 1995, with Sampdoria winning the second one with 1-0, following a goalless draw in the beginning of the league campaign.\n\nQuestion: The 1994–95 U.C. Sampdoria season included a midfielder who was of what nationality?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"season_year\": {\n      \"type\": \"string\",\n      \"description\": \"The specific season being referred to.\"\n    },\n    \"player_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the midfielder.\"\n    },\n    \"player_nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the midfielder.\"\n    },\n    \"player_position\": {\n      \"type\": \"string\",\n      \"description\": \"The position played by the player.\"\n    }\n  },\n  \"required\": [\n    \"season_year\",\n    \"player_name\",\n    \"player_nationality\",\n    \"player_position\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "season_year": {
        "type": "string",
        "description": "The specific season being referred to."
      },
      "player_name": {
        "type": "string",
        "description": "The name of the midfielder."
      },
      "player_nationality": {
        "type": "string",
        "description": "The nationality of the midfielder."
      },
      "player_position": {
        "type": "string",
        "description": "The position played by the player."
      }
    },
    "required": [
      "season_year",
      "player_name",
      "player_nationality",
      "player_position"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

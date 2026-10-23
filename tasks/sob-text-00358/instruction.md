{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\n1968–69 in Belgian football: The 1968–1969 season was the 66th season of competitive football in Belgium.  Standard Club Liégeois won their 4th Division I title.  No Belgian club managed to pass the second round of the European competitions, though for the first time 6 Belgian clubs qualified (1 more club qualified for the Inter-Cities Fairs Cup).  K Lierse SK won the Belgian Cup final against RR White (2-0).  The Belgium national football team continued their 1970 FIFA World Cup qualification campaign with 3 home wins against all other Group 6 teams (Finland, Yugoslavia and Spain) and a draw in Spain.  Belgium qualified for the 1970 FIFA World Cup finals in Mexico with one match to go.  For the first time since the 1954 FIFA World Cup, Belgium would qualify for a major tournament.\n\nGary Cooke: Gary Cooke is an Irish actor, satirist and writer who is one of the stars, on screen, of \"Après Match\" and, on stage, \"I, Keano\" and \"MacBecks\".  He is perhaps best known for his portrayal of media personality Eamon Dunphy, although he has also mocked \"Match of the Day\" presenter Gary Lineker and TV3 sports broadcaster Trevor Welch.\n\nFIFA World Cup qualification: The FIFA World Cup qualification is the process that a national association football team goes through to qualify for the FIFA World Cup finals.  The FIFA World Cup is the largest international team sport competition in the world with a qualification process required to reduce the large field of countries from 211 to just 32 for the World Cup finals until the 2022 edition.\n\nManuel Rosas: Manuel Rosas Sánchez (April 17, 1912 in Mexico City – February 20, 1989), nicknamed \"Chaquetas\", was a Mexican footballer who participated in the 1930 FIFA World Cup.  He was the first player in the history of FIFA World Cup who scored a goal from the penalty kick spot (against Argentina).  With the first goal he scored during the World Cup, he became at the time the youngest player to have scored in the FIFA World Cup, a record later broken by Pelé, although Rosas remains second youngest.  He was also the first Mexican player to score multiple goals in world cup play (the first to score more than two goals was Luis Hernandez, 68 years later) and the first player to score a own goal in the history of FIFA World Cup (against Chile).\n\n2002 FIFA World Cup: The 2002 FIFA World Cup was the 17th staging of the FIFA World Cup which took place from 31 May to 30 June 2002 in South Korea and Japan.  It was the first World Cup to be held in Asia, the first to be held on a continent other than Europe or the Americas, the last World Cup during which the golden goal rule was in force and the only World Cup to be jointly hosted by more than one nation.  Brazil won the tournament for a record fifth time, winning the final against Germany 2–0.  The victory meant Brazil qualified for the 2005 FIFA Confederations Cup for the fifth time, representing the World.  In the third place play-off match against South Korea, Turkey won 3–2 taking third place in only their second ever FIFA World Cup finals.  China PR, Ecuador, Senegal and Slovenia made their first appearances at the finals with Turkey making its first appearance since 1954.  Republic of Ireland, Russia and Sweden returned after missing the 1998 tournament.\n\nJapan 2022 FIFA World Cup bid: The Japan 2022 FIFA World Cup bid is the second official bid from the Japan Football Association or the JFA.  Had this bid been successful, Japan would have been hosting their second World Cup Finals and it would have been their first solo hosting since they shared the 2002 FIFA World Cup with other co-host South Korea, becoming the sixth nation to host the tournament twice, after Italy, France, Mexico, Brazil and (West) Germany.  On May 4, 2010, the Japanese Football Association Bid team decided to concentrate solely on winning the right to host the 2022 FIFA World Cup.\n\nFIFA 06: Road to FIFA World Cup: FIFA 06: Road to FIFA World Cup is a video game developed by EA Sports and DICE for the Xbox 360.  The game is an officially licensed product of the 2006 FIFA World Cup finals held in Germany.  \"FIFA 06: Road to FIFA World Cup\" World Cup mode only includes UEFA qualification groups for the 2006 World Cup.\n\n2015 FIFA Women's World Cup Final: The 2015 FIFA Women's World Cup Final was a professional women's soccer match that took place on 5 July 2015 at BC Place, in Vancouver, British Columbia, Canada, to determine the winner of the 2015 FIFA Women's World Cup.  It was played between Japan and the United States, in a rematch of the 2011 final.  The stakes were high for both sides: if the United States won the match, it would be the only country to have won in three Women's World Cup finals; if Japan had won instead, then it would be the first soccer team, men's or women's, to win twice under the same coach (Norio Sasaki for Japan) since Vittorio Pozzo lead Italy to victory in the 1934 World Cup and the 1938 World Cup 77 years ago.  Ultimately, the United States won 5–2, winning its first title in sixteen years and becoming the first team to win three Women's World Cup finals.\n\nJosé Altafini: José João Altafini (born 24 July 1938), also known as \"Mazzola\" in Brazil (as when he started to play it was noted that he resembled the Italian legend Valentino Mazzola), is an Italian-Brazilian former footballer, who played as a forward.  Although he began his career with Palmeiras in Brazil, he soon moved to play football in Italy, and is mostly remembered for his highly successful stint with Italian club A.C. Milan, with which he achieved great domestic and international success; he later also played for Napoli and Juventus, before ending his career in Switzerland with spells at Chiasso and Mendrisiostar.  A highly prolific goalscorer, Altafini also held the record for the most goals scored in a single European Cup campaign for over 50 years; he is also one of only eight players to have scored five goals in a single European Cup match.  He is the joint-fourth highest scorer in Italian Serie A history (along with Giuseppe Meazza) with 216 goals, and also holds the record for being the youngest player in Serie A to score 100 goals.  At international level, he represented both Brazil and Italy; he was a member of the Brazilian side that won the 1958 FIFA World Cup, and later also represented Italy at the 1962 FIFA World Cup.\n\nGary Lineker: Gary Winston Lineker, OBE ( ; born 30 November 1960) is an English retired footballer and current sports broadcaster.  He holds England's record for goals in FIFA World Cup finals, with 10 scored.  Lineker's media career began with the BBC, where he has presented the flagship programme \"Match of the Day\" since the late 1990s.  He has also worked for Al Jazeera Sports, Eredivisie Live, NBC Sports Network and currently hosts BT Sport's coverage of the UEFA Champions League.\n\nQuestion: What media personality is the Irish actor who has also mocked the footballer who holds Englands record of goals in FIFA World Cup finals, best known for portraying?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"irish_actor\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the Irish actor.\"\n        },\n        \"best_known_for_portraying\": {\n          \"type\": \"string\",\n          \"description\": \"The media personality the actor is best known for portraying.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"best_known_for_portraying\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"mocked_footballer\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the footballer who was mocked by the actor.\"\n        },\n        \"record_held\": {\n          \"type\": \"string\",\n          \"description\": \"The record held by the footballer in FIFA World Cup finals.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"record_held\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"answer\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the media personality the Irish actor is best known for portraying.\"\n    }\n  },\n  \"required\": [\n    \"irish_actor\",\n    \"mocked_footballer\",\n    \"answer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "irish_actor": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the Irish actor."
          },
          "best_known_for_portraying": {
            "type": "string",
            "description": "The media personality the actor is best known for portraying."
          }
        },
        "required": [
          "name",
          "best_known_for_portraying"
        ],
        "additionalProperties": false
      },
      "mocked_footballer": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the footballer who was mocked by the actor."
          },
          "record_held": {
            "type": "string",
            "description": "The record held by the footballer in FIFA World Cup finals."
          }
        },
        "required": [
          "name",
          "record_held"
        ],
        "additionalProperties": false
      },
      "answer": {
        "type": "string",
        "description": "The name of the media personality the Irish actor is best known for portraying."
      }
    },
    "required": [
      "irish_actor",
      "mocked_footballer",
      "answer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

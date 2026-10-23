{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nHans Simonsson: Hans Simonsson (born 1 May 1962 in Färgaryd) is a retired professional tennis player from Sweden.  Primarily a doubles specialist, he won 12 ATP Tour titles in his career.  He won the French Open doubles title in 1983 with his countryman Anders Järryd.  He also played in the 1983 Davis Cup final for Sweden.  He reached his career high doubles ranking of No. 10 in the world on 2 January 1984.  Simonsson again reached the French Open doubles final in 1985, but he and Schlomo Glickstein were defeated by Mark Edmondson and Kim Warwick.  The Swede finished his career prematurely at the age of 25.  He's the brother of Stefan Simonsson.\n\nAlbert Burke (tennis): Albert Burke (1901 – 1958) was an Irish professional tennis player based in France.  Albert Burke was the son of Thomas Burke.  Thomas Burke was a professional tennis player when professional tennis began in the late 19th century and Albert Burke's brother Edmund Burke was also a professional tennis player .  Albert Burke won the Bristol Cup in France (the top professional tournament in the world in the 1920s), in 1924 and 1925 (beating Roman Najuch in both finals) .  He was also losing finalist in the Bristol Cup in 1926, 1929 and 1931 (losing all three finals to Karel Kozeluh) .  Burke finished second in the 1930 French Pro Championship round robin (Karel Kozeluh was first) .  At the US Pro Tennis Championships Burke was a quarter finalist in 1931 (losing to Howard Kinsey) and 1932 (losing to Bill Tilden) .  At the Wembley Championships Burke lost in the quarter finals in 1935 (losing to Ellsworth Vines) .\n\nKim Warwick: Kim Warwick (born 8 April 1952) is an Australian former professional male tennis player who competed on the ATP Tour from 1970–1987 reaching the final of the singles Australian Open in 1980.  He defeated over 35 players ranked in the top 10 including Guillermo Vilas, Raul Ramerez, Vitas Gerulaitis, Jan Kodeš, Bob Lutz and Arthur Ashe.  Warwick's career-high singles ranking was World No. 15, achieved in 1981.  He won three singles titles and 26 doubles, including Australian Open 1978 (with Wojtek Fibak) and Australian Open 1980 and 1981, Roland Garros 1986 and also a runner-up in Australian Open 1985, all of them partnering fellow countryman Mark Edmondson.  Partnering with Evonne Goolagong, he won the French Open 1972, defeating Françoise Dürr and Jean-Claude Barclay in the final 6–2, 6–4.  Evonne and Kim were finalists in 1972 at Wimbledon against Rosie Casals and Ilie Năstase who won 6–4, 6–4.\n\nWojciech Fibak: Wojciech Fibak (popular Wojtek Fibak; born 30 August 1952) is a Polish former tennis player best known for his doubles success with Tom Okker and Kim Warwick, but also for having reached the Top 10 in singles.\n\nCedar Grove Open: The Cedar Grove Open is a defunct tennis tournament that was played on the Grand Prix tennis circuit in 1974.  The event was held in Cedar Grove, New Jersey.  Ilie Năstase won the singles title while Kim Warwick and Steve Siegel partnered to win the doubles title.\n\nEvonne Goolagong career statistics: This is a list of the main career statistics of Australian former tennis player Evonne Goolagong.  During her career, which lasted from 1967 to 1983, Goolagong won seven singles titles at a Grand Slam event and was a runner-up on 11 occasions.  In addition she won five Grand Slam doubles titles, partnering Margaret Court, Peggy Michel and Helen Gourlay, as well as one mixed doubles title with Kim Warwick.  In total she won 82 singles titles, 46 doubles titles and 4 mixed doubles titles.  She achieved a No. 1 singles ranking for a two-week period in April–May 1976 although this was only officially recognized in 2007.  She was a member of the Australian Federation Cup teams that won the cup in 1971, 1973 and 1974.\n\n1992 US Open – Men's Doubles: The Men's Doubles tournament at the 1992 US Open was held between August 31 and September 13, 1992, on the outdoor hard courts at the USTA National Tennis Center in New York City, United States.  Jim Grabb and Richey Reneberg won the title, defeating Kelly Jones and Rick Leach in the final.\n\nRichey Reneberg: Richey Reneberg (born October 5, 1965) is an American former professional tennis player.\n\nBrisbane International: The origins of the Brisbane International trace back to the early 1970s, when the Grand Prix tennis circuit, formed in 1970, and which ran concurrently with other tours as the World Championship Tennis circuit, decided to feature on its calendar an event in Queensland to develop a South West Pacific season around the Australian Open - then taking place in Brisbane - alongside other Oceanian events of Sydney, New South Wales; Hobart, Tasmania; and Auckland, New Zealand.  The Adelaide-based South Australian Tennis Championships, running as an amateur, then as a State championship, since 1889, were brought to the professional circuit in 1972.  The first professional edition of the men's event, played, like the Australian Open, on outdoor grass courts, saw the victory of Soviet Alex Metreveli over Kim Warwick, while the women's event, still not featured in either the Commercial Union Grand Prix circuit or the Virginia Slims circuit, saw Australian Evonne Goolagong win the title.\n\nCliff Richey: George Clifford Richey Jr. (born December 31, 1946) is an American former amateur and professional tennis player who was active during the 1960s and 1970s.  Richey achieved a highest singles ranking of World No. 6 and reached at least the quarterfinal stage of the singles event at all four Grand Slam tournaments.\n\nQuestion: Which professional tennis player was Australian, Richey Reneberg or Kim Warwick?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"question_players\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"player_name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the tennis player.\"\n          },\n          \"nationality\": {\n            \"type\": \"string\",\n            \"description\": \"The nationality of the player.\"\n          },\n          \"is_australian\": {\n            \"type\": \"boolean\",\n            \"description\": \"True if the player is Australian, false otherwise.\"\n          }\n        },\n        \"required\": [\n          \"player_name\",\n          \"nationality\",\n          \"is_australian\"\n        ],\n        \"additionalProperties\": false\n      },\n      \"description\": \"Details for each player mentioned in the question.\"\n    },\n    \"australian_player_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the professional tennis player who is Australian.\"\n    },\n    \"final_answer\": {\n      \"type\": \"string\",\n      \"description\": \"The final answer to the question, which is the name of the Australian player.\"\n    }\n  },\n  \"required\": [\n    \"question_players\",\n    \"australian_player_name\",\n    \"final_answer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "question_players": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "player_name": {
              "type": "string",
              "description": "The name of the tennis player."
            },
            "nationality": {
              "type": "string",
              "description": "The nationality of the player."
            },
            "is_australian": {
              "type": "boolean",
              "description": "True if the player is Australian, false otherwise."
            }
          },
          "required": [
            "player_name",
            "nationality",
            "is_australian"
          ],
          "additionalProperties": false
        },
        "description": "Details for each player mentioned in the question."
      },
      "australian_player_name": {
        "type": "string",
        "description": "The name of the professional tennis player who is Australian."
      },
      "final_answer": {
        "type": "string",
        "description": "The final answer to the question, which is the name of the Australian player."
      }
    },
    "required": [
      "question_players",
      "australian_player_name",
      "final_answer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

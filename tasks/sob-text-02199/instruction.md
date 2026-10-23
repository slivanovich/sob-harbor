{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMarc Rosset: Marc Rosset (born 7 November 1970) is a former professional tennis player from Switzerland who is best remembered for winning the men's singles gold medal at the 1992 Olympic Games.  He also won one Grand Slam doubles title at the French Open in 1992 partnering compatriot Jakob Hlasek.\n\nTony Roche: Anthony Dalton Roche, AO MBE (born 17 May 1945) is a former professional Australian tennis player, native of Tarcutta.  He played junior tennis in the New South Wales regional city of Wagga Wagga.  He won one Grand Slam singles title and thirteen Grand Slam doubles titles, and was ranked as high as World No. 2 by Lance Tingay of \"The Daily Telegraph\" in 1969.  He also coached multi-Grand Slam winning World No. 1s, Ivan Lendl, Patrick Rafter, Roger Federer, Lleyton Hewitt and former World No. 4, Jelena Dokic.\n\nMichael Phelps: Michael Fred Phelps II (born June 30, 1985) is an American former competitive swimmer and the most decorated Olympian of all time, with a total of 28 medals.  Phelps also holds the all-time records for Olympic gold medals (23), Olympic gold medals in individual events (13), and Olympic medals in individual events (16).  In winning eight gold medals at the 2008 Beijing Games, Phelps broke fellow American swimmer Mark Spitz's 1972 record of seven first-place finishes at any single Olympic Games.  At the 2004 Summer Olympics in Athens, Phelps had already tied the record of eight medals of any color at a single Games by winning six gold and two bronze medals.  At the 2012 Summer Olympics in London, Phelps won four gold and two silver medals, and at the 2016 Summer Olympics in Rio de Janeiro, he won five gold medals and one silver.  This made him the most successful athlete of the Games for the fourth Olympics in a row.\n\nWang Meng (speed skater): Wang Meng (; born April 10, 1985 in Qitaihe, Heilongjiang) is a Chinese short track speed skater.  She is a four-time Olympic Champion and 2008 and 2009 Overall World Champion.  She is the most decorated Chinese Winter Olympic athlete ever with four Olympic gold medals, a silver and a bronze.  Wang won gold in the 500 m event, silver in the 1000 m and bronze in the 1500 m event at the 2006 Winter Olympics.  She won 500 m and 1000 m gold medals at the 2010 Vancouver Olympics and added a third gold medal in the 3000 m relay with the China team.  She also holds the world and Olympic records in the 500 m distance and the 3000 m relay.  Wang has also won 18 gold medals at the World Championships.  She is one of the most decorated short track speed skaters of all time.\n\nNikolai Andrianov: Nikolai Yefimovich Andrianov (Russian: Николай Ефимович Андрианов , 14 October 1952 – 21 March 2011) was a Soviet/Russian gymnast.  He held the record for men for the most Olympic medals at 15 (7 gold medals, 5 silver medals, 3 bronze medals) until Michael Phelps surpassed him at the 2008 Beijing Summer Olympics.  Andrianov is the third athlete (male or female) in cumulative Olympic medals after Phelps's 28 and Larisa Latynina, who earned 18.  Andrianov won the most medals at the 1976 Summer Olympics with 6 individual medals and one team medal.  Within the sport of Men's Artistic Gymnastics, he also holds the men's record for most individual Olympic medals (12) and shares the male record for most individual Olympic gold medals in gymnastics (6), tied with Boris Shakhlin and Dmitry Bilozerchev (the latter of which only if you count the 1984 Alternate Olympics).  In many other rankings among all-time medal winners at the Olympic, World, and European levels, he ranks very high, (for example, he is second only to Vitaly Scherbo in total individual medal counts at either the gold level or any level at the combined Olympic and World levels as well as at the combined Olympic, World, and European levels) – easily making him one of the most decorated gymnasts of all time.\n\nNicolás Massú: Nicolás Alejandro Massú Fried (born October 10, 1979), nicknamed \"El Vampiro\" (Spanish: \"the vampire\"), is a Chilean former tennis player, a former World No. 9 in singles, and a winner of two Olympic gold medals.  He is the only male player to have won both the singles and doubles gold medals during the same games in modern Olympic tennis (since 1988), the only two gold medals Chile has won at the Olympics.  Massú also reached the final of the 2003 Madrid Masters and won six singles titles.\n\nRalf Schumann: Ralf Schumann (born June 10, 1962) is a German 25 m Rapid Fire Pistol shooter.  He is a three-time Olympic Champion and twice the World Champion.  One of the most decorated shooters of the modern era, he is the first of two sport shooters to have won three Olympic gold medals in one individual event (25 metre rapid fire pistol) and became the first of three sport shooters to have won three Olympic individual gold medals.  He won the gold medals for the 25 metre rapid fire pistol event at the 1992, 1996 and 2004 Olympics and also won two silver medals at this event, becoming the most successful Olympic shooter at this event.  Schumann has participated in seven consecutive Olympic Games since 1988, setting a new record for most Olympic appearances by a German athlete.\n\nZhao Yunlei: Zhao Yunlei (born August 25, 1986) is a mixed and women's doubles badminton athlete from China.  She graduated with a BA from Huazhong University of Science and Technology.  She is the first and only badminton player to have ever won two Gold medals in the same Olympic edition, winning in both the Mixed and Women's Doubles categories in 2012.  Zhao joins the ranks with nine other players with two Olympic Gold Medals, the highest number of Gold Medals won by any badminton athlete.  Through her performance at the 2014 and 2015 BWF World Championships, she became the first player to win two consecutive gold medals in two consecutive BWF World Championships.\n\nVille Ritola: Vilho \"Ville\" Eino Ritola (18 January 1896 – 24 April 1982) was a Finnish long-distance runner.  Known as one of the \"Flying Finns\", he won five Olympic gold medals and three Olympic silver medals in the 1920s.  He holds the record of winning most athletics medals in one Olympic games event - four golds and two silvers in Paris 1924.  He has won the second biggest number of athletics Olympic gold medals in one event.\n\nLidiya Skoblikova: Lidiya Pavlovna Skoblikova (Russian: Лидия Павловна Скобликова ; born 8 March 1939) is a retired Russian speed skater and coach.  She represented the USSR Olympic team during the Olympic Winter Games in 1960 and 1964, and won a total of six gold medals, which is still a record for a speed skater.  She also won 25 gold medals at the world championships and 15 gold medals at the USSR National Championships in several distances.  She was also the first athlete to earn six gold medals in the Winter Olympics and the first to earn four gold medals at a single Olympic Winter Games.  She was the most successful athlete at the 1960 and 1964 Winter Olympics, sharing the honour for 1960 Games with her compatriot Yevgeny Grishin.\n\nQuestion: Which tennis player won more Olympic gold medals, Tony Roche or Marc Rosset?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"sport\": {\n      \"type\": \"string\",\n      \"description\": \"The sport in which the athletes compete.\"\n    },\n    \"player_comparison\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"player_name\": {\n            \"type\": \"string\",\n            \"description\": \"The name of the tennis player.\"\n          },\n          \"olympic_gold_medals\": {\n            \"type\": \"integer\",\n            \"description\": \"The number of Olympic gold medals won by the player.\"\n          }\n        },\n        \"required\": [\n          \"player_name\",\n          \"olympic_gold_medals\"\n        ],\n        \"additionalProperties\": false\n      },\n      \"minItems\": 2,\n      \"maxItems\": 2\n    },\n    \"player_with_more_gold_medals\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the player who won more Olympic gold medals.\"\n    }\n  },\n  \"required\": [\n    \"sport\",\n    \"player_comparison\",\n    \"player_with_more_gold_medals\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "sport": {
        "type": "string",
        "description": "The sport in which the athletes compete."
      },
      "player_comparison": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "player_name": {
              "type": "string",
              "description": "The name of the tennis player."
            },
            "olympic_gold_medals": {
              "type": "integer",
              "description": "The number of Olympic gold medals won by the player."
            }
          },
          "required": [
            "player_name",
            "olympic_gold_medals"
          ],
          "additionalProperties": false
        },
        "minItems": 2,
        "maxItems": 2
      },
      "player_with_more_gold_medals": {
        "type": "string",
        "description": "The name of the player who won more Olympic gold medals."
      }
    },
    "required": [
      "sport",
      "player_comparison",
      "player_with_more_gold_medals"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

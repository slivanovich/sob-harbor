{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nRoman Catholic Diocese of Mymensingh: The Roman Catholic Diocese of Mymensingh (Latin: \"Dioecesis Mymensinghensis\" ) is a diocese located in the city of Mymensingh in the Ecclesiastical province of Dhaka in Bangladesh.  Bishop Ponen Paul Kubi, CSC, DD is head of the Diocese of Mymensingh.  Most of the people in this Diocese are from Garo tribal community.  Bishop is also a Garo tribal.  A total of 76,047 Catholics and 6665 Protestant Christians live here.  People live on farming, day laborer in rural area and many people live in cities as migrant workers.  Female Garo are very skill in beauty parlor profession.\n\nHoward Kazanjian: Howard G. Kazanjian (born July 26, 1942) is an American film producer known for \"Raiders of the Lost Ark\" and \"Return of the Jedi\".  Kazanjian is also a former 8-year Vice President of Lucasfilm, Ltd., and a published non-fiction author.\n\nChris Enss: Chris Enss (born 1961) is an American author and screenwriter.  Enss has written more than 20 books on the subject of women in the Old West, and has collaborated with producer Howard Kazanjian on four books, including two about Roy Rogers and Dale Evans.\n\nMatrilineal society of Meghalaya: Multiple tribes in the state of Meghalaya in northeast India practise matrilineal descent.  Often referred to as Khasi people, Khasi is used as a blanket term for various subgroups in Meghalaya who have distinguishing languages, rites, ceremonies, and habits, but share an ethnic identity as \"Ki Hynniew Trep\" (The Seven Huts).  The Khasi, Garo, and other subgroups have a proud heritage, including matrilineality, although it was reported in 2004 that they were losing some of their matrilineal traits.  The tribes are said to belong to one of the \"largest surviving matrilineal culture[s]\" in the world.\n\nRaiders of the Lost Ark: Raiders of the Lost Ark (also known as Indiana Jones and the Raiders of the Lost Ark) is a 1981 American action adventure film directed by Steven Spielberg, with a screenplay written by Lawrence Kasdan, from a story by George Lucas and Philip Kaufman.  It was produced by Frank Marshall for Lucasfilm Ltd., with Lucas and Howard Kazanjian as executive producers.  Starring Harrison Ford, it was the first installment in the \"Indiana Jones\" film franchise to be released, though it is the second in internal chronological order.  It pits Indiana Jones (Ford) against a group of Nazis who are searching for the Ark of the Covenant, which Adolf Hitler believes will make his army invincible.  The film co-stars Karen Allen as Indiana's former lover, Marion Ravenwood; Paul Freeman as Indiana's rival, French archaeologist René Belloq; John Rhys-Davies as Indiana's sidekick, Sallah; Ronald Lacey as Gestapo agent Arnold Toht; and Denholm Elliott as Indiana's colleague, Marcus Brody.\n\nThe Rookie (1990 film): The Rookie is a 1990 American buddy cop film directed by Clint Eastwood and produced by Howard G. Kazanjian, Steven Siebert and David Valdes.  It was written from a screenplay conceived by Boaz Yakin and Scott Spiegel.  The film stars Charlie Sheen, Clint Eastwood, Raúl Juliá, Sônia Braga, Lara Flynn Boyle, and Tom Skerritt.  Eastwood plays a veteran police officer teamed up with a younger detective played by Sheen (\"the rookie\"), whose intent is to take down a German crime lord in downtown Los Angeles following months of investigation into an exotic car theft ring.\n\nReturn of the Jedi: Return of the Jedi (also known as Star Wars: Episode VI – Return of the Jedi) is a 1983 American epic space opera film directed by Richard Marquand.  The screenplay by Lawrence Kasdan and George Lucas was from a story by Lucas, who was also the executive producer.  It was the third installment in the original \"Star Wars\" trilogy and the first film to use THX technology.  The film is set one year after \"The Empire Strikes Back\" and was produced by Howard Kazanjian for Lucasfilm Ltd.  The film stars Mark Hamill, Harrison Ford, Carrie Fisher, Billy Dee Williams, Anthony Daniels, David Prowse, Kenny Baker, Peter Mayhew and Frank Oz.\n\nGaro Yepremian: Garabed Sarkis \"Garo\" Yepremian (June 2, 1944 – May 15, 2015) was an American football placekicker in the National Football League for the Detroit Lions, Miami Dolphins, New Orleans Saints, and Tampa Bay Buccaneers, during a career that spanned from 1966 to 1981.\n\nBill Capece: William George Capece (born April 1, 1959 in Miami, Florida) is a former professional American football player who played placekicker for three seasons for the Tampa Bay Buccaneers.  He attended Chaminade-Madonna College Preparatory School in Hollywood, Florida along with David Shula, and was invited by Shula's father, Miami Dolphins coach Don Shula, to attend Dolphin practices and work out with placekicker Garo Yepremian.  It was Yepremian who provided Capece with the encouragement to consider a career in professional football.  Capece attended Florida State University, where he graduated as the holder of FSU's records for single-season scoring (104 points), most field goals in a game (five, against Pittsburgh), and field goal percentage (100%).  His 104 points in 1980 were the most by a kicker in national collegiate history.  He was signed to a professional contract with the Buccaneers in 1981, during a week in which the Buccaneers cut both their placekicker and their punter.  Ironically, Capece's signing marked the end of his former mentor's career, as Yepremian was the player he was signed to replace.  After a late-1983 loss to the Green Bay Packers in which missed kicks provided the margin of defeat, coach John McKay made his famous announcement that \"Capece is kaput\".  Capece returned as the team's placekicker the following season, but was waived following a poor performance in a preseason game against the Dolphins.  His 41 field goals stood as the Buccaneers' career record until broken in 1987 by Donald Igwebuike.\n\nJoseph H. Howard: Dr. Joseph H. Howard (1912 - 1994) a dentist by profession gathered what is arguably the \"largest collection\" of drums in the Americas.  Dr. Howard and his wife Bootsie travelled around the world over a period of 40 years amassing this collection of 800 drums, representing the drums and other musical instruments of cultures from Alaska to Argentina and from California to the Pacific islands, as well as Africa and Asia.  The importance of his collection has been noted by experts on folk instruments at the Smithsonian Institution and were part of a major touring exhibit with artifacts collected by Fernando Ortiz the Cuban ethnographer who defined Afro-Cuban culture and wrote 30 books on the subject.\n\nQuestion: Do Garo Yepremian and Howard Kazanjian both share the same profession ?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"question_asked\": {\n      \"type\": \"string\",\n      \"description\": \"The original question posed.\"\n    },\n    \"person_1\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the first person.\"\n        },\n        \"profession\": {\n          \"type\": \"string\",\n          \"description\": \"The profession of the first person.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"profession\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"person_2\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the second person.\"\n        },\n        \"profession\": {\n          \"type\": \"string\",\n          \"description\": \"The profession of the second person.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"profession\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"share_same_profession\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates whether both individuals share the same profession.\"\n    },\n    \"reasoning\": {\n      \"type\": \"string\",\n      \"description\": \"Explanation for why they do or do not share the same profession.\"\n    }\n  },\n  \"required\": [\n    \"question_asked\",\n    \"person_1\",\n    \"person_2\",\n    \"share_same_profession\",\n    \"reasoning\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "question_asked": {
        "type": "string",
        "description": "The original question posed."
      },
      "person_1": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the first person."
          },
          "profession": {
            "type": "string",
            "description": "The profession of the first person."
          }
        },
        "required": [
          "name",
          "profession"
        ],
        "additionalProperties": false
      },
      "person_2": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the second person."
          },
          "profession": {
            "type": "string",
            "description": "The profession of the second person."
          }
        },
        "required": [
          "name",
          "profession"
        ],
        "additionalProperties": false
      },
      "share_same_profession": {
        "type": "boolean",
        "description": "Indicates whether both individuals share the same profession."
      },
      "reasoning": {
        "type": "string",
        "description": "Explanation for why they do or do not share the same profession."
      }
    },
    "required": [
      "question_asked",
      "person_1",
      "person_2",
      "share_same_profession",
      "reasoning"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nTodd Lowe: Todd Lowe (born May 10, 1977) is an American actor.  He is best known for his role as Terry Bellefleur, a PTSD-suffering Iraq War veteran who works as a short order cook at Merlotte's Bar & Grill., on HBO's \"True Blood\" and as Zach Van Gerbig on \"Gilmore Girls\".  In 2017 he played the role of Colin Dobbs, another war veteran, in five episodes of the \"USA Network\" series \"Shooter (TV series)\", based on the 2007 film of the same name and the novel \"Point of Impact\" by Stephen Hunter\n\nSpringtown Camp: Springtown Camp was a United States military camp near Derry, in Northern Ireland, in use during World War II.  It was sited outside the western part of the city, off the Buncrana Road in an area now covered by an industrial estate.  After United States Navy had evacuated the camp at the end of the war, local people living in over-crowded terraced homes, sometimes three families living in one small house, broke into the camp and \"squatted\" in to the huts in August 1946.  The huts although without running water, electricity or any means of heating, they still provided the families with space, which was lacking in their previous homes.  After a public outcry the Londonderry Corporation who were unionist/Protestant in the majority and who only obtained power by vote gerrymandering, granted \"temporary\" rentals to the new occupants and charged rent.  This agreement was supposed to last 6 months after which the families were to be housed in proper house in Derry City.  But this never happened due to discrimination, as the residents of Springtown Camp were over 90% catholic/nationalist. The quality of the accommodation was poor, however, and over time, children grew up, married and were obliged to live with parents, resulting in over-crowding.  The conditions, in the tin huts deteriorated due to lack of repairs and became very unsafe, led to a sustained campaign for rehousing.  The Corporation resisted this campaign for years but after a \"silent\" protest march by the residents from the camp to Derry's Guildhall was televised and beamed in to many homes throughout Ireland, pressure was mounting on the Londonderry Corporation to act.They again refused to re house the people of the camp, fearing the movement of so many catholic/nationalist to different areas of Derry could jeopardise their grip on power.  However the residents protest gained so much support the Londonderry Corporation was forced to move on the rehousing of the people.  Eventually all the residents were rehoused when on the 11th October 1967 the two last families were finally housed to make way for the Springtown Industrial estate.  Springtown Camp which was to provide temperory housing for the people for a maximum of six months...was in existence for period of over twenty one years...\n\nFred Reed: Fred Reed (born 1945 in Crumpler, West Virginia) is a writer and former technology columnist for \"The Washington Times\".  He has also written for \"The American Conservative\" and LewRockwell.com.  Additionally, he has spoken at one \"American Renaissance\" conference and currently writes for \"Taki's Magazine\".  A former Marine and Vietnam War veteran, Reed is a police writer and an occasional war correspondent.  Reed writes weekly columns for the website \"Fred on Everything\".\n\nIn Harm's Way: In Harm's Way is a 1965 American epic Panavision war film produced and directed by Otto Preminger and starring John Wayne, Kirk Douglas, Patricia Neal, Tom Tryon, Paula Prentiss, Stanley Holloway, Burgess Meredith, Brandon deWilde, Jill Haworth, Dana Andrews, and Henry Fonda.\n\nThe Sandstorm: The Sandstorm is a history play written by playwright and Iraq War veteran Sean Huze.  It was originally an eleven character play (Los Angeles 2004–2005).  It later became a ten character play after revisions for the East Coast debut in Washington, D.C. (2005).  The play premiered in Los Angeles, California, in September 2004 for a limited engagement directed by Marlon Hoffman at Gardner Stages, a small 30 seat basement theater in Hollywood, California.  It received a “rave,” an overwhelmingly positive review, from the \"Los Angeles Times\" calling the play \"“a heart clutching eye witness mosaic,”\" and praised its \"“shocking force and awesome honesty”\".  Due to first-time playwright and cast member Sean Huze being an active-duty Marine on leave, he returned to his duty station at Camp Lejeune, North Carolina, and the play's brief run closed in October 2004.\n\nDana Andrews: Carver Dana Andrews (January 1, 1909 – December 17, 1992) was an American film actor and a major Hollywood star during the 1940s.  He continued acting in less prestigious roles into the 1980s.  The role for which he received the most praise, was as war veteran Fred Derry in \"The Best Years of Our Lives\" (1946).\n\nLast Stand at Saber River: Last Stand at Saber River is a 1997 American made-for-television western drama film directed by Dick Lowry and starring Tom Selleck, Suzy Amis, Haley Joel Osment, Keith Carradine, David Carradine, Tracey Needham, David Dukes and Harry Carey Jr..  Based on the 1959 novel of the same title by Elmore Leonard, the film is about a Civil War veteran who tries to put the pieces of his life back together but finds himself fighting a new battle on the frontier.  Seeking to reclaim his Arizona homestead from rebel pioneers who sympathize with the Union war effort, he joins forces with his Union adversary to make a last stand for the one thing worth fighting for, his family.  In 1997, Osment won a YoungStar Award for Best Performance by a Young Actor in a Made For TV Movie.  In 1998, the film received the Western Heritage Awards Bronze Wrangler for Television Feature Film.\n\nDoug Stanton: Doug Stanton is a journalist, lecturer, screenwriter, and author of the \"New York Times\" bestsellers In Harm’s Way and Horse Soldiers.  Horse Soldiers is the basis for a Jerry Bruckheimer-produced movie by the same name, starring Chris Hemsworth and Michael Shannon, to be released by Warner Bros. in 2018.  In Harm’s Way spent more than six months on the \"New York Times\" bestseller list and became required reading on the U.S. Navy's reading list for officers.  The unabridged audiobook edition of In Harm’s Way is the winner of the 2017 Audie Award in the History category.  Horse Soldiers was featured on the front page of the Sunday \"New York Times Book Review.\"  His third book is called The Odyssey of Echo Company and is forthcoming in September, 2017.\n\nErnest Miller: Ernest Clifford Miller (born January 14, 1964) is an American actor and former professional wrestler who worked for World Championship Wrestling (WCW) and World Wrestling Entertainment (WWE) better known by his ring name, Ernest \"The Cat\" Miller.  As an actor, he's perhaps best known for his critically praised role in the popular 2008 drama \"The Wrestler\".\n\nHard Tack and Coffee: Hard Tack and Coffee: The Unwritten Story of Army Life (1887) is a memoir by John D. Billings.  Billings was a veteran of the 10th Massachusetts Volunteer Light Artillery Battery in the American Civil War.  Originally published in 1888, \"Hard Tack and Coffee\" quickly became a best seller, and is now considered one of the most important books written by a Civil War veteran.  The book is abundantly illustrated by the pen and ink drawings of Charles Reed, also a veteran, who served as bugler in the 9th Massachusetts Battery.  Reed received the Medal of Honor for saving the life of his battery commander at Gettysburg.  \"Hard Tack and Coffee\" is not about battles, but rather about how the common Union soldiers of the Civil War lived in camp and on the march.  What would otherwise be a mundane subject is enlivened by Billings' humorous prose and Reed's superb drawings which are based on the sketches he kept in his journal during the war.\n\nQuestion: One of the actor's from Harm's way received his most praised role as a war veteran Fred Derry.  What was the name of the movie Fred Derry is from?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor who played the praised role.\"\n    },\n    \"movie_in_harm_s_way\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the movie the actor was also in, as mentioned in the question.\"\n    },\n    \"praised_role\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"character_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the character in the praised role.\"\n        },\n        \"character_description\": {\n          \"type\": \"string\",\n          \"description\": \"A description of the character's background or type.\"\n        },\n        \"movie_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the movie where the actor played the praised role.\"\n        },\n        \"movie_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The release year of the movie where the actor played the praised role.\"\n        }\n      },\n      \"required\": [\n        \"character_name\",\n        \"character_description\",\n        \"movie_name\",\n        \"movie_year\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"movie_in_harm_s_way\",\n    \"praised_role\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The name of the actor who played the praised role."
      },
      "movie_in_harm_s_way": {
        "type": "string",
        "description": "The name of the movie the actor was also in, as mentioned in the question."
      },
      "praised_role": {
        "type": "object",
        "properties": {
          "character_name": {
            "type": "string",
            "description": "The name of the character in the praised role."
          },
          "character_description": {
            "type": "string",
            "description": "A description of the character's background or type."
          },
          "movie_name": {
            "type": "string",
            "description": "The name of the movie where the actor played the praised role."
          },
          "movie_year": {
            "type": "integer",
            "description": "The release year of the movie where the actor played the praised role."
          }
        },
        "required": [
          "character_name",
          "character_description",
          "movie_name",
          "movie_year"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "actor_name",
      "movie_in_harm_s_way",
      "praised_role"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

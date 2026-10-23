{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nJohn Wayne Parr: John Wayne \"The Gunslinger\" Parr (born 25 May 1976), also known as JWP, is an Australian kickboxer and boxer, fighting out of Boonchu Gym in Gold Coast, Queensland.  He is a former 10-time World Champion and was the runner up on \"The Contender Asia\".\n\nChangpuek Kiatsongrit: Changpuek [English: Crazy Elephant] Kiatsongrit (Thai: ช้างเผือก เกียรติทรงฤทธิ์ , born October 13, 1966) is a retired Thai Muay Thai fighter.  He is credited as being one of the first Muay Thai fighters to go abroad and fight other fighters of other martial arts styles, often stronger and heavier than himself, bringing to the world an understanding of the effectiveness of Muay Thai.  Changpuek is a seven time world champion who has fought some of the world's best fighters at middleweight to heavyweight and has wins against world class fighters such as Rob Kaman (x3), Rick Roufus, Peter Smit and Tosca Petridis.  After ending his career as a professional fighter while working for Sitpholek gym in Pattaya, Thailand, he continued his employment at that gym as a Muay Thai trainer.\n\nLloyd van Dams: Lloyd \"The Tornado\" van Dams (born March 5, 1972 in Para District) is a Dutch-Surinamese super heavyweight kickboxer.  He is a former Dutch, European and World Muay Thai champion.  In 2006 Lloyd opened his own gym, Fight Club Van Dams in Utrecht, Netherlands.  He still continues to fight professionally but spends most of his time training young fighters at his gym.\n\nIvan Hippolyte: Ivan \"The Hydro\" Hippolyte (born October 7, 1964) is a Dutch-Surinamese former kickboxer World champion.  He is currently a martial arts coach at the Vos Gym in Amsterdam, Netherlands, the same gym he used to fight out of during his active career.  He is a former sparring partner and teammate of four time K-1 World champion Ernesto Hoost as well as veteran mixed martial artist Gilbert Yvel.\n\nAngela Rivera-Parr: Angela Rivera-Parr is an American born Australian female kickboxer and mixed martial artist, and wife of John Wayne Parr.\n\nTiffany (comics): Tiffany is a fictional character in Todd McFarlane's \"Spawn\" comic book series.  She was first introduced to the series in issues #44 and #45.  Tiffany, like fellow angel Angela, is a Hellspawn hunter.  Therefore, the most current Hellspawn, Al Simmons, is her primary target.  She has a long-standing rivalry with Angela, but since Angela has gone rogue, Tiffany's aim is to fill her place as the top Hellspawn slayer in Heaven's army.  In her first attempt to slay Spawn, she was over-zealous and was defeated in a grisly manner.  Although she lost the fight, she escaped with her life, since the still inexperienced Spawn did not realize that merely destroying an angel's physical body is not enough to truly kill it.  She has not appeared in the comic since.\n\nPakorn PKSaenchaimuaythaigym: Pakorn started training at the age of 9 and had his first fight a few months later, winning by decision.  His father is a Muay Thai enthusiast and trained Pakorn until he joined the Sitphateang camp.  Pakorn first camp in Bangkok was Sakyothin, moving to Jitti Gym for a year and finally joining former opponent Saenchai PKSaenchaimuaythaigym's camp at the 13 Coins resort.  Pakorn subsequently moved with Saenchai to the PK Saenchai Muay Thai Gym in Bangkok before joining Evolve MMA in October, 2016.\n\nNana's Party: \"Nana's Party\" is the fifth episode of the second series of the British dark comedy anthology television programme \"Inside No. 9\".  It was first broadcast on 23 April 2015 on BBC Two.  Written and directed by Steve Pemberton and Reece Shearsmith, the episode starred Claire Skinner as the obsessive-compulsive and aspirational Angela, who is hosting a party for the 79th birthday of her mother Maggie, played by Elsie Kelly.  Angela's husband Jim, played by Pemberton, is keen to play a prank on Pat, Angela's brother-in-law, who is a practical joker. Pat is played by Shearsmith, while Carol, a recovering alcoholic who is Pat's wife and Angela's sister, is played by Lorraine Ashbourne.  The episode also features Eve Gordon as Katie, Angela and Jim's teenage daughter, and Christopher Whitlow as a paramedic seen at the beginning and end of the episode.\n\nSamson Dutch Boy Gym: Samson Dutch Boy Gym is one of the fight names used by former professional boxer and Muaythai practitioner from Thailand, Somboon Phantasi (Thai: สมบูรณ์ พานตะสี ; born 11 July 1972 in Changhan, Roi-Et, Thailand).  His Muaythai fight name was Saenmuangnoi Lukchaopormahesak (Thai: แสนเมืองน้อย ลูกเจ้าพ่อมเหศักดิ์ ), in Muaythai, he is a famous and popular Muaythai fighter, ever lost-won with Veeraphol Sahaprom 2 times.  His other fight names were Samson Esarn, Samson Isaan, Saenmuangnoi Lukchaopormahesak, Samson Kratingdaenggym, Samson 3-K Battery, Samson Toyota-Thailand and Samson Elite Gym.\n\nGleason's Gym: Gleason's is a boxing gym located on the Brooklyn waterfront.  Since 1937, when the gym was founded in the Bronx, boxers with their eyes on Olympic glory or a shot at the title have been training at Gleason's.  Fighters who trained at the gym include Jake LaMotta, Roberto Durán, Benny \"Kid\" Paret, Paulie Malignaggi, Gerry Cooney, and Mike Tyson.  Before his first title fight against Sonny Liston, Muhammad Ali, then known as Cassius Clay, also trained at Gleason's.\n\nQuestion: Out of which gym did Angela Rivera-Parr's husband fight?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"husband_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of Angela Rivera-Parr's husband.\"\n    },\n    \"gym_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"gym_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the gym the husband fought out of.\"\n        },\n        \"gym_location\": {\n          \"type\": \"string\",\n          \"description\": \"The location of the gym.\"\n        }\n      },\n      \"required\": [\n        \"gym_name\",\n        \"gym_location\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"fighter_status\": {\n      \"type\": \"string\",\n      \"description\": \"Describes the husband's fighting status related to the gym.\"\n    }\n  },\n  \"required\": [\n    \"husband_name\",\n    \"gym_details\",\n    \"fighter_status\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "husband_name": {
        "type": "string",
        "description": "The name of Angela Rivera-Parr's husband."
      },
      "gym_details": {
        "type": "object",
        "properties": {
          "gym_name": {
            "type": "string",
            "description": "The name of the gym the husband fought out of."
          },
          "gym_location": {
            "type": "string",
            "description": "The location of the gym."
          }
        },
        "required": [
          "gym_name",
          "gym_location"
        ],
        "additionalProperties": false
      },
      "fighter_status": {
        "type": "string",
        "description": "Describes the husband's fighting status related to the gym."
      }
    },
    "required": [
      "husband_name",
      "gym_details",
      "fighter_status"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

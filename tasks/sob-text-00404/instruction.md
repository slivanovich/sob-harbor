{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCulverden Stadium: Culverden Stadium is an association football stadium in Royal Tunbridge Wells, Kent, England.  It is the home ground of Tunbridge Wells F.C.  It has a capacity of 3,750, with 250 seats.  It is located in Culverden Park Road, Tunbridge Wells.\n\nLahore Lions: Lahore Lions (Urdu: لاہور لائنز‎ , abbreviated as LIO) is a Pakistani franchise cricket team representing the city Lahore and is one of the 19 domestic teams.  The team was established by Lahore Regional Cricket Association in 2004/05 in its home ground Lahore City Cricket Association Ground.  Domestically, the team plays in the Haier T20 Cup.  The team won its first title in 2010 where they defeated Karachi Dolphins by 37 runs in their home ground Gaddafi Stadium.\n\nKongu riders cricket club: The Kongu Riders Cricket Club (abbreviated as KRCC), also referred in other names as Kongu Cricket Club or Arumuga Koundanur Cricket Club, is a regional club cricket team based in Coimbatore, India The primary home ground of Kongu Riders Cricket Club is Arumuga Koundanur MR Garden Ground- Krishna Nagar.  They also have one more home ground in Arumuga Koundanur Teachers Colony Ground, situated about 1 km from the old ground.\n\nAdelaide Raiders SC: Adelaide Croatia Raiders is a soccer club in Adelaide, South Australia, that plays in the National Premier Leagues South Australia.  Its home ground is the Croatian Sports Centre in Gepps Cross, a northern suburb of Adelaide.  It is a Croatian Australian-backed club and is also known by the name \"Adelaide Croatia\".\n\nHughenden, Glasgow: Hughenden is a multi-sports venue in the Hyndland area of Glasgow, Scotland.  It has been the home since 1924 of Hillhead Sports Club, a private members' club catering for cricket, rugby union and tennis.  Hughenden is best known as a rugby venue and is the home ground of Hillhead Jordanhill RFC.  It was also used as the home ground of the professional Glasgow Rugby team from 1996 to 2005 and again from 2006 to 2007.  The main rugby ground has a capacity of 6,000.\n\nScott Tunbridge: Scott Tunbridge (born 26 June 1982 in Adelaide, Australia) is a Australian footballer who plays for Adelaide Raiders.\n\nPatna Pirates: Patna Pirates (PTP) is a kabaddi team based in Patna, Bihar that plays in the Pro Kabaddi League.  The team is led by Pardeep Narwal and coached by Ram Mehar Singh.  They are champions of season 3 and season 4.  They became the first team to retain their title after defeating Jaipur Pink Panthers in season 4 final.  The team is owned by Rajesh V. Shah and their home ground is Harivansh Tana Bhagat Indoor Stadium, Ranchi for this year.  In previous year it was Patliputra Complex,Patna and from next session again patna will be the home ground.\n\nUllevaal Stadion: Ullevaal Stadion (] ) is an all-seater football stadium located in Oslo, Norway.  It is the home ground of the Norway national football team, and the site of the Norwegian Cup Final.  From its opening in 1926 to 2009 it was the home ground of FK Lyn and from 1999 to 2017 was a home ground of Vålerenga IF.  With a capacity of approximately 28,000, it is the largest football stadium in Norway.  The national stadium is fully owned by the Football Association of Norway (NFF).\n\nButts Park Arena: Butts Park Arena is a multi-use sports stadium in Spon End, Coventry, England.  Its main use is as a rugby stadium (both Union and League).  It is the home ground for Coventry RFC (since its opening ) and Coventry Bears, (who moved there for the start of the 2004–05 season).  It was formerly the home ground of the Coventry Jets, an American football team.  The stadium will become the new home of Coventry United, a non league football Club founded in 2013, the football club's men's and the women's sides will play home matches at the ground from the 2017–18 season.\n\nArbab Niaz Stadium: Arbab Niaz Stadium is a Test cricket ground in Peshawar, Khyber Pukhtunkhwa, Pakistan.  It is the home ground for Peshawar Zalmi.  It replaced the Peshawar Club Ground as the home ground for the Peshawar cricket team in 1985.  The ground has hosted 17 ODIs since 1984 (most recently on 6th February 2006, between Pakistan vs India where Pakistan won by 18 runs by Duckworth–Lewis method), and seven Test matches since 1995, most recently in 2003.  The ground has a seating capacity of 20,000.\n\nQuestion: Where is the home ground of the team that Scott Tunbridge plays on?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"player_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the player.\"\n    },\n    \"team\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the team the player plays for.\"\n        },\n        \"sport\": {\n          \"type\": \"string\",\n          \"description\": \"The sport the team plays.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"sport\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"home_ground\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the team's home ground.\"\n        },\n        \"location\": {\n          \"type\": \"string\",\n          \"description\": \"The general location of the home ground.\"\n        }\n      },\n      \"required\": [\n        \"name\",\n        \"location\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"player_name\",\n    \"team\",\n    \"home_ground\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "player_name": {
        "type": "string",
        "description": "The name of the player."
      },
      "team": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the team the player plays for."
          },
          "sport": {
            "type": "string",
            "description": "The sport the team plays."
          }
        },
        "required": [
          "name",
          "sport"
        ],
        "additionalProperties": false
      },
      "home_ground": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the team's home ground."
          },
          "location": {
            "type": "string",
            "description": "The general location of the home ground."
          }
        },
        "required": [
          "name",
          "location"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "player_name",
      "team",
      "home_ground"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

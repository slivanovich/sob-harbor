{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBill Lawrence (TV producer): William Van Duzer \"Bill\" Lawrence IV (born December 26, 1968) is an American screenwriter, producer, and director.  He is best known as the creator of the series \"Scrubs\", co-creator of \"Cougar Town\" and co-creator of \"Spin City\".  He was also co-creator of the short-lived animated series \"Clone High\", in which he voiced the leader of the shadowy figures, and is the co-creator of \"Ground Floor\", which ran on TBS.  He has written for many other shows including \"Friends\", \"The Nanny\", and \"Boy Meets World\".\n\nPeter F. Paul: Peter Franklin Paul (born September 2, 1948) is a former lawyer and entrepreneur who was convicted for conspiracy and drug dealing, and later for securities fraud in connection with his business dealings with \"Spider-Man\" co-creator Stan Lee.  He has repeatedly brought suit against Hillary Clinton, accusing her of lying about donations he solicited on behalf of her 2000 senatorial campaign.\n\nJerry Robinson: Sherrill David Robinson (January 1, 1922 – December 7, 2011), known as Jerry Robinson, was an American comic book artist known for his work on DC Comics' Batman line of comics during the 1940s.  He is best known as the co-creator of Robin and the Joker and for his work on behalf of creators' rights.\n\nInteractions (The Spectacular Spider-Man): \"Interactions\" is the second episode of the animated television series \"The Spectacular Spider-Man,\" based on the comic book character Spider-Man created by Stan Lee and Steve Ditko.  The episode sees Spider-Man confronting the supervillain Electro, whose body was corrupted with electricity after a freak lab accident.\n\nStan Lee: Stan Lee (born Stanley Martin Lieber , December 28, 1922) is an American comic-book writer, editor, film executive producer, and publisher.  He was formerly editor-in-chief of Marvel Comics, and later its publisher and chairman before leaving the company to become its chairman emeritus, as well as a member of the editorial board.\n\nGreg Weisman: Greg Weisman (born September 28, 1963) is an American novelist and comic book and animation writer and producer, best known as the co-creator and producer of \"Young Justice\", the (uncredited) co-creator of \"Gargoyles\", the Supervising Producer of \"The Spectacular Spider-Man\".  In addition, Weisman wrote the script for \"\", an animated short feature that is included on the DVD for the film, \"\".  His first novel, \"Rain of the Ghosts\" was released on December 3, 2013.  Its sequel, \"Spirits of Ash and Foam\" was released on July 8, 2014.  Weisman was executive producer on the \"Star Wars Rebels\" animated series, alongside Dave Filoni and Simon Kinberg, but left the show after season one had been produced.  In 2015, Weisman launched a KickStarter campaign to crowdfund $43,000 for a full-cast unabridged AudioPlay based on \"Rain of the Ghosts\".  The project reached 100% of funding in less than a month, raising $54,022 (more 25% than its intended goal) backed by 512 pledges, and it stands as the most funded Young Adult project on KickStarter.\n\nRino Romano: Rino Romano (born December 1, 1969) is a Canadian voice actor who has voiced Batman in the animated TV series \"The Batman\", Spider-Man in the animated TV series \"Spider-Man Unlimited\", Eduardo Rivera in \"Extreme Ghostbusters\", Luis Sera in \"Resident Evil 4\", Scorp in the \"Skylanders\" franchise\" and the original Tuxedo Mask in the 90's English dub of the anime series \"Sailor Moon\".\n\nJeff &quot;Swampy&quot; Marsh: Jeff \"Swampy\" Marsh (born December 9, 1960) is an American animator, writer, director, producer, and voice actor associated with several animated television series, most notably as the co-creator, executive producer, and voice of Major Monogram of Disney's animated series \"Phineas and Ferb\".  Marsh was born in Santa Monica, California, where he grew up with a heavily blended family dynamic.  Marsh has been and continues to be a driving force behind several animation projects, working for over six seasons on the animated television series \"The Simpsons\".  Marsh continued to work on other animated television series, including \"King of the Hill\" and \"Rocko's Modern Life,\" before moving to England in 1996.\n\nThe Story of a Great Schoolmaster: The Story of a Great Schoolmaster is a 1924 biography of Frederick William Sanderson (1857-1922) by H. G. Wells.  It is the only biography Wells wrote.  Sanderson was a personal friend, having met Wells in 1914 when his sons George Philip ('Gip'), born in 1901, and Frank Richard, born in 1903, became pupils at Oundle School, of which Sanderson was headmaster from 1892 to 1922.  After Sanderson died while giving a lecture at University College London at which he was introduced by Wells, the famous author agreed to help produce a biography to raise money for the school.  But in December 1922, after disagreements emerged with Sanderson's widow about his approach to the subject, Wells withdrew from the official biography (published in 1923 as \"Sanderson of Oundle\"; Wells wrote much of the text but the volume was published without listing an author) and published his own work separately.\n\nSteve Ditko: Stephen J. Ditko ( ; born November 2, 1927) is an American comics artist and writer best known as the artist and co-creator, with Stan Lee, of the Marvel Comics superheroes Spider-Man and Doctor Strange.\n\nQuestion: Which co-creator of spider-man was born in December of 1922?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the individual.\"\n    },\n    \"role\": {\n      \"type\": \"string\",\n      \"description\": \"The role of the individual related to Spider-Man.\"\n    },\n    \"birth_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"month\": {\n          \"type\": \"string\",\n          \"description\": \"The month of birth.\"\n        },\n        \"day\": {\n          \"type\": \"integer\",\n          \"description\": \"The day of birth.\"\n        },\n        \"year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year of birth.\"\n        }\n      },\n      \"required\": [\n        \"month\",\n        \"day\",\n        \"year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"final_answer_person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the co-creator of Spider-Man who was born in December of 1922.\"\n    }\n  },\n  \"required\": [\n    \"person_name\",\n    \"role\",\n    \"birth_details\",\n    \"final_answer_person_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_name": {
        "type": "string",
        "description": "The name of the individual."
      },
      "role": {
        "type": "string",
        "description": "The role of the individual related to Spider-Man."
      },
      "birth_details": {
        "type": "object",
        "properties": {
          "month": {
            "type": "string",
            "description": "The month of birth."
          },
          "day": {
            "type": "integer",
            "description": "The day of birth."
          },
          "year": {
            "type": "integer",
            "description": "The year of birth."
          }
        },
        "required": [
          "month",
          "day",
          "year"
        ],
        "additionalProperties": false
      },
      "final_answer_person_name": {
        "type": "string",
        "description": "The name of the co-creator of Spider-Man who was born in December of 1922."
      }
    },
    "required": [
      "person_name",
      "role",
      "birth_details",
      "final_answer_person_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

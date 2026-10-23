{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nPowerstrip Studio: Powerstrip Studio, based in Los Angeles, California, is a private company established in 2000.  It specializes in conceptual design for hotels, restaurants, lounges, spas, outdoor living areas and theatres throughout the United States.  It had created such hotels as Ivy Hotel, 39 Degrees Aspen, The Bridge, W Los Angeles, W New Orleans, Blowfish, Hotel Derek, Westin Governor Morris, and Quarter Kitchen.  Powerstrip Studio has worked with Jim Jarmusch, Ridley Scott, Kevin Costner, Wayne Wang, and Paul T. Anderson with projects that have been acknowledged with Emmy nominations for Outstanding Art Direction and an Academy Award nomination for Best Art Direction.  Powerstrip Studio has been featured in such editorials as Space, Los Angeles Confidential, Cool Hotels, Fortune Magazine, Gold Key Awards, Hip Hotels Thames and Hudson, Interior Design, Business Traveler, Hotels Magazine, Metropolitan, Architectural Record, Ski Hotels Te Neues, Wallpaper, 944 San Diego, Pipedreams, Lucky Magazine, and Hotels: Designer & Design.\n\nDavid Snyder: David L. Snyder (born September 22, 1944) is a film and television production designer.  He has worked as an art director, producer, and assistant director on films including \"Blade Runner\", \"Bill & Ted's Bogus Journey\", \"The Whole Nine Yards\", and the television programs \"Buck Rogers in the 25th Century\" and \"Battlestar Galactica\".  He was nominated for Academy Award for Best Art Direction for his work on \"Blade Runner\" at the 55th Academy Awards.  The film won the BAFTA for Production Design in 1983.\n\nAcademy Award for Best Production Design: The Academy Award for Best Production Design recognizes achievement for art direction in film.  The category's original name was Best Art Direction, but was changed to its current name in 2012 for the 85th Academy Awards.  This change resulted from the Art Director's branch of the Academy of Motion Picture Arts and Sciences (AMPAS) being renamed the Designer's branch.  Since 1947, the award is shared with the set decorator(s).  It is awarded to the best interior design in a film.\n\nSo Matsuyama: Takashi Matsuyama (松山　崇 , Matsuyama Takashi (Sō), September 22, 1908 - July 14, 1977 ) , a.k.a. Sō Matsuda and Sō Matsuyama, was a Japanese production designer and art director.  He was nominated twice for the Academy Award for Best Art Direction: the first time for his work in \"Rashomon\" (1950), and the second time for his work in \"Seven Samurai\" (1954).  In 1950 he won the award for Best Art Direction at the Mainichi Film Concours for Stray Dog, directed by Akira Kurosawa.\n\nPatrice Vermette: Patrice Vermette (Born 1970) is a Canadian production designer/art director who has won three awards for his work on \"C.R.A.Z.Y.\", the Genie Award for Best Achievement in Art Direction/Production Design and a Jutra Award for Best Art Direction.  His other work includes \"1981\", \"La Cité\", \"Café de Flore\" and \"The Young Victoria\".  He was nominated for an Academy Award in the category Best Art Direction for his work in the film \"The Young Victoria\".  He was nominated again in the category Best Production Design for his work in the film \"Arrival\" at the 89th Academy Awards.\n\nGianni Quaranta: Gianni Quaranta (born August 30, 1943) is an Italian production designer and art director.  He was nominated for the Academy Award for Best Art Direction and won the BAFTA Award for Best Production Design and the Nastro d'Argento for Best Production Design for \"La Traviata\" (1983).  He won the Oscar for Best Art Direction for the film \"A Room with a View\".\n\nM. Prabhaharan: M. Prabhaharan (born 6 July 1966 at Dindigul) had his school education in Theni, Tamil Nadu and completed his degree course in Fine Arts at Government College of Fine Arts, Chennai.  He had a brief stint as an illustrator in Special Effects Venky's office in 1990.  He worked as an assistant Art Director under the noted Art Director, Mr. Ashok Kumar in Tamil and Telugu film industry for a few years.  He got a big break in 1995 when he was offered to do art direction for R. Parthiepan's movie \"Pulla Kuttikaran\", for which he achieved the award for Best Art Direction from Tamil Nadu Govt.  He did art direction for many Tamil movies,to name a few, \"Ullathai Allitha\", \"Thulladha Manamum Thullum\", \"Thirupaachi\", \"Anbe Sivam\", \"Virumaandi\", \"Dasavathaaram\",\"Majaa\", \"Vishwa Thulasi\",\"Tenaliraman\" and \"Bairavaa\"\n\nDonald Graham Burt: Donald Graham Burt is a film production designer.  He has worked on multiple films including The Joy Luck Club, Dangerous Minds, and Donnie Brasco, as well as with David Fincher on Zodiac in 2007.  In 2008 he designed the sets for The Curious Case of Benjamin Button which won an Academy Award for Best Art Direction in 2009, an Art Directors Guild Award for Best Achievement in Art Direction, and a BAFTA Film Award for Best Production Design, along with a nomination for a Satellite Award for Best Art Direction & Production Design.\n\nBrian Ackland-Snow: Brian Ackland-Snow (31 March 1940 – 30 March 2013) was an English production designer.  He won an Academy Award in the category Best Art Direction for the film \"A Room with a View\".  He also won an Emmy for best art direction for a miniseries or special in 1995 for \"Scarlett\" on CBS.\n\nBlade Runner: Blade Runner is a 1982 American neo-noir science fiction film directed by Ridley Scott and starring Harrison Ford, Rutger Hauer, Sean Young, and Edward James Olmos.  The script was written by Hampton Fancher and David Peoples, and is a loose adaptation of the 1968 novel \"Do Androids Dream of Electric Sheep? \" by Philip K. Dick.  Set in a dystopian Los Angeles in 2019, the story depicts a future in which bioengineered androids known as replicants are manufactured by the powerful Tyrell Corporation to work on off-world colonies.  When a renegade group of replicants led by Roy Batty (Hauer) escape back to Earth, burnt-out LA cop Rick Deckard (Ford) reluctantly accepts one last assignment to hunt them down.  During his investigations, Deckard meets Rachael (Young), an advanced replicant who causes him to question his mission.\n\nQuestion: What kind of film is the one that got David Snyder a nomination for Academy Award for Best Art Direction?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"award_nomination\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"award_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the award.\"\n        },\n        \"category\": {\n          \"type\": \"string\",\n          \"description\": \"The category of the award nomination.\"\n        }\n      },\n      \"required\": [\n        \"award_name\",\n        \"category\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"film_genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the film.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"award_nomination\",\n    \"film_genre\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "award_nomination": {
        "type": "object",
        "properties": {
          "award_name": {
            "type": "string",
            "description": "The name of the award."
          },
          "category": {
            "type": "string",
            "description": "The category of the award nomination."
          }
        },
        "required": [
          "award_name",
          "category"
        ],
        "additionalProperties": false
      },
      "film_genre": {
        "type": "string",
        "description": "The genre of the film."
      }
    },
    "required": [
      "film_title",
      "award_nomination",
      "film_genre"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

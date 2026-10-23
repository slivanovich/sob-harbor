{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nKeisha Castle-Hughes: Keisha Castle-Hughes (born 24 March 1990) is a New Zealand actress who rose to prominence for playing Paikea \"Pai\" Apirana in the film \"Whale Rider\".  The film was nominated for many awards, including an Academy Award for Best Actress (at the time the youngest person nominated in the Best Actress category) and an award at the Broadcast Film Critics Association Awards for Best Young Actor/Actress, which she won in 2004.\n\nCritics' Choice Movie Awards: The Critics' Choice Movie Awards (formerly known as the Broadcast Film Critics Association Award) is an awards show presented annually by the Broadcast Film Critics Association (BFCA) to honor the finest in cinematic achievement.  Written ballots are submitted during a week-long nominating period, and the resulting nominees are announced in December.  The winners chosen by subsequent voting are revealed at the annual Critics' Choice Movie Awards ceremony in January.  Additional, special awards are given out at the discretion of the BFCA Board of Directors.\n\nThe Silent House (2010 film): The Silent House (Spanish: \"La Casa Muda\" ) is a 2010 Uruguayan horror film directed by Gustavo Hernández.  The film is supposedly inspired by real events that took place in the 1940s, but no information can be found to authenticate the aforementioned claims.  A small-budget film originally intended for local audiences, it has achieved success in several important international film festivals such as the Cannes Film Festival (where it was shown at Director's Fortnight).  At the 2011 Sundance Film Festival, Chris Kentis and Laura Lau presented an English-language remake titled \"Silent House\", starring Elizabeth Olsen.\n\nList of roles and awards of Mélanie Laurent: Mélanie Laurent is a French actress, singer, screenwriter and director.  She initially rose to prominence for her performance in the 2006 French drama film \"Don't Worry, I'm Fine\" for which she later won the César Award for Most Promising Actress and the Prix Romy Schneider.  Laurent further became known to international audiences for her starring role as Shosanna Dreyfus in Quentin Tarantino's \"Inglourious Basterds\" (2009), for which she won the Online Film Critics Society and the Austin Film Critics Association Award for Best Actress.  She went on star in commercially successful Hollywood films including, the comedy drama \"Beginners\" (2011), and the caper film \"Now You See Me\" (2013), with the former earning her a nomination at the San Diego Film Critics Society Award for Best Supporting Actress.\n\nCritics' Choice Movie Award for Best Actress: The Critics' Choice Movie Award for Best Actress is an award given out at the annual Critics' Choice Movie Awards.  The awards are presented by the Broadcast Film Critics Association (BFCA) and was first presented in 1995.  There were no official nominees announced until 2001.  There have been two ties in this category (2008, 2009) and there are currently six nominees annually.  This is the main best actress award for leading dramatic performances.  The Critics' Choice also have other categories for lead actress; Best Actress in a Comedy and Best Actress in an Action Movie.  For supporting actress, see Critics' Choice Movie Award for Best Supporting Actress.\n\nAnamaria Marinca: Anamaria Marinca (born 1 April 1978) is a Romanian actress.  She made her screen debut with the Channel 4 film \"Sex Traffic\", for which she won the British Academy Television Award for Best Actress.  Marinca is also known for her performance in \"4 Months, 3 Weeks and 2 Days\", earning several awards for her performance, and was nominated for the European Film Award for Best Actress, London Film Critics Circle Award for Actress of the Year, Los Angeles Film Critics Association Award for Best Actress and National Society of Film Critics Award for Best Actress.  In 2008, at the 58th Berlin International Film Festival, she was presented the Shooting Stars Award by the European Film Promotion.\n\nElizabeth Olsen: Elizabeth Chase Olsen (born February 16, 1989) is an American actress.  Her breakthrough came in 2011 when she starred in the independent thriller drama \"Martha Marcy May Marlene\", for which she was nominated for the Broadcast Film Critics Association Award for Best Actress and Independent Spirit Award for Best Female Lead, among other awards.  She subsequently starred in the films \"Silent House\" (2011), \"Liberal Arts\" (2012), \"Godzilla\" (2014), \"I Saw the Light\" (2015), and \"Wind River\" (2017).  Since 2014, she has portrayed Wanda Maximoff / Scarlet Witch in the Marvel Cinematic Universe.\n\nList of accolades received by Titanic: \"Titanic\" began its awards sweep starting with the Golden Globes, winning four, namely Best Motion Picture – Drama, Best Director, Best Original Score, and Best Original Song.  Kate Winslet and Gloria Stuart were also nominees.  It won the ACE \"Eddie\" Award, ASC Award, Art Directors Guild Award, Cinema Audio Society Awards, Screen Actors Guild Award (Best Supporting Actress for Gloria Stuart), The Directors Guild of America Award, and Broadcast Film Critics Association Award (Best Director for James Cameron), and The Producer Guild of America Award.  It was also nominated for ten BAFTA awards, including Best Film and Best Director; it failed to win any.\n\nRussell Crowe: Russell Ira Crowe (born 7 April 1964) is an actor, film producer and musician.  Although a New Zealand citizen, he has lived most of his life in Australia.  He came to international attention for his role as the Roman General Maximus Decimus Meridius in the 2000 historical epic film \"Gladiator\", directed by Ridley Scott, for which Crowe won an Academy Award for Best Actor, a Broadcast Film Critics Association Award for Best Actor, an Empire Award for Best Actor and a London Film Critics Circle Award for Best Actor and 10 further nominations for best actor.\n\nBeyond Darkness: Beyond Darkness (Italian: La Casa 5, also known as Horror House II) is a 1990 Italian horror film directed by Claudio Fragasso.  It was written by Fragasso and screenwriter and wife Rossella Drudi and produced by Joe D'Amato.  The La Casa films (III, IV and V) in Italy were all marketed as sequels of a sort to the American films \"The Evil Dead\" and \"Evil Dead II\", which were released in Italy as \"La Casa\" and \"La Casa 2\" respectively.\n\nQuestion: The film, The Silent House (Spanish: \"La Casa Muda\"), starred which actress who was also nominated for the Broadcast Film Critics Association Award for Best Actress?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actress_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actress who starred in the film.\"\n    },\n    \"film_starred_in\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film the actress starred in.\"\n    },\n    \"award_nomination\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"award_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the award for which the actress was nominated.\"\n        },\n        \"award_category\": {\n          \"type\": \"string\",\n          \"description\": \"The specific category of the award nomination.\"\n        },\n        \"nominated_for_film\": {\n          \"type\": \"string\",\n          \"description\": \"The film for which the actress received the nomination.\"\n        }\n      },\n      \"required\": [\n        \"award_name\",\n        \"award_category\",\n        \"nominated_for_film\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"actress_name\",\n    \"film_starred_in\",\n    \"award_nomination\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actress_name": {
        "type": "string",
        "description": "The name of the actress who starred in the film."
      },
      "film_starred_in": {
        "type": "string",
        "description": "The title of the film the actress starred in."
      },
      "award_nomination": {
        "type": "object",
        "properties": {
          "award_name": {
            "type": "string",
            "description": "The name of the award for which the actress was nominated."
          },
          "award_category": {
            "type": "string",
            "description": "The specific category of the award nomination."
          },
          "nominated_for_film": {
            "type": "string",
            "description": "The film for which the actress received the nomination."
          }
        },
        "required": [
          "award_name",
          "award_category",
          "nominated_for_film"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "actress_name",
      "film_starred_in",
      "award_nomination"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

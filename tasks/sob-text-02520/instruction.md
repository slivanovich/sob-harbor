{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nSecrets of the Furious Five: Secrets of the Furious Five (also known as Kung Fu Panda: Secrets of the Furious Five) is an American animated short produced by DreamWorks Animation, which serves as a semi-sequel or spin-off to the animated feature film \"Kung Fu Panda\" and appears on a companion disc of the original film's deluxe DVD release.  It was later broadcast on NBC on February 26, 2009 and is now available as a separate DVD as of March 24, 2009.\n\nAnnie Award for Writing in a Feature Production: The Annie Award for Writing in a Feature Production (or Annie Award for Writing in an Animated Feature Production) is an Annie Award awarded annually, except in 1997, to the best animated feature film and introduced in 1996.  It reward screenwriting for animated feature films.\n\nUdedh Bun: Udedh Bun (English title: Unravel) is award winning short Bhojpuri film released in 2008 directed by Siddharth Sinha.  The 21-minute diploma film by Siddharth Sinha, an Film and Television Institute of India (FTII), Pune graduate, was selected for world premiere at the Berlin International Film Festival, where it won the Silver Bear for Best Short Film at the 2008 Berlin International Film Festival, first ever such award in the history of Bhojpuri cinema.  Later it won the National Film Award for Best Short fiction Film.\n\nAnnie Award for Best Animated Video Game: The Annie Award for Best Animated Video Game is awarded annually by ASIFA-Hollywood, a non-profit organization that honors contributions to animation, to one animated video game each year.  The award is one of the Annie Awards, which are given to contributions to animation, including producers, directors, and voice actors.  The Annie Awards were created in 1972 by June Foray to honor individual lifetime contributions to animation.  In 1992, the scope of the awards was expanded to honor animation as a whole; the Annie Award for Best Animated Feature was created as a result of this move, and subsequent awards have been created to recognize different contributions to animation.  The Annie Award for Best Animated Video Game was created in 2005, and has been awarded yearly since except in 2009.  To be eligible for the award, the game must have been released in the year before the next Annie Awards ceremony, and the developers of the game must send a five-minute DVD that shows the gameplay and graphics of the game to a committee appointed by the Board of Directors of ASIFA-Hollywood.\n\nAnnie Award for Directing in a Feature Production: The Annie Award for Directing in a Feature Production (or Annie Award for Directing in an Animated Feature Production) is an Annie Award, awarded annually to the best animated feature film and introduced in 1996.  It reward directing for animated feature films.  The recipients are directors as well as co-directors.\n\nAnnie Award for Best Animated Short Subject: The Annie Award for Best Animated Short Subject is an Annie Award given annually to the best animated short film.  It was introduced in 1995.  In 1998, the award was renamed to Outstanding Achievement in an Animated Short Subject, and renamed again to Outstanding Individual Achievement in Animated Short Subject in 1999, but went back to its second title in 2000.  In 2005, it was again reverted to its original title, and has remained so ever since.\n\nAnnie Award for Music in a Feature Production: The Annie Award for Music in a Feature Production (or Annie Award for Music in an Animated Feature Production) is an Annie Award given annually to the best music in an animated feature film, theatrical or direct-to-video.  It began in 1997 as the \"Annie Award for Best Individual Achievement: Music in a Feature/Home Video Production\".  Throughout the following years, the title was renamed \"Outstanding Individual Achievement for Music in an Animated Feature Production\", \"Outstanding Individual Achievement for Music Score in an Animated Feature Production\", and \"Outstanding Music in an Animated Feature Production\" before changing to its current title in 2005.  It was retitled \"Best Music in an Animated Feature Production\" in 2006 for three years before being reverted to \"Music in an Animated Feature Production\" in 2009.\n\nPierre Perifel: Pierre Perifel is a French animator, best known for his character work at DreamWorks Animation and for his award-winning student film \"Le Building\".  He joined DreamWorks in 2008, after working on 2D animated films in France.  The following year, Perifel won an Annie Award for the short film \"Secrets of the Furious Five\".  He received subsequent nominations for \"Kung Fu Panda 2\" and \"Rise of the Guardians\".\n\nLe Building: Le Building is a 2005 French animated short film directed by a team of final year students at Gobelins, l'École de l'image.  The story depicts a series of slapstick accidents that cause destruction to a three-story apartment complex.  \"Le Building\"'s team of five directors is composed of Pierre Perifel and Olivier Staphylas, both of whom went on to become Annie Award-recognized animators at DreamWorks, Marco Nguyen and Xavier Ramonède, who have continued their careers with animation credits on various high-profile French productions, and Rémi Zaarour, who has since become a comic book artist, published under the pseudonym Pozla.\n\nAnnie Award for Best Animated Feature: The Annie Award for Best Animated Feature is an Annie Award introduced in 1992, awarded annually to the best animated feature film.  In 1998 the award was renamed Outstanding Achievement in an Animated Theatrical Feature, only to revert to its original title again in 2001.  Since the inception of Best Animated Feature at the Academy Awards in 2001, the Annie Award winner has matched up every year except for 2006, 2008, 2010, 2012, and 2014.\n\nQuestion: Question:What station did Pierre Perifel's Annie award winning short broadcast on?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"award_recipient_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person who received the Annie Award.\"\n    },\n    \"awarded_film_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the short film that won the Annie Award.\"\n        },\n        \"type\": {\n          \"type\": \"string\",\n          \"description\": \"The type of film, e.g., 'short film'.\"\n        },\n        \"award_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the Annie Award was won for the film.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"type\",\n        \"award_year\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"broadcast_information\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"station_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the television station that broadcast the film.\"\n        },\n        \"broadcast_date\": {\n          \"type\": \"string\",\n          \"description\": \"The date the film was broadcast.\"\n        }\n      },\n      \"required\": [\n        \"station_name\",\n        \"broadcast_date\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"award_recipient_name\",\n    \"awarded_film_details\",\n    \"broadcast_information\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "award_recipient_name": {
        "type": "string",
        "description": "The name of the person who received the Annie Award."
      },
      "awarded_film_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the short film that won the Annie Award."
          },
          "type": {
            "type": "string",
            "description": "The type of film, e.g., 'short film'."
          },
          "award_year": {
            "type": "integer",
            "description": "The year the Annie Award was won for the film."
          }
        },
        "required": [
          "title",
          "type",
          "award_year"
        ],
        "additionalProperties": false
      },
      "broadcast_information": {
        "type": "object",
        "properties": {
          "station_name": {
            "type": "string",
            "description": "The name of the television station that broadcast the film."
          },
          "broadcast_date": {
            "type": "string",
            "description": "The date the film was broadcast."
          }
        },
        "required": [
          "station_name",
          "broadcast_date"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "award_recipient_name",
      "awarded_film_details",
      "broadcast_information"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

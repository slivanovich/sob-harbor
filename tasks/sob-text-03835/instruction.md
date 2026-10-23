{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAll About Steve: All About Steve is a 2009 American comedy film directed by Phil Traill that stars Sandra Bullock, Thomas Haden Church, and Bradley Cooper as the eponymous Steve.  The film is the winner of two Golden Raspberry Awards and has a 7% approval rating at Rotten Tomatoes.\n\nHeaven Is for Real (film): Heaven Is for Real is a 2014 American Christian drama film directed by Randall Wallace and written by Wallace and Christopher Parker, based on Pastor Todd Burpo and Lynn Vincent's 2010 book of the same name.  The film stars Greg Kinnear, Kelly Reilly, Margo Martindale, Jacob Vargas, Connor Corum, and Thomas Haden Church.  The soundtrack of the film contains Darlene Zschech's song \"Heaven in Me\".  The film was released on April 16, 2014.\n\nThomas Haden Church: Thomas Haden Church (born Thomas Richard McMillen; June 17, 1960) is an American actor, director, and writer.  After co-starring in the 1990s sitcom \"Wings\", Church became known for his film roles, including his Academy Award-nominated performance in \"Sideways\" and his role as the Sandman in \"Spider-Man 3\".  He also made his directorial debut with \"Rolling Kansas\".\n\nRolling Kansas: Rolling Kansas is a 2003 independent film directed and co-written by Oscar-nominated actor Thomas Haden Church.\n\nMax (2015 film): Max is a 2015 American adventure drama film directed by Boaz Yakin, and co-written with Sheldon Lettich.  The film stars Josh Wiggins, Mia Xitlali, Dejon LaQuake, Thomas Haden Church, Robbie Amell, Lauren Graham, Luke Kleintank, and Jay Hernandez.  The film was released by Warner Bros. on June 26, 2015.\n\nKiller Joe (film): Killer Joe is a 2011 American Southern Gothic black comedy crime film directed by William Friedkin.  The screenplay by Tracy Letts is based on his 1993 play of the same name.  The film stars Matthew McConaughey in the title role, Emile Hirsch, Juno Temple, Gina Gershon, and Thomas Haden Church.  Friedkin and Letts had similarly collaborated on the 2006 film \"Bug\".\n\nSideways: Sideways is a 2004 American independent black comedy drama film directed by Alexander Payne and written by Jim Taylor and Payne.  A film adaptation of Rex Pickett's novel of the same name, \"Sideways\" follows two men in their forties, Miles Raymond (Paul Giamatti), a depressed teacher and unsuccessful writer and Jack Cole (Thomas Haden Church), a past-his-prime actor, who take a week-long road trip to Santa Barbara County wine country to celebrate Jack's upcoming wedding.  Sandra Oh and Virginia Madsen also star.\n\nGeorge of the Jungle 2: George of the Jungle 2 is the 2003 direct-to-video sequel of the 1997 Disney film \"George of the Jungle\".  It was directed by David Grossman, written by Jordan Moffet, and stars Thomas Haden Church, Julie Benz, Christina Pickles, Angus T. Jones, Michael Clarke Duncan, John Cleese, and introducing Christopher Showerman as \"George\".  The movie focuses on George trying to save Ape Mountain from his evil nemesis Lyle (Thomas Haden Church).  The sequel was widely panned.\n\nSpider-Man 3: Spider-Man 3 is a 2007 American superhero film based on the fictional Marvel Comics comic book series \"The Amazing Spider-Man\".  It was directed by Sam Raimi from a screenplay by Raimi, Ivan Raimi and Alvin Sargent.  It is the final film in Raimi's original \"Spider-Man\" film trilogy, following \"Spider-Man\" (2002) and \"Spider-Man 2\" (2004).  The film stars Tobey Maguire, Kirsten Dunst, James Franco, Thomas Haden Church, Topher Grace, Bryce Dallas Howard, Rosemary Harris, J. K. Simmons, James Cromwell, and Cliff Robertson in his final acting appearance before his death in 2011.  Following the events of \"Spider-Man 2\", Peter Parker has become a cultural phenomenon as Spider-Man, while Mary Jane \"M.J.\" Watson continues her Broadway career.  Harry Osborn still seeks vengeance for his father's death, and an escaped Flint Marko falls into a particle accelerator and is transformed into a shape-shifting sand manipulator.  An extraterrestrial symbiote crashes to Earth and bonds with Peter, influencing his behavior for the worse.\n\nSandman (Marvel Comics): Sandman (William Baker a.k.a. Flint Marko) is a fictional supervillain appearing in American comic books published by Marvel Comics.  A shapeshifter endowed through an accident with the ability to turn himself into sand, he began as a villain and later became an ally of Spider-Man.  The character has been adapted into various other media incarnations of Spider-Man, including animated cartoons and the 2007 film \"Spider-Man 3\", in which he is portrayed by Thomas Haden Church.\n\nQuestion: Thomas Haden Church had a role as the Sandman in the film directed by whom?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor.\"\n    },\n    \"character_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the character played by the actor.\"\n    },\n    \"film_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the film.\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\",\n          \"description\": \"The release year of the film.\"\n        },\n        \"director_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the director of the film.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"release_year\",\n        \"director_name\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"character_name\",\n    \"film_details\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The name of the actor."
      },
      "character_name": {
        "type": "string",
        "description": "The name of the character played by the actor."
      },
      "film_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the film."
          },
          "release_year": {
            "type": "integer",
            "description": "The release year of the film."
          },
          "director_name": {
            "type": "string",
            "description": "The name of the director of the film."
          }
        },
        "required": [
          "title",
          "release_year",
          "director_name"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "actor_name",
      "character_name",
      "film_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

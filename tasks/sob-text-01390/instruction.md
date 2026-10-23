{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nUniversal Soldier: Regeneration: Universal Soldier: Regeneration (also known in some countries as Universal Soldier: A New Beginning) is a 2009 American sci-fi action film directed and edited by John Hyams (the son of director Peter Hyams, who previously worked with Jean-Claude Van Damme on three films, 1994's \"Timecop\", 1995's \"Sudden Death\" and 2013's \"Enemies Closer\"; in this film Peter is the director of photography).  The film stars Jean-Claude Van Damme and Dolph Lundgren, who both reprise their roles from the first film.  It is the third theatrical installment in the \"Universal Soldier series\".  The film is a direct sequel to the original \"Universal Soldier\" from 1992, unrelated to the two \"Universal Soldier\" television sequels that were produced in 1998 and completely ignores the events from the 1999 theatrical sequel \"\".\n\nThe Shepherd: Border Patrol: The Shepherd: Border Patrol is a 2008 American action film directed by Isaac Florentine and starring Jean-Claude Van Damme, Stephen Lord, Natalie J. Robb, Gary McDonald, Scott Adkins and Jean-Claude Van Damme's real life daughter Bianca Van Varenberg.  The film was released on direct-to-DVD in the United States on March 4, 2008.\n\nJean-Claude Van Damme: Jean-Claude Camille François Van Varenberg (born 18 October 1960), professionally known as Jean-Claude Van Damme and abbreviated as JCVD, is a Belgian actor, martial artist, screenwriter, film producer, and director best known for his martial arts action films.  The most successful of these films include \"Bloodsport\" (1988), \"Kickboxer\" (1989), \"Lionheart\" (1990), \"Double Impact\" (1991), \"Universal Soldier\" (1992), \"Hard Target\" (1993), \"Street Fighter\" (1994), \"Timecop\" (1994), \"Sudden Death\" (1995), \"JCVD\" (2008) and \"The Expendables 2\" (2012).\n\nDerailed (2002 film): Derailed is a 2002 American action film directed by Bob Misiorowski, and starring Jean-Claude Van Damme, Tomas Arana, Laura Harring and Jean-Claude Van Damme's real life son Kristopher Van Varenberg.  The film was released on direct-to-DVD in the United States on October 15, 2002.\n\nKickboxer: Retaliation: Kickboxer: Retaliation is an upcoming American martial arts film directed and written by Dimitri Logothetis.  Logothetis was attracted to the original Jean Claude Van Damme’s Kickboxer because of his martial arts background and that’s what inspired him to pursue the rights to the original, develop a reboot of the franchise and ultimately write, produce and direct a contemporary version of the pop culture, iconic Kickboxer.  It was important that Logothetis to convince Van Damme to step into the role of mentor to ordain a new, high octane Kickboxer who has a sixth degree black belt in BJJ, Alain Moussi.  Because Kickboxer: Vengeance was such a successful independent feature in the world market, it generated a sequel.  It is a sequel to the 2016 film \"\".  The film stars Alain Moussi, Jean-Claude Van Damme, Christopher Lambert, Ronaldinho, Mike Tyson and Hafþór Júlíus Björnsson.  Aside from Moussi and Van Damme, Sara Malakul Lane and Sam Medina are reprising their roles from the previous film.\n\nSudden Death (1995 film): Sudden Death is a 1995 American action film directed by Peter Hyams, and starring Jean-Claude Van Damme, Powers Boothe, and Dorian Harewood.  The film was released in the United States on December 22, 1995.  Set in a hockey arena, the film was written by Gene Quintano, based on a story by Karen Elise Baldwin, the wife of Pittsburgh Penguins owner Howard Baldwin, who was a co-producer.  It was the second collaboration between Van Damme and Hyams, after \"Timecop\" (1994).\n\nReplicant (film): Replicant is a 2001 American science fiction action film directed by Ringo Lam, and starring Jean-Claude Van Damme and Michael Rooker.  It is the second collaboration between Jean-Claude Van Damme and Hong Kong film director Ringo Lam, and the fifth time that Van Damme has starred in a dual role.  The film had a limited theatrical release in many European countries, and was released on direct-to-DVD in the United States on September 18, 2001.\n\nPjetër Malota: Peter Malota (born Pjetër Malota Lulgjuraj; 4 July 1959 in Lofka, Malësia, Albania) is best known for his appearances in films starring Jean-Claude Van Damme.  He has over 40 years Tae Lwon Do/Hapkido experience.  In 1984, Malota made his film debut in a small role in \"Furious\" and then played a member of a syndicate gang in the action movie \"Ninja Turf\".  In 1991, Malota began to work with Van Damme.  1991's Double Impact, where he played an assassin with kicking skills with knives in his shoes. \" Nowhere to Run\", in which he is seen playing the convict Van Damme tries to free, but is killed.  In 1996's \"The Quest\".  In this film, Malota puts his kicking skills to use again as he played the Spanish fighter that Van Damme fights in the tournaments.  He returns as a costar in Van Dammes Honor.\n\nThe Hard Corps: The Hard Corps is a 2006 American action film written and directed by Sheldon Lettich.  It stars Jean-Claude Van Damme, Raz Adoti, Vivica A. Fox, and Peter Bryant.  It is the fourth collaboration between Jean-Claude Van Damme and film director Sheldon Lettich.  The film was released direct-to-DVD in the United States on August 15, 2006.\n\nEnemies Closer: Enemies Closer is a 2013 American action thriller film directed and photographed by Peter Hyams, and starring Jean-Claude Van Damme, Tom Everett Scott and Orlando Jones.  It is Hyams' third directorial collaboration with Van Damme, following 1994's \"Timecop\" and 1995's \"Sudden Death\".\n\nQuestion: What film directed by Peter Hyams was one of Jean-Claude Van Damme's most successful?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"director_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the film's director.\"\n    },\n    \"is_listed_as_successful\": {\n      \"type\": \"boolean\",\n      \"description\": \"Indicates if the film is listed among Jean-Claude Van Damme's most successful films.\"\n    },\n    \"van_damme_involvement\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"actor_name\": {\n          \"type\": \"string\",\n          \"description\": \"The name of the actor.\"\n        },\n        \"role\": {\n          \"type\": \"string\",\n          \"description\": \"The role Jean-Claude Van Damme played in the film.\"\n        }\n      },\n      \"required\": [\n        \"actor_name\",\n        \"role\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"director_van_damme_collaborations\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of other films where the director and Jean-Claude Van Damme collaborated.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"director_name\",\n    \"is_listed_as_successful\",\n    \"van_damme_involvement\",\n    \"director_van_damme_collaborations\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "director_name": {
        "type": "string",
        "description": "The name of the film's director."
      },
      "is_listed_as_successful": {
        "type": "boolean",
        "description": "Indicates if the film is listed among Jean-Claude Van Damme's most successful films."
      },
      "van_damme_involvement": {
        "type": "object",
        "properties": {
          "actor_name": {
            "type": "string",
            "description": "The name of the actor."
          },
          "role": {
            "type": "string",
            "description": "The role Jean-Claude Van Damme played in the film."
          }
        },
        "required": [
          "actor_name",
          "role"
        ],
        "additionalProperties": false
      },
      "director_van_damme_collaborations": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of other films where the director and Jean-Claude Van Damme collaborated."
      }
    },
    "required": [
      "film_title",
      "director_name",
      "is_listed_as_successful",
      "van_damme_involvement",
      "director_van_damme_collaborations"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

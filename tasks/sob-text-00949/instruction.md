{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nFrank Capra: Frank Russell Capra (born Francesco Rosario Capra; May 18, 1897September 3, 1991) was an Italian-American film director, producer and writer who became the creative force behind some of the major award-winning films of the 1930s and 1940s.  Born in Italy and raised in Los Angeles from the age of five, his rags-to-riches story has led film historians such as Ian Freer to consider him the \"American dream personified.\"\n\nRendezvous in Space: Rendezvous in Space is a 1964 documentary film about the future of space exploration, directed by Frank Capra.  It is notable for being the final film that Frank Capra directed.  The film was funded by Martin Marietta and was shown at the Hall of Science Pavilion of the 1964-1965 New York World's Fair.  Animated sections illustrate the invention of gunpowder, a space shuttle resupplying a space station, and the problems to be overcome living for long periods in space.\n\nThe Younger Generation: The Younger Generation is a 1929 American part-talkie drama film directed by Frank Capra.  It was produced by Jack Cohn for Columbia Pictures.  This was Capra's first sound film.  While mostly silent, the film had talking sequences, as well as a synchronized music score and sound effects.  The screenplay was adapted from a Fannie Hurst play entitled \"It Is to Laugh\".\n\nManuel Argüello Mora: Manuel Argüello Mora was born in San José, Costa Rica in 1834.  He is one of the first Costa Rican authors, and with 1888's \"Misterio\", was its first novelist.  He obtained his education at the University of Santo Tomás in Costa Rica and the Universidad de San Carlos in Guatemala, where he obtained a degree in law.  Orphaned at a young age, he was brought up by his uncle Juan Rafael Mora Porras, the president of Costa Rica between 1849 and 1859, and his historical novel \"La trinchera\" recounts Mora Porras' campaign against William Walker's forces in Nicaragua in 1856.  After Mora Porras was deposed, he followed his uncle into exile in Europe in 1859.  He returned in 1860 during Mora Porras' attempt to regain power, and was spared from the firing squad which executed the former president.  Between 1860 and 1902 he served on the Costa Rican Supreme Court and was the rector of the University of Santo Tomás.  Along with writing within a number of genres, he also founded the weekly newspaper \"La Reforma\".  He died in San José in 1902.\n\nFrank Capra Jr.: Frank Warner Capra (March 20, 1934 – December 19, 2007), known as Frank Capra Jr., was an American film and television producer.  He was one of the three children of film director Frank Capra and his second wife, Lucille.  His own sons, Frank Capra III and Jonathan Capra, are assistant directors.\n\nKen Mora: Kenneth Oscar \"Ken\" Mora (born December 17, 1960) is an American screenplay writer, director, producer, editor, and voice actor.  He is best known for creating the computer-animated short films \"Magnum Farce: A Shot in the Park\" (2009) and \"Magnum Farce: Along Came a Sniper\" (2011).  He is currently producing the feature film \"Magnum Farce\" under the aegis of his production company Bella Fe Films, in cooperation with Light Row Pictures.  Mora is also executive producer of \"Adventures in Plymptoons\" (2012) the official biographical documentary of animator Bill Plympton, and associate producer of Revengeance (2017) the feature animated film by Plympton and Jim Lujan.\n\nArsenic and Old Lace (film): Arsenic and Old Lace is a 1944 American dark comedy film directed by Frank Capra, starring Cary Grant, and based on Joseph Kesselring's play \"Arsenic and Old Lace\".  The script adaptation was by Julius J. Epstein and Philip G. Epstein.  Capra actually filmed the movie in 1941 because of star Cary Grant's availability, but it was not released until 1944, after the original stage version had finished its run on Broadway.  The lead role of Mortimer Brewster was originally intended for Bob Hope, but he could not be released from his contract with Paramount.  Capra had also approached Jack Benny and Ronald Reagan before learning that Grant would accept the role.  Boris Karloff played Jonathan Brewster, who \"looks like Karloff,\" on the Broadway stage, but he was unable to do the movie as well because he was still appearing in the play during filming, and Raymond Massey took his place.  The film's supporting cast also features Priscilla Lane, Jack Carson, Edward Everett Horton and Peter Lorre.\n\nMr. Deeds Goes to Town: Mr. Deeds Goes to Town (a.k.a.  A Gentleman Goes to Town and Opera Hat) is a 1936 American romantic comedy film directed by Frank Capra, starring Gary Cooper and Jean Arthur in her first featured role.  Based on the 1935 short story \"Opera Hat\" by Clarence Budington Kelland, which appeared in serial form in \"The American Magazine\", the screenplay was written by Robert Riskin in his fifth collaboration with Frank Capra.\n\nLady for a Day: Lady for a Day is a 1933 American pre-Code comedy-drama film directed by Frank Capra.  The screenplay by Robert Riskin is based on the short story \"Madame La Gimp\" by Damon Runyon.  It was the first film for which Capra received an Academy Award nomination for Best Director and the first Columbia Pictures release to be nominated for Best Picture.\n\nThe Congress (1988 film): The Congress is a 1988 documentary film directed by the Emmy Award-winning director Ken Burns.  The Florentine Films production, which focuses on the United States Congress, aired on PBS in 1989.  Narrated by David McCullough, the documentary features use of photographs, paintings, and film from sessions of Congress, in its implementation of the Ken Burns Effect.  Scenes from the Academy Award-winning Frank Capra film \"Mr. Smith Goes to Washington\" are also used.  The work features numerous interviews from writers and historians including Charles McDowell, David McCullough, Cokie Roberts, George Tames, David Broder, James MacGregor Burns, Barbara Fields, and Alistair Cooke.  Many congressmen are specifically referred to, including Henry Clay, John C. Calhoun, Jefferson Davis, Thomas Brackett Reed, Joseph Gurney Cannon, George William Norris, Jeannette Rankin, and Everett Dirksen.  The film also includes focus on the Congress' work during pivotal periods in United States history, including the Civil War, Civil Rights Movement, and Women's suffrage.  The documentary was released by PBS, on DVD in 2004.  Footage of the Capitol from the film was later incorporated into Burns' later masterpiece, The Civil War.\n\nQuestion: Who was born first, Frank Capra or Ken Mora?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_1_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the first person being compared.\"\n    },\n    \"person_1_birth_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The birth year of the first person.\"\n    },\n    \"person_2_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the second person being compared.\"\n    },\n    \"person_2_birth_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The birth year of the second person.\"\n    },\n    \"earliest_born_person_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person who was born first.\"\n    },\n    \"earliest_birth_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The earliest birth year among the two people.\"\n    }\n  },\n  \"required\": [\n    \"person_1_name\",\n    \"person_1_birth_year\",\n    \"person_2_name\",\n    \"person_2_birth_year\",\n    \"earliest_born_person_name\",\n    \"earliest_birth_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_1_name": {
        "type": "string",
        "description": "The name of the first person being compared."
      },
      "person_1_birth_year": {
        "type": "integer",
        "description": "The birth year of the first person."
      },
      "person_2_name": {
        "type": "string",
        "description": "The name of the second person being compared."
      },
      "person_2_birth_year": {
        "type": "integer",
        "description": "The birth year of the second person."
      },
      "earliest_born_person_name": {
        "type": "string",
        "description": "The name of the person who was born first."
      },
      "earliest_birth_year": {
        "type": "integer",
        "description": "The earliest birth year among the two people."
      }
    },
    "required": [
      "person_1_name",
      "person_1_birth_year",
      "person_2_name",
      "person_2_birth_year",
      "earliest_born_person_name",
      "earliest_birth_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

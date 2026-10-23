{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCruella de Vil: Cruella de Vil (spelled de Vil in the novel, spelled De Vil by Disney) is a character who appeared in Dodie Smith's 1956 novel \"The Hundred and One Dalmatians\", Disney's animated film adaptations \"101 Dalmatians\" and \"\", and Disney's live-action film adaptations \"101 Dalmatians\" and \"102 Dalmatians\" as the main antagonist.\n\nDodie Smith: Dorothy Gladys \"Dodie\" Smith (3 May 1896 – 24 November 1990) was an English children's novelist and playwright, known best for the novel \"The Hundred and One Dalmatians\" (1956).  Other works include \"I Capture the Castle\" (1948), and \"The Starlight Barking\" (1967).  \"The Hundred and One Dalmatians\" was adapted into a 1961 Disney animated movie version.  Her novel \"I Capture the Castle\" was adapted into a 2003 movie version.  \"I Capture the Castle\" was voted number 82 as \"one of the nation's 100 best-loved novels\" by the British public as part of the BBC's The Big Read (2003).\n\nThe Starlight Barking: The Starlight Barking is a 1967 children's novel by Dodie Smith.  It is a sequel to the 1956 novel \"The Hundred and One Dalmatians\".\n\n101 Dalmatians II: Patch's London Adventure: 101 Dalmatians II: Patch's London Adventure is a 2003 American direct-to-video animated adventure musical drama film, written and directed by Jim Kammerud and Brian Smith, released by Walt Disney Home Entertainment on February 25, 2003, and based on Dodie Smith's characters, \"The Hundred and One Dalmatians\" and is also inspired by \"The Starlight Barking\".  It is the sequel to the 1961 Disney animated film \"101 Dalmatians\".  It features the voices of Martin Short, Jason Alexander, Barry Bostwick, Susanne Blakeslee, Kath Soucie, Jeff Bennett, Jim Cummings, and Bobby Lockwood.  It garnered DVDX awards for best animated feature, best director, best editing, and best musical score.  Disney re-released it on September 16, 2008.\n\n101 Dalmatians (1996 film): 101 Dalmatians is a 1996 American live-action comedy adventure film based on Walt Disney's animated 1961 movie adaptation of Dodie Smith's 1956 novel \"The Hundred and One Dalmatians.\"  Directed by Stephen Herek and co-produced by John Hughes and Ricardo Mestres, it stars Glenn Close, Jeff Daniels, Joely Richardson, Joan Plowright, Hugh Laurie, Mark Williams and Tim McInnerny.  In contrast with the 1961 film, none of the animals talk in this version.  Released on November 27, 1996 by Walt Disney Pictures, the film was praised for its faithfulness to the animated classic.  It received mixed reviews, but was a commercial success, grossing $320.6 million in theaters against a $75 million budget.  Close, who was universally praised for her portrayal as Cruella de Vil, was nominated for a Golden Globe for Best Performance by an Actress in a Motion Picture - Comedy or Musical, but lost to Madonna in \"Evita\".  The film was also nominated for a BAFTA award for best makeup effects.  A theatrical sequel titled \"102 Dalmatians\" was released on November 22, 2000 with Close and McInnerny reprising their roles.\n\nMarie Antoinette syndrome: Marie Antoinette syndrome is a sudden whitening of the hair.  The event that named the syndrome was the observation that the hair of Queen Marie Antoinette of France turned stark white after her capture following the ill-fated Flight to Varennes during the French Revolution.  Witnesses have alleged that Antoinette's hair suddenly turned white on three separate occasions.  In the novel 'One hundred and One Dalmatians', by Dodie Smith, after the Dalmatians destroy Cruella de Vil's stock of furs, the shock renders her black hair white (and her white hair green).  In Victor Hugo's novel 'Les Miserables' Jean Val-Jean's hair also goes pure white after the trauma of appearing in court in Arras.  Other examples can be found in George R.R. Martin's \"A Song of Ice and Fire\" series, where the character Theon Greyjoy's hair turns white and brittle from extended brutal torture.\n\nThe Hundred and One Dalmatians: The Hundred and One Dalmatians, or the Great Dog Robbery is a 1956 children's novel by Dodie Smith about the kidnapping of a family of 101 Dalmatian dogs.  A sequel, \"The Starlight Barking\", continues from the end of the first novel.\n\n102 Dalmatians: 102 Dalmatians is a 2000 American live action and CG-animated film adventure drama film directed by Kevin Lima in his live-action directorial debut and produced by Edward S. Feldman and Walt Disney Pictures.  It is the sequel to the 1996 film \"101 Dalmatians\", a live-action remake of the 1961 Disney animated film of the same name and stars Glenn Close reprising her role as Cruella de Vil as she attempts to steal puppies for her \"grandest\" fur coat yet.  Close and Tim McInnerny were the only two actors from the first film to return for the sequel, however.  The film was nominated for an Academy Award for Best Costume Design, but lost to \"Gladiator.\"\n\nOne Hundred and One Dalmatians: One Hundred and One Dalmatians, often abbreviated as 101 Dalmatians, is a 1961 American animated adventure film produced by Walt Disney and based on the 1956 novel \"The Hundred and One Dalmatians\" by Dodie Smith.  The 17th Disney animated feature film, the film tells the story of a litter of dalmatian puppies who are kidnapped by the villainous Cruella de Vil (Betty Lou Gerson), who wants to use their fur to make into coats.  Their parents, Pongo and Perdita, (Rod Taylor and Cate Bauer respectively) set out to save their children from Cruella, all the while rescuing 84 additional puppies that were bought in pet shops, bringing the total of dalmatians to 101.\n\nThe 101 Dalmatians Musical: The 101 Dalmatians Musical is a musical produced by Luis Alvarez, directed by Jerry Zaks, and sponsored by Purina Dog Chow.  The music written by former Styx member Dennis DeYoung, who also co-wrote the lyrics with the musical's book author B. T. McNicholl.  Based on the 1956 children's novel \"The Hundred and One Dalmatians\" written by Dodie Smith, the musical follows a pair of Dalmatian dogs as they search through London in search of their litter of fifteen puppies, which were stolen by Cruella DeVil to make dog skin fur coats.  The musical features Rachel York as the infamous Cruella DeVil, and has actors sharing the stage with fifteen real Dalmatians and using stilts to simulate the novel's original canine perspective.\n\nQuestion: Who direction the live action sequel to the Disney film based on Dodie Smith's 1956 novel \"The Hundred and One Dalmatians\"?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film being asked about.\"\n    },\n    \"film_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"director_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the director of the film.\"\n    },\n    \"is_live_action\": {\n      \"type\": \"boolean\",\n      \"description\": \"True if the film is a live-action production.\"\n    },\n    \"is_sequel\": {\n      \"type\": \"boolean\",\n      \"description\": \"True if the film is a sequel to another film.\"\n    },\n    \"original_novel_author\": {\n      \"type\": \"string\",\n      \"description\": \"The author of the original novel that the film series is based on.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"film_year\",\n    \"director_name\",\n    \"is_live_action\",\n    \"is_sequel\",\n    \"original_novel_author\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film being asked about."
      },
      "film_year": {
        "type": "integer",
        "description": "The release year of the film."
      },
      "director_name": {
        "type": "string",
        "description": "The name of the director of the film."
      },
      "is_live_action": {
        "type": "boolean",
        "description": "True if the film is a live-action production."
      },
      "is_sequel": {
        "type": "boolean",
        "description": "True if the film is a sequel to another film."
      },
      "original_novel_author": {
        "type": "string",
        "description": "The author of the original novel that the film series is based on."
      }
    },
    "required": [
      "film_title",
      "film_year",
      "director_name",
      "is_live_action",
      "is_sequel",
      "original_novel_author"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

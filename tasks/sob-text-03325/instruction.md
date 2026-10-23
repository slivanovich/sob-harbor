{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nKitty Hawks: Kitty Hawks is an interior designer currently living in New York City and Westchester, New York.  She is the daughter of New York socialite Slim Keith and film director Howard Hawks and is married to Larry Lederman, a photographer and retired corporate attorney.\n\nScarface (1932 film): Scarface (also known as Scarface: The Shame of the Nation and The Shame of a Nation) is a 1932 American pre-Code gangster film starring Paul Muni as Antonio \"Tony\" Camonte.  It was produced by Howard Hughes and Howard Hawks and directed by Hawks.  The story is based on Armitage Trail's 1929 novel of the same name, which is loosely based on the rise and fall of Al Capone.  The film features Ann Dvorak as Camonte's sister, and also stars Karen Morley, Osgood Perkins, and Boris Karloff.  The plot centers on gang warfare and police intervention when rival gangs fight over control of Chicago.  A version of the Saint Valentine's Day Massacre is also depicted.\n\nTim Roth: Timothy Simon \"Tim\" Roth (born 14 May 1961) is an English actor and director.  He made his debut role in the 1982 television film \"Made in Britain\" (1982).  He garnered critical acclaim for his role as Myron in the 1984 film \"The Hit\" (1984), for which he was nominated for his first BAFTA Award.  Roth gained more attention for his performances in \"The Cook, the Thief, His Wife & Her Lover\" (1989), \"Vincent & Theo\" (1990) and \"Rosencrantz & Guildenstern Are Dead\" (1990).\n\nViva Villa!: Viva Villa!  is a 1934 American Pre-Code film starring Wallace Beery as Pancho Villa and was written by Ben Hecht, adapted from the book \"Viva Villa! \".  The film was shot on location in Mexico and directed by Jack Conway.  There was uncredited assistance with the script by Howard Hawks, James Kevin McGuinness, and Howard Emmett Rogers.  Hawks and William A. Wellman were also uncredited directors on the film.\n\nThe Big Sky (film): The Big Sky is a 1952 American Western film produced and directed by Howard Hawks, based on the novel of the same name.  The cast includes Kirk Douglas, Dewey Martin, Elizabeth Threatt and Arthur Hunnicutt, who was nominated for an Academy Award for Best Supporting Actor.  Though not considered among Hawks's major achievements by most critics, the film was chosen by Jonathan Rosenbaum for his alternative list of the Top 100 American Films.\n\nHoward Hawks: Howard Winchester Hawks (May 30, 1896December 26, 1977) was an American film director, producer and screenwriter of the classic Hollywood era.  Critic Leonard Maltin called him \"the greatest American director who is not a household name.\"\n\nOnly Angels Have Wings: Only Angels Have Wings is a 1939 American drama film directed by Howard Hawks, and starring Cary Grant and Jean Arthur, based on a story written by Hawks.  The film also marked the first significant role in a major film for Rita Hayworth.  It is generally regarded as being among Hawks' finest films, particularly in its portrayal of the professionalism of the pilots of the film, its atmosphere, and the flying sequences.  The supporting cast features Thomas Mitchell and Richard Barthelmess.\n\nHagar Wilde: Hagar Wilde (July 7, 1905 – September 25, 1971) was a writer for Hollywood films and television shows in the late thirties till the late fifties.  Her work includes co-writing the screenplay for \"Bringing Up Baby\" (for which she had also written the original story, published in the mass-market magazine \"Collier's Weekly\"), starring Katharine Hepburn and Cary Grant, and was directed by Howard Hawks, and the screenplay for \"I Was a Male War Bride\", also starring Cary Grant and again directed by Howard Hawks as well as co-wrote \"The Unseen\".  \"She died in 1971, penniless and bitter, at the Motion Picture Country Home.\"\n\nElizabeth Threatt: Elizabeth Coyote Threatt (April 12, 1926 – November 22, 1993) was an American model and actress, best known for her starring role in Howard Hawks's 1952 film \"The Big Sky\", where she is in a love triangle with Kirk Douglas and Dewey Martin.  It was her only film appearance, and all dialogue spoken by Threatt was in the depicted Native American language.  She was spotted by Howard Hawks and cast for the part of an Indian princess captured by white man as hostage for a trade deal.  Threatt left the film industry (and acting) after this one film.\n\nMonkey Business (1952 film): Monkey Business is a 1952 American screwball comedy film directed by Howard Hawks and written by Ben Hecht, which stars Cary Grant, Ginger Rogers, Charles Coburn, and Marilyn Monroe.  To avoid confusion with the famous 1931 Marx Brothers film of the same name, this film is sometimes referred to as Howard Hawks' Monkey Business.\n\nQuestion: Tim Roth and Howard Hawks, share which mutual occupation?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"person_1_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the first person.\"\n    },\n    \"person_2_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the second person.\"\n    },\n    \"shared_occupation\": {\n      \"type\": \"string\",\n      \"description\": \"The occupation shared by both individuals.\"\n    },\n    \"person_1_other_occupations\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Other occupations of the first person mentioned in the context.\"\n    },\n    \"person_2_other_occupations\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"Other occupations of the second person mentioned in the context.\"\n    }\n  },\n  \"required\": [\n    \"person_1_name\",\n    \"person_2_name\",\n    \"shared_occupation\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "person_1_name": {
        "type": "string",
        "description": "The name of the first person."
      },
      "person_2_name": {
        "type": "string",
        "description": "The name of the second person."
      },
      "shared_occupation": {
        "type": "string",
        "description": "The occupation shared by both individuals."
      },
      "person_1_other_occupations": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Other occupations of the first person mentioned in the context."
      },
      "person_2_other_occupations": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "Other occupations of the second person mentioned in the context."
      }
    },
    "required": [
      "person_1_name",
      "person_2_name",
      "shared_occupation"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

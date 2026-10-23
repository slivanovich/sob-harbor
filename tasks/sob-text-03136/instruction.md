{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nConcussion (2013 film): Concussion is a 2013 American drama film written and directed by Stacie Passon and starring Robin Weigert.  Although not autobiographical, the story was partially inspired by Passon herself suffering a mild concussion, in the same manner depicted in the film, shortly before she began writing the screenplay.\n\nMarion Jackson: Marion Jackson (December 3, 1897 – November 28, 1962) was an American screenwriter of the late silent and early sound film eras.  During her fifteen-year career she would pen the scripts for over 40 films, both original and adaptations.  Born in Walla Walla, Washington, she wrote her first script, an original screenplay, which was produced by Monogram Pictures in 1924, \"The Mask of Lopez\", directed by Albert Rogell.  It would be her most prolific year, as she would contribute to 11 screenplays that year, either as the screenwriter, or providing the story, or adapting from another source.  One of the films she adapted that year was 1924's \"A Boy of Flanders\", from Marie Louise de la Ramée's 1872 novel, \"A Dog of Flanders\".  The film was directed by Victor Schertzinger, and starred Jackie Coogan.  Some of her notable films were her 1928 adaptation of \"The Shepherd of the Hills\", based on the 1907 novel of the same name by Harold Bell Wright; her original screenplay for The Wagon Master (1929), starring Ken Maynard; and the hit film, \"Min and Bill\" (1930), which she co-wrote with Frances Marion, which stars Marie Dressler and Wallace Beery.\n\nWe Have Always Lived in the Castle (film): We Have Always Lived in the Castle is an upcoming American mystery thriller film directed by Stacie Passon and written by Passon and Mark Kruger, based on the 1962 novel of the same name by Shirley Jackson.  The film stars Taissa Farmiga, Alexandra Daddario, Crispin Glover, and Sebastian Stan.\n\nThe Human Comedy (film): The Human Comedy is a 1943 American drama film directed by Clarence Brown and adapted by Howard Estabrook.  It is often thought to be based on the William Saroyan novel of the same name, but Saroyan actually wrote the screenplay first, was fired from the movie project, and quickly wrote the novel and published it just before the film was released.  The picture stars Mickey Rooney with Frank Morgan.  Also appearing in the film are James Craig, Marsha Hunt, Fay Bainter, Ray Collins, Van Johnson, Donna Reed and Jackie 'Butch' Jenkins.  Robert Mitchum (as \"Quentin\") and Don DeFore appear together as boisterous soldiers in uncredited supporting roles.\n\nAlong the Navajo Trail (film): Along the Navajo Trail is a 1945 American western film directed by Frank McDonald and starring Roy Rogers, George 'Gabby' Hayes and Dale Evans.  The film's story was based on a William Colt MacDonald novel.  The film marked the debut of the Cuban actress Estelita Rodriguez, who Republic Pictures then began to build up into a star.  Its title song is \"Along the Navajo Trail\", an instrumental version of which appears with the opening credits, with a brief vocal version during the last twenty seconds of the film.  The first few bars of the song are used as background music in several chase scenes.\n\nBright Lights, Big City (film): Bright Lights, Big City is a 1988 American drama film directed by James Bridges, starring Michael J. Fox, Kiefer Sutherland, Phoebe Cates, Dianne Wiest and Jason Robards, and based on the novel by Jay McInerney, who also wrote the screenplay.  It was the last film directed by Bridges, who died in 1993.\n\nRipley Under Ground (film): Ripley Under Ground (also known as White on White) is a 2005 German-British-French crime thriller film directed by Roger Spottiswoode and based on the second novel in Patricia Highsmith's Tom Ripley series.  It stars Barry Pepper as the cunning psychopath Ripley and features Willem Dafoe, Alan Cumming and Tom Wilkinson in supporting roles.  \"Ripley Under Ground\" was produced during July and August 2003, but was only released two years later.  The film was shown on the 2005 AFI Fest by American Film Institute, receiving a low-profile wide theatrical release.\n\nTaissa Farmiga: Taissa Farmiga ( ; born August 17, 1994) is an American actress.  She began her career in film in the drama \"Higher Ground\" (2011), and subsequently made her television debut in the FX series \"\" (2011).  Farmiga made her stage debut in the Off-Broadway revival of the drama play \"Buried Child\" (2016).\n\nHigher Ground (film): Higher Ground is a 2011 American drama film directed by Vera Farmiga in her directorial debut.  The film is an adaptation of the 2002 memoir \"This Dark World: A Memoir of Salvation Found and Lost\" by Carolyn S. Briggs, who co-wrote the screenplay.  The film follows Corinne Walker (Farmiga) and her vacillating relationship with Christianity.  The cast also includes Joshua Leonard, John Hawkes, Donna Murphy, Norbert Leo Butz, and Bill Irwin.\n\nSissy Spacek: Mary Elizabeth \"Sissy\" Spacek ( ; born December 25, 1949) is an American actress and singer.  She began her career in the early 1970s and first gained attention for her role in the film \"Badlands\" (1973).  Her major breakthrough came in 1976 when she played the title character of Carrie White in Brian De Palma's horror film \"Carrie\", based on the first novel by Stephen King, for which she earned an Oscar nomination (a rare feat for an actor or actress in a horror movie).  She won the Academy Award for Best Actress for her portrayal of Loretta Lynn in the 1980 film \"Coal Miner's Daughter,\" and also earned a Grammy nomination for the song \"Coal Miner's Daughter\" from the film's soundtrack.  She went on to receive further Oscar nominations for her roles in \"Missing\" (1982), \"The River\" (1984) and \"Crimes of the Heart\" (1986).  \"Coal Miner's Daughter\" and \"Crimes of the Heart\" also won her the Golden Globe Award for Best Actress in a Musical or Comedy.\n\nQuestion: Who wrote the novel  a film directed by Stacie Passon and starring an actress who began her career in \"Higher Ground\" is based on?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film directed by Stacie Passon.\"\n    },\n    \"director_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the film's director.\"\n    },\n    \"lead_actress_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actress starring in the film who also began her career in 'Higher Ground'.\"\n    },\n    \"actress_debut_film\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film where the lead actress began her career.\"\n    },\n    \"novel_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the novel the film is based on.\"\n    },\n    \"novel_author\": {\n      \"type\": \"string\",\n      \"description\": \"The author of the novel.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"director_name\",\n    \"lead_actress_name\",\n    \"actress_debut_film\",\n    \"novel_title\",\n    \"novel_author\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film directed by Stacie Passon."
      },
      "director_name": {
        "type": "string",
        "description": "The name of the film's director."
      },
      "lead_actress_name": {
        "type": "string",
        "description": "The name of the actress starring in the film who also began her career in 'Higher Ground'."
      },
      "actress_debut_film": {
        "type": "string",
        "description": "The title of the film where the lead actress began her career."
      },
      "novel_title": {
        "type": "string",
        "description": "The title of the novel the film is based on."
      },
      "novel_author": {
        "type": "string",
        "description": "The author of the novel."
      }
    },
    "required": [
      "film_title",
      "director_name",
      "lead_actress_name",
      "actress_debut_film",
      "novel_title",
      "novel_author"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

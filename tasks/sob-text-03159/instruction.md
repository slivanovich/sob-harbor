{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nRed October (fictional submarine): Red October (Russian: Красный Oктябрь , [ˈkrasnɨj ɐkˈtʲabrʲ] \"Krasniy Oktyabr\") is a modified \"Typhoon\" class submarine in the Tom Clancy novel \"The Hunt for Red October\" and the film of the same name.  It was built with a revolutionary stealth propulsion system called a \"caterpillar drive\", which is described as a pump-jet system in the book.  In the film however, it is shown as being a magnetohydrodynamic drive.\n\nCrazy Ivan: Crazy Ivan is a cold war term used in the US to describe two different concepts.  The most common usage was the name given to a maneuver used by Soviet submarines to clear their baffles to see if they were being followed.  The second use was a catch-all term for the possibility of a rogue Soviet leader committing to military action, typically in reference to a limited launch of ICBMs against the US.  The term Red October was sometimes used to describe the second concept, a reference to the 1984 Tom Clancy novel \"The Hunt for Red October\" in which a rogue Soviet submarine commander appears to threaten to launch a nuclear strike on the US.  The novel uses the first version of the term as a plot point.\n\nPatriot Games (film): Patriot Games is a 1992 American spy thriller film directed by Phillip Noyce and based on Tom Clancy's novel of the same name.  It is a sequel to the 1990 film \"The Hunt for Red October\", but with different actors in the leading roles, Harrison Ford starring as Jack Ryan and Anne Archer as his wife.  James Earl Jones is the lone holdover, reprising his role as Admiral James Greer.  The cast also includes Sean Bean, Patrick Bergin, Thora Birch, Samuel L. Jackson, James Fox, and Richard Harris.\n\nSam Neill: Nigel John Dermot Neill {'1': \", '2': \", '3': \", '4': \"} (born 14 September 1947), known professionally as Sam Neill, is a New Zealand actor who first achieved leading roles in films such as \"\" and \"Dead Calm\" and on television in \"Reilly, Ace of Spies\".  He won a broad international audience in 1993 for his roles as Alisdair Stewart in \"The Piano\" and Dr. Alan Grant in \"Jurassic Park\", a role he reprised in 2001's \"Jurassic Park III\".  Neill also had notable roles in \"Merlin\", \"The Hunt for Red October\", \"Peaky Blinders\", and \"The Tudors\".  In 2016, he starred in \"Hunt for the Wilderpeople\" alongside Julian Dennison, to great acclaim.\n\nThe Art of War (film): The Art of War is a 2000 Canadian-American action film directed by Christian Duguay and starring Wesley Snipes, Michael Biehn, Anne Archer and Donald Sutherland.  The film's title refers to the ancient Chinese text of the same name by war strategist Sun Tzu.  The film was followed by two direct-to-video sequels, \"\" and \"\", which the latter did not feature Snipes.\n\nThe Hunt for Red October (1990 video game): The Hunt for Red October is video game based on the movie \"The Hunt for Red October\".  It was developed by Images Software and released by Grandslam Interactive Ltd. in 1990 and was available for the Amiga, Amstrad CPC, Atari ST, Commodore 64, MS-DOS, and ZX Spectrum.\n\nThe Hunt for Red October (console game): The Hunt for Red October is a video game based on the movie \"The Hunt for Red October\".  It was first released in 1991 for the Nintendo Entertainment System.  Versions for the Game Boy and Super NES were subsequently released.\n\nThe Blue Knight (film): The Blue Knight is a 1973 made-for-TV film based on Joseph Wambaugh's 1973 novel \"The Blue Knight\".  It gave rise to the 1975 TV series also named \"The Blue Knight\".  It ran originally on NBC TV in November 1973, was directed by Robert Butler, and starred an all star cast headed by William Holden as Police Officer Bumper Morgan.  The additional cast includes Lee Remick, Anne Archer, Sam Elliott, Joe Santos, and Vic Tayback.  The film was a four-hour series.\n\nThe Hunt for Red October (1987 video game): The Hunt for Red October is a video game based on the book The Hunt for Red October.  It was released in 1987 and was available for the Atari ST, Amiga, Apple II, ZX Spectrum, MSX, Commodore 64 and IBM PC.  A port for the Apple IIGS was released in 1989.  The player must navigate the \"Red October\" towards U.S. waters while avoiding the Soviet Navy.  The game is a combination of submarine simulator and strategy game.\n\nAnne Archer: Anne Archer (born August 24, 1947) is an American actress.  She was nominated for the Academy Award for Best Supporting Actress for the 1987 film \"Fatal Attraction\".  Her other film appearances include \"Paradise Alley\" (1978), \"Patriot Games\" (1992), \"Short Cuts\" (1993), \"Clear and Present Danger\" (1994) and \"Lullaby\" (2014).  On stage, she starred as Mrs. Robinson in the West End production of \"The Graduate\" in 2001, and in the title role of \"The Trial of Jane Fonda\" at the 2014 Edinburgh Festival Fringe.\n\nQuestion: What is the name of the film that Anne Archer starred in that was a sequel to The Hunt for Red October?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"is_sequel_to\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film it is a sequel to.\"\n    },\n    \"actress_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actress who starred in the film.\"\n    },\n    \"director\": {\n      \"type\": \"string\",\n      \"description\": \"The director of the film.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"is_sequel_to\",\n    \"actress_name\",\n    \"director\",\n    \"release_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "is_sequel_to": {
        "type": "string",
        "description": "The title of the film it is a sequel to."
      },
      "actress_name": {
        "type": "string",
        "description": "The name of the actress who starred in the film."
      },
      "director": {
        "type": "string",
        "description": "The director of the film."
      },
      "release_year": {
        "type": "integer",
        "description": "The release year of the film."
      }
    },
    "required": [
      "film_title",
      "is_sequel_to",
      "actress_name",
      "director",
      "release_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

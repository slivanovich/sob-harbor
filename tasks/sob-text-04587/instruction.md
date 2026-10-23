{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Associate: The Associate is a 1996 American comedy film directed by Donald Petrie and written by Nick Thiel.  The film, a remake of René Gainville's 1979 French film of the same name, which, in turn, was based on Jenaro Prieto's 1928 novel \"The Partner\", stars Whoopi Goldberg, Dianne Wiest, Eli Wallach, Tim Daly, and Bebe Neuwirth, alongside Austin Pendleton and Lainie Kazan.\n\nTough Guys: Tough Guys is a 1986 action comedy film starring Burt Lancaster, Kirk Douglas, Eli Wallach, Charles Durning, Dana Carvey and Darlanne Fluegel.  It was directed by Jeff Kanew.  This was the first film to be released under the banner of Touchstone Pictures rather than Touchstone Films.\n\nThe Godfather Part III: The Godfather Part III is a 1990 American crime film written by Mario Puzo and Francis Ford Coppola, and directed by Coppola.  A sequel to \"The Godfather\" (1972) and \"The Godfather Part II\" (1974), it completes the story of Michael Corleone, a Mafia kingpin who attempts to legitimize his criminal empire.  The film also includes fictionalized accounts of two real-life events: the 1978 death of Pope John Paul I and the Papal banking scandal of 1981–82, both linked to Michael Corleone's business affairs.  The film stars Al Pacino, Diane Keaton, Talia Shire, and Andy García, and features Eli Wallach, Joe Mantegna, George Hamilton, Bridget Fonda, and Sofia Coppola.\n\nThe Adventures of Gerard: The Adventures of Gerard is a 1970 British-Italian-Swiss adventure comedy film directed by Jerzy Skolimowski and starring Peter McEnery, Claudia Cardinale, Eli Wallach and Jack Hawkins.  It was based on \"The Exploits of Brigadier Gerard\" by Arthur Conan Doyle.\n\nThe Holiday: The Holiday is a 2006 American romantic comedy film written, produced and directed by Nancy Meyers.  Co-produced by Bruce A. Block, it was filmed in both California and England, and stars Cameron Diaz and Kate Winslet as Amanda and Iris, two lovelorn women from opposite sides of the Atlantic Ocean, who temporarily exchange homes to escape heartbreak during the holiday season.  Jude Law and Jack Black were cast as the film's leading men Graham and Miles, with Eli Wallach, Shannyn Sossamon, Edward Burns and Rufus Sewell playing key supporting roles.\n\nThe Misfits (film): The Misfits is a 1961 American drama film written by Arthur Miller, directed by John Huston, and starring Clark Gable, Marilyn Monroe and Montgomery Clift.  The supporting cast features Thelma Ritter, Eli Wallach and Kevin McCarthy.  It marked the last completed film of Gable and Monroe.  For Gable, the film was posthumously released, while Monroe died the following year.  The plot centers on a recently divorced woman (Monroe) and her time spent with a cowboy (Gable), his tow truck-driving friend (Wallach) and his rodeo-riding friend (Clift) in the Western Nevada desert in the 1960s.  The film was a commercial failure at the time of its release, but received positive critical comments for its script and performances, and is highly regarded today.\n\nSam's Son: Sam's Son is a 1984 American semi-autobiographical coming-of-age drama film written and directed by Michael Landon loosely based on his early life and is also the only feature film ever made by him.  The film stars Eli Wallach, Anne Jackson, Timothy Patrick Murphy, Hallie Todd, Jonna Lee, James Karen, and even Landon in a cameo at the beginning and the end.  The film was produced independently by Landon himself and released by Utah-based distributor Invictus Entertainment.\n\nThe Tiger Makes Out: The Tiger Makes Out is a 1967 American comedy film about a kidnapper and his unintended victim, starring Eli Wallach and Anne Jackson and directed by Arthur Hiller.  Making a brief appearance is Dustin Hoffman in his film debut.\n\nKeeping the Faith: Keeping the Faith is a 2000 American romantic comedy film written by Stuart Blumberg, and starring Ben Stiller, Edward Norton (in his directorial debut), Jenna Elfman, Eli Wallach, and Anne Bancroft.  This film was released by Touchstone Pictures and Spyglass Entertainment, in association with Triple Threat Talent, on April 14, 2000.\n\nEli Wallach credits: The following is the filmography and credits for American actor Eli Wallach.  He started acting in 1945 and is known for his film roles as Calvera in \"The Magnificent Seven\" (1960), Tuco in \"The Good, the Bad and the Ugly\" (1966), Napoleon in \"The Adventures of Gerard\" (1970), Cotton Weinberger in \"The Two Jakes\" (1990), Don Altobello in \"The Godfather Part III\" (1990), Donald Fallon in \"The Associate\" (1996), Arthur Abbott in \"The Holiday\" (2006), Noah Dietrich in \"The Hoax\" (2007), and Julie Steinhardt in \"\" (2010), which was the last film he appeared in before retiring in 2010.\n\nQuestion: Eli Wallach played Arthur Abbott is a romantic comedy film written by who?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor.\"\n    },\n    \"role_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the role played by the actor.\"\n    },\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"film_genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the film.\"\n    },\n    \"writer_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the writer of the film.\"\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"role_name\",\n    \"film_title\",\n    \"film_genre\",\n    \"writer_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "actor_name": {
        "type": "string",
        "description": "The name of the actor."
      },
      "role_name": {
        "type": "string",
        "description": "The name of the role played by the actor."
      },
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "film_genre": {
        "type": "string",
        "description": "The genre of the film."
      },
      "writer_name": {
        "type": "string",
        "description": "The name of the writer of the film."
      }
    },
    "required": [
      "actor_name",
      "role_name",
      "film_title",
      "film_genre",
      "writer_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

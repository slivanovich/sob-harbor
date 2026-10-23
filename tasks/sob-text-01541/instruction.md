{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAlex Jennings: Alex Jennings (born 10 May 1957) is an English actor, who has worked extensively with the Royal Shakespeare Company and National Theatre.  A three-time Olivier Award winner, he won for \"Too Clever by Half\" (1988), \"Peer Gynt\" (1996), and \"My Fair Lady\" (2003).  He is the only performer to have won Olivier awards in the drama, musical and comedy categories.  He played Prince Charles in the 2006 film \"The Queen\".  His other film appearances include \"The Wings of the Dove\" (1997), \"\" (2004), \"Babel\" (2006) and \"The Lady in the Van\" (2015).\n\nBreathe (2 AM): \"Breathe (2 AM)\" is a song by American singer-songwriter Anna Nalick.  The single was first released in 2004, then it was re-released in 2006 and charted at #45 on the \"Billboard\" Hot 100 and #4 on the Adult Contemporary in the United States, as well as #79 on the Australian singles charts.  \"Breathe (2 AM)\" has been certified Gold by RIAA.  The song was featured prominently in shows like ABC's \"Grey's Anatomy\" episodes \"As We Know It\" and \"Song Beneath the Song\", as well as other shows such as the WB series \"Charmed\", \"Smallville\" and the movies \"\"A Lot Like Love\" a\"nd \"Griffin & Phoenix\" (2006 film) (both films the female character was played by Amanda Peet).\n\nTouchstone (As You Like It): Touchstone is a fictional character in Shakespeare's play \"As You Like It\".\n\nAs You Like It (2006 film): As You Like It is a 2006 film written and directed by Kenneth Branagh, and based on the Shakespearean play of the same name.  It stars Bryce Dallas Howard as Rosalind, David Oyelowo as Orlando De Boys, Romola Garai as Celia, Adrian Lester as Oliver De Boys, Alfred Molina as Touchstone, Kevin Kline as Jaques, Janet McTeer as Audrey, and Brian Blessed as Duke Frederick and his brother Duke Senior.\n\nJacob Clement Utzon-Krefeld: Jacob Clement Utzon-Krefeld (born 1990, Denmark) is a Danish actor Played Hamlet in Shakespeare's Hamlet at the Castle of Elsinore for two consecutive years 2016-17.  Studied at East 15 Drama School in London.\n\nRama Paduka Pattabhishekam: Rama Paduka Pattabhishekam (\"English\": The Coronation Of Lord Rama's Slippers) (\"Telugu:\" రామ పాదుక పట్టాభిషేకం) is a 1932 Telugu mythological drama film directed by Sarvottam Badami.  Badami was contracted by Sagar Movietone (Sagar Film Company) to direct \"Rama Paduka Pattabhishekham\" in Telugu.  The success of the film established him as a director.  He went on to direct \"Galava Rishi\" (Tamil), and \"Shakuntala\" in Telugu for Sagar Movietone.  Suryanarayana Yadavalli, who was a renowned stage actor played the lead role of Lord Rama in \"Rama Paduka Pattabhishekam\".  The film starred C. S. R. Anjaneyulu, Surabhi Kamalabai, Yadavalli Suryanarayana.\n\nJimmy Yuill: He is a member of the Royal Shakespeare Company and later joined the Renaissance Theatre Company.  He has appeared in many of Kenneth Branagh's films, most recently as Corin in the 2006 film \"As You Like It\".  Yuill was also the music composer for \"A Midwinter's Tale\" and \"Swan Song\".\n\nD.C. Follies: D.C. Follies is a syndicated sitcom which aired from 1987–1989 and was set in a Washington, D.C. bar, where bartender Fred Willard would welcome puppet caricatures of politicians and pop culture figures.  The show was satirical, and frequently commented on politicians and the political process.  Although Willard was the only live actor appearing regularly, each episode brought a celebrity guest into the bar, such as Martin Mull, Robin Leach, Bob Uecker, and Betty White.  In one episode, Robert Englund showed up as his Freddy Krueger character, and in a special Christmas episode an un-billed actor played Santa Claus.  Another episode had Mike Tyson confront his own puppet character.\n\nThemes in Titus Andronicus: Although traditionally Titus Andronicus has been seen as one of Shakespeare's least respected plays, its fortunes have changed somewhat in the latter half of the twentieth century, with numerous scholars arguing that the play is more accomplished than has hitherto been allowed for.  In particular, scholars have argued that the play is far more thematically complex than has traditionally been thought, and features profound insights into Ancient Rome, Elizabethan society, and the human condition.  Such scholars tend to argue that these previously unacknowledged insights have only become apparent during the twentieth and twenty-first centuries as only now has the ultraviolent content of the play achieved a sense of relevance.  For example, in his 1987 edition of the play for the \"Contemporary Shakespeare\" series, A.L. Rowse writes; \"in the civilised Victorian age the play could not be performed because it could not be believed.  Such is the horror of our own age, with the appalling barbarities of prison camps and resistance movements paralleling the torture and mutilation and feeding on human flesh of the play, that it has ceased to be improbable.\"  Similarly, director Julie Taymor, who staged a production Off-Broadway in 1994 and directed a film version in 1999, says she was drawn to the play because she found it to be the most \"relevant of Shakespeare's plays for the modern era;\" She feels that the play has more relevance for us than it had for the Victorians; \"it seems like a play written for today, it reeks of now.\"  Because of this new found relevance, previously unrecognised thematic strands have thus come to the forefront.\n\nRogues of Sherwood Forest: Rogues of Sherwood Forest is a 1950 Technicolor Columbia Pictures film directed by Gordon Douglas and featuring John Derek as Robin the Earl of Huntingdon, the son of Robin Hood, Diana Lynn as Lady Marianne, and Alan Hale, Sr. in his third movie as Little John over a 28-year span; he'd played the part opposite Douglas Fairbanks in 1922 and Errol Flynn in 1938, one of the longest periods over which any film actor played the same major role.  (Sylvester Stallone played Rocky Balboa over an even longer span, between 1976 and 2015.)  It was also Hale's final film.  The film was written by Ralph Gilbert Bettison and George Bruce.\n\nQuestion: What actor played a character that appears in both Shakespeare's play, \"As You Like It\", and the 2006 film, \"As You Like It\"?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"actor_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the actor.\"\n    },\n    \"character_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the character played by the actor.\"\n    },\n    \"play_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the Shakespearean play.\"\n    },\n    \"film_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the film adaptation.\"\n        },\n        \"year\": {\n          \"type\": \"integer\",\n          \"description\": \"The release year of the film.\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"year\"\n      ],\n      \"additionalProperties\": false\n    }\n  },\n  \"required\": [\n    \"actor_name\",\n    \"character_name\",\n    \"play_title\",\n    \"film_details\"\n  ],\n  \"additionalProperties\": false\n}"
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
      "play_title": {
        "type": "string",
        "description": "The title of the Shakespearean play."
      },
      "film_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the film adaptation."
          },
          "year": {
            "type": "integer",
            "description": "The release year of the film."
          }
        },
        "required": [
          "title",
          "year"
        ],
        "additionalProperties": false
      }
    },
    "required": [
      "actor_name",
      "character_name",
      "play_title",
      "film_details"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

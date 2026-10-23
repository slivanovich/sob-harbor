{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nThe Andromeda Strain (miniseries): The Andromeda Strain is a 2008 science fiction miniseries, based on the 1969 novel of the same name written by Michael Crichton about a team of scientists who investigate a deadly disease of extraterrestrial origin.  The miniseries is a \"reimagining\" of the original novel rather than an adaptation.  In addition to updating the setting to the early 21st century, the miniseries makes a great many plot and character changes from its source.  The mini-series has two episodes for a total of 169 minutes.\n\nSilent Running: Silent Running is a 1972 environmentally-themed American post-apocalyptic science fiction film starring Bruce Dern, featuring Cliff Potts, Ron Rifkin and Jesse Vint.  It was directed by Douglas Trumbull, who had previously worked as a special effects supervisor on science fiction films, including \"\" and \"The Andromeda Strain\".\n\nCarl Reindel: Carl Warren Reindel (January 20, 1935   September 4, 2009) was an American actor, known for portraying Lieutenant Kenneth M. Taylor in the epic war film \"Tora!  Tora!  Tora! \".  Reindel also played \"Stanton\" in Steve McQueen's hit film \"Bullitt\" and \"Lt. Comroe\" in classic science fiction film \"The Andromeda Strain\".  Reindel also made several appearances on popular TV series.  In 1964 he appeared on \"Perry Mason\" as defendant and title character Barry Davis in \"The Case of the Drifting Dropout,\" and in 1966 he played golf caddy and murderer Danny Bright in \"The Case of the Golfer's Gambit.\"  He also appeared on \"Gunsmoke\", \"The F.B.I.\", \"Bonanza\", \"The Virginian\" (as Carl Reindell), and \"Voyage to the Bottom of the Sea\", and also played the son of a man bent on vengeance on the western series Wagon Train before leaving show business in the early 1980s.  Reindel was born in Philadelphia, Pennsylvania and died of a heart attack at the age of 74, on September 4, 2009 in Valley Village, California.\n\nEve Harlow: In 2008 Harlow appeared in a science fiction miniseries \"The Andromeda Strain\".  She also showed up in a Leo Awards winning short film \"Paul Pontius\" and was cast as Tina Renwald in a Canadian television series \"The Guard\".  For this role Harlow won a Leo Award for Best Supporting Performance by a Female in a Dramatic Series in 2009 and was nominated for Gemini Award in 2010.\n\nThe Andromeda Strain: The Andromeda Strain is a 1969 techno-thriller novel by Michael Crichton documenting the efforts of a team of scientists investigating the outbreak of a deadly extraterrestrial microorganism in Arizona.  \"The Andromeda Strain\" appeared in the \"New York Times\" Best Seller list, establishing Michael Crichton as a genre writer.\n\nThe Andromeda Strain (film): The Andromeda Strain is a 1971 American science fiction film produced and directed by Robert Wise.  Based on Michael Crichton's 1969 novel of the same name and adapted by Nelson Gidding, the film stars Arthur Hill, James Olson, Kate Reid, and David Wayne as a team of scientists who investigate a deadly organism of extraterrestrial origin.  With a few exceptions, the film follows the book closely.  The special effects were designed by Douglas Trumbull.  The film is notable for its use of split screen in certain scenes.\n\nMichael Crichton: John Michael Crichton ( ; October 23, 1942 – November 4, 2008) was an American best-selling author, screenwriter, film director and producer best known for his work in the science fiction, medical fiction and thriller genres.  His books have sold over 200 million copies worldwide, and many have been adapted into films.\n\nLois H. Gresh: Lois Harriet Gresh is a New York Times Best-Selling author of ten science fiction novels and story collections and seventeen popular science and pop culture books, some in collaboration with Robert Weinberg.  Gresh has also written approximately sixty short stories.  Her work spans genres such as mysteries, thriller, suspense, dark fantasy, horror, and science fiction.  She is probably best known  for weird science fiction stories, which blend computer technology with biology, botany, and post-cyberpunk.  She was a staff book reviewer for \"Science Fiction Weekly\" from November 2004 through December 2008. \n\nA for Andromeda: A for Andromeda is a British television science fiction drama serial first made and broadcast by the BBC in seven parts in 1961.  Written by cosmologist Fred Hoyle, in conjunction with author and television producer John Elliot, it concerns a group of scientists who detect a radio signal from another galaxy that contains instructions for the design of an advanced computer.  When the computer is built, it gives the scientists instructions for the creation of a living organism named Andromeda, but one of the scientists, John Fleming, fears that Andromeda's purpose is to subjugate humanity.\n\nLarry Eisenberg: Lawrence (Larry) Eisenberg (born December 21, 1919) is a science fiction writer.  He is best known for his short story \"What Happened to Auguste Clarot? ,\" published in Harlan Ellison's anthology \"Dangerous Visions\".  Eisenberg's stories have also been printed in a number of leading science fiction magazines, including \"The Magazine of Fantasy and Science Fiction\", \"Galaxy Science Fiction\", and \"Asimov's Science Fiction\".  His stories have been reprinted in anthologies such as \"Great Science Fiction of the 20th Century\", \"The 10th Annual of the Year’s Best S-F\", and \"Great Science Fiction By the World's Great Scientists\".  He is also known for the limericks he posts in the comments sections of various articles in \"The New York Times\".\n\nQuestion: The Andromeda Strain is a 2008 science fiction miniseries, based on the 1969 novel of the same name, a team of scientists who investigate a deadly disease of extraterrestrial origin, written by which American best-selling author, screenwriter, film director and producer best known for his work in the science fiction, medical fiction and thriller genres?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"author_name\": {\n      \"type\": \"string\",\n      \"description\": \"The full name of the author.\"\n    },\n    \"author_nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the author.\"\n    },\n    \"author_professions\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of professions the author is known for.\"\n    },\n    \"author_primary_genres\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of genres the author is best known for.\"\n    },\n    \"novel_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the novel.\"\n    },\n    \"novel_publication_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The publication year of the novel.\"\n    },\n    \"miniseries_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the miniseries.\"\n    },\n    \"miniseries_release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the miniseries.\"\n    }\n  },\n  \"required\": [\n    \"author_name\",\n    \"author_nationality\",\n    \"author_professions\",\n    \"author_primary_genres\",\n    \"novel_title\",\n    \"novel_publication_year\",\n    \"miniseries_title\",\n    \"miniseries_release_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "author_name": {
        "type": "string",
        "description": "The full name of the author."
      },
      "author_nationality": {
        "type": "string",
        "description": "The nationality of the author."
      },
      "author_professions": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of professions the author is known for."
      },
      "author_primary_genres": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of genres the author is best known for."
      },
      "novel_title": {
        "type": "string",
        "description": "The title of the novel."
      },
      "novel_publication_year": {
        "type": "integer",
        "description": "The publication year of the novel."
      },
      "miniseries_title": {
        "type": "string",
        "description": "The title of the miniseries."
      },
      "miniseries_release_year": {
        "type": "integer",
        "description": "The release year of the miniseries."
      }
    },
    "required": [
      "author_name",
      "author_nationality",
      "author_professions",
      "author_primary_genres",
      "novel_title",
      "novel_publication_year",
      "miniseries_title",
      "miniseries_release_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

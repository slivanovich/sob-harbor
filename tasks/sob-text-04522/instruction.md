{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nKatharine McMahon: Katharine McMahon is a British writer born in north-west London.  She is an historical novelist who, since 1990, has published nine books.  Her latest, \"The Woman in the Picture\", was released in hardback on 3 July 2014 and in paperback on 30 July 2015.  McMahon is the best-selling author of \"The Rose of Sebastopol\" which was officially announced on 27 December 2007 as one of the ten titles for the Richard & Judy Book Club 2008.  McMahon’s book was subsequently reviewed on the Channel 4 Richard & Judy Show on 24 January 2008.  The Rose of Sebastopol was shortlisted for the Best Read Award at the Galaxy British Book Awards 2008, but received mixed reviews in North America during the following year.\n\nRain (short story): \"Rain\" is a short story by the British writer W. Somerset Maugham.  It was originally published as \"Miss Thompson\" in April 1921, in the American literary magazine \"The Smart Set\".\n\nW. Somerset Maugham: William Somerset Maugham CH ( ; 25 January 1874 – 16 December 1965), better known as W. Somerset Maugham, was a British playwright, novelist and short story writer.  He was among the most popular writers of his era and reputedly the highest-paid author during the 1930s.\n\nA Deal in Ostriches: \"A Deal in Ostriches\" is a short story by the British writer H. G. Wells.  It is a cautionary tale about simple human greed.  The taxidermist of Wells’ story \"Triumphs of a Taxidermist\" (1894) makes a return appearance as the narrator of the story.  The story was originally published anonymously in the December 20th, 1894 issue of the Pall Mall Gazette and later published in the 1895 short story collection \"The Stolen Bacillus and Other Incidents\".  The story is the tale of a carefully crafted and skillfully executed con that exploited the natural greed the protagonist's fellow passengers.\n\nThe Fallen Curtain: The Fallen Curtain is a short story collection by British writer Ruth Rendell.  The title story won the MWA Edgar Award for Best Short Story of the Year.\n\nJulia Gregson: Julia Gregson (born 1947) is a British writer of short stories and novels.  Her first published short story won Ryman's Literary Review Short story award.  In 2009, her novel \"East of the Sun\" won the Prince Maurice Prize for Literary Love stories, and the Romantic Novel of the Year Award by the Romantic Novelists' Association.\n\nHate (short story): \"Hate\" is a science fiction short story by British writer Arthur C. Clarke, first published in 1961 and subsequently included in several collections of Clarke's writings, including \"The Collected Stories of Arthur C. Clarke\".  The story originated when movie producer William MacQuitty asked Clarke to write a film treatment titled \"The Sea and the Stars\".  Nothing came of the project so Clarke transformed the treatment into a short story.  \"If\" magazine retitled it \"At the End of Orbit\" for publication but Clarke preferred his original title because it has \"more punch\" and it is under that title that the story has since been published.\n\nRain Shower: \"Rain Shower\", also \"Shower\" or \"Sonagi,\" (소나기) is a Korean short story written by Korean writer Hwang Sun-won in 1959.  \"Rain Shower\" is a translation of the Korean title “Sonagi.”  A sonagi is a brief but heavy rain shower that starts suddenly, usually on a hot afternoon.  In Hwang’s story, the rain shower symbolizes the short but heart-rending love between the boy and the girl.  The story begins with the boy encountering the girl playing by the stream on his way back home.\n\nThe New Girlfriend: The New Girlfriend and Other Stories is a short story collection by British writer Ruth Rendell.  The title story won the MWA Edgar Award for Best Short Story of the Year.\n\nChris Wooding: Chris Wooding (born 28 February 1977) is a British writer born in Leicester, and now living in London.  His first book, \"Crashing\", which he wrote at the age of nineteen, was published in 1998 when he was twenty-one.  Since then he has written many more, including \"The Haunting of Alaizabel Cray\", which was silver runner-up for the Nestlé Smarties Book Prize, and \"Poison\", which won the Lancashire Children's Book of the Year.  He is also the author of three different, completed series; \"Broken Sky\", an anime-influenced fantasy serial for children, \"Braided Path\", a fantasy trilogy for adults, and \"Malice\", a young adult fantasy that mixes graphic novel with the traditional novel; as well as another, four-part series, \"Tales of the Ketty Jay\", a steampunk sci-fi fantasy for adults.\n\nQuestion: \"Rain\" is a short story by a British writer born in what year?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"story_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the short story.\"\n    },\n    \"author_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the author of the short story.\"\n    },\n    \"author_nationality\": {\n      \"type\": \"string\",\n      \"description\": \"The nationality of the author.\"\n    },\n    \"author_birth_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The birth year of the author.\"\n    }\n  },\n  \"required\": [\n    \"story_title\",\n    \"author_name\",\n    \"author_nationality\",\n    \"author_birth_year\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "story_title": {
        "type": "string",
        "description": "The title of the short story."
      },
      "author_name": {
        "type": "string",
        "description": "The name of the author of the short story."
      },
      "author_nationality": {
        "type": "string",
        "description": "The nationality of the author."
      },
      "author_birth_year": {
        "type": "integer",
        "description": "The birth year of the author."
      }
    },
    "required": [
      "story_title",
      "author_name",
      "author_nationality",
      "author_birth_year"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

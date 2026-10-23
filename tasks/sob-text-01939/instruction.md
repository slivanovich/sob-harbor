{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nAdvanced Warriors: Advanced Warriors is an Interactive movie starring Jeremy Bulloch which was released in 2003.\n\nWar Horse (film): War Horse is a 2011 British war drama film directed and co-produced by Steven Spielberg from a screenplay written by Lee Hall and Richard Curtis, adapted from English author Michael Morpurgo's 1982 novel of the same name.  The film's cast includes Jeremy Irvine (in his film acting debut), Emily Watson, David Thewlis, Tom Hiddleston, Benedict Cumberbatch, Eddie Marsan, Niels Arestrup, Toby Kebbell, David Kross and Peter Mullan.  Set before and during World War I, it tells of the journey of Joey, a bay Thoroughbred horse raised by British teenager Albert (Irvine), as he is bought by the British Army, leading him to encounter numerous individuals and owners throughout Europe, all the while experiencing the tragedies of the war happening around him.\n\nBeyond the Reach: Beyond the Reach is a 2014 American adventure thriller film directed by Jean-Baptiste Léonetti and written by Stephen Susco.  It is based on the 1972 novel \"Deathwatch\" by Robb White.  The film, starring Michael Douglas, Jeremy Irvine, and Ronny Cox, was released on April 17, 2015, by Roadside Attractions.\n\nFallen (2016 film): Fallen is an American romantic fantasy film directed by Scott Hicks, based on the novel of same name by Lauren Kate.  The film stars Addison Timlin, Jeremy Irvine, Harrison Gilbertson, and Joely Richardson.\n\nMamma Mia: Here We Go Again!: Mamma Mia: Here We Go Again!  is an upcoming American romantic comedy musical film directed and written by Ol Parker.  It is based on the musical of same name and a sequel to 2008 film \"Mamma Mia! \" The film stars Amanda Seyfried, Dominic Cooper, Meryl Streep, Lily James, Colin Firth, Pierce Brosnan, and Jeremy Irvine.  It is scheduled to be released on July 20, 2018, 10 years after the original, by Universal Pictures.  The film is currently in production.\n\nNow Is Good: Now Is Good is a 2012 British teen drama film directed by Ol Parker.  Based on the 2007 novel \"Before I Die\" by Jenny Downham, it was adapted by Parker who had recently written the screenplay for \"The Best Exotic Marigold Hotel\".  The film, which stars Dakota Fanning, Jeremy Irvine and Paddy Considine, centres on Tessa, a girl who is dying of leukaemia and tries to enjoy her remaining life as much as she possibly can.\n\nGreat Expectations (2012 film): Great Expectations is a 2012 British film adaptation of Charles Dickens' novel of the same name.  The film was directed by Mike Newell, with the adapted screenplay by David Nicholls, and stars Jeremy Irvine, Helena Bonham Carter, Holliday Grainger, Ralph Fiennes and Robbie Coltrane.  It was distributed by Lionsgate.\n\nA Night in Old Mexico: A Night in Old Mexico is a 2013 Spanish-American co-production film directed by Emilio Aragón about a man (Robert Duvall) and his grandson (Jeremy Irvine).\n\nJeremy Irvine: Jeremy William Fredric Smith (born 18 June 1990), better known as Jeremy Irvine, is an English actor who made his film debut in the epic war film \"War Horse\" (2011).  In 2012, he portrayed Philip \"Pip\" Pirrip in the film adaptation of \"Great Expectations\", and earned widespread critical acclaim for his role in the independent film \"Now Is Good\" (2012).\n\nThe Railway Man (film): The Railway Man is a 2013 British–Australian war film directed by Jonathan Teplitzky.  It is an adaptation of the autobiography \"The Railway Man\" by Eric Lomax, and stars Colin Firth, Nicole Kidman, Jeremy Irvine, and Stellan Skarsgård.  It premiered at the 2013 Toronto International Film Festival on 6 September 2013.\n\nQuestion: which movie starring Jeremy Irvine is based on the novel Before I Die\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"movie_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the movie.\"\n    },\n    \"release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the movie.\"\n    },\n    \"director\": {\n      \"type\": \"string\",\n      \"description\": \"The director of the movie.\"\n    },\n    \"based_on_novel\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the novel the movie is based on.\"\n    },\n    \"novel_author\": {\n      \"type\": \"string\",\n      \"description\": \"The author of the novel.\"\n    },\n    \"starring_actors\": {\n      \"type\": \"array\",\n      \"items\": {\n        \"type\": \"string\"\n      },\n      \"description\": \"A list of main actors starring in the movie.\"\n    }\n  },\n  \"required\": [\n    \"movie_title\",\n    \"release_year\",\n    \"director\",\n    \"based_on_novel\",\n    \"novel_author\",\n    \"starring_actors\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "movie_title": {
        "type": "string",
        "description": "The title of the movie."
      },
      "release_year": {
        "type": "integer",
        "description": "The release year of the movie."
      },
      "director": {
        "type": "string",
        "description": "The director of the movie."
      },
      "based_on_novel": {
        "type": "string",
        "description": "The title of the novel the movie is based on."
      },
      "novel_author": {
        "type": "string",
        "description": "The author of the novel."
      },
      "starring_actors": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of main actors starring in the movie."
      }
    },
    "required": [
      "movie_title",
      "release_year",
      "director",
      "based_on_novel",
      "novel_author",
      "starring_actors"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

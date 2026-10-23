{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nA Long Way Down (film): A Long Way Down is a 2014 British black comedy film directed by Pascal Chaumeil, loosely based on author Nick Hornby's 2005 novel, \"A Long Way Down\".  It stars Pierce Brosnan, Toni Collette, Imogen Poots, and Aaron Paul as four strangers who happen to meet on the roof of a London building on New Year's Eve, each with the intent of committing suicide.  Their plans for death in solitude are ruined when they meet as they decide to come down from the roof alive — however temporary that may be.\n\nKemper: The CoEd Killer: Kemper: The CoEd Killer is a 2008 American direct-to-video horror film directed by Rick Bitzelberger, and written by Jack Perez.  The film is loosely based on the murders committed by California serial killer Edmund Kemper.\n\nBurke &amp; Hare (2010 film): Burke & Hare is a 2010 British black comedy film, loosely based on the Burke and Hare murders.  Directed by John Landis, the film stars Simon Pegg and Andy Serkis as William Burke and William Hare respectively.  It was Landis's first feature film release in 12 years, the last being 1998's \"Susan's Plan\".  The film was released in the United Kingdom on 29 October 2010.\n\nMurder by Decree: Murder by Decree is a 1979 British-Canadian mystery thriller film directed by Bob Clark.  It features the Sherlock Holmes and Dr John Watson characters created by Sir Arthur Conan Doyle, who are embroiled in the investigation surrounding the real-life 1888 Whitechapel murders committed by \"Jack the Ripper\".  Christopher Plummer plays Holmes and James Mason plays Watson.  Though it features a similar premise, it is notably different in tone and result to \"A Study in Terror\".  It is loosely based on \"The Ripper File\" by Elwyn Jones and John Lloyd.\n\nAtlanta murders of 1979–81: The Atlanta murders of 1979–1981, sometimes called the Atlanta Child Murders (although several of the purported victims were adults), were a series of murders committed in the American city of Atlanta, Georgia, from the middle of 1979 until May 1981.  Over the two-year period, at least 28 African-American children, adolescents and adults were killed.  Wayne Williams, an Atlanta native who was 23 years old at the time of the last murder, was arrested for and convicted of two of the adult murders, and sentenced to two consecutive life terms.  Police subsequently have attributed a number of the child murders to Williams and closed the cases, although he has not been tried or convicted in any of those cases.\n\nBurke and Hare murders: The Burke and Hare murders were a series of 16 murders committed over a period of about ten months in 1828 in Edinburgh, Scotland.  The killings were undertaken by William Burke and William Hare, who sold the corpses to Doctor Robert Knox for dissection at his anatomy lectures.\n\nUncle David: Uncle David is a 2010 British black comedy film directed by David Hoyle, Gary Reich, and Mike Nicholls.  It was produced by Reich and stars Hoyle, an English performance artist, in the titular role alongside English pornographic actor Ashley Ryder.  Developed collectively under the banner of the Avant-Garde Alliance, it was filmed in October 2009.  Created without a script, every scene was improvised and filmed in a single take.\n\nKind Hearts and Coronets: Kind Hearts and Coronets is a 1949 British black comedy film.  It features Dennis Price, Joan Greenwood, Valerie Hobson and Alec Guinness; Guinness plays nine characters.  The plot is loosely based on the novel \"Israel Rank: The Autobiography of a Criminal\" (1907) by Roy Horniman.  It concerns Louis D'Ascoyne Mazzini, the son of a woman disowned by her aristocratic family for marrying out of her social class.  After her death Louis decides to take revenge on the family, and to take the dukedom, by murdering the eight people ahead of him in succession to the title.\n\nThe Tarnished Eye: The Tarnished Eye is a 2004 crime novel by Judith Guest, based on the Robison family murders that occurred in June 1968 in Good Hart, Michigan and the murders committed by John Norman Collins in the Ann Arbor and Ypsilanti areas of Michigan in the late 1960s.  In an interview with Metro Times,Guest explained why she chose to write a fictionalized account of these two murder cases: \"I’m very interested in people’s motivations, why they do the things they do, why go to such extremes as if that’s the only solution to their problem.  Those two crimes laid awake in my mind for a long time, and, about five years ago, I decided to write about them, but write a novel.\"\n\nSmooth Talk: Smooth Talk is a 1985 drama film, loosely based on Joyce Carol Oates' 1966 short story \"Where Are You Going, Where Have You Been? \", which was in turn inspired by the Tucson murders committed by Charles Schmid.  The protagonist and main character, Connie Wyatt, is played by Laura Dern.  The antagonist, Arnold Friend, is played by Treat Williams.\n\nQuestion: This 2010 British black comedy film was loosely based on a series of murders committed over a period about how long?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film.\"\n    },\n    \"film_release_year\": {\n      \"type\": \"integer\",\n      \"description\": \"The release year of the film.\"\n    },\n    \"film_genre\": {\n      \"type\": \"string\",\n      \"description\": \"The genre of the film.\"\n    },\n    \"based_on_murders\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the murder series the film is based on.\"\n    },\n    \"murder_duration_months\": {\n      \"type\": \"integer\",\n      \"description\": \"The approximate duration of the murder series in months.\"\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"film_release_year\",\n    \"film_genre\",\n    \"based_on_murders\",\n    \"murder_duration_months\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film."
      },
      "film_release_year": {
        "type": "integer",
        "description": "The release year of the film."
      },
      "film_genre": {
        "type": "string",
        "description": "The genre of the film."
      },
      "based_on_murders": {
        "type": "string",
        "description": "The name of the murder series the film is based on."
      },
      "murder_duration_months": {
        "type": "integer",
        "description": "The approximate duration of the murder series in months."
      }
    },
    "required": [
      "film_title",
      "film_release_year",
      "film_genre",
      "based_on_murders",
      "murder_duration_months"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}

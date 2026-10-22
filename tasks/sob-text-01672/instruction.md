Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Jessica Darling: The Jessica Darling books are a "The New York Times" bestselling series of five young adult novels by Megan McCafferty, published between 2001 and 2009.  Told from the diary-style perspective of character Jessica Darling, the series chronicles her misadventures through high school, college, and beyond.  McCafferty also published a Jessica Darling short story called "Fifteen Going On ..." in a 2004 anthology she edited called "Sixteen: Stories About That Sweet and Bitter Birthday".

Plum Stones: Plum Stones are 12 volumes of uncollected short stories by P.G. Wodehouse, all previously published in magazines.  Each contains a different character (as in Plum Pie).  They were published posthumously in 1993 in the UK in a limited edition by Galahad Books.  One of the stories is a Bobbie Wickham story called "Dudley Is Back to Normal".  Another, "Reggie and the Greasy Bird", has nothing to do with Jeeves and the Greasy Bird, but is a rewrite of "The Masked Troubadour".

The Red Convertible (1984): "The Red Convertible" is a short story from "Love Medicine", a collection of narratives written in 1974 by American author Louise Erdrich.

The Sea and Little Fishes: "The Sea and Little Fishes" is a short story by Terry Pratchett, written in 1998.  It is set in his "Discworld" universe, and features Lancre witches Granny Weatherwax and Nanny Ogg.  It was originally published in a sampler alongside a story called "The Wood Boy" by Raymond E. Feist, and later in a collection called "Legends".

Lassie: Lassie is a fictional character created by Eric Knight; she is a female Rough Collie dog, and is featured in a short story that was later expanded to a full-length novel called "Lassie Come-Home".  Knight's portrayal of Lassie bears some features in common with another fictional female collie of the same name, and is featured in the British writer Elizabeth Gaskell's 1859 short story called "The Half Brothers."  In "The Half Brothers", Lassie is loved only by her young master and guides the adults back to where two boys are lost in a snowstorm.

The Little Match Girl: "The Little Match Girl" (Danish: "Den Lille Pige med Svovlstikkerne" , meaning "The little girl with the matchsticks") is a short story by Danish poet and author Hans Christian Andersen.  The story, about a dying child's dreams and hope, was first published in 1845.  It has been adapted to various media, including an animated short film, a television musical, and an animated virtual reality story called "Allumette".

Manoos: Manoos, also called "Life's for Living", is a 1939 Indian Marathi social melodrama film directed by V. Shantaram.  The movie then remade in Hindi as "Aadmi".  The film was based on a short story called "The Police Constable".  The story was by A. Bhaskarrao with screenplay and dialogue by Anant Kanekar.  The cinematographer was V. Avadhoot and the music was composed by Master Krishna Rao with lyrics by Kanekar.  The cast included Shahu Modak, Shanta Hublikar, Sundara Bai, Ram Marathe, Narmada, Ganpatrao, Raja Paranjpe.

The Little Shop of Horrors: The Little Shop of Horrors is a 1960 American black comedy horror film directed by Roger Corman.  Written by Charles B. Griffith, the film is a farce about an inadequate florist's assistant who cultivates a plant that feeds on human flesh and blood.  The film's concept is thought to be based on a 1932 story called "Green Thoughts", by John Collier, about a man-eating plant.  However, Dennis McDougal in Jack Nicholson's biography suggests that Griffith may have been influenced by Arthur C. Clarke's sci-fi short story from 1956, "The Reluctant Orchid" (which was in turn inspired by the 1905 H. G. Wells story "The Flowering of the Strange Orchid").  Mythology about man-eating plants dates back to at least the 1800s, and probably much earlier.

Landscape After the Battle: Landscape After the Battle (Polish: Krajobraz po bitwie ) is a 1970 Polish drama film directed by Andrzej Wajda and starring Daniel Olbrychski; telling a story of a Nazi German concentration camp survivor soon after liberation, residing in a DP camp somewhere in Germany.  It is based on the writings of Holocaust survivor and Polish author Tadeusz Borowski.  In most part, the plot revolves around the events depicted in Borowski's short story called "Bitwa pod Grunwaldem" ("The Battle of Grunwald") from his collection "This Way for the Gas, Ladies and Gentlemen".  The film was entered into the 1970 Cannes Film Festival.

Love Medicine: Love Medicine is Louise Erdrich’s first novel, published in 1984.  Erdrich revised and expanded the novel for an edition issued in 1993, and then revised it again for the 2009 edition.  The book explores 60 years in the lives of a small group of Chippewa (also known as Ojibwa or Anishinaabe) living on an unnamed Ojibwe Reservation in North Dakota (possibly based on the Turtle Mountain Indian Reservation).  "Love Medicine" won the 1984 National Book Critics Circle Award.

Question: What was published in 1984 and contains a short story called "The Red Convertible"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "publication_title": {
      "type": "string",
      "description": "The title of the publication that matches the criteria."
    },
    "publication_year": {
      "type": "integer",
      "description": "The year the publication was published."
    },
    "author": {
      "type": "string",
      "description": "The author of the publication."
    },
    "contained_short_story_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the short story contained within the publication."
        },
        "author": {
          "type": "string",
          "description": "The author of the short story."
        },
        "original_writing_year": {
          "type": "integer",
          "description": "The year the collection of narratives (including the short story) was written."
        }
      },
      "required": [
        "title",
        "author",
        "original_writing_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "publication_title",
    "publication_year",
    "author",
    "contained_short_story_details"
  ],
  "additionalProperties": false
}

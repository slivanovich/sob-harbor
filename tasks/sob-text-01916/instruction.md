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
The Bible (miniseries): The Bible is a television miniseries based on the Bible.  It was produced by Roma Downey and Mark Burnett and was broadcast weekly between March 3 and March 31, 2013 on History channel.  It has since been adapted for release to theaters as a feature film (138 minutes), the 2014 American epic biblical drama "Son of God".

The Fountain: The Fountain is a 2006 American epic magical realism romantic drama film that blends elements of fantasy, history, spirituality, and science fiction.  It is directed by Darren Aronofsky, and stars Hugh Jackman and Rachel Weisz.  The film consists of three storylines involving immortality and the resulting loves lost, and one man's pursuit of avoiding this fate in this life or beyond it.  Jackman and Weisz play sets of characters bonded by love across time and space: a conquistador and his ill-fated queen, a modern-day scientist and his cancer-stricken wife, and a traveler immersed in a universal journey alongside aspects of his lost love.  The storylines—interwoven with use of match cuts and recurring visual motifs—reflect the themes and interplay of love and mortality.

Pi (film): Pi, also titled π , is a 1998 American surrealist psychological thriller film written and directed by Darren Aronofsky in his directorial debut.  The film earned Aronofsky the Directing Award at the 1998 Sundance Film Festival, the Independent Spirit Award for Best First Screenplay and the Gotham Open Palm Award.  The title refers to the mathematical constant pi.  The film is notable for its covering of an array of themes including religion, mysticism and the relationship of the universe to mathematics.

Exodus: Gods and Kings: Exodus: Gods and Kings is a 2014 epic biblical drama film directed by Ridley Scott.  An international co-production between the United States, the United Kingdom, and Spain, it was produced by Peter Chernin, Ridley Scott, Jenno Topping, Michael Schaefer and Mark Huffam with music by Alberto Iglesias and written by Adam Cooper, Bill Collage, Jeffrey Caine and Steven Zaillian.  The film stars Christian Bale, Joel Edgerton, John Turturro, Aaron Paul, Ben Mendelsohn, María Valverde, Sigourney Weaver, Ghassan Massoud, Indira Varma, Golshifteh Farahani and Ben Kingsley.  It is inspired by the biblical episode of the exodus of the Hebrews from Egypt as led by Moses and related in the Book of Exodus.

Ari Handel: Ari Handel (born in Zürich, Switzerland) is an American neuroscientist, film producer, and writer.  He is known for co-writing the films "Noah" and "The Fountain" with his Harvard Dunster House suitemate Darren Aronofsky and for helping to produce these films along with two other Darren Aronofsky films, "The Wrestler" and "Black Swan".  He started co-writing the film "Noah" around 2003.

Son of God (film): Son of God is a 2014 American epic biblical drama film, produced by Mark Burnett and Roma Downey.  The film premiered in New York, and Los Angeles for a limited release on February 21, 2014, and then into a wide release on February 28, 2014.  The film retells the life of Jesus and is an adaptation of the ten-hour miniseries "The Bible", which aired in March 2013 on the History channel.

The Wrestler (2008 film): The Wrestler is a 2008 American sports drama film co-produced and directed by Darren Aronofsky, written by Robert D. Siegel, and starring Mickey Rourke, Marisa Tomei, and Evan Rachel Wood.  Production began in January 2008 and Fox Searchlight Pictures acquired rights to distribute the film in the U.S.; it was released in a limited capacity on December 17, 2008, and was released nationwide on January 23, 2009.  It was released on DVD and Blu-ray Disc on April 21, 2009, in the United States.  It was released in the United Kingdom on June 1, 2009.

Requiem for a Dream (disambiguation): Requiem for a Dream is a 2000 American drama film directed by Darren Aronofsky

Requiem for a Dream: Requiem for a Dream is a 2000 American psychological drama film directed by Darren Aronofsky and starring Ellen Burstyn, Jared Leto, Jennifer Connelly, and Marlon Wayans.  The film is based on the novel of the same name by Hubert Selby, Jr., with whom Aronofsky wrote the screenplay.

Noah (2014 film): Noah is a 2014 American epic biblical drama film directed by Darren Aronofsky and inspired by the Biblical story of Noah's Ark from the "Book of Genesis".  The film, which was co-written by Aronofsky and Ari Handel, stars Russell Crowe as Noah, along with Jennifer Connelly, Emma Watson, Ray Winstone, Logan Lerman, Douglas Booth, and Anthony Hopkins.  The film was released in North American theaters on March 28, 2014, in 2D and IMAX, while a version of the film converted to 3D and IMAX 3D was released in several other countries.

Question: Which of the film that Ari Handel co-wrote is a 2014 American epic biblical drama film directed by Darren Aronofsky?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film that meets the criteria."
    },
    "release_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "is_american_production": {
      "type": "boolean",
      "description": "Indicates if the film is an American production."
    },
    "genre_type": {
      "type": "string",
      "description": "The specific genre description of the film, e.g., 'epic biblical drama'."
    },
    "director_name": {
      "type": "string",
      "description": "The name of the film's director."
    },
    "co_writer_name": {
      "type": "string",
      "description": "The name of the film's co-writer."
    }
  },
  "required": [
    "film_title",
    "release_year",
    "is_american_production",
    "genre_type",
    "director_name",
    "co_writer_name"
  ],
  "additionalProperties": false
}

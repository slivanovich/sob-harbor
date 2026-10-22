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
The Cat in the Hat (TV special): The Cat in the Hat is an American animated musical television special first aired on CBS on March 10, 1971, based on the 1957 Dr. Seuss children's book of the same name, and produced by DePatie-Freleng Enterprises.  With voices by Allan Sherman and prolific vocal performer Daws Butler, this half-hour special is a loose adaptation with added musical sequences.

Tolkien Estate: The Tolkien Estate is the legal body which manages the property of the English writer J. R. R. Tolkien, including the copyright for most of his works.  The individual copyrights have for the most part been assigned by the Estate to subsidiary entities such as the J. R. R. Tolkien Discretionary Settlement and the Tolkien charitable Trust.  The various holdings of the Tolkien family, including the Estate, have been organised under The Tolkien Company, the directors of which are Christopher Tolkien, his wife Baillie Tolkien, and J. R. R. Tolkien's grandson Michael George Tolkien.  The executors of the Estate proper are Christopher Tolkien, who is sole literary executor, and (succeeding J. R. R. Tolkien's lawyer Frank Williamson) Cathleen Blackburn of Maier Blackburn, who has also been the Estate's solicitor for many years.

The Hobbit (1977 film): The Hobbit is a 1977 animated musical television special created by Rankin/Bass, a studio known for their holiday specials, and animated by Topcraft, a precursor to Studio Ghibli, using lyrics adapted from the book.  The film is an adaptation of the 1937 book of the same name by J. R. R. Tolkien and was first broadcast on NBC in the United States on Sunday, November 27, 1977.

Pontoffel Pock, Where Are You?: Pontoffel Pock, Where Are You?  (titled Pontoffel Pock & His Magic Piano for the sing-a-long videocasette release) is an animated musical television special written by Dr. Seuss, directed by Gerard Baldwin, produced by DePatie-Freleng Enterprises, completed in 1979 and first aired on ABC on May 2, 1980.  This was one of the final cartoons done at DePatie-Freleng as the studio would be sold to Marvel Comics and become Marvel Productions in 1981.  The songs are by Joe Raposo.

The Return of the King (1980 film): The Return of the King (also known as The Return of the King: A Story of the Hobbits), is a 1979 animated musical television film created by Rankin/Bass and Topcraft.  The film is an adaptation of "The Return of the King", the third book in "The Lord of the Rings" by J. R. R. Tolkien.

Dr. Seuss on the Loose: Dr. Seuss on the Loose (titled Green Eggs and Ham and Other Stories for the sing-a-long videocasette release and the deluxe edition releases) is an animated musical television special, first airing on CBS on October 15, 1973, and hosted by The Cat in the Hat who appears in bridging sequences where he introduced animated adaptations of Dr. Seuss children's stories "The Sneetches", "The Zax" and "Green Eggs and Ham".  Allan Sherman reprised his role as the voice of The Cat in the Hat from the 1971 television special.  This was the final project Sherman worked on before his death.

How Murray Saved Christmas: How Murray Saved Christmas is a 2014 animated musical television special, directed by Peter Avanzino and written by Mike Reiss.  The voice actors include Jerry Stiller, Sean Hayes, Kevin Michael Richardson, Jason Alexander, John Ratzenberger and Dennis Haysbert.

The Wind in the Willows (TV series): The Wind in the Willows is a TV series that was originally broadcast between 1984 and 1987, based on characters from Kenneth Grahame's classic story "The Wind in the Willows" and following the 1983 film "The Wind in the Willows".  It was made by animation company Cosgrove Hall for Thames Television and shown on the ITV network.  An hour-long feature, "A Tale Of Two Toads", was broadcast in 1989, and a fifth season of 13 episodes was shown in 1990 under the title "Oh!  Mr Toad" in some countries, whilst retaining the title "The Wind in the Willows" in others.

The Wind in the Willows (1987 film): The Wind in the Willows is a 1987 American animated musical television film directed by Arthur Rankin, Jr. and Jules Bass.  It is an adaptation of "The Wind in the Willows" by Kenneth Grahame.  Set in a pastoral version of England, the film focuses on four anthropomorphised animal characters (Moley, Ratty, Mr. Toad, and Mr. Badger) and contains themes of mysticism, adventure, morality, and camaraderie.  The film features the voices of Charles Nelson Reilly, Roddy McDowall, José Ferrer, and Eddie Bracken.  The screenplay was written by Romeo Muller, a long-time Rankin/Bass writer whose work included "Rudolph the Red-Nosed Reindeer", "The Hobbit", and "The Flight of Dragons", among others.

Jack DeLeon: Jack DeLeon (December 19, 1924 – October 16, 2006) was an American actor.  He is best known for playing Marty Morrison on the television series "Barney Miller" from 1975 to 1982.  In 1972, he appeared in an episode of "Emergency! " ("Show Biz") as Billy Zimmer from an advertising agency.  His film credits included "Linda Lovelace for President" (1975), "I Wonder Who's Killing Her Now? " (1975), "The Choirboys" (1977) and "Little Miss Marker" (1980), and he voiced Sergeant Samuel McPherson in the 1977 Dr. Seuss animated television special "Halloween Is Grinch Night".  He was also known for the voice of Dwalin in the 1977 animated version of "The Hobbit".

Question: On which channel was this J. R. R. Tolkien inspired 1977 animated musical television special written by the same writer responsible for "The Wind in the Willows" broadcast?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "special_title": {
      "type": "string",
      "description": "The title of the animated musical television special."
    },
    "inspiration_author": {
      "type": "string",
      "description": "The author whose work inspired the special."
    },
    "broadcast_year": {
      "type": "integer",
      "description": "The year the special was first broadcast."
    },
    "screenwriter": {
      "type": "string",
      "description": "The writer responsible for the screenplay of the special."
    },
    "broadcast_channel": {
      "type": "string",
      "description": "The television channel on which the special was first broadcast."
    }
  },
  "required": [
    "special_title",
    "inspiration_author",
    "broadcast_year",
    "screenwriter",
    "broadcast_channel"
  ],
  "additionalProperties": false
}

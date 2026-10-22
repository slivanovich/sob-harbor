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
Marshall Brickman: Marshall Brickman (born August 25, 1939) is an American screenwriter and director, best known for his collaborations with Woody Allen.  He is the co-recipient of the 1977 Academy Award for Best Original Screenplay for "Annie Hall".  He is also known for playing the banjo with Eric Weissberg in the 1960s, and for a series of comical parodies published in "The New Yorker".

Sleeper (1973 film): Sleeper is a 1973 American futuristic science fiction comedy film, directed by Woody Allen and written by Allen and Marshall Brickman.  The plot involves the adventures of the owner of a health food store who is cryogenically frozen in 1973 and defrosted 200 years later in an ineptly led police state.  The film contains many elements which parody notable works of science fiction and was made as a tribute to comedians Groucho Marx and Bob Hope.

Manhattan Murder Mystery: Manhattan Murder Mystery is a 1993 American comedy murder mystery film directed by Woody Allen, co-written by Allen and Marshall Brickman, and starring Allen, Diane Keaton, Anjelica Huston and Alan Alda.  The film centers on a married couple's investigation of the death of their neighbor's wife.

Annie Hall: Annie Hall is a 1977 American romantic comedy film directed by Woody Allen from a screenplay he co-wrote with Marshall Brickman.  Produced by Allen's manager, Charles H. Joffe, the film stars the director as Alvy "Max" Singer, who tries to figure out the reasons for the failure of his relationship with the film's eponymous female lead, played by Diane Keaton in a role written specifically for her.

Manhattan (film): Manhattan is a 1979 American romantic comedy film directed by Woody Allen and produced by Charles H. Joffe.  The screenplay was written by Allen and Marshall Brickman.  Allen co-stars as a twice-divorced 42-year-old comedy writer who dates a 17-year-old girl (Mariel Hemingway) but falls in love with his best friend's (Michael Murphy) mistress (Diane Keaton).  Meryl Streep and Anne Byrne also star.

Lovesick (1983 film): Lovesick is a 1983 American romantic comedy film written and directed by Marshall Brickman.  It stars Dudley Moore and Elizabeth McGovern and features Alec Guinness as the ghost of Sigmund Freud.

Simon (1980 film): Simon is a 1980 American comedy film.  It was written and directed by Marshall Brickman and stars Alan Arkin.

The Manhattan Project (film): The Manhattan Project is an American film, released in 1986.  Named after the World War II-era program that constructed the first atomic bombs, the plot revolves around a gifted high school student who decides to construct an atomic bomb for a national science fair.  It was directed by Marshall Brickman, based upon his screenplay co-written with Thomas Baum, and starred Christopher Collet, John Lithgow, John Mahoney, Jill Eikenberry and Cynthia Nixon.  This was the first production from short-lived Gladden Entertainment.

The Addams Family (musical): The Addams Family is a musical comedy with music and lyrics by Andrew Lippa and the book by Marshall Brickman and Rick Elice.  The show is based upon "The Addams Family" characters created by Charles Addams in his single-panel gag cartoons, which depict a ghoulish American family with an affinity for all things macabre.  Although numerous film and television adaptations of Addams' cartoons exist, the musical is the first stage show based on the characters.  "The Addams Family" is also the first show produced by Elephant Eye Theatricals.

The New Yorker: The New Yorker is an American magazine of reportage, commentary, criticism, essays, fiction, satire, cartoons, and poetry.  It is published by Condé Nast.  Started as a weekly in 1925, the magazine is now published 47 times annually, with five of these issues covering two-week spans.

Question: Who is the publisher of the American magazine who published a series of comical parodies by Marshall Brickman?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_who_published_content": {
      "type": "string",
      "description": "The name of the person who published content in the magazine."
    },
    "magazine_name": {
      "type": "string",
      "description": "The name of the American magazine."
    },
    "content_type_published": {
      "type": "string",
      "description": "The type of content published by the person in the magazine."
    },
    "publisher_name": {
      "type": "string",
      "description": "The name of the publisher of the magazine."
    }
  },
  "required": [
    "person_who_published_content",
    "magazine_name",
    "content_type_published",
    "publisher_name"
  ],
  "additionalProperties": false
}

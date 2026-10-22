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
Lord of the Rings (musical): The Lord of the Rings is the most prominent of several theatre adaptations of J. R. R. Tolkien's epic high fantasy book series of the same name, with music by A. R. Rahman, Christopher Nightingale and the band Värttinä, and book and lyrics by Matthew Warchus and Shaun McKenna.

Steve Weston: Steve Weston (1940 - May 12, 1985) was a Canadian television and theatre actor.  He is best known to Canadian audiences from his stint as the husband in the sitcom "The Trouble With Tracy", and as a series regular on the sketch comedy series "Bizarre".  However, he was also an accomplished stage actor and once played the role of Gooper Pollitt in a Toronto production of "Cat on a Hot Tin Roof".

Nonnie Griffin: Nonnie Griffin was born in 1933 in Canada.  She studied at the Toronto Conservatory in her native land, the Royal Academy of Dramatic Arts in London, and even with famed mime artist Marcel Marceau.  Her stage work includes playing Mrs. Rafi in the original Toronto production of "The Sea" and a 10-month run as the title character in "Hello, Dolly! " at the Limelight Dinner Theatre in Toronto in 1990.

Let the Right One In (franchise): Let the Right One In is a horror media franchise encompassing a book, two films, a comic book series, several theatre productions and an upcoming television series.

Over the Rainbow (Canadian TV series): Over the Rainbow is a Canadian reality talent competition, which premiered on CBC Television on September 16, 2012.  Based on the 2010 series "Over the Rainbow" in the United Kingdom, the series auditioned aspiring musical theatre performers for the role of Dorothy for a Toronto production of Andrew Lloyd Webber's stage musical adaptation of "The Wizard of Oz".  The series was hosted by Daryn Jones.  Arlene Phillips, Thom Allison, and Louise Pitre served as judges alongside Webber.

Evan Buliung: Evan Buliung is a Canadian actor.  He has played roles on stage and in musical theatre, including the role of Aragorn in the Toronto production of "Lord of the Rings", Khashoggi in "We Will Rock You", William Burke in "Bloodless: The Trial of Burke and Hare" and Pericles in the Stratford Festival's 2015 production of "The Adventures of Pericles".

James Cade: James Cade is a Toronto-based actor.  He graduated from the National Theatre School of Canada and has since then performed in several theatre productions in Toronto, including Single Threat's Dora Award winning production of "A Quiet Place."  Other theatre companies James has worked with include Unspun Theatre, Crate Productions, Convergence Theatre and Native Earth Performing Arts.

Jeremy Ferdman: First seen in the Toronto production of "Flora, the Red Menace", Ferdman started his acting career performing on stage.  In 2003, he began his television career with a walk-on role in Queer As Folk.  Since then, he has starred in several films including the critically acclaimed 2005 film, "Stock Boy", and the award-winning short film "Dirty Talk", which he \ co-wrote and Produced.  At an early age, he appeared in several memorable commercials for Rogers Wireless, McDonald's, and 23 Degrees Coffee.  He has also appeared in various award-winning television shows including NBC's Angela's Eyes, the FXX series "Man Seeking Woman", Lifetime's Killer Kids, ABC's "Home for the Holidays" and Syfy's Warehouse 13.

Illya Woloshyn: Illya Woloshyn is a Canadian actor of Ukrainian descent.  He started acting at a very young age, playing the role of Jacob in Jacob Two Two Meets the Hooded Fang at Young People's Theatre in Toronto, and later Gavroche in the original Toronto production of Les Misérables at the Royal Alexandra Theatre in 1988.  He later joined the touring production and performed the role in theatres across Canada.

Alberta Opera: Alberta Opera Musical Theatre for Young People, based in Edmonton, Alberta, Canada, is the major touring Theatre for Young Audiences company in Alberta.  It has been presenting original musical theatre adaptations in schools in British Columbia, Saskatchewan and Alberta since 1984 and its repertoire includes such fairytales as "Rapunzel", "Puss in Boots", "Cinderella", "Sleeping Beauty", "Rumplestiltskin", "The Frog Prince", "The Red Shoes", and the Elizabeth Sterling Haynes Award-winning "Jack and the Beanstalk".  Besides exploring traditional themes with contemporary eyes, Alberta Opera offers 16 students the chance to actively participate in each production as actors and stagehands.

Question: Evan Buliung played the role of Aragorn in the Toronto production of the most prominent of several theatre adaptations of what kind of book series?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor."
    },
    "role_played": {
      "type": "string",
      "description": "The role played by the actor."
    },
    "production_title": {
      "type": "string",
      "description": "The title of the theatre production."
    },
    "production_location": {
      "type": "string",
      "description": "The location where the production took place."
    },
    "book_series_genre": {
      "type": "string",
      "description": "The genre of the book series that the production is adapted from."
    }
  },
  "required": [
    "actor_name",
    "role_played",
    "production_title",
    "production_location",
    "book_series_genre"
  ],
  "additionalProperties": false
}

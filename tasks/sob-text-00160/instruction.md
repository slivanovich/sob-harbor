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
Hairshirt (film): Hairshirt (released to home video as Too Smooth) is a 1998 romantic comedy film starring Dean Paras, Neve Campbell, Katie Wright, Rebecca Gayheart and Stefan Brogren.

Litza Bixler: Litza Bixler (born 25 August 1970) is an American and British film choreographer, Artistic Director and Writer.  She is best known for her work with Edgar Wright<ref name="Wright/Pegg/Frost Interview"> </ref> on "The World's End", "Scott Pilgrim vs. the World" and "Shaun of the Dead".  Other films with the Wright/Frost/Pegg stable include Nick Frost's salsa comedy "Cuban Fury" and the romantic comedy "Man Up" (starring Simon Pegg).

Sandra Bullock filmography: Sandra Bullock is an American actress who made her film debut with a minor role in the 1987 thriller "Hangmen".  She made her television debut in the television film "Bionic Showdown: The Six Million Dollar Man and the Bionic Woman" (1989) and played the lead role in the short-lived sitcom "Working Girl" (1990) before making her breakthrough starring in the action film "Speed" (1994).  She starred with Sylvester Stallone in "Demolition Man" (1994).  Bullock founded her own production company, Fortis Films, and starred in the romantic comedy "While You Were Sleeping" in 1995.  Her performance in the film earned her first nomination for the Golden Globe Award for Best Actress – Motion Picture Comedy or Musical.  The following year, Bullock starred with Matthew McConaughey in the film adaptation of John Grisham's novel "A Time to Kill" (1996).  In 1997, she reprised her "Speed" role in the sequel, "".  The following year, Bullock starred in the romantic comedy "Practical Magic", voiced Miriam in the animated biblical film "The Prince of Egypt" and also executive produced her first film, the romantic drama "Hope Floats".

Ed's Next Move: Ed's Next Move is a 1996 American romantic comedy film written and directed by John C. Walsh.  It stars Matt Ross and Callie Thorne.  A micro-budget romantic comedy about a transplanted Midwesterner adapting to life in New York's East Village, the film appeared at the 1996 Sundance Film Festival where it received critical praise and was picked up by Orion Classics for theatrical release.  The LA Times' Kenneth Turan called the movie "one of the most appealing, audience friendly films at Sundance," while Roger Ebert referred to the film as "a truth telling comedy with quiet wit and bright dialogue. "  Sight & Sound called it "a perfectly formed romantic comedy."

Katie Wright: Kathryn "Katie" Wright (born December 25, 1971) is a former American actress.

Monte Carlo (2011 film): Monte Carlo is a 2011 American romantic comedy film based on "Headhunters" by Jules Bass.  It was directed by Thomas Bezucha.  Denise Di Novi, Alison Greenspan, Nicole Kidman, and Arnon Milchan produced the film for Fox 2000 Pictures and Regency Enterprises.  It began production in Harghita, Romania on May 5, 2010.  "Monte Carlo" stars Selena Gomez, Leighton Meester and Katie Cassidy as three friends posing as wealthy socialites in Monte Carlo, Monaco.  The film was released on July 1, 2011.  It features the song "Who Says" by Selena Gomez & the Scene and numerous songs by British singer Mika.  "Monte Carlo" received mixed to negative reviews from critics, but earned over $39 million on a $20 million budget.  Fox Home Entertainment released "Monte Carlo" on DVD and Blu-ray Disc on October 18, 2011.

Cross-Country Romance: Cross-Country Romance is a 1940 American romantic comedy film starring Gene Raymond and Wendy Barrie.  With the huge success of "It Happened One Night", the 1934 American romantic comedy film directed by Frank Capra and starring Claudette Colbert and Clark Gable, every studio in Hollywood attempted to cash in with a similar storyline.  In addition to this film, there was also "Love on the Run" (1936) from MGM, "The Bride Came C.O.D." (1941) by Warner Bros.; even Columbia Pictures, which had made "It Happened One Night", produced the musical remake "Eve Knew Her Apples" (1945).

Isn't It Romantic (2019 film): Isn't It Romantic is an upcoming American romantic comedy film directed by Todd Strauss-Schulson and written by Erin Cardillo, Dana Fox, Katie Silberman, and Paula Pell.  The film stars Rebel Wilson, Adam DeVine, Liam Hemsworth, Priyanka Chopra, and Betty Gilpin.  It is scheduled to be released on February 14, 2019, by Warner Bros.  Pictures.

Bride for Rent: Bride for Rent is a 2014 Filipino romantic comedy film directed by Mae Czarina Cruz starring Kim Chiu and Xian Lim.  It is produced by Star Cinema as its opening salvo for the year.  The film achieved numerous milestones including being the second highest grossing Filipino romantic comedy movie of all-time after "It Takes a Man and a Woman" and third highest grossing non-MMFF film of all-time after "It Takes a Man and a Woman" and "Praybeyt Benjamin" respectively, and also the highest-grossing January-released film of all-time in the country.

I Love NY (2015 film): I Love NY, also known as I Love New Year, is an Indian romantic comedy film directed by Radhika Rao and Vinay Sapru starring Sunny Deol and Kangana Ranaut in lead roles.  The film is produced by Bhushan Kumar and Krishan Kumar under the banner of Super Cassettes Industries Ltd.  The film was extensively shot in Mumbai, New York City and Bangkok.  The main plot was taken from the Russian romantic comedy "The Irony of Fate" (1976).  After numerous delays, the film released on 10 July 2015.

Question: The romantic comedy film Hairshirt, starring Katie Wright, was released in what year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the romantic comedy film."
    },
    "release_year": {
      "type": "integer",
      "description": "The year the film was released."
    },
    "genre": {
      "type": "string",
      "description": "The genre of the film."
    },
    "starring_actors": {
      "type": "array",
      "description": "A list of actors who starred in the film.",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "film_title",
    "release_year",
    "genre",
    "starring_actors"
  ],
  "additionalProperties": false
}

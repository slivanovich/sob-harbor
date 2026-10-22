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
She's Out of My League: She's Out of My League is a 2010 American romantic comedy film directed by Jim Field Smith and written by Sean Anders and John Morris.  The film stars Jay Baruchel and Alice Eve, and was produced by Jimmy Miller and David Householter for Paramount Pictures and DreamWorks Pictures and filmed in Pittsburgh, Pennsylvania.  Production on the film finished in 2008.  The film received its wide theatrical release on March 12, 2010.  It is the first feature film directed by Smith.

Valentine's Day (2010 film): Valentine's Day is a 2010 American romantic comedy film directed by Garry Marshall.  The screenplay and the story were written by Katherine Fugate, Abby Kohn and Marc Silverstein.  The film consists of an ensemble cast led by Jessica Alba, Kathy Bates, Jessica Biel, Bradley Cooper, Eric Dane, Patrick Dempsey, Héctor Elizondo, Jamie Foxx, Jennifer Garner, Topher Grace, Anne Hathaway, Ashton Kutcher, Queen Latifah, Taylor Lautner, George Lopez, Shirley MacLaine, Emma Roberts, Julia Roberts, Carter Jenkins, and Taylor Swift in her film debut.  While the film received negative reviews, it was a major box office success.

Cross-Country Romance: Cross-Country Romance is a 1940 American romantic comedy film starring Gene Raymond and Wendy Barrie.  With the huge success of "It Happened One Night", the 1934 American romantic comedy film directed by Frank Capra and starring Claudette Colbert and Clark Gable, every studio in Hollywood attempted to cash in with a similar storyline.  In addition to this film, there was also "Love on the Run" (1936) from MGM, "The Bride Came C.O.D." (1941) by Warner Bros.; even Columbia Pictures, which had made "It Happened One Night", produced the musical remake "Eve Knew Her Apples" (1945).

Sweet and Wild: Sweet and Wild is the ninth studio album by American recording artist Jewel.  It was released on June 8, 2010, through Valory Music Group as her second country album with the label.  The song "Stay Here Forever" was released as a single from the soundtrack of "Valentine's Day" and as the lead-off single to the album.  It was a minor Top 30 hit on the U.S. "Billboard" Hot Country Songs chart.  The album's second single, "Satisfied", was released on May 17, 2010, and debuted at #59 on the U.S. "Billboard" Hot Country Songs chart for the week of June 19, 2010.  The album debuted at number eleven on the "Billboard" 200, with sales of 32,000 copies.

Ed's Next Move: Ed's Next Move is a 1996 American romantic comedy film written and directed by John C. Walsh.  It stars Matt Ross and Callie Thorne.  A micro-budget romantic comedy about a transplanted Midwesterner adapting to life in New York's East Village, the film appeared at the 1996 Sundance Film Festival where it received critical praise and was picked up by Orion Classics for theatrical release.  The LA Times' Kenneth Turan called the movie "one of the most appealing, audience friendly films at Sundance," while Roger Ebert referred to the film as "a truth telling comedy with quiet wit and bright dialogue. "  Sight & Sound called it "a perfectly formed romantic comedy."

Sex and the City 2: Sex and the City 2 is a 2010 American romantic comedy film written, co-produced, and directed by Michael Patrick King.  It is the sequel to the 2008 film "Sex and the City", which is based on the 1998-2004 HBO comedy series of the same name (itself based on the book of the same name by Candace Bushnell).

Leap Year (2010 film): Leap Year is a 2010 American romantic comedy film directed by Anand Tucker, and starring Amy Adams and Matthew Goode.  Written by Harry Elfont and Deborah Kaplan, the film is about a woman who heads to Ireland to ask her boyfriend to accept her wedding proposal on leap day, when tradition supposedly holds that men cannot refuse a woman's proposal for marriage.  Her plans are interrupted by a series of increasingly unlikely events and are further complicated when she hires a handsome Irish innkeeper to take her to her boyfriend in Dublin.  The film was shot in County Wicklow, Dublin, County Mayo, and County Galway, with filming taking place in and around the Aran Islands, Connemara, Temple Bar, Georgian Dublin, Wicklow National Park, and Olaf Street, Waterford.  "Leap Year" premiered in New York City on January 6, 2010.  The film received mostly negative reviews.

Jack Goes Boating (film): Jack Goes Boating is a 2010 American romantic comedy film directed by Philip Seymour Hoffman (in his only career directorial effort) and stars Hoffman in the title role, as well as Amy Ryan, John Ortiz and Daphne Rubin-Vega.  The film's script was written by Robert Glaudini, based on his 2007 play "Jack Goes Boating".  The film's cast was mostly the same as the cast of the play's premiere at The Public Theater, although Amy Ryan replaced Beth Cole.  The film was produced by Overture Films and Relativity Media.  It premiered at the 26th Sundance Film Festival and was later released in the United States on September 17, 2010.

Stay Here Forever: "Stay Here Forever" is a song written by Jewel, Dallas Davidson, and Bobby Pinson and recorded by American recording artist Jewel.  It was released to country radio in January 2010 and as a music download on February 9, 2010, and serves as the lead song for the movie "Valentine's Day", as well as the lead-off single to Jewel's second country album, "Sweet and Wild", which was released on June 8, 2010 via Valory Music Group.  The song is Jewel's first chart single on the country charts since "Till It Feels Like Cheating," which peaked at number 57 in November 2008.

Henry's Crime: Henry's Crime is a 2010 American romantic comedy film directed by Malcolm Venville and starring Keanu Reeves, Vera Farmiga, and James Caan.  The film follows Henry (Reeves), who goes to jail for a robbery he did not commit.  Once released, he plans on robbing the same bank with his former cellmate Max (Caan).  The film premiered at the Toronto International Film Festival on September 14, 2010, and was given a limited release in the United States on April 8, 2011.

Question: Which 2010 American romantic comedy film included Jewel's song "Stay Here Forever" on its soundtrack?

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
    "soundtrack_song": {
      "type": "object",
      "properties": {
        "song_title": {
          "type": "string",
          "description": "The title of the song featured on the soundtrack."
        },
        "artist": {
          "type": "string",
          "description": "The artist who recorded the song."
        },
        "role_in_film": {
          "type": "string",
          "description": "Describes how the song was used in relation to the film."
        }
      },
      "required": [
        "song_title",
        "artist",
        "role_in_film"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_title",
    "release_year",
    "genre",
    "soundtrack_song"
  ],
  "additionalProperties": false
}

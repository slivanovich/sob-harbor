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
Come What May (2001 song): "Come What May" is a song composed by David Baerwald and Kevin Gilbert, originally intended for the film "William Shakespeare's Romeo + Juliet".  However, it was first heard publicly, and is best known as the romantic love theme from Baz Luhrmann's 2001 film "Moulin Rouge! ", where it is sung by Ewan McGregor and Nicole Kidman in their respective roles as Christian and Satine.

Quindon Tarver: Quindon Tarver (born August 4, 1982) is an American singer.  He is best known for his cover of Prince's "When Doves Cry" for the 1996 film "William Shakespeare's Romeo + Juliet".

Romeo and Juliet on screen: William Shakespeare's Romeo and Juliet may be one of the most-screened plays of all time.  The most notable theatrical releases were George Cukor's multi-Oscar-nominated 1936 production "Romeo and Juliet", Franco Zeffirelli's 1968 film "Romeo and Juliet", and Baz Luhrmann's 1996 MTV-inspired "Romeo + Juliet".  The latter two were both, at the time, the highest-grossing Shakespeare films.  Cukor featured the mature actors Norma Shearer and Leslie Howard as the teenage lovers while Zeffirelli populated his film with beautiful young people, and Baz Luhrmann produced a heavily cut fast-paced version aimed at teenage audiences.

Jill Bilcock: Jill Bilcock (born 1948) is an Australian film editor, a member of the ASE (Australian Screen Editors), as well as the ACE (American Cinema Editors), and has edited films such as "William Shakespeare's Romeo + Juliet", "Moulin Rouge! " and "Road to Perdition".  She occasionally gives seminars at the Victorian College of the Arts in Melbourne, of which she is an alumna.

Romeo + Juliet: William Shakespeare's Romeo + Juliet (shortened to Romeo + Juliet) is a 1996 American romantic drama film directed, co-produced, and co-written by Baz Luhrmann, co-produced by Gabriella Martinelli, and co-written by Craig Pearce, being an adaptation and modernization of William Shakespeare's tragedy "Romeo and Juliet".  The film stars Leonardo DiCaprio and Claire Danes in the leading roles of Romeo and Juliet, who instantly fall in love when Romeo crashes a party and meets her, despite their being members of the Montague and Capulet family; Brian Dennehy, John Leguizamo, Pete Postlethwaite, Paul Sorvino, and Diane Venora star in supporting roles.

Claire Danes: Claire Catherine Danes (born April 12, 1979) is an American actress.  She is the recipient of three Emmy Awards, four Golden Globe Awards, and two Screen Actors Guild Awards.  In 2012, "Time" named her one of the 100 most influential people in the world, and she was awarded a star on the Hollywood Walk of Fame in 2015.

Romeo + Juliet (soundtrack): William Shakespeare's Romeo + Juliet: Music from the Motion Picture is the soundtrack to the 1996 film of the same name.  The soundtrack contained two separate releases: the first containing popular music from the film and the second containing the score to the film composed by Nellee Hooper, Craig Armstrong and Marius de Vries.

Baz Luhrmann: Mark Anthony "Baz" Luhrmann ( ; born 17 September 1962) is an Australian film director, screenwriter and producer best known for "Red Curtain Trilogy", comprising his romantic comedy film "Strictly Ballroom" (1992), the romantic drama "Romeo + Juliet" (1996), and the pastiche-jukebox musical "Moulin Rouge! " (2001).  His 2008 film "Australia" is an epic historical romantic drama film starring Hugh Jackman and Nicole Kidman.  His 2013 drama "The Great Gatsby", based on F. Scott Fitzgerald's 1925 novel of the same name, stars Leonardo DiCaprio (whom he also used in "Romeo + Juliet") and Tobey Maguire.

Kissing You (Des'ree song): "Kissing You" (or "I'm Kissing You") is a song by British singer Des'ree.  It was written by the singer with Timothy Atack for Baz Luhrmann's 1996 film "Romeo + Juliet".  The song was included on the film's soundtrack album and Des'ree's third studio album, "Supernatural" (1998).  A pop ballad set in the key of A minor, the record uses a simple instrumentation consisting only of piano and string instruments. "Kissing You" featured in "Romeo + Juliet" when the title characters meet at a ball.  The song was well received by critics for its emotional melody and toned-down production.  First released as a single in Australia on 24 February 1997, it appeared on the ARIA Singles Chart and the UK Singles Chart.  A music video accompanied the single, which included scenes from "Romeo + Juliet".

Something for Everybody (Baz Luhrmann album): Something for Everybody is an album released by Baz Luhrmann in 1998.  It contains new ambient versions (either newly recorded or remixed) of music from his films and plays, including hits from "William Shakespeare's Romeo + Juliet", "Strictly Ballroom" and "La bohème".  The most popular single from the album is the spoken word song "Everybody's Free (To Wear Sunscreen)".

Question: Which star of William Shakespeare's Romeo + Juliet movie was named one of the 100 most influential people in the world by Time magazine in 2012?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person identified as influential."
    },
    "film_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film the person starred in."
        },
        "role": {
          "type": "string",
          "description": "The role played by the person in the film."
        },
        "director": {
          "type": "string",
          "description": "The director of the film."
        }
      },
      "required": [
        "title",
        "role",
        "director"
      ],
      "additionalProperties": false
    },
    "recognition_details": {
      "type": "object",
      "properties": {
        "award_name": {
          "type": "string",
          "description": "The name of the recognition received."
        },
        "awarding_body": {
          "type": "string",
          "description": "The organization that bestowed the recognition."
        },
        "year": {
          "type": "integer",
          "description": "The year the recognition was received."
        }
      },
      "required": [
        "award_name",
        "awarding_body",
        "year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_name",
    "film_details",
    "recognition_details"
  ],
  "additionalProperties": false
}

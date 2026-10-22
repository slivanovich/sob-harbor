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
Secret Admirer: Secret Admirer is a 1985 American teen romantic comedy film written and directed by David Greenwalt in his feature film directorial debut, and starring C. Thomas Howell, Lori Loughlin, Kelly Preston and Fred Ward.  The original music score was composed by Jan Hammer.  The film was produced at the height of the teen sex comedy cinema craze in the mid-1980s.

Loser (film): Loser is a 2000 American teen romantic comedy film starring Jason Biggs, Mena Suvari, and Greg Kinnear.

Kelly Preston: Kelly Preston (born October 13, 1962) is an American actress and former model.  She has appeared in more than sixty television and film productions, most notably including "Mischief", "Twins" and "Jerry Maguire".  She is married to John Travolta, with whom she collaborated on the fantasy film "Battlefield Earth".  She also starred in the films "The Cat in the Hat", "Old Dogs", and "Broken Bridges".

Better Off Dead (film): Better Off Dead is a 1985 American teen romantic comedy film starring John Cusack and written and directed by Savage Steve Holland.  It tells the story of high school student Lane Myer who is suicidal after his girlfriend breaks up with him shortly before Christmas.

Eiffel I'm in Love: Eiffel I'm in Love is a 2003 Indonesian teen romantic comedy film directed by was Nasri Cheppy.  The film stars Samuel Rizal and Shandy Aulia as the main characters, the film adaptation of the bestselling novel of the same name by Rachmania Arunita.  Other people appearing in the film include Titi Kamal, Helmy Yahya, Didi Petet, and Hilda Arifin.

John Tucker Must Die: John Tucker Must Die is a 2006 American teen romantic comedy film directed by Betty Thomas.  The film is about a trio of girls (played by Arielle Kebbel, Sophia Bush, and Ashanti) who plot to break the heart of manipulative basketball star John Tucker (Jesse Metcalfe) after they learn he has been secretly dating all three and pledging each is "the one".  They recruit cute wallflower Kate (Brittany Snow) in their scheme to publicly humiliate the cad.  Released in North America on July 29, 2006, the film made $68 million worldwide.

She's All That: She's All That is a 1999 American teen romantic comedy film directed by Robert Iscove and starring Freddie Prinze Jr., Rachael Leigh Cook, Paul Walker and Matthew Lillard.  It is a modern adaptation of George Bernard Shaw's play "Pygmalion" and George Cukor's 1964 film "My Fair Lady".  It was one of the most popular teen films of the 1990s and reached No. 1 at the box office in its first week of release.  In April 2015, it was announced that the film will be remade by The Weinstein Company.

Can't Buy Me Love (film): Can't Buy Me Love is a 1987 American teen romantic comedy feature film starring Patrick Dempsey and Amanda Peterson in a story about a nerd at a high school in Tucson, Arizona who gives a cheerleader $1,000 to pretend to be his girlfriend for a month.  The film was directed by Steve Rash and takes its title from a Beatles song with the same title.

Sydney White: Sydney White is a 2007 American teen romantic comedy film directed by Joe Nussbaum and written by Chad Gomez Creasey based on the story of "Snow White".  The film, starring Amanda Bynes, Sara Paxton and Matt Long, was released theatrically on September 21, 2007 by Universal Pictures.

It Happened One Sunday: It Happened One Sunday is a 1944 British romantic comedy film directed by Karel Lamac and starring Robert Beatty, Barbara White, Marjorie Rhodes, Kathleen Harrison and Moore Marriott.  In the film, an Irish servant girl working in Liverpool mistakenly believes that she has a secret admirer working at a hospital, and while seeking him out accidentally meets and falls in love with a serviceman there.  She spends the rest of the day around Liverpool with him and they eventually decide to marry.  The film was based on the play "She Met Him One Sunday" by Victor Skutezky.

Question: Secret Admirer is a teen romantic comedy film starring an American actress who collaborated with her husband on what film?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "source_film_title": {
      "type": "string",
      "description": "The title of the initial film mentioned in the question."
    },
    "source_film_year": {
      "type": "integer",
      "description": "The release year of the initial film."
    },
    "source_film_genre": {
      "type": "string",
      "description": "The genre of the initial film."
    },
    "starring_actress": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the American actress starring in the source film."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the actress."
        }
      },
      "required": [
        "name",
        "nationality"
      ],
      "additionalProperties": false
    },
    "actress_husband_name": {
      "type": "string",
      "description": "The name of the actress's husband."
    },
    "collaborative_film": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film the actress collaborated on with her husband."
        },
        "genre": {
          "type": "string",
          "description": "The genre of the collaborative film."
        }
      },
      "required": [
        "title",
        "genre"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "source_film_title",
    "source_film_year",
    "source_film_genre",
    "starring_actress",
    "actress_husband_name",
    "collaborative_film"
  ],
  "additionalProperties": false
}

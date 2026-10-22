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
Advanced Warriors: Advanced Warriors is an Interactive movie starring Jeremy Bulloch which was released in 2003.

War Horse (film): War Horse is a 2011 British war drama film directed and co-produced by Steven Spielberg from a screenplay written by Lee Hall and Richard Curtis, adapted from English author Michael Morpurgo's 1982 novel of the same name.  The film's cast includes Jeremy Irvine (in his film acting debut), Emily Watson, David Thewlis, Tom Hiddleston, Benedict Cumberbatch, Eddie Marsan, Niels Arestrup, Toby Kebbell, David Kross and Peter Mullan.  Set before and during World War I, it tells of the journey of Joey, a bay Thoroughbred horse raised by British teenager Albert (Irvine), as he is bought by the British Army, leading him to encounter numerous individuals and owners throughout Europe, all the while experiencing the tragedies of the war happening around him.

Beyond the Reach: Beyond the Reach is a 2014 American adventure thriller film directed by Jean-Baptiste Léonetti and written by Stephen Susco.  It is based on the 1972 novel "Deathwatch" by Robb White.  The film, starring Michael Douglas, Jeremy Irvine, and Ronny Cox, was released on April 17, 2015, by Roadside Attractions.

Fallen (2016 film): Fallen is an American romantic fantasy film directed by Scott Hicks, based on the novel of same name by Lauren Kate.  The film stars Addison Timlin, Jeremy Irvine, Harrison Gilbertson, and Joely Richardson.

Mamma Mia: Here We Go Again!: Mamma Mia: Here We Go Again!  is an upcoming American romantic comedy musical film directed and written by Ol Parker.  It is based on the musical of same name and a sequel to 2008 film "Mamma Mia! " The film stars Amanda Seyfried, Dominic Cooper, Meryl Streep, Lily James, Colin Firth, Pierce Brosnan, and Jeremy Irvine.  It is scheduled to be released on July 20, 2018, 10 years after the original, by Universal Pictures.  The film is currently in production.

Now Is Good: Now Is Good is a 2012 British teen drama film directed by Ol Parker.  Based on the 2007 novel "Before I Die" by Jenny Downham, it was adapted by Parker who had recently written the screenplay for "The Best Exotic Marigold Hotel".  The film, which stars Dakota Fanning, Jeremy Irvine and Paddy Considine, centres on Tessa, a girl who is dying of leukaemia and tries to enjoy her remaining life as much as she possibly can.

Great Expectations (2012 film): Great Expectations is a 2012 British film adaptation of Charles Dickens' novel of the same name.  The film was directed by Mike Newell, with the adapted screenplay by David Nicholls, and stars Jeremy Irvine, Helena Bonham Carter, Holliday Grainger, Ralph Fiennes and Robbie Coltrane.  It was distributed by Lionsgate.

A Night in Old Mexico: A Night in Old Mexico is a 2013 Spanish-American co-production film directed by Emilio Aragón about a man (Robert Duvall) and his grandson (Jeremy Irvine).

Jeremy Irvine: Jeremy William Fredric Smith (born 18 June 1990), better known as Jeremy Irvine, is an English actor who made his film debut in the epic war film "War Horse" (2011).  In 2012, he portrayed Philip "Pip" Pirrip in the film adaptation of "Great Expectations", and earned widespread critical acclaim for his role in the independent film "Now Is Good" (2012).

The Railway Man (film): The Railway Man is a 2013 British–Australian war film directed by Jonathan Teplitzky.  It is an adaptation of the autobiography "The Railway Man" by Eric Lomax, and stars Colin Firth, Nicole Kidman, Jeremy Irvine, and Stellan Skarsgård.  It premiered at the 2013 Toronto International Film Festival on 6 September 2013.

Question: which movie starring Jeremy Irvine is based on the novel Before I Die

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "movie_title": {
      "type": "string",
      "description": "The title of the movie."
    },
    "release_year": {
      "type": "integer",
      "description": "The release year of the movie."
    },
    "director": {
      "type": "string",
      "description": "The director of the movie."
    },
    "based_on_novel": {
      "type": "string",
      "description": "The title of the novel the movie is based on."
    },
    "novel_author": {
      "type": "string",
      "description": "The author of the novel."
    },
    "starring_actors": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of main actors starring in the movie."
    }
  },
  "required": [
    "movie_title",
    "release_year",
    "director",
    "based_on_novel",
    "novel_author",
    "starring_actors"
  ],
  "additionalProperties": false
}

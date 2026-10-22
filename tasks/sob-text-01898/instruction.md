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
Now Is Good: Now Is Good is a 2012 British teen drama film directed by Ol Parker.  Based on the 2007 novel "Before I Die" by Jenny Downham, it was adapted by Parker who had recently written the screenplay for "The Best Exotic Marigold Hotel".  The film, which stars Dakota Fanning, Jeremy Irvine and Paddy Considine, centres on Tessa, a girl who is dying of leukaemia and tries to enjoy her remaining life as much as she possibly can.

Mamma Mia: Here We Go Again!: Mamma Mia: Here We Go Again!  is an upcoming American romantic comedy musical film directed and written by Ol Parker.  It is based on the musical of same name and a sequel to 2008 film "Mamma Mia! " The film stars Amanda Seyfried, Dominic Cooper, Meryl Streep, Lily James, Colin Firth, Pierce Brosnan, and Jeremy Irvine.  It is scheduled to be released on July 20, 2018, 10 years after the original, by Universal Pictures.  The film is currently in production.

The Best Exotic Marigold Hotel: The Best Exotic Marigold Hotel is a 2011 British comedy-drama film directed by John Madden.  The screenplay, written by Ol Parker, is based on the 2004 novel "These Foolish Things", by Deborah Moggach, and features an ensemble cast consisting of Judi Dench, Celia Imrie, Bill Nighy, Ronald Pickup, Maggie Smith, Tom Wilkinson and Penelope Wilton, as a group of British pensioners moving to a retirement hotel in India, run by the young and eager Sonny, played by Dev Patel.  The movie was produced by Participant Media and Blueprint Pictures on a budget of $10 million.

Stonewall (2015 film): Stonewall is a 2015 American drama film directed by Roland Emmerich and written by Jon Robin Baitz.  The film stars Jeremy Irvine, Ron Perlman, Jonathan Rhys Meyers, Joey King, Caleb Landry Jones, Matt Craven, Atticus Mitchell, and Mark Camacho.  The film was released on September 25, 2015, by Roadside Attractions.

Linda (1960 film): Linda is a 1960 British teen drama film, directed by Don Sharp and starring Carol White and Alan Rothwell.  The film was shot on location in South London and Brighton, and played in cinemas as the support feature to "Saturday Night and Sunday Morning".

This Beautiful Fantastic: This Beautiful Fantastic is a 2016 British romantic drama film directed and written by Simon Aboud.  The film stars Jessica Brown Findlay, Tom Wilkinson, Andrew Scott, Jeremy Irvine, Anna Chancellor, Eileen Davies and Sheila Hancock.  Principal photography began in London in July 2015.

War Horse (film): War Horse is a 2011 British war drama film directed and co-produced by Steven Spielberg from a screenplay written by Lee Hall and Richard Curtis, adapted from English author Michael Morpurgo's 1982 novel of the same name.  The film's cast includes Jeremy Irvine (in his film acting debut), Emily Watson, David Thewlis, Tom Hiddleston, Benedict Cumberbatch, Eddie Marsan, Niels Arestrup, Toby Kebbell, David Kross and Peter Mullan.  Set before and during World War I, it tells of the journey of Joey, a bay Thoroughbred horse raised by British teenager Albert (Irvine), as he is bought by the British Army, leading him to encounter numerous individuals and owners throughout Europe, all the while experiencing the tragedies of the war happening around him.

Jeremy Irvine: Jeremy William Fredric Smith (born 18 June 1990), better known as Jeremy Irvine, is an English actor who made his film debut in the epic war film "War Horse" (2011).  In 2012, he portrayed Philip "Pip" Pirrip in the film adaptation of "Great Expectations", and earned widespread critical acclaim for his role in the independent film "Now Is Good" (2012).

Great Expectations (2012 film): Great Expectations is a 2012 British film adaptation of Charles Dickens' novel of the same name.  The film was directed by Mike Newell, with the adapted screenplay by David Nicholls, and stars Jeremy Irvine, Helena Bonham Carter, Holliday Grainger, Ralph Fiennes and Robbie Coltrane.  It was distributed by Lionsgate.

Dev Patel: Dev Patel (born 23 April 1990) is an English actor.  Born and raised in London to Indian parents, Patel made his screen debut as Anwar Kharral in the first two seasons of the British teen drama television series "Skins" (2007–2008), landing the role with no prior professional acting experience.  His breakthrough came in 2008 with the leading role of Jamal Malik in Danny Boyle's drama "Slumdog Millionaire", which won the Academy Award for Best Picture, and for which he was nominated for the BAFTA Award for Best Actor and the SAG Award for Best Supporting Actor.

Question: Which of the film in which Jeremy Irvine had a role is a 2012 British teen drama film directed by Ol Parker?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "release_year": {
      "type": "integer",
      "description": "The year the film was released."
    },
    "director": {
      "type": "string",
      "description": "The director of the film."
    },
    "genre": {
      "type": "string",
      "description": "The primary genre of the film."
    },
    "is_british": {
      "type": "boolean",
      "description": "Indicates if the film is British."
    },
    "stars_jeremy_irvine": {
      "type": "boolean",
      "description": "Indicates if Jeremy Irvine had a role in the film."
    }
  },
  "required": [
    "film_title",
    "release_year",
    "director",
    "genre",
    "is_british",
    "stars_jeremy_irvine"
  ],
  "additionalProperties": false
}

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
Kevin Kline: Kevin Delaney Kline (born October 24, 1947) is an American film and stage actor and singer.  He has won an Academy Award and three Tony Awards and is a 2003 American Theatre Hall of Fame inductee.

In &amp; Out (film): In & Out is a 1997 American romantic comedy film directed by Frank Oz and starring Kevin Kline, Tom Selleck, Joan Cusack, Matt Dillon, Debbie Reynolds, and Wilford Brimley.  It is an original story by screenwriter Paul Rudnick.  Joan Cusack was nominated for an Academy Award for Best Supporting Actress for her performance.

Dave (film): Dave is a 1993 American political comedy film directed by Ivan Reitman, written by Gary Ross, and starring Kevin Kline and Sigourney Weaver.  Frank Langella, Kevin Dunn, Ving Rhames, and Ben Kingsley appear in supporting roles.

About Last Night (2014 film): About Last Night is a 2014 American romantic comedy film starring Kevin Hart, Michael Ealy, Regina Hall and Joy Bryant.  The film is directed by Steve Pink and written by Leslye Headland.  It is based on the 1974 David Mamet play "Sexual Perversity in Chicago" and is a remake of the 1986 film of the same name with a black cast.  While the original film is set in Chicago, Illinois, the remake is set in Los Angeles, California where filming took place in late 2012.

The Pirates of Penzance (film): The Pirates of Penzance is a 1983 British-American romantic musical comedy film written and directed by Wilford Leach based on Gilbert and Sullivan's comic opera of the same name.  The film, starring Kevin Kline, Angela Lansbury, Linda Ronstadt, George Rose, and Rex Smith, is an adaptation of the 1980 Joseph Papp production of "Pirates".  The original Broadway cast reprised their roles in the film, except that Lansbury replaced Estelle Parsons as Ruth.  The minor roles used British actors miming to their Broadway counterparts.  Choreography was by Graciela Daniele.  It was produced by Papp and filmed at Shepperton Studios in London.

Picture Perfect (1997 film): Picture Perfect is a 1997 American romantic comedy film directed by Glenn Gordon Caron and starring Jennifer Aniston, Jay Mohr, Kevin Bacon, Illeana Douglas, Olympia Dukakis, and Anne Twomey.

Housesitter: Housesitter is a 1992 American romantic comedy film directed by Frank Oz, written by Mark Stein, and starring Steve Martin and Goldie Hawn.  The premise involves a woman with con-artist tendencies who worms her way into the life of a reserved architect by claiming to be his wife.

Cross-Country Romance: Cross-Country Romance is a 1940 American romantic comedy film starring Gene Raymond and Wendy Barrie.  With the huge success of "It Happened One Night", the 1934 American romantic comedy film directed by Frank Capra and starring Claudette Colbert and Clark Gable, every studio in Hollywood attempted to cash in with a similar storyline.  In addition to this film, there was also "Love on the Run" (1936) from MGM, "The Bride Came C.O.D." (1941) by Warner Bros.; even Columbia Pictures, which had made "It Happened One Night", produced the musical remake "Eve Knew Her Apples" (1945).

French Kiss (1995 film): French Kiss is a 1995 American romantic comedy film directed by Lawrence Kasdan and starring Meg Ryan and Kevin Kline.  Written by Adam Brooks, the film is about a woman who flies to France to confront her straying fiancé and gets into trouble when the charming crook seated next to her uses her to smuggle a stolen diamond necklace.  "French Kiss" was filmed on location in Paris, the Provence-Alpes-Côte d'Azur région of southeastern France, and Cannes.  The film was released in the United States on May 5, 1995, and received mixed reviews.  The film went on to earn a total worldwide gross of $101,982,854.

The Muppets Take Manhattan: The Muppets Take Manhattan is a 1984 American musical comedy film directed by Frank Oz.  It is the third of a series of live-action musical feature films starring Jim Henson's Muppets with special appearances by Art Carney, James Coco, Dabney Coleman, Gregory Hines, Linda Lavin, and Joan Rivers.  The film was produced by Henson Associates and TriStar Pictures, and was filmed on location in New York City during the summer of 1983 and released theatrically the following summer.  It was the first film to be directed solely by Oz (who also performs Sam the Eagle, Fozzie Bear, Miss Piggy, and Animal), as he previously co-directed "The Dark Crystal" with Henson.

Question: In & Out is a 1997 American romantic comedy film directed by Frank Oz and starring Kevin Delaney Kline, an American film and stage actor and singer, he's won how many Tony Awards, among other various awards?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The full name of the actor."
    },
    "award_type": {
      "type": "string",
      "description": "The type of award being inquired about."
    },
    "number_of_awards": {
      "type": "integer",
      "description": "The count of the specified award won by the actor."
    },
    "other_awards_mentioned": {
      "type": "array",
      "description": "A list of other awards mentioned for the actor in the context.",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "actor_name",
    "award_type",
    "number_of_awards",
    "other_awards_mentioned"
  ],
  "additionalProperties": false
}

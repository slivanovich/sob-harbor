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
Abigail Eames: Abigail Eames is a British child actress born on October 5, 2003, and first appeared on British television and most recently the Bollywood movie "Shivaay".  She is best known for being her roles in "Mr Selfridge" (2013), "Crimson Fields" (2014), "Lawless" (2013), "Harry and Paul's of 2s" (2014), "Doctor Who" and "The Interceptor".  She made her Bollywood debut alongside Ajay Devgan in his movie "Shivaay" (2016).  Abigail got positive response for her performance as the daughter of Ajay Devgn in Shivaay.

Kaitlyn Maher: Kaitlyn Ashley Maher (born January 10, 2004) is an American child singer and actress born in Michigan, and raised in Ashburn, Virginia.  In 2008, at the age of 4, she appeared on the third season of "America's Got Talent" and for her audition sang "Somewhere Out There".  She reached the top 10 of AGT season 3, and was the youngest person to ever reach that level.  Maher has since appeared live at The Great Kids Expo in Chantilly, Virginia, on October 25, 2008, a live broadcast of the 2008 lighting of the National Christmas Tree, on December 4, 2008, attended by President George W. Bush and over 7,000 guests, and the 2009 Cherry Blossom Festival on April 11, 2009.  On October 3, 2009, Maher was the opening act of The Addi and Cassi Hempel Fund benefit.  Maher has appeared in a Harris Teeter commercial airing during December 2008.  She was also selected by Compassion International as its first ever Child Ambassador, visited children in El Salvador with Compassion, got to meet her sponsored child, and shot a music video to her title song "You Were Meant to Be."

Contest (film): Contest is a 2013 American comedy-drama film written and directed by Anthony Joseph Giunta and starring Kenton Duty, Daniel Flaherty, Katherine McNamara, and Mary Beth Peil.

Ant Timpson: Ant Timpson (born 21 April 1966) is a New Zealand producer best known for producing "The ABCs of Death" series, "Turbo Kid", "Deathgasm" and "The Greasy Strangler".  He founded and hosts the 48Hours film contest.

Daniela Castillo: Daniela Paz Castillo Vicuña (born September 26, 1984 in Santiago) is a Chilean female pop singer and actress born in Santiago.  She debuted in 2002 as a solo artist on the Chilean TV show "Rojo: Fama Contra Fama".  She studied four years at the Alicia Puccio Academy where she met the casting crew for the TV show "Rojo".  Although she did not win first place in the singer talent contest, she became very popular due to her voice.

Cieri Media International Corporation: Cieri Media International Corp. is a technology driven video production company.  They specialize in high quality but price driven videos for small company's websites and commercials, artist videos, actor's reels, author's book videos, sizzle reels, original show production and video production for filmmakers and theater companies.  They have been running NYC Independent Film Festival since 2010 and introduced Parody 48 Hour Film Contest in 2013.  The film festival is a showcase for independent filmmakers and have multiple competitive categories.  The contest is a 48 hour challenge where participating teams have to parody a film chosen by the organizers and script, shoot, edit and submit the film within that time frame.

Hilda Plowright: Hilda Plowright (November 29, 1890 - October 9, 1973) was an actress born in Swaffham, Norfolk.  Following a career on the stage in Britain she came to the United States and obtained work and a Social Security number in New York.  She died in San Diego, California following a career in film, theater and television, primarily playing older women in assorted small roles.  She had over 50 film and television appearances between 1938 and 1965.  She also appeared in at least 13 theater productions on Broadway between 1925 and 1940.

Louisa Lytton: Louisa Claire Lytton (born 7 February 1989) is an English actress born in Camden and living in Islington.  She rose to fame in 2005 when joining "EastEnders" as Ruby Allen.  After leaving "EastEnders" in November 2006, Lytton joined "The Bill" as PC Beth Green, a role she played from May 2007 to March 2009.  She also appeared on "Strictly Come Dancing" in 2006.  Lytton also represented the UK at the Eurovision Dance Contest 2008 in Glasgow and finished in 9th place out of 14 with 47 points.

Mary Beth Peil: Mary Beth Peil (born June 25, 1940) is an American actress and singer.

Ruth Eweler: Ruth Eweler (March 19, 1913 – October 1, 1947) was a German actress born in Plettenberg.  She appeared in a number of films during the 1930s and 1940s, notably as a female lead in the 1937 film "The Daughter of the Samurai", which was a German-Japanese co-production.

Question: What nationality is the actress born in 1940 who appeared in the 2013 film Contest?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actress_name": {
      "type": "string",
      "description": "The full name of the actress."
    },
    "birth_year": {
      "type": "integer",
      "description": "The birth year of the actress."
    },
    "film_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film the actress appeared in."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the film."
        }
      },
      "required": [
        "title",
        "release_year"
      ],
      "additionalProperties": false
    },
    "nationality": {
      "type": "string",
      "description": "The nationality of the actress."
    }
  },
  "required": [
    "actress_name",
    "birth_year",
    "film_details",
    "nationality"
  ],
  "additionalProperties": false
}

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
Total Recall (1990 film): Total Recall is a 1990 American science-fiction action film directed by Paul Verhoeven, starring Arnold Schwarzenegger, Rachel Ticotin, Sharon Stone, Ronny Cox, and Michael Ironside.  The film is loosely based on the Philip K. Dick short story "We Can Remember It for You Wholesale".  It tells the story of a construction worker who is having troubling dreams about Mars and a mysterious woman there.  It was written by Ronald Shusett, Dan O'Bannon, Jon Povill, and Gary Goldman, and won a Special Achievement Academy Award for its visual effects.  The original score composed by Jerry Goldsmith won the BMI Film Music Award.

James Rebhorn: James Robert Rebhorn (September 1, 1948 – March 21, 2014) was an American character actor who appeared in over 100 films, television series, and plays.  At the time of his death, he had recurring roles in the current series "White Collar" and "Homeland".  He also appeared in films such as "Scent of a Woman", "Carlito's Way", "Independence Day", "My Cousin Vinny", and "Meet the Parents".

Total Recall (2012 film): Total Recall is a 2012 American science-fiction action film directed by Len Wiseman.  The screenplay by Kurt Wimmer and Mark Bomback was based on the 1990 film of the same name, which was inspired by the 1966 short story "We Can Remember It for You Wholesale" by Philip K. Dick.  The film stars Colin Farrell, Kate Beckinsale, Jessica Biel, Bryan Cranston, Bokeem Woodbine, John Cho, and Bill Nighy.  Unlike the first film, the setting is on a dystopian Earth, not Mars and has more political themes.  The film blends American and Asian influences, notably in the settings and dominant populations of the two nation-states in the story: the United Federation of Britain (Western Europe) and the Colony (Australia).

Predators (film): Predators is a 2010 American science-fiction action film directed by Nimród Antal and starring Adrien Brody, Topher Grace, Alice Braga, Walton Goggins, Laurence Fishburne, Danny Trejo, Mahershala Ali, Oleg Taktarov and Louis Ozawa Changchien.  It was distributed by 20th Century Fox.  It is the third installment of the "Predator" franchise, following "Predator" (1987) and "Predator 2" (1990).  A prequel, "The Predator", is set for 2018.

Terminator 3: Rise of the Machines: Terminator 3: Rise of the Machines (also referred to as Terminator 3 or T3) is a 2003 American science-fiction action film directed by Jonathan Mostow and starring Arnold Schwarzenegger, Nick Stahl, Claire Danes, David Andrews and Kristanna Loken.  It is the third installment in the "Terminator" film series, following "" (1991) and "The Terminator" (1984).  It does not involve James Cameron, who directed and wrote the first two films.  It grossed over $434 million worldwide, and is the third highest-grossing film of the franchise (after the 2015 film "Terminator Genisys").

Terminator 2: Judgment Day: Terminator 2: Judgment Day (also referred to as Terminator 2 or T2) is a 1991 American science-fiction action film co-written, produced and directed by James Cameron.  The film stars Arnold Schwarzenegger, Linda Hamilton, and Robert Patrick, with Edward Furlong also in its principal cast as John Connor.  It is the sequel to the 1984 film "The Terminator", and the second installment in the "Terminator franchise".  "Terminator 2" follows Sarah Connor (Hamilton) and her ten-year-old son John (Furlong) as they are pursued by a new, more advanced Terminator, the liquid metal, shapeshifting T-1000 (Patrick), sent back in time to kill John Connor and prevent him from becoming the leader of the human resistance.  A second, less advanced Terminator (Schwarzenegger) is also sent back in time to protect John.

Omega Doom: Omega Doom is a 1996 American science-fiction action film directed by Albert Pyun and starring Rutger Hauer.  It was written by Pyun and Ed Naha.  The story, set in a dystopian future, concerns a robot warrior who, during a nuclear winter, plays both sides of a robot civil war in a small town.  The film is mostly based on "Yojimbo" by Akira Kurosawa, and it was the third movie in Pyun's "Cyborg Trilogy".  It is considered a cult film.

Dick Miller: Richard "Dick" Miller (born December 25, 1928) is an American character actor who has appeared in over 100 films, particularly those produced by Roger Corman, and later in films of directors who started their careers with Corman, including James Cameron and Joe Dante, with the distinction of appearing in every film directed by Dante.  Miller's main roles have been in films such as "Gremlins", "", "The Explorers", "Piranha", "The Howling", "A Bucket of Blood", "The Little Shop of Horrors", "Chopping Mall", "Night of the Creeps", "The Terminator", "The 'Burbs" and "Small Soldiers".

Lady Terminator: Lady Terminator (Indonesian: "Pembalasan ratu pantai selatan" ) is a 1989 Indonesian fantasy horror action film directed by H. Tjut Djalil, under the pseudonym of Jalil Jackson.  The film stars Barbara Anne Constable, Christopher J. Hart, and Claudia Angelique Rademaker, and is considered to be a rip-off of the 1984 American film "The Terminator".

The Terminator: The Terminator is a 1984 American science-fiction action film directed by James Cameron.  It stars Arnold Schwarzenegger as the Terminator, a cyborg assassin sent back in time from 2029 to 1984 to kill Sarah Connor (Linda Hamilton), whose son will one day become a savior against machines in a post-apocalyptic future.  Michael Biehn plays Kyle Reese, a soldier from the future sent back in time to protect Connor.  The screenplay is credited to Cameron, along with producer Gale Anne Hurd.  Executive producers John Daly and Derek Gibson of Hemdale Film Corporation were instrumental in the film's financing and production.

Question: Richard "Dick" Miller, is an American character actor, who has appeared in over 100 films, Miller's main roles have been in films such as The Terminator, a 1984 American science-fiction action film directed by who?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "film_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "director_name": {
      "type": "string",
      "description": "The name of the director of the film."
    },
    "film_genre": {
      "type": "string",
      "description": "The genre of the film."
    }
  },
  "required": [
    "film_title",
    "film_year",
    "director_name",
    "film_genre"
  ],
  "additionalProperties": false
}

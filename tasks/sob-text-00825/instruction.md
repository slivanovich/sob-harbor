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
Warriors of Virtue: The Return to Tao: Warriors of Virtue: The Return to Tao (also known as simply "Warriors of Virtue 2" or "Warriors of Virtue 2: The Return to Tao") is a 2002 fantasy martial arts film, the straight-to-DVD sequel to the 1997 film "Warriors of Virtue".  This is the last film to star actor Kevin Smith, who died in February 2002 after falling from a prop tower.

Kidnapping of Rajkumar: Kannada film industry's legendary star actor Rajkumar was abducted by forest Veerappan on July 30, 2000 during the course of an armed attack on a farmhouse belonging to the actor in Gajanur, Tamil Nadu, India.  Rajkumar was released by Veerappan on November 15, 2000 after spending 108 days in his custody.  The kidnapping resulted in the further deterioration of already strained relations between the Indian states of Tamil Nadu and Karnataka and created a tense situation in the two states.

The Getaway (1994 film): The Getaway is a 1994 crime film directed by Roger Donaldson.  The screenplay was written by Walter Hill and Amy Holden Jones, based on the Jim Thompson novel of the same name.  The film stars Alec Baldwin and Kim Basinger, with Michael Madsen, James Woods, and Jennifer Tilly in supporting roles.

The Show Must Go On (play): The Show Must Go On, a play by Kōki Mitani, written in 1991 for his theatre group Tokyo Sunshine Boys.  It was so popular in Japan that it brought media fame to the entire company and gained its star actor Masahiko Nishimura an award for Best Actor, in that year's Japanese Theatre Awards.

Najwa Najjar: Najwa Najjar (Arabic: نجوى نجار‎ ‎ ) is a Palestinian filmmaker.  She began her career making commercials and has worked in both documentary and fiction since 1999.  Her debut feature film 'Pomegranates and Myrrh picked up 10 international awards, sold worldwide and was released theatrically and screened at over 80 international festivals.  Her second film Eyes of a thief also is a multi award winning thriller based on a true story, and shot entirely in Palestinian Territories.  with Egyptian multi award-winning star actor and producer Khaled Abol Naga as the lead and the Algerian sensational singer Souad Massi debut as an actress, Eyes of a thief was the oficial Palestinian submission to the 2014 87th Academy Awards ("The Oscars").

Rohith Manikonda: Rohith Manikonda (born 2001) is a child star actor famous for his work in CBBC's TV show, Airmageddon.  His name derives from the Sanskrit word for 'red' - "Rohita".  He is perhaps most famous for being the smiliest contestant on the show (term coined by the presenter, Will Best).  Manikonda was an instant hit with the Airmageddon fanbase, as his outgoing personality and good sportsmanship far outweighed his unfortunate defeat on team Quadrosoar (affectionately dubbed Quadrosnore ) in episode 8 of the first series.

Alec Baldwin: Alexander Rae Baldwin III (born April 3, 1958) is an American actor, writer, producer, and comedian.

Getaway! (video game): Getaway!  is a crime-themed scrolling maze game for the Atari 8-bit family designed by Mark Reid and published by the Atari Program Exchange (APX) in 1982.  The game won the 1983 $25,000 Atari Star Award for best APX submission, an award previously given to "My First Alphabet" and "Typo Attack".  Prior to "Getaway!" , Reid, a chemical engineer, developed a skiing game for APX: "Downhill".

Ali MacGraw: Elizabeth Alice "Ali" MacGraw (born April 1, 1939) is an American actress, model, author, and animal rights activist.  She first gained attention with her role in the 1969 film "Goodbye, Columbus", for which she won the Golden Globe Award for Most Promising Newcomer.  She reached international fame in 1970's "Love Story", for which she was nominated for an Academy Award for Best Actress and won the Golden Globe Award for Best Actress in a Motion Picture – Drama.  In 1972, MacGraw was voted the top female box office star in the world and was honored with a hands and footprints ceremony at Grauman's Chinese Theatre after having been in just three films.  She went on to star in the popular action films "The Getaway" (1972) and "Convoy" (1978) as well as the romantic sports drama "Players" (1979), the comedy "Just Tell Me What You Want" (1980), and the historical novel-based television miniseries "The Winds of War" (1983).  In 1991, she published an autobiography, "Moving Pictures".

Jharana Thapa: Jharana Thapa (Nepali: झरना थापा ) (born March 28, 1970) is a Nepali actress, film producer and film director.  She make her Kollywood debut in "Daijo" (1996) opposite star actor Bhuwan K.C..  She played the leading lady role in numerous movies.She received critical acclaim for her breakout role in the 1998 movie "Dharam Sankat".

Question: What nationality is the star actor of The Getaway?

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
    "star_actor_name": {
      "type": "string",
      "description": "The name of the star actor in the film."
    },
    "actor_nationality": {
      "type": "string",
      "description": "The nationality of the star actor."
    }
  },
  "required": [
    "film_title",
    "film_year",
    "star_actor_name",
    "actor_nationality"
  ],
  "additionalProperties": false
}

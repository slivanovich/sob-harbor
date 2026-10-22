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
Viva (2015 film): Viva is a 2015 Spanish-language Irish drama film, set in Cuba, directed by Paddy Breathnach and written by Mark O'Halloran.  The film stars Héctor Medina as a young drag performer who, after reuniting with his estranged father, must come to terms with his sexuality.

I Went Down: I Went Down is an Irish comedy crime film by director Paddy Breathnach released 3 October 1997.

Bobby Cannavale: Robert Cannavale ( ; ] ; born May 3, 1970) is an American actor known for his leading role as Bobby Caffey in the first two seasons of the crime drama series "Third Watch".  Cannavale also had a recurring role on the NBC comedy series "Will & Grace" as Will Truman's long-term boyfriend Officer Vincent "Vince" D'Angelo, for which he won the 2005 Primetime Emmy Award for Outstanding Guest Actor in a Comedy Series, and portrayed Gyp Rosetti during the third season of the HBO drama series "Boardwalk Empire", for which he won the 2013 Primetime Emmy Award for Outstanding Supporting Actor in a Drama Series.  In 2016, he starred in the HBO drama series "Vinyl", produced by Martin Scorsese and Mick Jagger.

A Nightingale Falling: A Nightingale Falling is a 2014 Irish film set during the Irish War of Independence based on the 2012 novel by PJ Curtis.  Directed by Garret Daly and Martina McGlynn, and written by Daly, the film stars Tara Breathnach, Muireann Bird and Gerard McCarthy.  The story concerns two sisters who care for a wounded soldier.  The film was released in Irish cinemas in September 2014, and received its Irish television premiere on UTV Ireland on Easter Sunday, 5 April 2015.

Allen Leech: Alan "Allen" Leech (born 18 May 1981) is an Irish actor best known for his role as Tom Branson on the historical drama series "Downton Abbey".  He made his professional acting debut with a small part in a 1998 production of "A Streetcar Named Desire", made his first major film appearance as Vincent Cusack in "Cowboys & Angels", and earned an Irish Film & Television Awards nomination in 2004 with his performance as Mo Chara in "Man About Dog".  Leech played Marcus Agrippa on the HBO historical drama series "Rome".

Paddy Breathnach: Paddy Breathnach (born 1964, Dublin, Ireland) is an Irish film director and producer.  He directed "Man About Dog", "Blow Dry" and "Shrooms".  He was also involved in the production of "The Mighty Celt" and "Ape".

Shrooms (film): Shrooms is a 2007 horror film about a group of American students and their Irish guide who are stalked by a serial killer while out in the woods looking for psilocybin mushrooms.  The film was written by Pearse Elliott, directed by Paddy Breathnach, and stars Lindsey Haun, Jack Huston, and Max Kasch.

Man About Dog: Man About Dog is a 2004 Irish comedy film starring Allen Leech, Ciaran Nolan and Tom Murphy.  The film was distributed by Redbus Film Distribution and directed by Paddy Breathnach.

Ailsa (film): Ailsa is a 1994 film directed by Paddy Breathnach.  It stars Brendan Coyle and Andrea Irvine.  It won an award at the 1994 San Sebastián International Film Festival.

Blow Dry: Blow Dry is a 2001 British comedy film directed by Paddy Breathnach, written by Simon Beaufoy and starring Alan Rickman, Natasha Richardson, Rachel Griffiths, and Josh Hartnett.  The plot focuses on the takeover of a small English town by the British Hairdressing Championship who is holding their annual competition there.

Question: What character did the star of the Irish film directed by Paddy Breathnach play in the HBO drama series "Rome"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_context": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the Irish film directed by Paddy Breathnach."
        },
        "director_name": {
          "type": "string",
          "description": "The name of the director of the film."
        },
        "film_nationality": {
          "type": "string",
          "description": "The nationality of the film."
        }
      },
      "required": [
        "title",
        "director_name",
        "film_nationality"
      ],
      "additionalProperties": false
    },
    "actor_identified": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the actor who starred in the identified film."
        },
        "role_in_identified_film": {
          "type": "string",
          "description": "The role of the actor in the identified film (e.g., 'star')."
        }
      },
      "required": [
        "name",
        "role_in_identified_film"
      ],
      "additionalProperties": false
    },
    "tv_series_role_details": {
      "type": "object",
      "properties": {
        "series_name": {
          "type": "string",
          "description": "The name of the HBO drama series."
        },
        "character_played": {
          "type": "string",
          "description": "The name of the character played by the actor in the HBO drama series."
        },
        "series_network": {
          "type": "string",
          "description": "The network that aired the series."
        },
        "series_genre": {
          "type": "string",
          "description": "The genre of the series."
        }
      },
      "required": [
        "series_name",
        "character_played",
        "series_network",
        "series_genre"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_context",
    "actor_identified",
    "tv_series_role_details"
  ],
  "additionalProperties": false
}

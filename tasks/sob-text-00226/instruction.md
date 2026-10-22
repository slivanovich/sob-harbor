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
Martin Donovan: Martin Donovan (born August 19, 1957) is an American film, stage and television actor.  He has had a long collaboration with director Hal Hartley and appeared in many of Hartley's films, such as "Trust" (1990), "Surviving Desire" (1991), "Simple Men" (1992), "Flirt" (1993), "Amateur" (1994), and "The Book of Life" (1998; in which he played Jesus).  Donovan also played Peter Scottson on Showtime's cable series "Weeds".  He made his writing/directorial debut with the film "Collaborator" (2011).

H. B. Warner: Henry Byron Warner (26 October 1875 – 21 December 1958) was an English film and theatre actor.  He was a popular theatre and film actor during the silent era and played Jesus Christ in "The King of Kings".  In later years, he successfully transitioned into supporting roles and appeared in numerous films directed by Frank Capra.  Warner's most notable role to modern audiences is "Mr. Gower" in the perennially shown film "It's A Wonderful Life", directed by Capra.  and in a cameo in "Sunset Boulevard", directed by Billy Wilder.

Selva Rasalingam: Selva Rasalingam (born 1968) is a British actor.  He has appeared on stage in the West End theatre and for the Royal Shakespeare Company and has made appearances in many UK television series including "Doctor Who", "Luther and Hustle", and on film including "" and "Skyfall".  He played Jesus in the 2014 version of "The Gospel of John".

Brave New Jersey: Brave New Jersey is a 2016 American comedy film directed by Jody Lambert written by Michael Dowling and Jody Lambert.  The film stars Tony Hale, Anna Camp, Sam Jaeger, Heather Burns, Dan Bakkedahl and Raymond J. Barry.  The film was released on August 4, 2017, by Gravitas Ventures.

Catch and Release (film): Catch and Release is a 2007 American romantic comedy film directed by Susannah Grant in her directorial debut, and starring Jennifer Garner, Timothy Olyphant, Kevin Smith, Sam Jaeger and Juliette Lewis.  In the film, after a woman's fiancé dies, she seeks comfort in his friends, learning his secrets while falling for his best friend.  Filming took place in 2005 in Vancouver and Boulder, Colorado.  "Catch and Release" premiered at the Austin Film Festival in October 2006 and was released in the United States on January 26, 2007.  The film bombed at the box office, earning $16 million against a $25 million budget.

Take Me Home (2011 film): Take Me Home is a 2011 American romantic comedy film directed by and starring Sam Jaeger.  The film also stars his wife Amber Jaeger, Lin Shaye, and Victor Garber.  It premiered on April 19, 2011 at the Nashville Film Festival.  "Take Me Home" was released to DVD on May 29, 2012.

Michael Hobert: Michael Hobert is an American actor.  He had a recurring role on the TV show "Scrubs" as Lonnie.  His brother, Tim Hobert, is one of the show's producers.  Michael has also starred in "Spin City", "Matter of Life and Death", and "Gilmore Girls".  He also wrote a movie with Sam Jaeger called "Advantage Hart".  Michael was originally in the first episode of "Scrubs", "My First Day", as "Pizza Delivery Guy", who was the guy in the MRI machine.

Victor Garber: Victor Joseph Garber (born March 16, 1949) is a Canadian actor and singer.  He is known for playing Jesus in "Godspell", Anthony Hope in "", John Wilkes Booth in "Assassins", Jack Bristow in the television series "Alias", Max in "Lend Me a Tenor", Thomas Andrews in James Cameron's "Titanic", and Ken Taylor, Canadian Ambassador to Iran, in "Argo".  He is currently a series regular on "Legends of Tomorrow" as Dr. Martin Stein, playing the same role as a guest star on "The Flash" and the web series "Vixen.

Shredy Jabarin: Shredy Jabarin or Shredi Jabarin (Arabic: شريدي جبارين‎ ‎ , Hebrew: שרדי ג'בארין‎ ‎ ; other orthographies: Shredi Jabarin) is an actor, director, writer, producer, filmmaker, photographer, artist and acting teacher.  Born on the 2nd of Dec 1981 in Jaffa and studies acting in the faculty of art in the theater department and the film department in Tel Aviv University 1999-2003, participated in international films and theatre plays in English, French, German, Arabic and Hebrew.  He has one nomination for best actor for his role in the film For my Father.  He played main parts in films like For my Father and The Saviour where her played Jesus.

Ted Neeley: Teddie Joe "Ted" Neeley (born September 20, 1943) is an American rock and roll drummer, singer, actor, composer, and record producer.  He played Jesus Christ in the film "Jesus Christ Superstar" (1973).

Question: Which actor played Jesus in "Godspell" and starred alongside Sam Jaeger in the 2011 romantic comedy "Take Me Home"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor who played Jesus."
    },
    "role_played": {
      "type": "string",
      "description": "The specific role the actor played."
    },
    "jesus_film": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film where the actor played Jesus."
        }
      },
      "required": [
        "title"
      ],
      "additionalProperties": false
    },
    "co_star_film": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film where the actor co-starred with Sam Jaeger."
        },
        "year": {
          "type": "integer",
          "description": "The release year of the co-star film."
        },
        "co_star_name": {
          "type": "string",
          "description": "The name of the co-star in the specified film."
        }
      },
      "required": [
        "title",
        "year",
        "co_star_name"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "actor_name",
    "role_played",
    "jesus_film",
    "co_star_film"
  ],
  "additionalProperties": false
}

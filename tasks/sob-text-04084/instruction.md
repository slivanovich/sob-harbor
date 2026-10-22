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
Marnie (film): Marnie is a 1964 American psychological thriller film directed by Alfred Hitchcock.  The screenplay by Jay Presson Allen was based on the 1961 novel of the same name by Winston Graham.  The film stars Tippi Hedren and Sean Connery.

James Bond 007: From Russia with Love: James Bond 007: From Russia with Love is a third-person shooter video game developed by EA Redwood Shores and published by Electronic Arts featuring Ian Fleming's secret agent, James Bond 007, whose likeness and voice is that of Sean Connery.  The game is based on the 1957 novel and the 1963 film of the same name.  The game follows the storyline of the book and film, albeit adding in new scenes to make the game more action-oriented, as well as changing the affiliation of the main villains.  Additionally, it features many elements of later Bond films to recreate the feel of the era such as the Aston Martin DB5 that debuted in "Goldfinger" (1964) and the jet pack from "Thunderball" (1965).  "From Russia with Love" is also notable in that it is the first video game to use Sean Connery's younger likeness as James Bond and the first to include all new voice work by the actor after twenty-two years away from the role.  "From Russia with Love" is the last James Bond video game EA Games marketed before they lost the rights to Activision in 2006.

The Bowler and the Bunnet: The Bowler and the Bunnet was a Scottish television documentary programme on STV, directed and presented by Sean Connery.  It is the only film ever directed by Connery.

Adolfo Celi: Adolfo Celi (] ; 27 July 1922 – 19 February 1986) was an Italian film actor and director.  Born in Curcuraci, Messina, Sicily, Celi appeared in nearly 100 films, specialising in international villains.  Although a prominent actor in Italian cinema and famed for many roles, he is best remembered internationally for his portrayal of Emilio Largo in the 1965 James Bond film "Thunderball".  Celi later spoofed his "Thunderball" role in the film "OK Connery" (aka "Operation Double 007") opposite Sean Connery's brother, Neil Connery.

The League of Extraordinary Gentlemen (film): The League of Extraordinary Gentlemen, also promoted as LXG, is a 2003 steampunk-dieselpunk action film loosely based on the first volume of the comic book series of the same name by Alan Moore and Kevin O'Neill.  It was released on July 11, 2003, in the United States, and distributed by 20th Century Fox.  It was directed by Stephen Norrington and starred Sean Connery, Naseeruddin Shah, Peta Wilson, Tony Curran, Stuart Townsend, Shane West, Jason Flemyng, and Richard Roxburgh.

Spymaker: The Secret Life of Ian Fleming: Spymaker: The Secret Life of Ian Fleming is a 1990 TV biographical film of the life of Ian Fleming, creator of the popular James Bond spy character, retracing his playboy youth, his expulsion from various colleges, his experiences as a newspaper writer and his tour of duty for the British intelligence agency during World War II.  Fleming himself is played by Jason Connery, son of Sean Connery, the actor who helped make Bond an icon in the films made in the 1960s.  Ex-Bond girl Fiona Fullerton , who appeared in "A View To A Kill", made an appearance.

Sean Connery filmography: Sir Sean Connery is a retired Scottish actor and producer.  He was the first actor to have portrayed the literary character James Bond in a film, starring in seven Bond films between 1962 and 1983.  He is also known for his roles as Jimmy Malone in "The Untouchables" (1987), for which he won an Academy Award for Best Supporting Actor, along with his portrayals of Mark Rutland in "Marnie" (1964), Juan Sánchez Villa-Lobos Ramírez in "Highlander" (1986), Henry Jones Sr. in "Indiana Jones and the Last Crusade" (1989), Captain Marko Aleksandrovich Ramius in "The Hunt for Red October" (1990), and Allan Quatermain in "The League of Extraordinary Gentlemen" (2003).  Along with his Academy Award, Connery has won two BAFTA Awards, three Golden Globes, and a Henrietta Award.

Zardoz: Zardoz is a 1974 Irish-American science fantasy film written, produced, and directed by John Boorman and starring Sean Connery and Charlotte Rampling, and featuring Sara Kestelman.  The film, Connery's second post-James Bond role—after "The Offence"—was shot by cinematographer Geoffrey Unsworth on a budget of US$1.57 million.

Vartox: Vartox is a fictional superhero published by DC Comics.  Vartox bears a striking resemblance to Scottish actor Sean Connery and his name and appearance are regarded as an allusion to the movie "Zardoz" in which Connery starred.

Cheryl Crane: On April 4, 1958, at age 14, Crane stabbed her mother's boyfriend, Johnny Stompanato, to death.  The killing was ruled a justifiable homicide: she was deemed to have been protecting her mother.  Stompanato was well-known to have been abusive, extremely jealous of Turner and had previously pointed a gun at actor Sean Connery, her co-star in "Another Time, Another Place", only to have Connery "take the gun from him, beat him and force him from the movie set" and "Scotland Yard had him deported".

Question: Who directed the film in which Sean Connery played Allen Quatermain?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "character_played_by_sean_connery": {
      "type": "string",
      "description": "The name of the character Sean Connery played in the film."
    },
    "director_name": {
      "type": "string",
      "description": "The name of the director of the film."
    },
    "release_year": {
      "type": "integer",
      "description": "The year the film was released."
    },
    "other_starring_actors": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Other prominent actors starring in the film."
    }
  },
  "required": [
    "film_title",
    "character_played_by_sean_connery",
    "director_name",
    "release_year"
  ],
  "additionalProperties": false
}

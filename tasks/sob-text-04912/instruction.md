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
The Dog and Pony Show: "The Dog and Pony Show" is the eighth episode of the third season of the American sitcom "The Drew Carey Show", and the 54th overall.  The series focuses on the work and home life of a fictionalized version of actor and comedian Drew Carey.  The episode first aired on November 12, 1997 on ABC in the United States.  The episode's plot sees Mr. Wick (Craig Ferguson) pass off caring for his boss Mrs. Lauder's (Nan Martin) Hungarian Puli to his employee Drew (Drew Carey).  When Drew has the prize-winning dog shaved and neutered, he and his friends decide to perform a striptease at the local bar, The Warsaw Tavern, to earn quick cash to buy a replacement.

Cleveland Rocks! Music from The Drew Carey Show: Cleveland Rocks!  Music from The Drew Carey Show is a soundtrack for the ABC television series "The Drew Carey Show", released on May 19, 1998, by Rhino Records.  The album has 24 tracks of songs that have appeared in the show and performances by the cast.  An original composition titled "Bite Me, Doughboy!"  was created for the album by the show's music composer W. G. Snuffy Walden.  "Cleveland Rocks!  Music from The Drew Carey Show" received mostly positive reviews from music critics, who thought the album was perfect for fans of the show.  The album won Best New Material Record Release at the 12th TV Theme Music Awards.

The Founder: The Founder is a 2016 American biographical drama film directed by John Lee Hancock and written by Robert Siegel.  The film stars Michael Keaton as businessman Ray Kroc, and portrays the story of his creation of the McDonald's fast food chain.  Nick Offerman and John Carroll Lynch co-star as McDonald's founders Richard and Maurice McDonald.

Drew Live: "Drew Live" is the eighth episode of the fifth season of the American sitcom "The Drew Carey Show", and the 109th overall.  The episode's plot focuses on Drew (Drew Carey) trying to stop his friend, Kate (Christa Miller), from pursuing a relationship with a mystery guy, as Drew is in love with her.  However, Drew is unaware that he is stopping Kate from pursuing him.  Meanwhile, Drew's brother Steve (John Carroll Lynch) and his fiancée Mimi Bobeck (Kathy Kinney) hold a joint bachelor and bachelorette party.

List of The Drew Carey Show episodes: The following is a complete list of episodes for the television show sitcom "The Drew Carey Show", which first aired on ABC on September 13, 1995.  Throughout the show's run, nine seasons were filmed amassing 233 episodes, with the final episode airing on September 8, 2004.  The sitcom follows assistant personnel director Drew Carey, in his romances and relationships to friends Lewis, Oswald, and Kate.  There have been two DVD releases for "The Drew Carey Show": the first was a six-episode compilation released on February 28, 2006 and the first season was released on April 24, 2007.

John Carroll Lynch: John Carroll Lynch (born August 1, 1963) is an American actor.  He first gained notice for his role as Norm Gunderson in "Fargo".  He is also known for his television work on the ABC sitcom "The Drew Carey Show" as the title character's cross-dressing brother, Steve Carey, as well as on "" and "" as Twisty the Clown.  His films include "Face/Off", "Gran Torino", "Shutter Island", "Ted 2", "The Invitation", and "Zodiac".  Most recently, he portrayed McDonald's co-founder Maurice "Mac" McDonald in "The Founder".  He made his directorial debut with the 2017 film "Lucky".

Sean Masterson: Sean Masterson is a comedy actor, writer, director and producer known for his work with Drew Carey, writing on "The Drew Carey Show", and as an improvisational performer on "Whose Line Is It Anyway?"  spin-offs "Drew Carey's Green Screen Show", and "Drew Carey's Improv-A-Ganza".

Drew Cam: "Drew Cam" is the ninth episode of the fifth season of the American sitcom "The Drew Carey Show", and the 110th overall.  The episode sees Drew (Drew Carey) becoming a 24-hour salesman for the Winfred-Louder department store.  Webcams are installed in his house and he has to promote the store's range of appliances.  While Drew is out, the webcams continue to stream events that occur in his house.  When the viewers become bored of Drew's life, his friend Kate O'Brien (Christa Miller) is hired to play his girlfriend for the show.  Isabel (Rosa Blasi) replaces Kate, who becomes jealous.  She eventually tells Drew she loves him during the webcast.

Pilot (The Drew Carey Show): "Pilot" is the first episode and the series premiere of the American sitcom "The Drew Carey Show".  It first aired on September 13, 1995 on the ABC network in the United States.  The premise of the show revolves around the life Drew Carey would have lived if he had not become a stand-up comedian.  The pilot introduces the main characters of Drew (Carey), Kate (Christa Miller), Lewis (Ryan Stiles) and Oswald (Diedrich Bader), as well as Drew's workplace, the fictional Winfred-Lauder department store, and enemy Mimi Bobeck (Kathy Kinney).

Drew's in a Coma: "Drew's in a Coma" is the fifteenth episode of the sixth season of the American sitcom "The Drew Carey Show", and the 142nd overall.  The plot of the episode sees Drew (Drew Carey) left in a coma after he is hit by a car.  Drew entertains himself through a fantasy world he creates, while his friends try various things to get him to wake up.  At the end of the episode, Drew chooses whether to go to heaven or not and his sister-in-law, Mimi (Kathy Kinney), goes into labor.  The episode was written by Les Firestein and directed by Gerry Cohen.  It first aired on February 7, 2001 on the ABC network in the United States.

Question: Which actor from The Drew Carey Show also starred in The Founder?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor who appeared in both productions."
    },
    "drew_carey_show_role": {
      "type": "string",
      "description": "The character played by the actor in 'The Drew Carey Show'."
    },
    "founder_role": {
      "type": "string",
      "description": "The character played by the actor in 'The Founder'."
    },
    "other_notable_roles": {
      "type": "array",
      "description": "A list of other notable roles or films the actor is known for.",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "actor_name",
    "drew_carey_show_role",
    "founder_role"
  ],
  "additionalProperties": false
}

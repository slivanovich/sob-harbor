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
Tropicana – Las Vegas Boulevard intersection: The Tropicana – Las Vegas Boulevard intersection on the Las Vegas Strip (Tropicana Avenue and Las Vegas Boulevard), is noteworthy for several reasons.  It was the first intersection in Las Vegas completely closed to street level pedestrian traffic and its four corners are home to four major resorts: Excalibur Hotel and Casino, Tropicana Las Vegas, New York-New York Hotel and Casino and MGM Grand Las Vegas—the latter has 5,044 rooms and was once the largest hotel in the world.  The resorts at the four corners have a total of 12,536 hotel rooms as of 2016.

Omaha hold 'em: Omaha hold 'em (also known as Omaha holdem or simply Omaha) is a community card poker game similar to Texas hold 'em, where each player is dealt four cards and must make his or her best hand using exactly two of them, plus exactly three of the five community cards.  The exact origin of the game is unknown, but casino executive Robert Turner first brought Omaha into a casino setting when he introduced the game to Bill Boyd, who offered it as a game at the Las Vegas Golden Nugget Casino (calling it "Nugget Hold'em").  Omaha uses a 52-card French deck.  Limit Omaha hold 'em 8-or-better is the "O" game featured in H.O.R.S.E.  Both limit Omaha/8 and pot limit Omaha high are featured in the 8-Game.

Las Vegas Uncork'd: Las Vegas Uncork'd (also referred to as Vegas Uncork'd and Vegas Uncorked) is an annual culinary and wine event in Las Vegas, Nevada.  The concept was developed by the Las Vegas Convention and Visitors Authority, their advertising agency R&R Partners and Las Vegas resort partners who originally considered a number of magazine partners such as Bon Appetit, Food & Wine and Gourmet.  Bon Appetit was selected as the magazine partner after a review with each magazine.  The event was launched in 2007 by the Las Vegas Convention and Visitors Authority, "Bon Appétit" magazine led by Editor-in-Chief Barbara Fairchild and co-creator and Executive Director Rob O'Keefe who led the first five years of development of what Eater.com called "the world's most innovative culinary event".  Las Vegas resort partners over the years include Bellagio, Caesars Palace and Wynn Las Vegas, MGM Grand, Mandalay Bay, The Venetian, Las Vegas and The Palazzo and each year the event features more than 80 celebrated chefs and over 25 events occurring over a spectacular four-day weekend.

Robert De Niro filmography: Robert De Niro's filmography includes the year the film was/will be released, the name of his character, and other related notes.  There is also a list of films he has produced and his appearances in theater plays, TV series and documentaries.  He is sometimes credited as Robert DeNiro and Robert De Nero.  De Niro has appeared in over 100 films throughout his career.

Holy Cow Casino and Brewery: Holy Cow!  Casino and Brewery (formerly Foxy's Firehouse) was a locals casino and microbrewery on South Las Vegas Boulevard, north of the Las Vegas Strip, in Las Vegas, Nevada.  The property began in 1955 as Foxy's Deli, which operated until its closure in 1975.  A year later, the building was reopened as a casino named Foxy's Firehouse, which later closed in 1988.  Tom "Big Dog" Wiesner purchased the building and reopened it as the Holy Cow casino in 1992.  Wiesner added a microbrewery the following year, making the Holy Cow the first brewery to open in Las Vegas.  Wiesner persuaded the state to change its laws that had prohibited breweries from operating in Las Vegas.

John Strzemp: John Strzemp, II (born 1952) is a casino executive and poker player based in Las Vegas, Nevada, United States.  He is the Executive Vice President and Chief Administrative Officer of Wynn Resorts.  He was previously an executive with other casinos in Las Vegas, including the Mirage Casino.

Casino (film): Casino is a 1995 American epic crime drama film directed by Martin Scorsese and starring Robert De Niro, Joe Pesci, and Sharon Stone.  It is based on the non-fiction book "" by Nicholas Pileggi, who also co-wrote the screenplay for the film with Scorsese.  The two previously collaborated on the hit film "Goodfellas" (1990).

Frank Rosenthal: Frank Lawrence "Lefty" Rosenthal (June 12, 1929 – October 13, 2008) was a professional sports better, former Las Vegas casino executive, and organized crime associate.  Martin Scorsese's film "Casino" (1995) is based on his career in Las Vegas.

Fabrizio Boccardi: Fabrizio Boccardi is an Italian American entrepreneur, investor, and producer.  Boccardi is the owner and creator of the multimedia brand the Tyrant.  In addition, he controls several investments,including Media, technology, and Gaming in the United States and abroad.  Boccardi has attempted to buy control of a Las Vegas casino, most notably Riviera Holdings, former owner of the Riviera Hotel & Casino on the strip of Las Vegas, and Riviera Casino in Black Hawk Colorado.

Madame Tussauds Las Vegas: Madame Tussauds Las Vegas is a wax museum located in the Las Vegas Strip at The Venetian Las Vegas casino resort in Paradise, Nevada.  The attraction opened in 1999, becoming the first Madame Tussauds venue to open in the United States.  It features over 100 wax figures of famous celebrities, film and TV characters, athletes, musicians and Marvel superheroes, as well a 4D movie theatre.  Subsequent Madame Tussauds venues opened in the U.S in New York City in 2000, Washington D.C. in 2007, and Hollywood, California in 2009.

Question: Robert DeNiro starred in a film based on the career of which Las Vegas casino executive?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "casino_executive": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the casino executive."
        },
        "role": {
          "type": "string",
          "description": "The role of the individual in the casino industry."
        }
      },
      "required": [
        "name",
        "role"
      ],
      "additionalProperties": false
    },
    "film_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the film."
        },
        "starring_actor": {
          "type": "string",
          "description": "The name of the actor who starred in the film."
        }
      },
      "required": [
        "title",
        "release_year",
        "starring_actor"
      ],
      "additionalProperties": false
    },
    "relationship_description": {
      "type": "string",
      "description": "A description of how the film is related to the executive's career."
    }
  },
  "required": [
    "casino_executive",
    "film_details",
    "relationship_description"
  ],
  "additionalProperties": false
}

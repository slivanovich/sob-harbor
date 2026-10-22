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
Dralion: Dralion (pronounced Drah-lee-on) was a touring production by the Canadian entertainment company Cirque du Soleil.  The show combined elements of traditional Chinese circus with Western contemporary circus, complementing the "East-meets-West" theme implied in the title — the name is a portmanteau of "dragon" (representing the East) and "lion" (representing the West).  It is Cirque du Soleil's 12th touring production and the first Cirque show since 1985 not to be directed by Franco Dragone.  Dralion performed its final show at the Sullivan Arena in Anchorage, Alaska on January 18, 2015, bringing its 15 year world tour to a close.

Le Rêve (show): Le Rêve is a stage production in residence at the Wynn Las Vegas casino resort.  It is set in an aquatic stage with a one million-gallon water capacity and features diving and feats of strength with state-of-the-art special effects, where no seat is more than 40 feet (12 m) from the stage.  The production was created by Franco Dragone and is similar to the shows produced by Cirque du Soleil.  Dragone, who was the director behind "O", "La Nouba", "Mystère", "Alegría", and "Quidam", has not revealed the cost of the production.  However, major Las Vegas shows average around $30 to $40 million to produce.  The show features 90 performers and 250 cast and crew members.

Zumanity: Zumanity is a resident cabaret-style show by Cirque du Soleil at the New York-New York Hotel & Casino on the Las Vegas Strip.  The production was unveiled on September 20, 2003.  It is the first "adult-themed" Cirque du Soleil show, billed as "the sensual side of Cirque du Soleil" or "another side of Cirque du Soleil".  Created by René Richard Cyr and Dominic Champagne, "Zumanity" is a departure from the standard Cirque format.  Intended to be for mature adult audiences only, this show is centered on erotic song, dance, and acrobatics.

Anna Stankus: Anna Stankus is a circus performer who specialises in hula hoop manipulation whilst also incorporating rhythmic gymnastics and contortion in her acts.  She is currently on tour with Cirque du Soleil Amaluna for its European and South American tours.  Since first beginning her career in 2007, she has gone on to perform in many productions worldwide including for Cirque du Soleil, Cirque Le Noir, Franco Dragone shows and in various variety shows in her hometown of Las Vegas.

A New Day...: A New Day... was a Las Vegas residency show performed by Canadian singer Celine Dion at the 4,000-seat Colosseum at Caesars Palace in Las Vegas.  It was created and directed by Franco Dragone (known for his work with Cirque du Soleil) and premiered on 25 March 2003.  90-minute event, "A New Day..." introduced a new form of theatrical entertainment, a fusion of song, performance art, innovative stage craft and state-of-the-art technology.  Dion was originally contracted for three years (Dion received about $100 million, plus 50 percent of the profits during the three-year contract), however, due to its immediate success, the show continued for an additional two years.  "A New Day..." ended on 15 December 2007, after a 5-year run of more than 700 shows and 3 million spectators.  It reached one of the highest concert grosses in music history, grossing over $400,000,000 in its entire run.

Raffaele De Ritis: Raffaele De Ritis (born 1967) is an Italian theatre director.  He is known for having created and directed numerous circus productions that have been seen worldwide through his association with Cirque du Soleil, Big Apple Circus, Ringling Bros. and Barnum & Bailey, and Franco Dragone, among others, He Wrote and directed Barnum's Kaleidoscape for Feld Entertainment(1999), one of first "boutique circuses" oner-ring under canvas that toured the United States , and involved as writer/director of two shows for Big Apple Circus (2002 and 2003).  For Cirque du Soleil he co-wrote the original circus dinner show concept "Pomp, Duck and Circumstance" (1997).

La Nouba: La Nouba is a Cirque du Soleil show in residence in a custom-built, freestanding theater at Disney Springs' West Side at the Walt Disney World Resort in Orlando, Florida.  It is a contemporary circus performance featuring acrobats, gymnasts, and other skilled performers.  The show's creation was directed by Franco Dragone, who also directed many of Cirque du Soleil's earlier shows.  Its title derives from the French phrase "faire la nouba", meaning "to party" or "to live it up".

Benoît Jutras: Benoît Jutras, (born 1963) is a Canadian composer.  Jutras is best known for his work with the Canadian entertainment company Cirque du Soleil, first as music director and later as composer for several of the company's contemporary circus shows.  Jutras' music often blends eclectic influences, including world beat, classical, rock, trip hop, and electronica.  His scores for Cirque du Soleil shows include "O", "Mystère", "Quidam", and "La Nouba".  His work outside of Cirque du Soleil has included original soundtracks for "Le Rêve" (a show at the Wynn resort in Las Vegas), the "Glow in the Park Parade" (a nighttime parade at Six Flags theme parks), and "The House of Dancing Water" (a show at the City of Dreams resort in Macau).  He has also composed for film and television.

Cirque du Soleil: Worlds Away: Cirque du Soleil: Worlds Away is a 2012 American 3D family fantasy film directed by Andrew Adamson.  The film premiered on October 20, 2012 at the Tokyo International Film Festival, and was released theatrically in the United States on December 21, 2012.  Distributed worldwide by Paramount Pictures on December 21, 2012, the film tells the story of a girl named Mia going to a traveling circus and falling in love with its main attraction, the Aerialist.  After the Aerialist falls during his act, he and Mia are transported to another world where each encounter the different worlds of Cirque du Soleil through O, Mystère, Kà, Love, Zumanity, Viva Elvis and Criss Angel Believe.  It stars Erica Linz and Igor Zaripov as the main characters and incorporates acts from some of the Cirque du Soleil shows that were running in Las Vegas in 2011 including O, Mystère, Kà, Love, and Viva Elvis.

Mystère (Cirque du Soleil): Mystère is a Cirque du Soleil show in permanent residence at the Treasure Island Hotel and Casino in Las Vegas, Nevada, United States.  It is one of six resident Cirque du Soleil shows in Las Vegas, the others being "O", "Zumanity", "Kà", "Love", and "".  "Mystère" was first performed on December 25, 1993 and quickly won over audiences with its unique style of circus entertainment.  As with many Cirque du Soleil productions, "Mystère" features a mixture of circus skills, dance, elaborate sets, opera, worldbeat music, and street theatre-style comedy.

Question: Which Franco Dragone created production is one of six resident Cirque du Soleil shows in Las Vegas ?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "show_name": {
      "type": "string",
      "description": "The name of the production."
    },
    "creator_director": {
      "type": "string",
      "description": "The person credited with creating or directing the show."
    },
    "is_cirque_du_soleil_production": {
      "type": "boolean",
      "description": "Indicates if the production is by Cirque du Soleil."
    },
    "residency_status": {
      "type": "string",
      "description": "Describes whether the show is touring or in permanent residence."
    },
    "location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the show is located."
        },
        "state_country": {
          "type": "string",
          "description": "The state and/or country where the show is located."
        }
      },
      "required": [
        "city",
        "state_country"
      ],
      "additionalProperties": false
    },
    "is_one_of_six_las_vegas_resident_shows": {
      "type": "boolean",
      "description": "Indicates if the show is one of the six resident Cirque du Soleil shows in Las Vegas."
    }
  },
  "required": [
    "show_name",
    "creator_director",
    "is_cirque_du_soleil_production",
    "residency_status",
    "location",
    "is_one_of_six_las_vegas_resident_shows"
  ],
  "additionalProperties": false
}

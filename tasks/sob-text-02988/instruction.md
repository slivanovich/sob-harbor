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
Faline: Faline is a fictional character in Felix Salten's 1923 novel "Bambi, A Life in the Woods" and its sequel "Bambi's Children", as well as in the Disney animated films "Bambi" and "Bambi II".  Her mother is Ena.  First shown as a fawn and later as a young adult doe, Faline's role is as Bambi's friend and later mate.

Classic Disney: 60 Years of Musical Magic: Classic Disney: 60 Years of Musical Magic is a 5-volume compilation series, each containing 25 (125 in total) songs compiled from Disneyland and Walt Disney World, various Disney films in animation and live-action, and the Walt Disney anthology television series.  Each volume was released individually on CD and cassette between 1995 and 1998.  Volume One was released on March 28, 1995, Volume Two on September 12, 1995, Volume Three on July 2, 1996, Volume Four on July 15, 1997 and Volume Five on September 22, 1998.  In 2000, a box set was released containing volumes 1 - 3, followed by a box set containing volumes 1 - 4 in 2001.  Finally, a box set containing all five volumes packaged in a slipcase was released by Walt Disney Records in Australia, Japan, North America and Europe in 2003.

AquaDuck: AquaDuck is a water coaster (a water slide with similar turns, drops and g-forces to a roller coaster) that is located on the deck of two Disney cruise ships.  It was first constructed on the "Disney Dream" in January 2011 and then later on the "Disney Fantasy" in February 2012.  It was developed by Walt Disney Imagineers, and despite a few exceptions, is accessible to almost anyone.  The AquaDuck is the first water coaster to exist on a cruise ship, and so far it is the only one of its kind.

Disney Friends: Disney Friends is a simulation and adventure video game released in 2007 by Amaze Entertainment for the Nintendo DS loosely based on several animated Disney films.  Published by Disney Interactive Studios, the game features characters Stitch from "Lilo & Stitch", Dory from "Finding Nemo", Pooh from "Winnie the Pooh", and Simba from "The Lion King".  Players are able to befriend and interact with each film character through the Nintendo DS' microphone and touch screen, which influence the activities and emotions of the game's characters.

Walt Disney Records: The Legacy Collection: Walt Disney Records The Legacy Collection is a compilation album series produced and released by Walt Disney Records.  The album series commemorates distinct anniversaries of Disney films and the 60th anniversary of Disneyland.  Each individual title features original artwork and illustrations by Walt Disney Animation Studios visual development artist, Lorelay Bové.  A majority of the releases feature "The Lost Chords"; newly recorded tracks done in-house by Disney staff musicians of originally discarded songs and produced to sound period-appropriate to their album counterparts.  The first entry in the series—dedicated to "The Lion King"—was released on June 24, 2014.  The thirteenth and currently most recent volume in the series—dedicated to "Robin Hood"—was released on August 4, 2017.  The entirety of the original twelve-volume series was released as a box set on November 15, 2015.

Disney Sing-Along Songs: Disney Sing-Along Songs is a series of videos, laserdiscs and DVDs with musical moments from various Disney films, TV shows and attractions.  Lyrics for the songs are displayed on-screen with the Mickey Mouse icon as a "bouncing ball".  Early releases open with a theme song introduction (written by Patrick DeRemer) containing footage featuring Professor Owl and his class, seen originally in 1953 in two Disney shorts, "Melody" and "Toot, Whistle, Plunk, and Boom" (voiced then by Bill Thompson).  Professor Owl (now voiced by Corey Burton) hosts some of the videos, while either Ludwig Von Drake or Jiminy Cricket host others, and later volumes, as well as the two Christmas videos, had no host at all.  The footage of Von Drake and Jiminy Cricket were taken from several television programs (including the Walt Disney anthology television series, and "Mickey Mouse Club") featuring the characters in the 1950s and 1960s.

Elena and the Secret of Avalor: Elena and the Secret of Avalor is an American computer-animated musical fantasy adventure crossover television movie between two Disney television series, Disney Junior's "Sofia the First" and Disney Channel's "Elena of Avalor", taking place before the latter series.  It is also the 21st episode of "Sofia the First" - Season 3 and the 74th episode in the series.  It premiered on November 20, 2016, on both Disney Channel and Disney Junior.  The Primetime special was directed and Executive Produced by Jamie Mitchell and Craig Gerber Executive Produced and wrote the screenplay.  The show was honored with a 2017 Emmy nomination for Outstanding Animated Show by the Television Academy.  "The Secret of Avalor" debuted on Disney Channel in the UK on December 3, 2016.

Bambi II: Bambi II, also known as Bambi and the Great Prince of the Forest, is a 2006 American animated drama film directed by Brian Pimental and produced by DisneyToon Studios, that initially premiered in theaters in Argentina on January 26, 2006, before being released as a direct-to-video title in the United States on February 7, 2006.  It holds the world record for the longest span of time between two consecutive installments of a franchise, being released 64 years after the original film came out in 1942.

Pinto Colvig: Vance DeBar "Pinto" Colvig (September 11, 1892 – October 3, 1967) was an American vaudeville actor, voice actor, radio actor, newspaper cartoonist, and circus performer, whose schtick was playing the clarinet off-key while mugging.  Colvig was the original Bozo The Clown, and the original voice of the Disney character Goofy.  In 1993, he was posthumously made a Disney Legend for his contributions to Walt Disney films, including "Snow White and the Seven Dwarfs" and "Fun and Fancy Free".

Pirates of the Caribbean Trading Card Game: The Pirates of the Caribbean Trading Card Game is a collectible card game based on the two Disney films "" and "".  Upper Deck Entertainment launched this title in June 2006 to roughly correspond to the release of the second film but canceled due to lack of interest.

Question: Faline is a fictional character in two Disney films the first of which came out in what year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "character_name": {
      "type": "string",
      "description": "The name of the fictional character."
    },
    "first_film_appearance": {
      "type": "string",
      "description": "The title of the first Disney film the character appeared in."
    },
    "first_film_release_year": {
      "type": "integer",
      "description": "The release year of the first Disney film the character appeared in."
    },
    "related_films": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of Disney films the character is featured in."
    }
  },
  "required": [
    "character_name",
    "first_film_appearance",
    "first_film_release_year",
    "related_films"
  ],
  "additionalProperties": false
}

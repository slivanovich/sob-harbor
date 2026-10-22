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
Sam Young (DJ): Sam Young (born 27 July 1979), is a West London DJ, remixer and producer.  He is the son of the photographer Richard Young.  Sam has played high profile events such as George Clooney's wedding in Venice in 2014, Elton John's 60th birthday party, various Brit Awards after parties for Sony BMG, film premieres such as The Hobbit, Entourage, Sex and the City, The Golden Compass, Hugo to name a few, fashion events for Gucci, Valentino, Christoper Kane, parties for Drake, Rick Ross, Timbaland, Lady Gaga, Bruno Mars, Mark Ronson, Pharrell Williams, Justin Timberlake.  Sam also DJ'd the Team USA Olympics 2012 closing party alongside Swizz Beats and Nas.

His Dark Materials: His Dark Materials is an epic trilogy of fantasy novels by Philip Pullman consisting of "Northern Lights" (1995, published as "The Golden Compass" in North America), "The Subtle Knife" (1997), and "The Amber Spyglass" (2000).  It follows the coming of age of two children, Lyra Belacqua and Will Parry, as they wander through a series of parallel universes.  The three novels have won a number of awards, most notably the 2001 Whitbread Book of the Year prize, won by "The Amber Spyglass".  "Northern Lights" won the Carnegie Medal for children's fiction in the UK in 1995.  The trilogy took third place in the BBC's Big Read poll in 2003.

The Golden Compass (film): The Golden Compass is a 2007 British-American fantasy adventure film based on "Northern Lights", the first novel in Philip Pullman's trilogy "His Dark Materials".  Written and directed by Chris Weitz, it stars Nicole Kidman, Dakota Blue Richards, Daniel Craig, Sam Elliott, Eva Green, and Ian McKellen.  The project was announced in February 2002, but difficulties over the script and the selection of a director caused significant delays.  At US$180 million, it was one of New Line Cinema's most expensive projects ever, and its disappointing results in the USA contributed to New Line's February 2008 restructuring.

Mir Zafar Ali: Mir Zafar Ali (Urdu:میر ظفر علی) is a Pakistani movie visual effects artist.  He worked in the team that won the Academy Award for best visual effects for the 2007 movie "The Golden Compass".  He is the first Pakistani to have been connected with an Academy Award-winner for Best Visual Effects.

Studio Alchimia: Studio Alchimia was a design collective, founded in 1976 in Milan, Italy by Italian Architect Alessandro Guerriero.  Studio Alchimia's aim was to recalibrate notions of craft to alignment with modern industrial civilization.  "Alchemia was part of a larger movement of Italian designers intent on coming up with strategies to dismantle the rigid ideology of modernism—they called their alternative “Nuovo Design.”  Much of their design work consisted of experimental prototypes employing technological innovation.  Studio Alchimia presented their first collection of furniture, "Bau.Haus uno" in 1978, followed by the collection, "Bau.Haus due" in 1979.  In 1981 Studio Alchimia was awarded the Golden Compass for design research.  "The "new handicrafts", which were first put on show by Alessandro Guerriero at huis Alchymia, possess certain very precise characteristics: the craftsmanship employed, given that production is made uo of small runs or unique pieces, does not depend on the us of particular techniques, but rather on the speed with which the models - whose design makes no concessions to the possibility of future mass-production - are constructed by craftsmen using the most advanced techniques in modern joinery."

Compasso d'Oro: Compasso d'Oro (] ; Golden Compass) is the name of an industrial design award originated in Italy in 1954 by the "La Rinascente" company from an original idea of Gio Ponti and Alberto Rosselli.  From 1964 it has been hosted exclusively by Associazione per il Disegno Industriale (ADI).  It is the first and most recognized award in its field.  The prize aims to acknowledge and promote quality in the field of industrial designs made in Italy and is awarded by ADI.

Brunton compass: A Brunton compass, properly known as the Brunton Pocket Transit, is a type of precision compass made by Brunton, Inc. of Riverton, Wyoming.  The instrument was patented in 1894 by a Canadian-born Colorado geologist named David W. Brunton.  Unlike most modern compasses, the Brunton Pocket Transit utilizes magnetic induction damping rather than fluid to damp needle oscillation.  Although Brunton Inc. makes many other types of magnetic compasses, the Brunton Pocket Transit is a specialized instrument used widely by those needing to make accurate degree and angle measurements in the field.  These people are primarily geologists, but archaeologists, environmental engineers, and surveyors also make use of the Brunton's capabilities.  The United States Army has adopted the Pocket Transit as the M2 Compass for use by crew-served artillery.

Chris Weitz: Christopher John "Chris" Weitz (born November 30, 1969) is an American film producer, screenwriter, author, occasional actor, and film director.  He is the brother of filmmaker Paul Weitz.  He is best known for his work with his brother on the comedy films "American Pie" and "About a Boy," the latter of which was Oscar-nominated for adapted screenplay.  Weitz directed the film adaptation of the novel "The Golden Compass" and the of "New Moon" from the series of "Twilight" books, as well wrote the screenplay for Disney's 2015 live-action adaptation of "Cinderella" and co-wrote "Rogue One: A Star Wars Story" alongside with Tony Gilroy.

Paul Weitz (filmmaker): Paul John Weitz (born November 19, 1965) is an American film director, film producer, screenwriter, playwright actor.  He is the older brother of filmmaker Chris Weitz.  He is best known for his work with his brother, Chris Weitz, on the comedy films "American Pie" and "About a Boy", for which the brothers, who co-directed, were nominated for an Oscar.  He also serves as a writer, executive producer, and director of the television series "Mozart in the Jungle".

John Weitz: Hans Werner "John" Weitz (May 25, 1923 – October 3, 2002) was a successful menswear designer who innovated the use of licensing products and selling affordable but stylish clothing that featured his image in the advertising.  He had a second career as a writer and historian.  Weitz was also well known for being the husband of actress Susan Kohner and father of directors Paul Weitz and Chris Weitz.

Question: What year was Christopher John "Chris" Weitz movie The Golden Compass made?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "movie_title": {
      "type": "string",
      "description": "The title of the movie."
    },
    "director_name": {
      "type": "string",
      "description": "The name of the director of the movie."
    },
    "release_year": {
      "type": "integer",
      "description": "The year the movie was released."
    },
    "film_type": {
      "type": "string",
      "description": "The genre or type of the film."
    }
  },
  "required": [
    "movie_title",
    "director_name",
    "release_year",
    "film_type"
  ],
  "additionalProperties": false
}

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
Solomon Kane (film): Solomon Kane is a 2009 French-British-Czech dark fantasy action-adventure film written and directed by Michael J. Bassett based on the pulp magazine character Solomon Kane created in 1928 by Robert E. Howard.  James Purefoy stars in the title role.  Despite optioning the rights in 1997, filming did not begin until January 2008.

Kubo and the Two Strings: Kubo and the Two Strings is a 2016 American 3D stop-motion fantasy action-adventure film directed and co-produced by Travis Knight (in his directorial debut), and written by Marc Haimes and Chris Butler.  It stars the voices of Art Parkinson, Charlize Theron, Ralph Fiennes, Rooney Mara, George Takei, and Matthew McConaughey.  It is Laika's fourth feature film produced.  The film revolves around Kubo, who wields a magical shamisen and whose left eye was stolen.  Accompanied by an anthropomorphic snow monkey and beetle, he must subdue his mother's corrupted Sisters and his power-hungry grandfather Raiden (aka, the Moon King), who stole his left eye.

Van Helsing (film): Van Helsing is a 2004 American dark fantasy action-adventure film written and directed by Stephen Sommers.  It stars Hugh Jackman as vigilante monster hunter Van Helsing, and Kate Beckinsale as Anna Valerious.  The film is an homage and tribute to the Universal Horror Monster films from the 1930s and '40s (also produced by Universal Studios which were in turn based on novels by Bram Stoker and Mary Shelley), of which Sommers is a fan.

Amy Mizzi: Amy Mizzi (born 21 July 1983) is an Australian actress.  She starred as Kit Hunter in the Australian soap opera "Home and Away" in 2003 and early 2004.  Mizzi's departure from "Home and Away" was announced on 13 February 2004 but she continued to appear on a recurring basis throughout 2004 and returned in August 2005.  She also made appearances in 2006, most recently in the last episode of "Home and Away" for 2006, when she returned pregnant with the baby of Kim Hyde (played by actor Chris Hemsworth).  She was nominated for Most Popular New Female Talent in the Logie Awards of 2004, but the award was won by her "Home and Away" co-star Isabel Lucas.

Isabel Lucas: Isabel Lucas (born 29 January 1985) is an Australian actress, and model.  She is best known for her roles in "Home and Away" (2003–2006), "" (2009), "Daybreakers" (2009), "The Pacific" (2010), "Immortals" (2011), and "Red Dawn" (2012).  In 2014, she appeared alongside Karl Urban in "The Loft" (2014), and in the following year, she appeared alongside Nick Jonas in the thriller film "Careful What You Wish For" (2015).

The Mortal Instruments: City of Bones: The Mortal Instruments: City of Bones is a 2013 Canadian-German urban fantasy action-adventure film based on the first book of "The Mortal Instruments" series by Cassandra Clare.  The story takes place in an urban and contemporary New York City.  Directed by Harald Zwart, the film stars an international cast, including Lily Collins, Jamie Campbell Bower, Robert Sheehan, Kevin Zegers, Jemima West, Godfrey Gao, Lena Headey, Jonathan Rhys Meyers, Aidan Turner, Kevin Durand, and Jared Harris.  It was released in theaters on August 21, 2013, by Screen Gems in the United States and Entertainment One in the United Kingdom.  "The Mortal Instruments: City of Bones" earned $91 million against a $60 million production budget.  "The Mortal Instruments: City of Bones" was released on DVD and Blu-ray on December 3, 2013, by Sony Pictures Home Entertainment.

Dragonheart: Dragonheart is a 1996 British-American fantasy action-adventure film directed by Rob Cohen.  It stars Dennis Quaid, David Thewlis, Pete Postlethwaite, Dina Meyer, and the voice of Sean Connery.  It was nominated for the Academy Award for Best Visual Effects and various other awards in 1996 and 1997.

Immortals (2011 film): Immortals is a 2011 American epic fantasy action-adventure film directed by Tarsem Singh and starring Henry Cavill, Freida Pinto, and Mickey Rourke.  The film also stars Luke Evans, Steve Byers, Kellan Lutz, Joseph Morgan, Stephen Dorff, Daniel Sharman, Alan van Sprang, Isabel Lucas, Corey Sevier, and John Hurt.  The film was previously named "Dawn of War" and "War of the Gods" before being officially named "Immortals", and is loosely based on the Greek myths of Theseus, the Minotaur and the Titanomachy.

Mga Kwento ni Lola Basyang: Mga Kwento ni Lola Basyang (lit.  "The Stories of Grandma Basyang") was an withdrawn fantasy action-adventure film produced by Unitel Productions.  The film is a two-story, "Pedrong Walang Takot" and "Mariang Alimango" derived from the short stories of Mga Kuwento ni Lola Basyang written by Severino Reyes.  The film is directed by Mark Meilly, and Chris Martinez.  It stars Richard Gomez, Paolo Contis, Sam Concepcion, Iza Calzado, Rufa Mae Quinto, Empress Schuck and Zsa Zsa Padilla.  It is one of the 8 official entries for 2012 Metro Manila Film Festival but later on the film sent a request letter to MMDA to pull out of the festival.  On October 19, the film was replaced by Thy Womb.

Gods of Egypt (film): Gods of Egypt is a 2016 English-language fantasy action-adventure film directed by Alex Proyas and portraying ancient Egyptian deities.  It stars Nikolaj Coster-Waldau, Brenton Thwaites, Chadwick Boseman, Élodie Yung, Courtney Eaton, Rufus Sewell, Gerard Butler and Geoffrey Rush.  The film portrays a mortal Egyptian hero who partners with the Egyptian god Horus to save the world from Set and rescue his love.

Question: Immortals, released in which year, is an American epic fantasy action-adventure film, the film also stars Isabel Lucas, an Australian actress, and model?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "release_year": {
      "type": "integer",
      "description": "The year the film was released."
    },
    "genre": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The genres of the film."
    },
    "country_of_origin": {
      "type": "string",
      "description": "The country where the film was produced."
    },
    "starred_actress": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the actress who starred in the film."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the actress."
        },
        "professions": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "The professions of the actress."
        }
      },
      "required": [
        "name",
        "nationality",
        "professions"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "film_title",
    "release_year",
    "genre",
    "country_of_origin",
    "starred_actress"
  ],
  "additionalProperties": false
}

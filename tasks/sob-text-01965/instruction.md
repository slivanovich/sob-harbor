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
Stargate SG-1: Stargate SG-1 (often abbreviated as SG-1) is an adventure and military science fiction television series and part of Metro-Goldwyn-Mayer's "Stargate" franchise.  The show, created by Brad Wright and Jonathan Glassner, is based on the 1994 science fiction film "Stargate" by Dean Devlin and Roland Emmerich.  The television series was filmed in and around the city of Vancouver, British Columbia, Canada.  The series premiered on Showtime on July 27, 1997 and moved to the Sci Fi Channel on June 7, 2002; the final episode first aired on Sky1 on March 13, 2007.  With 214 episodes over ten seasons, "Stargate SG-1" had surpassed "The X-Files" as the longest-running North American science fiction television series, until it was surpassed by the series "Smallville" in 2011.

Kashyyyk: Kashyyyk ( , or ), also known as Wookiee Planet C, is a planet in the "Star Wars" universe.  It is the tropical, forested home world of the Wookiees.  According to interviews given by "Star Wars" creator George Lucas, the home of the Wookiees was originally intended to be the forest moon of Endor which plays a key role in the plot of the sixth film of the series, "Return of the Jedi".  However, Lucas decided that since the Wookiee Chewbacca was clearly proficient with advanced technology (i.e. he was pilot and mechanic of the spaceship the "Millennium Falcon" and he repaired the damaged droid C-3PO), it would be confusing to show the Wookiees with a primitive, "stone age" culture on Endor.  The Ewoks were created instead to populate the moon and to help fight the Imperial garrison stationed there.  Kashyyyk made appearances in the "Star Wars Holiday Special" and "".

The Ghastly Love of Johnny X: The Ghastly Love of Johnny X is a 2012 American musical science fiction comedy film written, produced, and directed by Paul Bunnell.  It stars Will Keenan, Creed Bratton, and De Anna Joy Brooks, Reggie Bannister, Les Williams, Jed Rowen and features, in supporting roles, Kate Maberly, Paul Williams and Kevin McCarthy.  It was the last feature film shot in Kodak Plus-X.

Rock &amp; Rule: Rock & Rule (known as "Ring of Power" outside North America) is a 1983 Canadian adult animated musical science fiction fantasy film from the animation studio Nelvana, marking the first time the company has made an animated production for adults.  It was produced and directed by the company's founders, Michael Hirsh, Patrick Loubert, and Clive A. Smith.  The film features the voices of Don Francks, Greg Salata, and Susan Roman.  It was the studio's first feature film and the first English language one produced entirely within Canada.

The Stranger (Australian TV series): The Stranger (1964–65) was an Australian science fiction television series made for children and produced by the Australian Broadcasting Corporation (then known as the Australian Broadcasting Commission).  It is notable as Australia's first locally produced science fiction television series and one of the first Australian TV series to be sold overseas.

Martha Jones: Martha Jones is a fictional character played by Freema Agyeman in the long-running British science fiction television series "Doctor Who" and its spin-off series, "Torchwood".  She is a companion of the Tenth Doctor in "Doctor Who", after Rose Tyler (Billie Piper).  According to the character's creator and executive producer Russell T Davies in his non-fiction book "", the character was developed from the beginning with the intention of appearing for a whole of the 2007 series, and to later make guest appearances in subsequent series and crossover appearances in the show's two spin-offs; Martha subsequently made guest appearances in "Torchwood" series two and in "Doctor Who" series four in 2008 and special episode "The End of Time" in 2010.  Martha was also intended to make guest appearances in the 2009 series of "Torchwood" and "The Sarah Jane Adventures", but could not due to the actress's other obligations.

Cameron Mitchell (Stargate): Lieutenant Colonel Cameron "Cam" Mitchell, USAF is a fictional character in the Canadian-American military science fiction television series "Stargate SG-1", a science fiction show about a military team exploring the galaxy via a network of alien transportation devices.  Played by Ben Browder, Cameron Mitchell is introduced as a main character in the season 9 premiere "Avalon", holding the military rank of Lieutenant Colonel in the United States Air Force.  Learning of the SG-1 team's off-screen separation after the previous season, Mitchell is assigned as new commanding officer of SG-1, which he remains throughout season 10 (2006–2007) and the direct-to-DVD films "" and "" (2008).

The Magic of Lassie: The Magic of Lassie is a 1978 American musical drama film directed by Don Chaffey, starring Lassie, James Stewart, Stephanie Zimbalist, Pernell Roberts, and Michael Sharrett, with cameo appearances by Mickey Rooney and Alice Faye (in her final film appearance).  James Stewart is featured in one of only three musical film roles that he played: the first was "Born to Dance" (1936) in which he introduced the Cole Porter standard "Easy To Love" and the second was "Pot O' Gold" (1941).  This was also his final onscreen appearance in a live-action film.  The screenplay and song score are supplied by the prolific Sherman Brothers of "Mary Poppins" fame.  Their song "When You're Loved" was nominated for an Academy Award for "Best Original Song" and was sung by Debby Boone.  It is also the only musical film featuring Lassie.

Cindy (film): Cindy is a 1978 American musical television film that features an entirely African-American cast.  Directed by William A. Graham, the film is an urbanized retelling of Cinderella.

Star Wars Holiday Special: The Star Wars Holiday Special is a 1978 American musical science fiction television film set in the "Star Wars" galaxy.  It stars the first film's main cast while introducing the character Boba Fett, who would appear in later films.  It is one of the first official "Star Wars" spin-offs and was directed by Steve Binder.

Question: Kashyyyk made appearances in a 1978 American musical science fiction television film that introduced what character?

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
    "film_genre": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The genres of the film."
    },
    "film_type": {
      "type": "string",
      "description": "The type of film (e.g., 'television film')."
    },
    "film_country": {
      "type": "string",
      "description": "The country of origin for the film."
    },
    "introduced_character": {
      "type": "string",
      "description": "The character introduced in the film."
    },
    "planet_featured": {
      "type": "string",
      "description": "The planet that made an appearance in the film."
    }
  },
  "required": [
    "film_title",
    "film_year",
    "film_genre",
    "film_type",
    "film_country",
    "introduced_character",
    "planet_featured"
  ],
  "additionalProperties": false
}

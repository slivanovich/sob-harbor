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
Disneynature: Disneynature is an independent film unit of Walt Disney Studios that produces nature documentary films.  The production company was founded on April 21, 2008 and is headquartered in Paris, France.  Heading the unit is Disney veteran Jean-Francois Camilleri, who also serves as senior vice president and general manager for Walt Disney Studios Motion Pictures France.

Big Cat Diary: Big Cat Diary, also known as Big Cat Week or Big Cat Live according to the format of the show, was a long-running nature documentary series on BBC television which follows the lives of African big cats in Kenya's Maasai Mara.  The first series, broadcast on BBC One in 1996, was developed and jointly produced by Keith Scholey, who would go on to become Head of the BBC's Natural History Unit.  Eight further series have followed, most recently "Big Cat Live", a live broadcast from the Mara in 2008.

Bears (film): Bears is a 2014 nature documentary film about a family of brown bears living in the coastal mountain ranges of Alaska.  Directed by Alastair Fothergill and Keith Scholey and narrated by John C. Reilly, "Bears" was released theatrically by Disneynature on April 18, 2014, the seventh nature documentary released under that label.

Keith Scholey: Keith Scholey (born 24 June 1957 in Dar es Salaam, Tanzania) is a British producer of nature documentaries for television and cinema, and a former television executive.  He co-directed "African Cats" and "Bears" with Alastair Fothergill for Disneynature.  He is also the executive producer of the series 'North America' for the Discovery Channel.

African Cats: African Cats is a 2011 nature documentary film directed by Keith Scholey and Alastair Fothergill about a pride of lions and a family of cheetahs trying to survive on the African savannah.  The film was released theatrically by Disneynature on Earth Day, April 22, 2011.  The film is narrated by Samuel L. Jackson (Patrick Stewart in the UK release).  A portion of the proceeds for the film were donated to the African Wildlife Foundation and their effort to preserve Kenya's Amboseli Wildlife Corridor.  The film's initiative with the African Wildlife Foundation is named "See African Cats, Save the Savanna," and as of May 2, 2011, ticket sales translated into 50,000 acres of land saved in Kenya.

Disney Music Group: Disney Music Group (DMG) is the music production arm of Walt Disney Studios, a division of The Walt Disney Company.  The division's subsidiaries consist of two owned record labels—Walt Disney Records, Hollywood Records—and Disney Music Publishing, the publishing entity that administers the company's music, as well as Disney Concerts.  The president of the group is Ken Bunt, who reports to Alan F. Horn, the chairman of The Walt Disney Studios.  It is currently headquartered in the Frank G. Wells Building at The Walt Disney Studios in Burbank.

Walt Disney Pictures: Walt Disney Pictures, Inc. is an American film production company and a subsidiary of Walt Disney Studios, owned by The Walt Disney Company.  The division is based at the Walt Disney Studios in Burbank, California, and is the main producer of live-action feature films within the Walt Disney Studios unit.  It took on its current name in 1983.  Today, in conjunction with the other units of Walt Disney Studios, Walt Disney Pictures is classified as one of Hollywood's "Big Six" film studios.  Films produced by Walt Disney Animation Studios and Pixar Animation Studios are also released under this brand.

Disney Movies Anywhere: Disney Movies Anywhere is a digital film locker for Disney, Pixar, Marvel, and "Star Wars"-branded films in the United States.  It allows for the storage of digital movie rights via purchases from providers such as iTunes, Google Play, Vudu, Microsoft, Amazon Video, and Verizon Fios.  Rights to titles can also be added via redemption of Disney Movies Rewards "Magic/Action Codes" from select titles that provide either a digital HD download or digital copy.  The service allows consumers to redeem films produced by Walt Disney Pictures, Walt Disney Animation Studios, Pixar, Marvel Studios, Disneynature, and Lucasfilm, all owned by the Walt Disney Studios.  Disney Movies Anywhere allows streaming of content over the web or mobile apps, along with access to the title through the linked accounts in participating providers.  It is powered by a proprietary digital rights system called KeyChest.

Walt Disney Studios Motion Pictures: Walt Disney Studios Motion Pictures (formerly Buena Vista Pictures Distribution and Buena Vista Film Distribution Company) is an American film distributor owned by The Walt Disney Company.  Established in 1953 as Buena Vista Film Distribution Company, the company handles theatrical distribution, marketing and promotion for films produced and released by the Walt Disney Studios, including Walt Disney Pictures, Walt Disney Animation Studios, Pixar Animation Studios, DisneyToon Studios, Marvel Studios, Lucasfilm, Disneynature, and Touchstone Pictures.  The division took on its current name in late 2007, which before that had been Buena Vista Pictures Distribution since 1987.

Hollywood Pictures: Hollywood Pictures was an American film production label of The Walt Disney Studios, a division of The Walt Disney Company.  Similar to Disney's Touchstone Pictures and former Miramax and Dimension film labels, it produced films for a more mature adult audience than Walt Disney Pictures and Disneynature.  The label's metonym was the Sphinx.

Question: Who did Keith Scholey co-directed "African Cats" and "Bears" with Disneynature, an independent film unit of Walt Disney Studios?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "co_director_name": {
      "type": "string",
      "description": "The name of the person who co-directed the films with Keith Scholey."
    },
    "films_co_directed": {
      "type": "array",
      "description": "A list of films co-directed by Keith Scholey and the identified co-director.",
      "items": {
        "type": "string"
      }
    },
    "production_unit": {
      "type": "string",
      "description": "The name of the film production unit responsible for the films."
    },
    "production_unit_description": {
      "type": "string",
      "description": "A description of the production unit."
    }
  },
  "required": [
    "co_director_name",
    "films_co_directed",
    "production_unit",
    "production_unit_description"
  ],
  "additionalProperties": false
}

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
Jenny (doll): Jenny (ジェニー , Jenī ) is a 10½ inch fashion doll produced by Japanese toy company now known as Takara Tomy since 1982.  The doll was known as "Takara Barbie", and in 1986 the doll was renamed "Jenny" after Takara ended their licensing agreement with Mattel. Takara Barbie differs from a western Barbie.  Takara Barbie was altered to better appeal to Japanese preferences, with a shorter height, large rounded manga-style eyes and a closed mouth.  The doll's physical figure is more natural than the Western Barbie's exaggerated figure.  Like her Western counterpart, Jenny wears a large variety of outfits, which often include street fashion, school uniforms, kimonos, and other uniquely Japanese costumes, such as "Bullet-Train Stewardess Jenny".  Today the Jenny doll is a sentimental favorite doll in Japan, but she is much less popular than Licca-chan, Japan's market leader fashion doll.

Alexander Doll Company: Alexander Doll Company is an American manufacturer of collectible dolls.  The business was founded in 1923 by Beatrice Alexander, a New York City woman who designed and sewed cloth dolls.  Styling herself Madame Alexander, which also became the trade name for her dolls, Alexander went on to create dolls replicating famous personalities and characters in books, films, music, and art.  Among her notable creations were dolls replicating the Dionne quintuplets, Scarlett O'Hara, and the royal family and attendees at the 1953 coronation of Queen Elizabeth II.  The company produced the first fashion doll, "Cissy", four years before Barbie was released.  Continually aiming to improve her product, Alexander began making hard plastic dolls after World War I and vinyl plastic dolls in the 1960s.  By the 1960s the company was the leading American doll manufacturer.  In the 1980s, it released one million dolls annually.  Beatrice Alexander ran the company for 65 years and sold it in 1988.  As of 2016, the company has produced 6,500 dolls.

Dollfie: Dollfie is a brand of vinyl doll created by the Japanese company Volks in 1997.  It is a highly poseable hybrid of fashion doll and action figure.  A Dollfie doll is about the size of a Barbie doll, 1/6 or , though there are variants in different heights ranging from 23 – .  Dollfie dolls generally come blank, i.e., their heads are not painted.  When an artist paints a Dollfie, the technique is referred to as a "face-up" or "make-up".  Dollfie dolls are much more flexible than typical Barbie-style western fashion dolls of the same size, because of the much larger number of joints in the body.

Christina Aguilera doll: The Christina Aguilera doll was released in 2000 by Yaboom Toys.  The celebrity doll featured the likeness of Christina Aguilera, with different outfits from her concerts, appearances, photoshoots, and music videos.  Some dolls could "sing" when a button on their bellies was pressed.  Yaboom planned "talking dolls", but they were never developed.  The other dolls were standard fashion dolls (see Barbie) made with help from Play Along Toys.  They became a hit during the 2000 holiday season.  Later on, the line was promoted less often, and was eventually discontinued before Christina released her 2002 album "Stripped", with its more adult content.

Polly Fashion (Model) Doll: Polly was a popular fashion doll competitor that competed with various fashion dolls, though the 1960s and 2000s originally made by Valentine Doll Co in 1962 to 1964 and then by other manufactures for other companies through (1958–Present Known as the (Polly Series) she's currently being made by "Polyfect Toys" a private toy company in china.  Sold through Family Dollar department stores, as a cheaper alternative to other fashion dolls.

Family Dollar: Family Dollar is an American variety store chain.  With over 8,000 locations in all states except Alaska, Hawaii, Oregon and Washington, it is the second largest retailer of its type in the United States.  Family Dollar is headquartered in Matthews, a suburb of Charlotte, North Carolina, where it employs 1,400 people.

Bratzillaz (House of Witchez): Bratzillaz (House of Witchez) is an American line of fashion dolls released by MGA Entertainment in 2012.  The dolls, a spin-off of the company's popular franchise Bratz.  Bratzillaz dolls are marketed as witches with special powers that make each character unique.  The Bratzillaz girls are cousins of the Bratz and most of the characters have a similar name to a Bratz character.  Starting with the Summer/Fall 2013 doll lines, MGA began to use "House of Witchez" in the main logo to emphasize the Bratzillaz's "witchy" nature after they were thought to be copying Monster High, a line of monster-like fashion dolls by MGA's competitor Mattel.  The commercials for the "Back to Magic" and "Witchy Princesses" lines never said Bratzillaz in them, only "House of Witchez".

Asian fashion doll: Asian fashion dolls are fashion dolls that are made by Asian manufacturers or primarily targeted to an Asian market.  Some have received international attention, such as with Momoko Doll, and in 2005 the first annual Dollstyle convention was held in Tokyo.

Pippa (doll): Pippa was a "pocket-sized" fashion doll, like Polly Pocket, offered by British toymaker Palitoy between 1972 and 1980.  She was a 6.5 inch fashion doll with numerous friends, fashions, an apartment, a car, even her own hair salon.  Similar to Topper's Dawn doll, Pippa was marketed as "the pocket money fashion doll that puts fashion in your pocket".  The dolls small stature also meant that production costs were lower than competitors such as Sindy and Barbie.

Fashion doll: Fashion dolls are dolls primarily designed to be dressed to reflect fashion trends.  They are manufactured both as toys for children to play with and as collectibles for adult collectors.  The dolls are usually modeled after teen girls or adult women, though child, male, and even some non-human variants exist.  Contemporary fashion dolls are typically made of vinyl or another plastic.  Recently, 3D software versions have appeared.

Question:  Polly Fashion, was a popular fashion doll competitor that competed with various fashion dolls, though the 1960s and 2000s originally made by Valentine Doll Co in 1962 to what year, it was sold through the American variety store chain, Family Dollar department stores, as a cheaper alternative to other fashion dolls?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "doll_name": {
      "type": "string",
      "description": "The name of the fashion doll."
    },
    "original_manufacturer": {
      "type": "string",
      "description": "The company that originally manufactured the doll."
    },
    "original_production_start_year": {
      "type": "integer",
      "description": "The start year of the doll's original production by the specified manufacturer."
    },
    "original_production_end_year": {
      "type": "integer",
      "description": "The end year of the doll's original production by the specified manufacturer."
    },
    "retail_channel": {
      "type": "string",
      "description": "The retail store chain where the doll was sold."
    },
    "market_positioning": {
      "type": "string",
      "description": "How the doll was positioned in the market relative to competitors."
    }
  },
  "required": [
    "doll_name",
    "original_manufacturer",
    "original_production_start_year",
    "original_production_end_year",
    "retail_channel",
    "market_positioning"
  ],
  "additionalProperties": false
}

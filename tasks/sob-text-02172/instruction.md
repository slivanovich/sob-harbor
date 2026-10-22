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
The Tree That Remembers: The Tree That Remembers is a 2002 animated documentary by Iranian filmmaker Masoud Raouf, exploring the lives of former political prisoners like himself who had been active in the democratic movement during the days of the Shah of Iran, only to face imprisonment and torture under the Islamic regime after the 1979 Iranian revolution.

Crazy English: Crazy English () is a brand name related to a non-traditional method

Jorkens Remembers Africa: Jorkens Remembers Africa is a collection of fantasy short stories, narrated by Mr. Joseph Jorkens, by writer Lord Dunsany.  It was first published in New York City by Longmans, Green & Co. in October, 1934, with the English edition (under the alternate title "Mr. Jorkens Remembers Africa") following in November of the same year from the same publisher.  It was the second collection of Dunsany's Jorkens tales to be published.  It has also been issued in combination with the first book, "The Travel Tales of Mr. Joseph Jorkens", in the omnibus edition "The Collected Jorkens, Volume One", published by Night Shade Books in 2004.

Lilo &amp; Stitch: Lilo & Stitch is a 2002 American animated science fiction comedy-drama film produced by Walt Disney Feature Animation and released by Walt Disney Pictures.  The 42nd Disney animated feature film, "Lilo & Stitch" was written and directed by Dean DeBlois and Chris Sanders, the latter also starring as Stitch, and features the voices of Daveigh Chase, Tia Carrere, David Ogden Stiers, Kevin McDonald, Ving Rhames, Jason Scott Lee, and Kevin Michael Richardson.  It was the second of three Disney animated features produced primarily at the Florida animation studio located at Disney's Hollywood Studios (then known as Disney-MGM Studios during production) in Walt Disney World near Orlando, Florida.

Walt Disney Classics: Walt Disney Classics was a brand name used by Walt Disney Home Video on their American, Japanese, European, and Australian home video releases of List of Walt Disney Animation Studios features.  The last title in the Classics line from 1984–1994 was "The Fox and the Hound".  With the release of "Snow White and the Seven Dwarfs", all the existing titles in the Classics line were replaced with the Masterpiece Collection line and the Classics line was canceled in the United States and Canada.  Cassette copies of the original Classics series became much sought-after, and are very popular with collectors, since most retailers had the first home video release for Disney animated features in their stores up to the time when the label was discontinued.  Animated features and other films containing animation (such as "Mary Poppins" and "Pete's Dragon") continued to be released under the "Walt Disney Classics" label and its foreign language equivalents until around 2007 throughout Europe, and "Walt Disney Meisterwerke", the German equivalent series, is still in operation as of 2010 through its broader "Special Collection" range.

Crazy English (film): Crazy English is a 1999 Chinese documentary directed by Zhang Yuan.  The film premiered along with Zhang's "Seventeen Years" at the 1999 Locarno International Film Festival.  It established Zhang's position as a "legitimate" director after years of working independently from, and often at odds with, the Chinese authorities.

Li Yang (Crazy English): Li Yang (; born 1969 in Changzhou, Jiangsu) is a Chinese educator and language instructor.  He is the creator of "Crazy English", an unorthodox method of teaching English.  He claimed to have taught English to more than 20 million people in a decade.

Alice in Wonderland (1951 film): Alice in Wonderland is a 1951 American animated musical fantasy-adventure film produced by Walt Disney Productions and based on the "Alice" books by Lewis Carroll.  The 13th of Disney's animated features, the film premiered in New York City and London on July 26, 1951.  The film features the voices of Kathryn Beaumont as Alice, Sterling Holloway as the Cheshire Cat, Verna Felton as the Queen of Hearts, and Ed Wynn as the Mad Hatter.

Joyce Dyer: Joyce Dyer (born July 20, 1947) is a U.S. writer of nonfiction and memoirs whose most recent memoir, "Goosetown: Reconstructing an Akron Neighborhood", tells the story of the author's attempt to remember the first five years of her life growing up in an ethnic neighborhood in Akron called Old Wolf Ledge (known to residents as "Goosetown"), famous for its glacial formations, breweries, and cereal mills.  "Goosetown" is the prequel to "Gum-Dipped: A Daughter Remembers Rubber Town", her book about the decades when Akron was the Rubber Capital of the World.  In it Dyer provides a loving but complicated portrait of her father and a view of the relationships among Firestone Tire and Rubber Company, its employees, and the city of Akron, Ohio.  Earlier memoirs were "In a Tangled Wood: An Alzheimer's Journey" and "Gum-Dipped: A Daughter Remembers Rubber Town."  She has also edited two collections of essays, "Bloodroot: Reflections on Place by Appalachian Women Writers" and "From Curlers to Chainsaws: Women and Their Machines."  Her first book, "The Awakening: A Novel of Beginnings", was a scholarly study of Kate Chopin, a turn-of-the-century American writer.  Joyce Dyer is Professor Emerita of English at Hiram College, where she continues to teach occasional courses in creative writing.  Her teaching and writing specialties are essay and hybrid nonfiction.  Dyer's biography is included in "Contemporary Authors", volume 146, and in the New Revision Series, volume 91.

List of stop motion films: This is a list of films that showcase stop motion animation, and is divided into three sections: Animated features, Live action features, and Animated shorts.  For films made using puppetry (in other words, using puppets but not animation), please go .  Note: This list includes films that are not exclusively stop motion.

Question: Are Crazy English and The Tree That Remembers both animated features?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "are_both_animated_features": {
      "type": "boolean",
      "description": "True if both films are animated features, false otherwise."
    },
    "film_comparison": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the film."
          },
          "is_animated": {
            "type": "boolean",
            "description": "True if the film is animated, false otherwise."
          },
          "genre": {
            "type": "string",
            "description": "The genre of the film."
          },
          "release_year": {
            "type": "integer",
            "description": "The release year of the film."
          }
        },
        "required": [
          "title",
          "is_animated",
          "genre",
          "release_year"
        ],
        "additionalProperties": false
      },
      "description": "Details for each film being compared."
    },
    "conclusion_reasoning": {
      "type": "string",
      "description": "Explanation for the conclusion."
    }
  },
  "required": [
    "are_both_animated_features",
    "film_comparison",
    "conclusion_reasoning"
  ],
  "additionalProperties": false
}

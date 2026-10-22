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
Screenland: Screenland was a monthly U.S. magazine about movies, published between September 1920 and June 1971, when it merged with "Silver Screen".  In the September 1952 issue, the name changed to Screenland plus TV-Land.

Marion Lignana Rosenberg: Marion Lignana Rosenberg (December 8, 1961 – November 28, 2013) / / was a writer, music critic, translator and a broadcaster and journalist who blogged for "WQXR Operavore" and had a weekly column called "Prima Fila" for "La Voce di New York".  She contributed features, reviews, and essays about the arts to "NewMusicBox", "Town & Country", "Newsday", "Time Out New York", "The Wall Street Journal", "Capital New York", "The Classical Review", Salon.com, "Forward", "The New York Times", "San Francisco Chronicle", "Boston", "Opera News", and "Playbill".  Rosenberg's essay "Re-visioning Callas" won a Newswomen's Club of New York Front Page Award.  She also wrote an entry on Maria Callas for "Notable American Women: Completing the Twentieth Century" (Harvard University Press).

Playbill: Playbill is a monthly U.S. magazine for theatregoers.  Although there is a subscription issue available for home delivery, most copies of "Playbill" are printed for particular productions and distributed at the door as the show's program.

Autograph Collector Magazine: Autograph Collector Magazine is a U.S. magazine for autograph collectors.  The magazine was started in 1986.  They offer news, celebrity interviews and addresses, in-person signing event listings, counterfeit-detection articles, and in-depth articles on collecting autographs from people in various professions, from sports to Hollywood to business and more.  The magazine is now a web-only publication.  The print version was published on a monthly basis.

Black Enterprise: Black Enterprise is a monthly U.S. magazine that describes itself as "the premier business, investing, and wealth-building resource for African Americans." Since the 1970s, the magazine has been the most popular publication devoted to African-American businesses.  It reports a readership of 3.7 million.  It was founded in 1970 by Earl G. Graves, Sr. The publication is known for its annual listing of the largest African-American firms in the country, or "B.E. 100's", first compiled and published in 1973.  In 2002 the magazine launched a supplement targeting teens, "Teenpreneur".

Soldier of Fortune (magazine): Soldier of Fortune (SOF), "The Journal of Professional Adventurers", is a monthly U.S. periodical founded in 1975 as a mercenary magazine devoted to worldwide reporting of wars, including conventional warfare, low-intensity warfare, counter insurgency, and counter-terrorism.  It has been published by the Omega Group Ltd., in Boulder, Colorado.

Run (magazine): Run was an American computer magazine published monthly by IDG Communications with its first issue debuting in January 1984.  Bi-monthly publishing began in June/July 1990 (issue #78, volume 7 number 6), and went on until the magazine folded in November/December 1992 (issue #94, volume 9 number 6).  In its heyday, "Run"' s monthly circulation was in the 200,000–300,000 range. " Folio", the trade journal of the magazine industry, rated it as the second fastest-growing U.S. magazine of 1985.

Maddy Rosenberg: Maddy Rosenberg is an American artist from Brooklyn, New York, United States.  She has an active exhibition and freelance curatorial career and is now the director of Central Booking in DUMBO, Brooklyn, New York.  Rosenberg received a BFA from Cornell University and her MFA from Bard College.  Rosenberg is an artist and a curator.  She taught at Marymount Manhattan College and also at the Manhattan Graphics Center for more than ten years.  Rosenberg has worked on a number of international exchange exhibitions between New York and European artists.  Her profile appears in "Who's Who in American Women" and the "Dictionary of National Biography".  Articles and reviews include in "Printmaking Today", "Art and Métiers du Livre", "Artists Books Reviews", "Haberarts", "Umbrella", "Art Review", "Arlis" (UK), "NYArts" (International Edition), "Salzburger Nachrichten", and "New York Magazine", as well as on "BBC Radio" (Bristol, England).

Sister 2 Sister: Sister 2 Sister was a monthly U.S. four-color women's magazine devoted to the world of African-American entertainment.  It was in circulation between 1988 and 2014.

Stagebill: Stagebill was a monthly U.S. magazine for theatregoers.  Most copies of the publication were printed for particular productions and distributed at the door as the show's program.  It was launched as a direct rival to the highly successful monthly "Playbill".  But after five years of head-to-head tough competition with "Playbill", "Stagebill" became insolvent and was acquired by its rival who also kept the "Stagebill" trademark.

Question: What monthly U.S. magazine for theatregoers has Marion Lignana Rosenberg contributed to?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "contributor_name": {
      "type": "string",
      "description": "The name of the person who contributed to the magazine."
    },
    "magazine_name": {
      "type": "string",
      "description": "The name of the magazine."
    },
    "magazine_description": {
      "type": "string",
      "description": "A description of the magazine's target audience or type."
    },
    "contribution_types": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of types of content contributed to the magazine."
    }
  },
  "required": [
    "contributor_name",
    "magazine_name",
    "magazine_description",
    "contribution_types"
  ],
  "additionalProperties": false
}

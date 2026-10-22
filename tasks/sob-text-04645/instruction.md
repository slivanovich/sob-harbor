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
Carl-Eduard von Bismarck: Carl-Eduard Otto Wolfgang Jayme Anders Graf von Bismarck-Schönhausen (born February 16, 1961 in Zurich) is a German politician (CDU).

Mona von Bismarck: Mona von Bismarck (February 5, 1897 – July 10, 1983), known as Mona Bismarck, was an American socialite, fashion icon, and famed beauty.  Her five husbands included Harrison Williams, said to be the richest man in America, and the Graf von Bismarck-Schönhausen, grandson of German Chancellor Otto von Bismarck.  Mona was the first American to be named "The Best Dressed Woman in the World" by a panel of top couturiers including Chanel, and was also named to the International Best Dressed List Hall of Fame.

Count de Salis-Seewis: Count de Salis-Seewis (also written Comte or Graf v. Salis-Seewis / Graf Salis-Seewis / Graf Salis / Gräfin von Salis / Graf von Salis) is a primogenitive title created in Versailles, France on 1 February 1777, while the title Graf (to follow the Count) was created in Vienna, Austria, 16 March 1915.

Alexander Schenk Graf von Stauffenberg: Alexander Franz Clemens Maria Schenk Graf von Stauffenberg (15 March 1905 in Stuttgart – 27 January 1964 in Munich) was a German aristocrat and historian.  His older twin brother Berthold Schenk Graf von Stauffenberg and youngest brother Claus Schenk Graf von Stauffenberg were among the leaders of the 20 July Plot against Hitler in 1944.

Count of Merenberg: Count of Merenberg (German: "Graf von Merenberg") is the title bestowed in 1868 by the reigning Prince of Waldeck and Pyrmont, George Victor, upon the morganatic wife and male-line descendants of Prince Nikolaus Wilhelm of Nassau (1832-1905), who married Natalia Alexandrovna Pushkina (1836-1913), former wife of Russian General Mikhail Leontievich von Dubelt.

Gottfried von Bismarck: Gottfried Alexander Leopold Graf von Bismarck-Schönhausen (19 September 1962 – 30 June 2007) was a member of the German House of Bismarck.  He died of a cocaine overdose in 2007.

Marion Dönhoff: Marion Hedda Ilse Gräfin von Dönhoff (2 December 1909 – 11 March 2002) was a German journalist who participated in the resistance against Nazism, along with Helmuth James Graf von Moltke, Peter Yorck von Wartenburg, and Claus Schenk Graf von Stauffenberg.  After the war, she became one of the leading German journalists and intellectuals.  She worked over 55 years for the Hamburg-based, weekly newspaper "Die Zeit", as an editor and later publisher.

Wilhelm von Bismarck: Count Wilhelm von Bismarck-Schönhausen (né "Wilhelm Otto Albrecht von Bismarck") (1 August 1852 – 30 May 1901) was a German counselor, civil servant and politician, who served as a member of the Reichstag from 1880 to 1881 and president of the Regency of Hanover from 1889 to 1890.  The youngest son of Otto von Bismarck, he and his brother Herbert von Bismarck both resigned their posts after the elder Bismarck was dismissed as Chancellor of Germany in 1890.  Wilhelm subsequently accepted an appointment as Governor of East Prussia in 1894.

Kurt von Plettenberg: Kurt Freiherr von Plettenberg (31 January 1891 in Bückeburg – 10 March 1945 in Berlin) was a German forester, cavalry officer and a member of the German Resistance (Widerstand).  He was involved in the preparations for the 20 July plot, an attempt to assassinate Adolf Hitler, Führer of the Third Reich.  Plettenberg belonged to the circle of close friends which included Claus Schenk Graf von Stauffenberg, Johannes Popitz, Ludwig Beck, Ulrich von Hassell, Carl-Hans Graf von Hardenberg and Fabian von Schlabrendorff.

Bismarck Sapphire Necklace: The Bismarck Sapphire Necklace is a sapphire necklace designed by Cartier, Inc. in 1935.  As of 2010, the necklace is on display between the Hall Sapphire and Diamond Necklace and the Logan Sapphire in the Janet Annenberg Hooker Hall of Geology, Gems, and Minerals at the Smithsonian Institution's National Museum of Natural History in Washington D.C., United States.  It is named after Countess Mona von Bismarck, who donated the piece to the Smithsonian in 1967.  The sapphire itself was mined in Burma (now Myanmar, and was purchased by the Countess in Sri Lanka in 1926 during her honeymoon with Harrison Williams.

Question: When did the former wife of Graf von Bismarck-Schönhausen donate a piece to the Smithsonian she purchased on her honeymoon with a different man?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "donor_name": {
      "type": "string",
      "description": "The name of the person who made the donation."
    },
    "item_donated": {
      "type": "string",
      "description": "The name of the item that was donated."
    },
    "donation_year": {
      "type": "integer",
      "description": "The year the item was donated."
    },
    "item_purchase_year": {
      "type": "integer",
      "description": "The year the item was purchased by the donor."
    },
    "item_purchased_with_person": {
      "type": "string",
      "description": "The name of the person the donor was with when the item was purchased."
    },
    "recipient_institution": {
      "type": "string",
      "description": "The institution that received the donation."
    }
  },
  "required": [
    "donor_name",
    "item_donated",
    "donation_year",
    "item_purchase_year",
    "item_purchased_with_person",
    "recipient_institution"
  ],
  "additionalProperties": false
}

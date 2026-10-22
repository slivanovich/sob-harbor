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
Bull's Eye (postage stamp): The Bull's Eye "(Portuguese Olho-de-boi)" postage stamps were the first stamps issued by Brazil, on 1 August 1843, having face values of 30, 60, and 90 réis.  Brazil was the second country in the world, after the United Kingdom, to issue postage stamps valid within the entire country (as opposed to a local issue).  Like the United Kingdoms's first stamps, the design does not include the country name.

Fernão Mendes Pinto: Fernão Mendes Pinto (] ; c.1509 – 8 July 1583) was a Portuguese explorer and writer.  His voyages are recorded in "Pilgrimage" (Portuguese: "Peregrinação" ) (1614), his autobiographical memoir.  The historical accuracy of the work is debatable due to the many events which seem far fetched or at least exaggerated, earning him the nickname "Fernão Mentes Minto" (wordplay with the Portuguese verb "mentir" 'lie', meaning "Fernão, are you lying?  I am lying.") .  Some aspects of the work can be verified, particularly through Pinto's service to the Portuguese Crown and by his association with Jesuit missionaries.

Postage stamps and postal history of Tete: In 1913 and 1914, Portugal issued postage stamps specifically for Tete Province, now part of Mozambique.  The 1913 stamps were those of the Vasco da Gama issue of 1898, overprinted "REPUBLICA / TETE" and a new denomination in centavos. Each of the eight values from Macau, Portuguese Africa and Timor were overprinted, yielding a total of 24 stamps.  In 1914, the omnibus Ceres issue of Portugal included 16 values for Tete, ranging from 1/4 centavo to one escudo.  Subsequently, Tete reverted to using the stamps of Mozambique.  Although these stamps are not rare, none costing the collector over about US$10, genuinely-used examples are harder to find, and command a premium of about 50-100% over unused.

Revenue stamps of the United States: The first revenue stamps in the United States were used briefly during colonial times, among the most notable usage involved the Stamp Act.  Long after independence, the first revenue stamps printed by the United States government were issued in the midst of the American Civil War, prompted by the urgent need to raise revenue to pay for the great costs it incurred.  After the war ended however, revenue stamps and the taxes they represented still continued.  Revenue stamps served to pay tax duties on items that came under two main categories, "Proprietary" and "Documentary".  Proprietary stamps paid tax duties on goods like alcohol and tobacco, and were also used for various services, while Documentary stamps paid duties on legal documents, mortgage deeds, stocks and a fair number of other legal dealings.  "Proprietary" and "Documentary" stamps often bore these respective designations, while in several of the issues they shared the same designs, sometimes with minor variations.  Beginning in 1862 the first revenue stamps were issued, and would continue to be used for another hundred years and more.  For the first twelve years George Washington was the only subject featured on U.S. revenue stamps, when in 1875 an allegorical figure of "Liberty" finally appeared.  Revenue stamps were printed in many varieties and denominations and are widely sought after by collectors and historians.  Revenue stamps were finally discontinued on December 31, 1967.

Postage stamps and postal history of Zambezia: Although Zambezia was a part of the Portuguese East Africa Colony, the Portuguese government-issued separate postage stamps for it starting in 1894, with the standard design depicting King Charles, and likewise in 1898.  A provisional issue came in 1902 to reflect changed rates, then after the revolution of 1910 there were several issues overprinted "REPUBLICA".  The postal districts of Quelimane and Tete were created from parts of Zambezia in about 1913, and then stamps of Mozambique replaced stamps of Zambezia around 1920.

Rafael Perestrello: Rafael Perestrello (fl.  1514–1517) was a Portuguese explorer and a cousin of Filipa Moniz Perestrello, the wife of explorer Christopher Columbus.  He is best known landing on the southern shores of mainland China in 1516 and 1517 to trade in Guangzhou (then romanized as "Canton"), after the Portuguese explorer Jorge Álvares landed on Lintin Island within the Pearl River estuary in May 1513.  Rafael also served as a trader and naval ship captain for the Portuguese in Sumatra and Portuguese-conquered Malacca.

Liberty Issue: The Liberty issue was a definitive series of postage stamps issued by the United States between 1954 and 1965.  It offered twenty-four denominations, ranging from a half-cent issue showing Benjamin Franklin to a five dollar issue depicting Alexander Hamilton.  However, in a notable departure from all definitive series since 1870, the stamp for a normal first-class letter—the 3-cent value—did not present the portrait of a president, but instead offered a monocolor .  Moreover, two-color renderings of the Statue of Liberty appeared on both the 8 cent and 11 cent stamps; and it is from these three denominations that the Liberty issue takes its name.  (Oversized versions of the 3c and 8c stamps also appeared on a Miniature sheet issued in 1956 for the Fifth International Philatelic exhibition.)  Pictures of other national landmarks, such as Bunker Hill and Mount Vernon, are found on several values, while the rest of the stamps follow tradition, containing portraits of well-known historic Americans.  The six denominations in the set that illustrate buildings (The Alamo, Monticello, etc.) were all designed in landscape format, resulting in a free intermixture of landscape and portrait orientation for the first time in a definitive U. S. issue (in all previous mixed sets, landscape stamps had been confined to the highest denominations).

Pedro Mascarenhas: Dom Pedro Mascarenhas (1470 – 16 June 1555) was a Portuguese explorer and colonial administrator.  He was the first European to discover the island of Diego Garcia in the Indian Ocean in 1512.  He also encountered the Indian Ocean island of Mauritius in 1512, although he may not have been the first Portuguese explorer to do so; earlier expeditions by Diogo Dias and Afonso de Albuquerque along with Diogo Fernandes Pereira may have encountered the islands.  In 1528 explorer Diogo Rodrigues (after whom the island of Rodrigues is named) named the islands of Réunion, Mauritius, and Rodrigues the Mascarene Islands, after Mascarenhas.

Vasco da Gama: Vasco da Gama, 1st Count of Vidigueira (] ; c. 1460s – 24 December 1524), was a Portuguese explorer and the first European to reach India by sea.  His initial voyage to India (1497–1499) was the first to link Europe and Asia by an ocean route, connecting the Atlantic and the Indian oceans and therefore, the West and the Orient.

Enrique of Malacca: Enrique of Malacca (Spanish: "Enrique de Malaca" ; Portuguese: "Henrique de Malaca" ), was a native of the Malay Archipelago who became a slave of the Portuguese explorer Ferdinand Magellan in the 16th century.  Italian historian Antonio Pigafetta, who wrote the most comprehensive account of Magellan's voyage, named him "Henrique" (which was Hispanicised as "Enrique" in official Spanish documents).  Pigafetta explicitly states that "Henrique" was a native of Sumatra.  According to biographer-philosopher Stefan Zweig, he is the first person to circumnavigate the world.  His name appears as "Henrique", which is Portuguese, and is probably the name given to him at his christening, as he was baptised a Roman Catholic by his Portuguese captors.  His name appears only in Pigafetta's account, in Magellan's Last Will, and in official documents at the "Casa de Contratación de las Indias" of the Magellan expedition to the Philippines.

Question: A Portuguese explorer appeared on stamps for what province?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "explorer_name": {
      "type": "string",
      "description": "The name of the Portuguese explorer featured on the stamps."
    },
    "province_name": {
      "type": "string",
      "description": "The name of the province for which the stamps were issued."
    },
    "stamp_issue_details": {
      "type": "object",
      "properties": {
        "original_issue_year": {
          "type": "integer",
          "description": "The year of the original stamp issue that was overprinted."
        },
        "overprint_year": {
          "type": "integer",
          "description": "The year the stamps were overprinted for the specific province."
        },
        "overprint_text": {
          "type": "string",
          "description": "The text overprinted on the stamps."
        }
      },
      "required": [
        "original_issue_year",
        "overprint_year",
        "overprint_text"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "explorer_name",
    "province_name",
    "stamp_issue_details"
  ],
  "additionalProperties": false
}

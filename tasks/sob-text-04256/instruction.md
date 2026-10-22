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
Wendy Fitzwilliam: Wendy Marcelle Fitzwilliam (born 4 October 1972) is a Trinidadian lawyer, actress, model, singer, TV Host and beauty queen who won Miss Trinidad & Tobago Universe 1998 became the second Miss Universe in history from Trinidad & Tobago and was the fourth woman of African heritage to capture the Miss Universe crown.

Binibining Pilipinas 2016: Binibining Pilipinas 2016, the 53rd edition of Binibining Pilipinas, was held on April 17, 2016 at the Smart Araneta Coliseum, Quezon City, Philippines.  Pia Wurtzbach (Miss Universe 2015) crowned Maxine Medina as Miss Universe Philippines 2016 while Janicel Lubina (Miss International 2015 Top 10 finalist) crowned Kylie Verzosa as Binibining Pilipinas International 2016.  The pageant also awarded four other titles to participate in minor international beauty pageants in which Christi McGarry (Miss Intercontinental 2015 1st runner-up) crowned Jennifer Hammond as Binibining Pilipinas Intercontinental 2016, Rogelie Catacutan (Miss Supranational 2015 Top 20 semifinalist) crowned Joanna Eden as Binibining Pilipinas Supranational 2016, Parul Shah (Miss Grand International 2015 3rd runner-up) crowned Nicole Cordoves as Binibining Pilipinas Grand International 2016, and Ann Lorraine Colis (Miss Globe 2015) crowned Nichole Manalo as Binibining Pilipinas Globe 2016 as their successors at the end of the event.

Miss Universe 1998: Miss Universe 1998, the 47th Miss Universe pageant, was held on May 12, 1998 at the Stan Sheriff Arena in Honolulu, Hawaii.  Wendy Fitzwilliam of Trinidad & Tobago was crowned by Brook Lee of the United States at the end of the event.  Eighty-one contestants competed in this year.

Oana Paveluc: Oana Paveluc (born August 14, 1991 in Braşov, Romania) is a beauty pageant titleholder who was crowned new Miss Universe Romania 2010 on July 14, 2010 after Alexandra Cătălina Filip, the original winner, was dethroned, as she refused to sign the contract with the Miss Universe Organization (MUO).  The contract stipulates that the winner of Miss Universe 2010 must move to NYC and be under contract with Donald Trump for one year.  Filip is a professional sport dancer, and she wanted to be able to continue representing Romania at international sport dancing competitions and not be restrained by MUO's contract.  On July 14, 2010, at the official press conference where the winners of Miss Universe Romania 2010 had gathered to meet with all the sponsors and receive their prizes, Alexandra Cătălina Filip surprised everyone when she announced that she doesn't wish to continue the path to Las Vegas and in a friendly manner allowed Bianca Elena Constantin, Miss Universe Romania 2009, to crown Oana Paveluc.

Brook Lee: Brook Antoinette Mahealani Lee (born January 8, 1971 in Pearl City, Hawaii), known as Brook Lee, is an American actress, TV Host, model and beauty queen who was crowned Miss Hawaii USA 1997, Miss USA 1997, and Miss Universe 1997.

Binibining Pilipinas 2017: 'Binibining Pilipinas 2017, was the 54th edition of Binibining Pilipinas, that took place at the Smart Araneta Coliseum in Quezon City, Philippines on April 30, 2017.  Miss Universe 2016 Top 6 Maxine Medina crowned her successor Rachel Peters as Miss Universe Philippines 2017 at the end of the event while Miss International 2016 Kylie Verzosa crowned Mariel de Leon as Binibining Pilipinas-International.  The pageant also awarded four other titles to participate in minor international beauty pageants in which Miss Intercontinental 2016 Top 15 Jennifer Hammond crowned Katarina Rodriguez as Binibining Pilipinas-Intercontinental, Miss Supranational 2016 Top 25 Joanna Louise Eden crowned Chanel Olive Thomas as Binibining Pilipinas-Supranational, Miss Grand International 2016 1st Runner-up Nicole Cordoves crowned Elizabeth Clenci as Binibining Pilipinas-Grand International and Miss Globe 2016 3rd Runner-up Nichole Marie Manalo crowned Nelda Ibe as Binibining Pilipinas-Globe.

Miss Universe 1972: Miss Universe 1972, the 21st Miss Universe pageant, was held on 29 July 1972 at the Cerromar Beach Hotel in Dorado, Puerto Rico.  Kerry Anne Wells earned Australia's first Miss Universe crown.  Georgina Rizk of Lebanon, was not allowed to crown her successor due to government restrictions because of fears of a terrorist attack.  Lebanon did not compete in 1972 and Georgina could not be there to crown Miss Universe 1972.  Wells was crowned by Miss Universe 1970, Marisol Malaret of Puerto Rico and Miss Universe 1971 1st Runner-Up Toni Rayward.

Miss Ecuador 1998: The Miss Ecuador 1998 was held on March 21, 1998.  There were 15 candidates for the national title.  At the end of the night María Jóse López from Pichincha crowned Soraya Hogonaga from Pichincha as Miss Ecuador 1998.  The Miss Ecuador competed at Miss Universe 1998.

Miss Universe 1999: Miss Universe 1999, the 48th Miss Universe pageant, was held on 26 May 1999 at the Chaguaramas Convention Centre in Chaguaramas, Trinidad & Tobago.  Mpule Kwelagobe of Botswana was crowned by Wendy Fitzwilliam of Trinidad & Tobago at the end of the event.  Kwelagobe became the first Miss Universe to come from a debuting nation since 1958.  Eighty-four contestants competed in this year.

Renate Cerljen: Renate Veronica Cerljen (born March 26, 1988 in Staffanstorp, Sweden) is the first ever winner of the Miss Universe Sweden pageant which she won on June 6, 2009.  Cerljen represented Sweden at the Miss Universe 2009 pageant on the Bahamas on August 23, 2009 and placed in the Top 15.  Renate was the first non-winner of the Miss Sweden pageant since 1952 to represent Sweden at Miss Universe since Miss Sweden lost its rights to crown a contestant for Miss Universe earlier in 2009.  Cerljen was also the first delegate from Sweden at the international final since 2006 when Josephine Alhanko placed in the Top 20.  Miss Universe 1984 winner Yvonne Ryding was among the judges in the final which crowned Cerljen as winner.  By making the Top 15 Cerljen became Sweden's 29th semifinalist at the Miss Universe pageant overall.  In May 2010 Cerljen placed fifth in the Miss Beauty of the World pageant in China.  Cerljen was a judge at the Miss Sinergy competition for breast cancer in 2009 as well as 2010 which is an annual pageant made by the Sinergy group, held at the House of Sweden in Washington DC, United States.

Question: What is the birth date of the person who crowned Wendy Fitzwilliam as Miss Universe 1998?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "crowned_person_name": {
      "type": "string",
      "description": "The name of the person who crowned Wendy Fitzwilliam."
    },
    "crowned_person_role": {
      "type": "string",
      "description": "The title or role of the person who crowned Wendy Fitzwilliam."
    },
    "crowned_person_birth_date": {
      "type": "string",
      "format": "date",
      "description": "The birth date of the person who crowned Wendy Fitzwilliam."
    },
    "crowned_person_birth_location": {
      "type": "string",
      "description": "The birth location of the person who crowned Wendy Fitzwilliam."
    }
  },
  "required": [
    "crowned_person_name",
    "crowned_person_role",
    "crowned_person_birth_date",
    "crowned_person_birth_location"
  ],
  "additionalProperties": false
}

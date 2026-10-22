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
National Lampoon's Last Resort: National Lampoon's Last Resort (also known as Last Resort or National Lampoon's Scuba School) is a 1994 direct-to-video comedy film directed by Rafal Zielinski.  The film stars Corey Feldman and Corey Haim as Sam and Dave, two friends who are visiting a Caribbean island resort.

Lender of last resort: The term lender of last resort (LOLR) originates from the French expression "dernier ressort".  While the concept itself had been used previously, the term "lender of last resort" was supposedly first used in its current context by Sir Francis Baring, in his "Observations on the Establishment of the Bank of England", which was published in 1797.  In 1763, the king was the lender of last resort in Prussia.  Different definitions of the lender of last resort exist in the literature.  A comprehensive one is the following: "the discretionary provision of liquidity to a financial institution (or the market as a whole) by the central bank in reaction to an adverse shock which causes an abnormal increase in demand for liquidity which cannot be met from an alternative source".

The Last Resort (album): The Last Resort is the debut album by the Danish electronic musician Trentemøller.  It was released on October 9, 2006.  The album debuted at #5 on the Danish Albums Chart.  In Denmark, "The Last Resort" was certified platinum in October 2009 for sales over 30,000 copies, a rare feat for an electronic music album.  It is also available in a Limited Edition which includes a bonus disc with some of Trentemøller's previous 12-inch singles.

Last Resort: A last resort is something that is used when all other options have been exhausted.  Last Resort or The Last Resort may refer to:

Life in the Fast Lane: "Life in the Fast Lane" is a song written by Joe Walsh, Glenn Frey and Don Henley and recorded by the American rock band the Eagles on their 1976 studio album "Hotel California".  It was the third single released from this album, and peaked at No. 11 on the "Billboard" Hot 100.

Employer of last resort: Employers of last resort (ELR) are employers in an economy to whom workers go for jobs when no other jobs are available; the term is by analogy with "lender of last resort".  The phrase is used in two senses:

The Last Resort (Eagles song): "The Last Resort" is a song written by Don Henley and Glenn Frey, which tells about how man inevitably destroys the places he finds beautiful.  It was originally released on the Eagles' album "Hotel California" on December 8, 1976.  It was subsequently released as the B-side of "Life in the Fast Lane" single on May 3, 1977.

Supreme Court of the United Kingdom: The Supreme Court of the United Kingdom is the supreme court in all matters under English and Welsh law, Northern Ireland law and Scottish civil law.  It is the court of last resort and the highest appellate court in the United Kingdom, although the High Court of Justiciary remains the court of last resort for criminal law in Scotland.  The Supreme Court also has jurisdiction to resolve disputes relating to devolution in the United Kingdom and concerning the legal powers of the three devolved governments (in Scotland, Wales and Northern Ireland) or laws made by the devolved legislatures.

Supreme Court of Finland: The Supreme Court of Finland (Finnish: "korkein oikeus" , abbreviated as "KKO"; Swedish: "högsta domstolen" , abbreviated as "HD"), located in Helsinki, is the court of last resort for cases within the private law of Finland (that is, civil and criminal cases).  The Court's counterpart is the Supreme Administrative Court, which is the court of last resort for cases within the administrative law.

Supreme Court of Texas: The Supreme Court of Texas is the court of last resort for civil matters (including juvenile delinquency which the law considers to be a civil matter and not criminal) in the state of Texas.  A different court, the Texas Court of Criminal Appeals, is the court of last resort for criminal matters in the State of Texas.

Question: The Last Resort was the B-side of what Eagles' single in 1977?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "b_side_song_title": {
      "type": "string",
      "description": "The title of the song that was the B-side."
    },
    "artist": {
      "type": "string",
      "description": "The artist who recorded the song."
    },
    "single_release_year": {
      "type": "integer",
      "description": "The year the single was released."
    },
    "a_side_single_title": {
      "type": "string",
      "description": "The title of the A-side single."
    }
  },
  "required": [
    "b_side_song_title",
    "artist",
    "single_release_year",
    "a_side_single_title"
  ],
  "additionalProperties": false
}

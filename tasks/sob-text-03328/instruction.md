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
Isabelle Amyes: Isabelle Amyes (born 13 June 1950) is an English actress best known for her role as Barbara 'Babs' Hunt in the British TV drama "Bad Girls" from 2000–03.  Her various guest appearances on other television programmes include "The New Statesman", "House of Cards", "The Darling Buds of May", "A Touch of Frost" and "As Time Goes By".

H. E. Bates: Herbert Ernest Bates, CBE (16 May 1905 – 29 January 1974), better known as H. E. Bates, was an English writer and author.  His best-known works include "Love for Lydia", "The Darling Buds of May", and "My Uncle Silas".

Darling Buds of May (album): Darling Buds of May is the debut album by the rock band Faulter.

The Mating Game (film): The Mating Game (1959) is an MGM Metrocolor film in CinemaScope directed by George Marshall and starring Debbie Reynolds, Tony Randall, and Paul Douglas in his final screen appearance.  Reynolds sings the title song during the opening credits.  The film was written by William Roberts very loosely based on a British novel, "The Darling Buds of May" by H. E. Bates, which was later adapted into a more faithful 1991–93 British miniseries, starring Catherine Zeta-Jones in the role that Debbie Reynolds plays in the film.

Cake (band): Cake (stylized CAKE) is an American alternative rock band from Sacramento, California.  Consisting of singer John McCrea, trumpeter Vince DiFiore, guitarist Xan McCurdy, bassist Gabe Nelson and drummer Paulo Baldi, the band has been noted for McCrea's sarcastic lyrics and monotone vocals, DiFiore's trumpet parts, and their wide-ranging musical influences, including country music, Mariachi, rock, funk, Iranian folk music and hip hop.

Abigail Rokison: Abigail Rokison-Woodall (née Rokison) is an author and academic specialising in William Shakespeare, as well as a former actress.  She was Director of Studies in English and Drama at Homerton College, Cambridge until the end of 2012.  She is now lecturer in Shakespeare and Theatre at the Shakespeare Institute, Stratford upon Avon.  She previously played Primrose in "The Darling Buds of May".

The Darling Buds: The Darling Buds are an alternative rock band from Newport, South Wales.  The band formed in 1986 and were named after the H. E. Bates novel "The Darling Buds of May" – a title taken in turn, from the third line of Shakespeare's Sonnet 18: "Rough winds do shake the darling buds of May".

Pop Said...: Pop Said... is the debut album by Welsh band The Darling Buds.  All songs were written by Harley Farr and Andrea Lewis.  Originally released by Epic Records in 1989, the album was re-released by Cherry Red Records in 2006 in an expanded 21-track edition, including B-sides and rarities from the era.  The album charted at number 23 at the UK Albums Chart.

Famous First Words (Viva Brother album): Famous First Words is the debut studio album by English pop-rock band Viva Brother, released on 1 August 2011, on Geffen Records in the United Kingdom.  Preceded by the singles "Darling Buds of May", "Still Here" and "New Year's Day", the album was produced and mixed by Stephen Street, who had previously worked with acts such as Blur and The Smiths.

Faulter: Faulter is a rock band from Anaheim, California.  They formed in 2003, while the members were attending various high schools in Anaheim.  The band self-released their debut album "Darling Buds of May" before being signed to Abacus Recordings.  The album was then re-released nationally on their new label.  Songs from their debut have been featured on "" twice.  In 2007, the band released an EP, "The Other Side" (available as a free download on their official website).  The EP includes 2 rerecorded songs from their debut along with 3 new ones.  In July 2007, they announced on their Myspace that they were no longer with Abacus Recordings.

Question: Are Cake and The Darling Buds both from America?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_asked": {
      "type": "string",
      "description": "The original question asked."
    },
    "answer": {
      "type": "boolean",
      "description": "The boolean answer to the question: Are both bands from America?"
    },
    "bands_information": {
      "type": "array",
      "description": "Information about each band mentioned in the question.",
      "items": {
        "type": "object",
        "properties": {
          "band_name": {
            "type": "string",
            "description": "The name of the band."
          },
          "is_from_america": {
            "type": "boolean",
            "description": "True if the band is from America, false otherwise."
          },
          "origin_country": {
            "type": "string",
            "description": "The country where the band originated."
          },
          "origin_city_or_region": {
            "type": "string",
            "description": "The specific city or region of origin, if available."
          }
        },
        "required": [
          "band_name",
          "is_from_america",
          "origin_country"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "question_asked",
    "answer",
    "bands_information"
  ],
  "additionalProperties": false
}

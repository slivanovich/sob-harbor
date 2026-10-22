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
Weak (Skunk Anansie song): "Weak" is a song by Skunk Anansie, released as their fourth single.  It was the last release to be taken from their debut album "Paranoid & Sunburnt".  The song is one of Skunk Anansie's well known releases, and often a favourite at festivals.  Skin performs a slower, more ballad-like version at many of her solo gigs.  The song has also been covered by Rod Stewart on his 1998 album "When We Were the New Boys".

7 Year Bitch: 7 Year Bitch was an American punk rock band from Seattle, Washington that was active for 7 years, between 1990 and 1997.  Their career yielded three albums, and was impacted by the deaths of their guitarist Stefanie Sargent and close friend Mia Zapata, of fellow Seattle punks The Gits.

Skunk Anansie discography: The discography of Skunk Anansie, an English rock band, consists of six studio albums and twenty-four singles, including one re-issue.  The band's members include Skin (Deborah Dyer), Cass (Richard Lewis), Ace (Martin Kent) and Mark Richardson.  The group formed in 1994 and disbanded in 2001; they re-united in 2009.  Skunk Anansie are named after the West African folk tales of Anansi the Spider-man, with "Skunk" added to "make the name nastier".

Len Arran: Len Arran (born Leonard Arran, 7 June 1961, Thornaby-on-Tees, England) is an English composer of film scores, and songwriter for Skunk Anansie and solo artist Deborah Dyer (Skin).

Selling Jesus: "Selling Jesus" is a song by Skunk Anansie, released as their debut single.  Although Skunk Anansie previously released "Little Baby Swastikkka" as a limited release, it was not regarded as an actual single.  "Selling Jesus" is a song in protest of religion and politics, and in particular Christianity.  The single is taken from their debut album, "Paranoid & Sunburnt", and reached number 46 on the UK Singles Chart.  Three added B-Sides were included on the CD release, with track 4 'Skunk Song' being written by Ace, R. France, C. Lewis and Skin.  The title song was also included on the soundtrack to the motion picture "Strange Days".

Skunk Anansie: Skunk Anansie are a British rock band whose members include Skin (lead vocals, guitar), Cass (guitar, bass, backing vocals), Ace (guitar, backing vocals) and Mark Richardson (drums and percussion).

Hedonism (Just Because You Feel Good): "Hedonism (Just Because You Feel Good)" is a song by British group Skunk Anansie.  It was released in January 1997 as a single from their second album, "Stoosh".  The song reached #14 in the UK singles chart.  It also proved to be a top 20 hit in several countries such as France, Sweden and Austria and a top 10 hit in other countries such as Norway and The Netherlands and a #2 hit in Switzerland.  It is regarded as one of Skunk Anansie's most known singles and was a popular choice at concerts.  Skin performs a version of the song at many of her solo gigs, and US R&B group Groove Theory covered the song for their second album, "The Answer".

Skin discography: Skin is the lead singer of Skunk Anansie and a solo artist.  She has released two albums as a solo artist and featured on several other artists albums.  For Skunk Anansie's full discography see Skunk Anansie discography.

Roisin Dunne: Roisin Dunne Ross (born 18 September 1965 in Ireland), an Irish musician.  Best known for being the replacement guitarist of 7 Year Bitch, after their guitarist Stefanie Sargent died.  In 1992, they toured for their debut, with Valerie Agnew, Selene Vigil-Wilk, and Elizabeth Davis, which was her signature act with the band.  This was when Mia Zapata of the Gits had been raped and murdered on 7 July 1992.  The band had made a tribute album to her and Sargent.

Valerie Agnew: Valerie Agnew is best known for her relationship with the band called the Gits and as the drummer of 7 Year Bitch.  She started out in Ohio and was dating Steve Moriarty, the drummer of the Gits.  She was a very close friend of Mia Zapata.  The Gits, when they moved to Seattle Valerie went along with them, since she was good friends with them.  When Valerie comes to Seattle she meets up with the musicians that would soon to be her future band mates Selene Vigil (vocals), Elizabeth Davis (bass) and Stefanie Sargent (lead guitar), forming the band 7 Year Bitch.  Eventually signing with C/Z Records when they made their debut album "Sick 'Em" in 1992.

Question: Skunk Anansie and 7 Year Bitch are both the names of which type of groups?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "common_group_type": {
      "type": "string",
      "description": "The common type of group identified for all listed entities."
    },
    "groups_analyzed": {
      "type": "array",
      "description": "Details of each group analyzed to determine the common type.",
      "items": {
        "type": "object",
        "properties": {
          "group_name": {
            "type": "string",
            "description": "The name of the group."
          },
          "specific_type_in_context": {
            "type": "string",
            "description": "The specific type of the group as described in the context."
          },
          "origin_country": {
            "type": "string",
            "description": "The country of origin for the group."
          }
        },
        "required": [
          "group_name",
          "specific_type_in_context"
        ],
        "additionalProperties": false
      }
    },
    "analysis_summary": {
      "type": "string",
      "description": "A brief summary of how the common type was determined."
    }
  },
  "required": [
    "common_group_type",
    "groups_analyzed",
    "analysis_summary"
  ],
  "additionalProperties": false
}

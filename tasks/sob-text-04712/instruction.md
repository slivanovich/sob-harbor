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
Gettin' In the Way: "Gettin' In the Way" was the first single released in April 11, 2000 by American R&B/Soul singer-songwriter Jill Scott, off her debut studio album on Hidden Beach label, "Who Is Jill Scott?  Words and Sounds Vol.  1".  The song was her first charting UK single, which peaked to number 30 on the UK Singles Chart and top 40 R&B singles.

Who Is Jill Scott? Words and Sounds Vol. 1: Who Is Jill Scott?  Words and Sounds Vol.  1 is the debut album by American R&B-soul singer–songwriter Jill Scott, released in the United States on July 18, 2000 by Hidden Beach Recordings to positive acclaim.  The album was nominated for Best R&B Album at the 2001 Grammy Awards, whereas "Gettin' in the Way", "A Long Walk", and "He Loves Me (Lyzel in E Flat)" were nominated for Best Female R&B Vocal Performance in 2001, 2002, and 2003, respectively.  The album has been listed as one of the best albums of the 2000s by "Slant Magazine".

Love Rain (Jill Scott song): "Love Rain" is a 1999 song by Jill Scott co-written with Vidal Davis.  The song appears twice on Scott's debut album "Who Is Jill Scott?  Words and Sounds Vol.  1" with Mos Def.  A further two remixes, again with Mos Def, appeared on "Collaborations"; "Love Rain" (Head Nod Remix featuring Mos Def) – 5:02 and

Beautifully Human: Words and Sounds Vol. 2: Beautifully Human: Words and Sounds Vol.  2 is the second studio album (third overall) by American R&B-soul singer–songwriter Jill Scott, released in the United States on August 31, 2004, by Hidden Beach Recordings.  It entered the charts at number three on the "Billboard" 200 and number one on the "Billboard" Top R&B/Hip-Hop Albums with first-week sales of 193,000 copies, earning Scott her first number-one album.  Also, the song "Cross My Mind" brought Scott her first Grammy Award, under the Best Urban/Alternative Performance category in 2005.

He Loves Me (Lyzel In E Flat): "He Loves Me (Lyzel In E Flat)" was the fourth and final single released by American R&B/Soul singer Jill Scott and from her debut, "Who Is Jill Scott?  Words and Sounds Vol.  1".  The song was released as a single in support of Scott's live album, "".  A music video edit of Scott's performance of the song in Washington D.C. and played heavy rotation on BET and VH1 cable stations.  The song was nominated for Best Female R&B Vocal Performance at the 2003 Grammy Awards.

The Real Thing: Words and Sounds Vol. 3: The Real Thing: Words and Sounds Vol.  3 is the third studio album by American R&B/soul recording artist and actress Jill Scott.  It was recorded at Bazz Studio, The Cosmic Dust Recorders, Currie House Studio, Glenwood Place Studios, Headquarters Studio, The House That Quest Built, Keswick Studios, Kush Studio, Sigma Sound Studios, The Studio, Studio 609, and Studio Atlantis.  It was released on September 25, 2007, by Hidden Beach Recordings to positive reviews from music critics.

Jill Scott: Jill Scott (born April 4, 1972) is an American singer-songwriter, model, poet and actress.  Her 2000 debut, "Who Is Jill Scott?  Words and Sounds Vol.  1", went platinum, and the follow-ups "" (2004) and "" (2007) both achieved gold status.  She made her cinematic debut in the films "Hounddog" and Tyler Perry's "Why Did I Get Married? " in 2007.

The Way (Jill Scott song): "The Way" is the third single released in 2001 by American R&B/soul singer-songwriter Jill Scott, from her debut album, "Who Is Jill Scott?  Words and Sounds Vol.  1" on Hidden Beach.  The song was her second top 20 hit on Billboard's Hot R&B/Hip-Hop Singles & Tracks chart and peaked at number 60 on the Hot 100 chart.

A Long Walk (song): "A Long Walk" is a song released in 2001 by American recording artist Jill Scott, from her debut studio album, "Who Is Jill Scott?  Words and Sounds Vol.  1".  The song peaked at No. 9 on "Billboard's" R&B Singles chart.  It was sampled on the track "Stimulation" from Disclosure's 2013 album Settle.

Kindred the Family Soul: Kindred the Family Soul, also referred to as Kindred, are an American neo soul duo consisting of married couple of Fatin Dantzler (born in 1973 in Camden, New Jersey) and Aja Graydon (born September 25, 1978 in Los Angeles, California).  Signed to Hidden Beach Recordings, Kindred emerged from the Philadelphia neo soul movement that also includes Jill Scott, who introduced them to her then label president Steve McKeever of Hidden Beach Recordings while the couple was performing at the Black Lily Showcase in Philly weekly back in 2000.  Kindred would go on to sign their first recording contract with the label.

Question: What music movement did both Kindred the Family Soul and the singer-songwriter of the 2000 album "Who is Jill Scott? Words and Sounds Vol. 1" belong to?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "music_movement_name": {
      "type": "string",
      "description": "The name of the music movement."
    },
    "artists_involved": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of artists associated with the music movement."
    },
    "movement_origin_city": {
      "type": "string",
      "description": "The city where the music movement originated."
    }
  },
  "required": [
    "music_movement_name",
    "artists_involved",
    "movement_origin_city"
  ],
  "additionalProperties": false
}

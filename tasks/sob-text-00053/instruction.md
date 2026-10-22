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
Some Girls Wander by Mistake: Some Girls Wander by Mistake is a compilation album by English band the Sisters of Mercy, released on their own label Merciful Release, distributed by Eastwest/Warner Music UK, on 27 April 1992.

Merciful Release: Merciful Release is a record label started by Andrew Eldritch, frontman with Leeds band The Sisters of Mercy.  As Eldritch states in an early interview, he wanted to hear himself on the radio.  He and Gary Marx (Mark Pairman) played and recorded on the Sisters Of Mercy's initial single "Damage Done" and pressed one thousand copies.  This record was something of a collector's item.

Body and Soul (EP): Body and Soul is the third EP by The Sisters of Mercy.  It was the first release under a distribution contract with WEA, issued on 12" vinyl on 4 June 1984 by Merciful Release, the band's label.  The EP was never released on CD, but the title track was included on the "A Slight Case of Overbombing" collection.

Vision Thing (album): Vision Thing is the third and, to date, final studio album by British gothic rock band The Sisters of Mercy, released in November 1990 on the band's own label Merciful Release.

Alice (EP): Alice is the first independent EP by the Sisters of Mercy, released on 12" vinyl in March 1983 by Merciful Release, the band's own label.

A Slight Case of Overbombing: A Slight Case of Overbombing: Greatest Hits Volume One is a collection of all A-sides of The Sisters of Mercy UK singles released since the band was signed to Time Warner.  Non UK singles like "When You Don't See Me" aren't present, however "Vision Thing (Canadian Club Mix)" and "Detonation Boulevard (Radio Edit)", two North-American Promo singles are included.  It was released on 23 August 1993 on the band's own label, Merciful Release, (under distribution contract with EastWest).

The Sisters of Mercy discography: The discography of the British rock band The Sisters of Mercy consists of three studio albums, two compilation albums, two extended plays (EPs), and sixteen singles.  The Sisters of Mercy were formed in Leeds in 1977 by Andrew Eldritch (vocals, drums) and Gary Marx (guitar) and they released their debut single, "The Damage Done" in the same year on their own independent record label, Merciful Release.  In early 1981, Craig Adams (bass) joined the band and they started to use a drum machine, which was christened Doktor Avalanche.  Ben Gunn joined the band as a second guitarist by the end of 1981 and this line-up recorded four more singles and two EPs during 1982 and 1983.  Guitarist Wayne Hussey replaced Gunn in early 1984 and, after building up their live reputation, The Sisters signed with WEA, who distribute the band's releases on Merciful Release in the United Kingdom and on Elektra Records in the United States.  The band's next single, 1984's "Body and Soul", became their first charting effort in the UK when it reached number 46.  Three more singles were released before the band reached number 14 on the UK Albums Chart with their debut album, "First and Last and Always", which was released in March 1985.  Following the album's release, Marx left the band, before the rest of the group disbanded in mid-1985.

First and Last and Always: First and Last and Always is the debut studio album by English rock band The Sisters of Mercy.  It was released on 11 March 1985, through record labels Merciful Release and WEA.

Andrew Eldritch: Andrew Eldritch (born Andrew William Harvey Taylor, 15 May 1959) is the English frontman, singer, songwriter and only remaining original member of The Sisters of Mercy, a band that emerged from the British post-punk scene, transformed into a gothic rock band and, in later years, flirted with hard rock.

The Reptile House E.P.: The Reptile House E.P. is the second independent EP by the Sisters of Mercy, released on 12" vinyl in May 1983 on the band's own label, Merciful Release.  The EP was never released as a stand-alone CD, but was included on the "Some Girls Wander by Mistake" collection.

Question: The creator of the record label Merciful Release was born in what year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person."
    },
    "role": {
      "type": "string",
      "description": "The role of the person in relation to the record label."
    },
    "record_label_name": {
      "type": "string",
      "description": "The name of the record label."
    },
    "birth_year": {
      "type": "integer",
      "description": "The birth year of the person."
    }
  },
  "required": [
    "person_name",
    "role",
    "record_label_name",
    "birth_year"
  ],
  "additionalProperties": false
}

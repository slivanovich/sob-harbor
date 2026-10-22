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
Justin Hawkins: Justin David Hawkins (born 17 March 1975) is an English musician and singer-songwriter, best known for being the lead singer and lead guitarist of The Darkness, alongside his brother, guitarist Dan Hawkins.  Heavily influenced by classic hard rock and heavy metal bands of the 1970s and 1980s (particularly Queen, Aerosmith, Def Leppard and AC/DC), Hawkins is noted for his falsetto singing voice and on-stage persona.  He was also the lead singer and guitarist for the band Hot Leg, formed in 2008, and now on hiatus.  Since 2005 he is also active in his synthpop alter ego British Whale.

Lincoln Thompson: Prince Lincoln Thompson, known as Sax (18 June 1949 – 23 January 1999), was a Jamaican singer, musician and songwriter with the reggae band the Royal Rasses, and a member of the Rastafari movement.  He was born 18 June 1949 in Jonestown, next to Trenchtown, both parts of the slummy shanty town in the poor west side of inner Kingston, Jamaica and died of cancer in London on 23 January 1999, days after being first diagnosed.  He was noted for his high falsetto singing voice, very different from his spoken voice.

Sylvester (singer): Sylvester James, Jr. (September 6, 1947December 16, 1988), who used the stage name of Sylvester, was an American singer-songwriter.  Primarily active in the genres of disco, rhythm and blues, and soul, he was known for his flamboyant and androgynous appearance, falsetto singing voice, and hit disco singles in the late 1970s and 1980s.

By Your Side (Jimmy Somerville song): "By Your Side" is a song from Scottish singer-songwriter Jimmy Somerville, released as the third and final single from his 1995 album "Dare to Love".  The song was written and produced by Matt Rowe, Somerville and Richard Stannard.

The Age of Consent: The Age of Consent is the debut album by synthpop band Bronski Beat (Steve Bronski, Larry Steinbachek and Jimmy Somerville), released on London Records on 15 October 1984.  This was the only album released by the band to feature Somerville, who departed the band in 1985.

Jimmy Somerville: James William Somerville (born 22 June 1961) is a Scottish pop singer and songwriter.  He sang in the 1980s with the pop groups Bronski Beat and The Communards, and has also had a solo career.  He is known in particular for his falsetto singing voice.

The Haunted (album): The Haunted is the self titled debut studio album by The Haunted, released in 1998 on Earache Records.  Tracks 1-4 & 12, were part of the band's greatest hits, "Warning Shots".  Peter Dolving and Adrian Erlandsson both quit at different times after the album, but both returned on different releases, with Dolving on rEVOLVEr, and Erlandsson on "Eye of the Storm".

Raine Maida: Raine Maida {'1': ", '2': ", '3': ", '4': "} (born Michael Anthony Maida; February 18, 1970) is a Canadian musician best known as being the lead vocalist and primary songwriter of the alternative rock band Our Lady Peace.  He has come to be known for his unique countertenor nasal falsetto singing voice, as well as his cryptic and poetry-influenced song lyrics.  He occasionally plays certain instruments, such as the acoustic guitar, while performing with Our Lady Peace.

Peter Dolving: Peter Dolving (born 24 October 1969) is a Swedish musician, songwriter, visual artist and spoken word poet, now living in Salvador, Bahia, Brazil and is most commonly known as the former frontman of the metal band, the Haunted.

Bronski Beat: Bronski Beat were a popular British synthpop trio who achieved success in the mid-1980s, particularly with the 1984 chart hit "Smalltown Boy".  All members of the group were openly gay and their songs reflected this, often containing political commentary on gay-related issues.  The initial line-up, which recorded the majority of the band's hits, consisted of Jimmy Somerville (vocals), Steve Bronski (keyboards, percussion) and Larry Steinbachek (keyboards, percussion).  Somerville left Bronski Beat in 1985, and went on to have success as lead singer of The Communards and as a solo artist.  He was replaced by new vocalist John Foster, with whom the band continued to have hits in the UK and Europe through 1986.  Foster left Bronski Beat after their second album, and the band used a series of vocalists before dissolving in 1996.

Question: Which of the following is known particularly for his falsetto singing voice: Jimmy Somerville or Peter Dolving?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_known_for_falsetto": {
      "type": "string",
      "description": "The name of the person from the question who is known for a falsetto singing voice."
    },
    "person_not_known_for_falsetto": {
      "type": "string",
      "description": "The name of the person from the question who is NOT known for a falsetto singing voice, based on the context."
    },
    "falsetto_singers_mentioned_in_context": {
      "type": "array",
      "description": "A list of all individuals mentioned in the context who are noted for their falsetto singing voice.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the falsetto singer."
          },
          "bands": {
            "type": "array",
            "description": "A list of bands the singer was associated with.",
            "items": {
              "type": "string"
            }
          },
          "other_notable_characteristics": {
            "type": "array",
            "description": "Other notable characteristics or roles of the singer.",
            "items": {
              "type": "string"
            }
          }
        },
        "required": [
          "name",
          "bands",
          "other_notable_characteristics"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "person_known_for_falsetto",
    "person_not_known_for_falsetto",
    "falsetto_singers_mentioned_in_context"
  ],
  "additionalProperties": false
}

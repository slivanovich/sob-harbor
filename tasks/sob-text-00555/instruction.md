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
John Butler Trio: The John Butler Trio are an Australian roots and jam band led by guitarist and vocalist John Butler, an APRA and ARIA-award-winning musician.  They formed in Fremantle in 1998 with Jason McGann on drums and Gavin Shoesmith on bass.  By 2009, the trio consisted of Butler with Byron Luiters on bass and Nicky Bomba on drums and percussion, the latter being replaced by Grant Gerathy in 2013.

Shannon Birchall: Shannon Birchall is an Australian born musician, probably best known as the bassist for jam band the John Butler Trio.  Birchall is often labeled a virtuoso by different music experts.  He is also known for composing and conducting the string sections of the John Butler Trio's work.

The Music: The Music were an English alternative rock band, formed in Kippax, Leeds in 1999.  Comprising Robert Harvey (vocals, guitar), Adam Nutter (lead guitar), Stuart Coleman (bass) and Phil Jordan (drums), the band came to prominence with the release of their debut album, "The Music", in 2002.  The band released two further studio albums, "Welcome to the North" (2004) and "Strength in Numbers" (2008), before parting ways in 2011.

Nicky Bomba: Nicholas Caruana aka Nicky Bomba (born 7 September 1963, Malta) is an Australian musician and singer-songwriter.  He is the leader of the ARIA Award-winning Melbourne Ska Orchestra, frontman of his band, Bomba, as well as the former drummer and percussionist of John Butler Trio (2003–04, 2009–13).  He has performed in other acts and as a solo artist.  His youngest sister, Danielle Caruana, (who performs as Mama Kin), is married to his former band mate, John Butler.  His older brother, Michael Caruana, is a member of Bomba and of Mama Kin's backing band.

John Butler (musician): John Charles Wiltshire-Butler (born 1 April 1975), known professionally as John Butler, is an Australian singer, songwriter, and music producer.  He is the front man for the John Butler Trio, a roots and jam band, which formed in Fremantle, Western Australia in 1998.

Better Than: "Better Than" is a song by John Butler Trio from their fourth studio album, "Grand National".  Produced by John Butler and Mario Caldato Jr., it was released in the United States on 20 February 2007 as an online single, the third single in Australia and the first overseas single from the album.

Jarrah Records: Jarrah Records is an independent Australian record label which releases material by Western Australian-formed bands, John Butler Trio and The Waifs, and their members.  In July 2002 the label was founded and co-owned by John Butler; The Waifs' members Josh Cunningham, Donna Simpson, and her sister Vikki Thorn; and the artists' common manager, Philip Stevens.  Initially it was established to handle their releases for the territory of the United States by 2003 it expanded .

One Small Step (album): "One Small Step" (subtitled Live and Solo)", is a live album by John Butler.  It features 8 tracks from three previous John Butler Trio albums, recorded live at Twist & Shout Records in Colorado, United States.  It was originally released in 2007 as " Live At Twist & Shout".

Live at St. Gallen: Live at St. Gallen is a 2005 live CD and DVD by The John Butler Trio recorded in St. Gallen, Switzerland.  The CD version peaked at No. 47 on the ARIA Albums Chart.  The two CDs included in the set were recorded live at St. Gallen, whereas the DVD was recorded at the Sydney Opera House in 2004.  The cover art was designed by John Butler Trio regular Tom Walker.  On the Australian edition, the credits for the DVD include "In memory of Paul Hester", the original drummer from Crowded House.  By the end of 2005 the album was certified gold by Australian Recording Industry Association (ARIA).

Zebra (The John Butler Trio song): "Zebra" is the first single released from the John Butler Trio's album Sunrise Over Sea.  Featuring the Sunrise lineup of John Butler on guitar/vocals, Shannon Birchall on double bass and Nicky Bomba on drums/percussion, it blends the genres of folk, funk, rock, and a bit of blues.

Question: The Music and John Butler Trio, are musical groups?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_about_musical_groups": {
      "type": "boolean",
      "description": "Indicates if the question is about whether the listed entities are musical groups."
    },
    "are_all_entities_musical_groups": {
      "type": "boolean",
      "description": "The direct answer to whether all mentioned entities are musical groups."
    },
    "identified_musical_groups": {
      "type": "array",
      "description": "Details of the entities identified as musical groups from the context.",
      "items": {
        "type": "object",
        "properties": {
          "group_name": {
            "type": "string",
            "description": "The name of the musical group."
          },
          "is_a_musical_group": {
            "type": "boolean",
            "description": "Confirms if the entity is explicitly described as a musical group in the context."
          },
          "genre": {
            "type": "string",
            "description": "The primary genre of the musical group as described in the context."
          },
          "origin_country": {
            "type": "string",
            "description": "The country of origin for the musical group."
          }
        },
        "required": [
          "group_name",
          "is_a_musical_group",
          "genre",
          "origin_country"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "question_about_musical_groups",
    "are_all_entities_musical_groups",
    "identified_musical_groups"
  ],
  "additionalProperties": false
}

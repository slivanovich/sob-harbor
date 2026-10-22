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
Sharpen Your Teeth: Sharpen Your Teeth is an album by the indie rock band Ugly Casanova.  Brainchild of Modest Mouse lead singer Isaac Brock, Ugly Casanova was his attempt to try new methods and genres outside the realms of Modest Mouse.  The album sees Brock performing on more instruments and using a more stripped down method of recording.  The story given is that an eccentric character named Edgar Graham met with Modest Mouse while on tour.  During their time together, Graham and the band recorded a few songs together, and Graham completely disappeared.  In an attempt to get Graham to resurface, Brock took the recordings to Sub Pop Records, redid them in the studio, and had them released as Sharpen Your Teeth.  A follow-up is highly unlikely due to contractual obligations Brock has with Modest Mouse's label Epic Records.  It has since been revealed that Brock fabricated the story himself, using Ugly Casanova as a method of writing music whilst not being recognized instantly as Modest Mouse.

Isaac Brock (musician): Isaac Kristofer Brock (born July 9, 1975) is the lead singer, guitarist, banjoist, and songwriter for the American indie rock band Modest Mouse, as well as his side project band, Ugly Casanova.  As a songwriter he is noted for wordplay and frequent use of metaphors, philosophical lyrics, themes of oppressive rural lifestyles, and certain phrases and sayings commonly used in the early to mid-20th century and in blue collar environments.

Thomas Campbell (visual artist): Thomas Campbell (born c. 1969) is a California-based visual artist whose work has appeared on the Ugly Casanova album Sharpen Your Teeth and in Juxtapoz Magazine's September 2006 issue.

Ike Willis: Isaac "Ike" Willis (born November 12, 1955) is an American vocalist and guitarist who was a regular member of Frank Zappa's studio and touring bands from 1978 until the last tour in 1988.  He did not tour with Zappa in 1981 and 1982 because he wanted to be home for the birth of his two children, but returned to touring with Zappa for his final two tours in 1984 (which Zappa intended at the time to be his final tour) and 1988.  He currently tours with the Frank Zappa tribute bands Bogus Pomp, Ossi Duri, Project/Object, Pojama People, Ugly Radio Rebellion and ZAPPATiKA.  He also performed several times with the Brazilian Zappa cover band, The Central Scrutinizer Band, The Muffin Men, and with the Italian bands and Elio e le Storie Tese .  Additionally, he has appeared multiple times at the annual Zappanale Festival in Bad Doberan, Germany.  He is most recognized for his involvement in Zappa records such as playing Joe in "Joe's Garage", providing vocals on "Tinsel Town Rebellion", "You Are What You Is", and "The Man from Utopia", and as the title character and narrator in Zappa's off-Broadway-styled conceptual musical "Thing-Fish".

Howlin Maggie: Howlin' Maggie was a four-piece band founded by (and fronted by) Harold "Happy" Chichester in Columbus, OH in 1994.  Chichester was previously the bassist for Royal Crescent Mob, and is also a founding member of The Twilight Singers with Greg Dulli of The Afghan Whigs.

Pall Jenkins: Pall Jenkins is an American vocalist, guitarist and music producer.  He is best recognized as the front man for the bands Three Mile Pilot and The Black Heart Procession, as well as his collaborations with Vampire Rodents and Ugly Casanova.

Ugly Man Records: Ugly Man Records was started as a Manchester-based independent record label, but it is now based in Rhos on Sea.  The label released debut singles for many Manchester bands, including Elbow, the Man From Delmonte and I Am Kloot.  Ugly Man Records was set up in Bootle, Merseyside in 1986 with the release of "Wonderful Life" by the Liverpool-based band, Black.  This debut release reached number 72 in the UK Singles Chart.

Tim Rutili: Tim Rutili (born Temistocles Hugo Rutili) is a singer, guitarist, and keyboardist, and frontman/lyricist for the American rock band Califone.  Originally from Chicago, Rutili now lives in Los Angeles.  He was raised in Addison, IL.  After moving into Chicago in 1988, he found success with the band Red Red Meat.  The band was signed to the Sub Pop label, where they received high praise and moderate success.  He was also a member of the Indie rock supergroup Ugly Casanova, which included Modest Mouse singer Isaac Brock, producer and former Red Red Meat bandmate Brian Deck, and others.  He also appears on Joan of Arc's album Guitar Duets, performing a duet with Jeremy Boyle.

Ugly Casanova: Ugly Casanova is an American indie rock band carried on Sub Pop Records.  The band has released one album, "Sharpen Your Teeth".

Holopaw: Holopaw is an American indie band from Gainesville, Florida.  The band was named after the town of Holopaw in Osceola County, Florida, although none of the members of the band have ever lived there.  One of its members, John Orth, joined up with Modest Mouse frontman Isaac Brock and others in 2002 to release the album Sharpen Your Teeth under the band name Ugly Casanova.  Another member, Michael Johnson (Ape School), went on to join Kurt Heasley's Lilys.

Question: Were both Howlin Maggie and Ugly Casanova bands?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "howlin_maggie_info": {
      "type": "object",
      "properties": {
        "entity_name": {
          "type": "string"
        },
        "is_a_band": {
          "type": "boolean"
        },
        "founding_year": {
          "type": "integer"
        },
        "founding_location": {
          "type": "string"
        }
      },
      "required": [
        "entity_name",
        "is_a_band",
        "founding_year",
        "founding_location"
      ],
      "additionalProperties": false
    },
    "ugly_casanova_info": {
      "type": "object",
      "properties": {
        "entity_name": {
          "type": "string"
        },
        "is_a_band": {
          "type": "boolean"
        },
        "genre": {
          "type": "string"
        },
        "record_label": {
          "type": "string"
        }
      },
      "required": [
        "entity_name",
        "is_a_band",
        "genre",
        "record_label"
      ],
      "additionalProperties": false
    },
    "both_entities_are_bands": {
      "type": "boolean"
    }
  },
  "required": [
    "howlin_maggie_info",
    "ugly_casanova_info",
    "both_entities_are_bands"
  ],
  "additionalProperties": false
}

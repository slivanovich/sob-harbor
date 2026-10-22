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
The Lilacs: The Lilacs were a four-piece rock band from Chicago's North Side, formed in April 1990 by Ken Kurson, David Levinsky, Tom Whalen and John Packel.  Kurson had previously played bass for Green, and after leaving the fold, he and fellow Glenbrook North High School graduate David Levinsky joined together to form the Lilacs, recruiting Tom Whalen on bass and another Glenbrook North alum, John Packel.  The name was chosen for the group by Material Issue frontman Jim Ellison, who also produced the first 7" record -- "The Lilacs Love You".

Drakensberger cattle: Drakensberger Cattle are a breed of cattle indigenous to South Africa that were developed over several centuries.  In 1497 Vasco de Gama acquired a black ox from local natives and loved the meat.  Drakensberger cattle have the honor of being history's first recorded black cattle on the Cape of Africa, they were also called Uys Cattle until 1947.  They have the following characteristics they adapt well to local conditions, tender and succulent meat, exceptionally long breeding life, low mortality, high milk production, outstanding mother's, and are good-tempered.

Local Natives: Local Natives (previously known as Cavil at Rest) is an American indie rock band based in Silver Lake, Los Angeles, California, United States.  Their debut album, "Gorilla Manor", was first released in the UK in November 2009, and later released in the US on February 16, 2010.  The album received mostly positive reviews and debuted in the Billboard 200 and at No. 3 in the New Artist Chart.  Their second album, "Hummingbird", was released in January 2013.  Their third album, "Sunlit Youth", was released in September 2016.

William Pynchon: William Pynchon (October 11, 1590 – October 29, 1662) was an English colonist and fur trader in North America best known as the founder of Springfield, Massachusetts, USA.  He was also a colonial treasurer, original patentee of the Massachusetts Bay Colony, and the iconoclastic author of the New World's first banned book.  An original settler of Roxbury, Massachusetts, Pynchon became dissatisfied with that town's notoriously rocky soil and in 1635, led the initial settlement expedition to Springfield, Hampden County, Massachusetts, where he found exceptionally fertile soil and a fine spot for conducting trade.  In 1636, he returned to officially purchase its land, then known as "Agawam."  In 1640, Springfield was officially renamed after Pynchon's home village, now a suburb of Chelmsford in Essex, England — due to Pynchon's grace following a dispute with Hartford, Connecticut's Captain John Mason over, essentially, whether to treat local natives as friends or enemies.  (Pynchon was a man of peace and also very business-minded — thus he advocated for friendship with the region's natives.)  Pynchon's stance led to Springfield aligning with the faraway government of the Massachusetts Bay Colony rather than the more geographically and ideologically compatible Connecticut Colony.

Freak City Soundtrack: Freak City Soundtrack is the third studio album by Material Issue, released on Mercury Records in 1994.  It was the last studio album the band would record before frontman Jim Ellison committed suicide in 1996, and was produced by Mike Chapman, who also produced breakthrough albums for Blondie and The Knack.

Destination Universe: Destination Universe is the second studio album by Material Issue, released on Mercury Records in 1992.  The new album was not as well received by critics as the debut album, nor did it sell as well.  The album included the single "What Girls Want" and was, like their debut album, produced by Jeff Murphy.

Material Issue: Material Issue was an American power pop trio from Chicago, Illinois.  The band's trademark was pop songs with themes of love and heartbreak, with a number of song titles using girls' first names.

Jim Ellison: Jim Ellison (born James Walter Ellison) (April 18, 1964 – June 20, 1996) was the frontman for the band Material Issue.  He tirelessly promoted his band, booked tours, and secured a major-label deal in 1990.  Ellison — along with bassist Ted Ansani and drummer Mike Zelenko — would lead the renaissance of power pop in the early 1990s.  He committed suicide on June 20, 1996, by carbon monoxide poisoning.

Chiguata District: Chiguata is a district located in the Arequipa province, 30 km away from the city of Arequipa, Peru, on the slopes of the volcano Pikchu Pikchu (where at its summit pre-Inca worshipped remains and artifacts have been found).  The name "chiguata" comes from the Quechua words "chiri" meaning "cold" and "wata" meaning "year" (cold all year).  Ancient Chiguata was inhabited by the local natives until the arrival of Spanish influence in charge of the emissary Diego Hernández de Córdova in 1540.  Soon after, the construction of a small plaza was initiated, and according to the Dominican religious order and local sources, the plaza's "Templo del Espíritu Santo" ("Sacred Spirit temple") along with its domes and lateral cover was not begun until 1739.  The design of the temple is quite interesting, with two angels in feathered nightwear and their arms lifted vertically, separated by twelve fringes of rectangular flowers which add to the whole decoration of the temple.  Cherubs also decorate the circular cornice, along with four saints in full-length reliefs that occupy the "pechinas" of the columns that sustain the temple's dome, which is considered one of the most original works of the colony and now visited by occasional tourists.

Mendocino War: The Mendocino War was a violent conflict from July 1859 to January 18, 1860, between white settlers and local natives (mainly Yuki tribes) in Mendocino County, California.  It was caused by settler intrusion and slave raids on native lands and subsequent native retaliation, resulting in the deaths of hundreds of natives.  In 1859, a band of locally sponsored rangers led by Walter S. Jarboe, called the Eel River Rangers, raided the countryside in an effort to remove natives from settler territory and move them onto the Nome Cult Farm, an area near the Mendocino Indian Reservation.  By the time the Eel River Rangers were disbanded in 1860, Jarboe and his men had killed 283 warriors, captured 292, killed countless women and children, and only suffered 5 casualties themselves in just 23 engagements.  The bill to the state for the rangers’ services amounted to $11,143.43.  Scholars, however, state that the damage to the area and natives in particular was even higher than reported, especially given the vast number of raiding parties formed outside of the Eel River Rangers.  Frustrated with the inadequacy of federal protection, settlers formed their own raiding parties against the natives, joining Jarboe in his mission to rid Round Valley of its native population.  Those that survived were moved to the Nome Cult Farm, where they experienced hardships typical of the reservation system of the day.  After the conflict, contemporaries claimed that the conflict was more of a slaughter than a war, and later historians have labeled it a genocide.

Question: Did Local Natives or Material Issue originate in Chicago?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_originated_in_chicago": {
      "type": "string",
      "description": "The name of the band that originated in Chicago."
    },
    "other_band_origin_city": {
      "type": "string",
      "description": "The city where the other band originated."
    },
    "question_answered": {
      "type": "boolean",
      "description": "Indicates if the question about origin city was answered."
    },
    "bands_compared": {
      "type": "array",
      "description": "Details about the bands and their origin cities.",
      "items": {
        "type": "object",
        "properties": {
          "band_name": {
            "type": "string",
            "description": "The name of the band."
          },
          "origin_city": {
            "type": "string",
            "description": "The city where the band is based or originated."
          }
        },
        "required": [
          "band_name",
          "origin_city"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "band_originated_in_chicago",
    "other_band_origin_city",
    "question_answered",
    "bands_compared"
  ],
  "additionalProperties": false
}

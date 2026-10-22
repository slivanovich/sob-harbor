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
Spinmaster: Spinmaster, known in Japan as Miracle Adventure (ミラクルアドベンチャー ) , is an arcade game developed and released by Data East in December, 1993 in North America, in Europe the same year and on February 18, 1994 in Japan.  It is the first game Data East developed and released for the SNK Neo-Geo MVS hardware.  Its character designs are almost identical to the ones in Data East's Sega Genesis game titled "Dashin' Desperadoes"; however, the rest of both games are completely different.  Also, "Spinmaster"'s gameplay, artwork style, animations of some characters and the styles of its weapons were heavily inspired by another arcade game by Data East titled "Joe & Mac", according to the Japanese "Miracle Adventure" arcade flyer.

Dinosaur (film): Dinosaur is a 2000 American CGI animated adventure film produced by Walt Disney Feature Animation and The Secret Lab and released by Walt Disney Pictures.  It is the 39th Disney animated feature film and Disney's The Secret Lab computer animated feature, though it is not officially labeled as one of the animated classics in the United Kingdom, where "The Wild" (2006) is included in the canon instead.

Sebadoh: Sebadoh ( ) is an American indie rock band, currently signed with Joyful Noise Recordings.  Sebadoh were formed in 1988 in Northampton, Massachusetts, by Eric Gaffney and Dinosaur Jr bass player Lou Barlow.  Along with such bands as Pavement and Guided by Voices, Sebadoh helped pioneer lo-fi music, a style of indie rock characterized by low-fidelity recording techniques, often on four-track machines.  The band's early output, such as "The Freed Man" and "Weed Forestin'" (both released 1990), as well as "Sebadoh III" (1991), was typical of this style.  After a 14-year recording hiatus, during which time members pursued other projects while occasionally touring as Sebadoh, the group returned in 2013 with the "Secret EP" and a full-length album titled "Defend Yourself", which were both self-recorded.  Lead singer Lou Barlow says of the band's resurrected sound, "We kept to ourselves during the recording and didn’t have much, if any, outside intervention.  That, to my mind, makes it a true Sebadoh record and aligns the style of "Defend Yourself" with our early releases."

Dinosaur (Kisschasy song): "Dinosaur" is a song by Australian rock band Kisschasy, it is the third single released, in January 2010, from their third studio album, "Seizures" (August 2009).  It was written by their singer-guitarist, Darren Cordeux, which reached the top 40 on the ARIA Singles Chart.  By the end of that year it was certified gold by ARIA for shipment of 35,000 units.

The Miracle (album): The Miracle is the thirteenth studio album by the British rock band Queen, released on 22 May 1989 by Parlophone Records in the United Kingdom and by Capitol Records in the United States.  The album was recorded as the band recovered from Brian May's marital problems and Freddie Mercury's AIDS diagnosis in 1987 (which was, though known to the band, not publicised at the time).  Recording started in January 1988 and lasted for an entire year.  The album was originally going to be called "The Invisible Men", but three weeks before the release, according to Roger Taylor, they decided to change the name to "The Miracle".  It was also the last album to feature a band photo with all four original members on the front cover.

Chikarasaurus Rex: How to Hatch a Dinosaur: Chikarasaurus Rex: How to Hatch a Dinosaur was a professional wrestling internet pay-per-view (iPPV) event produced by the Chikara promotion, that took place on June 2, 2012 at the Trocadero Theatre in Philadelphia, Pennsylvania and aired live on GoFightLive, with a pre-show airing live on Ustream.  The event marked Chikara's second pay-per-view, following previous November's High Noon.  This was the third year in which Chikara promoted a summer event under the "Chikarasaurus Rex" banner, with the original "Chikarasaurus Rex: King of Show" having taken place July 25, 2010, and the "Chikarasaurus Rex: King of Sequel" weekend on July 30 and 31, 2011.  The event was released on DVD and downloadable MP4 by Smart Mark Video on June 4, 2012.

List of Pretty Cure films: The following is a list of Japanese animated films produced by Toei Animation, based on Izumi Todo's "Pretty Cure" ("PreCure") anime television franchise.  Beginning with 2005's "Futari wa Pretty Cure Max Heart", which had two films released for it, each subsequent series in the franchise has received a film, which is usually released towards the end of each year.  In addition, the "Pretty Cure All Stars" films, which feature storylines that crosses over characters from each of the series to date, began releasing annually in Japan from 2009, often airing in the Spring of each year.  Many of the films often incorporate electrical lights known as Miracle Lights, which are handed out to audience members during theatrical screenings so they can participate in the film's climax.

Miracle (2004 film): Miracle is a 2004 American sports docudrama about the United States men's hockey team, led by head coach Herb Brooks, portrayed by Kurt Russell, that won the gold medal in the 1980 Winter Olympics.  The American team's victory over the heavily favored Soviet professionals in the medal round was dubbed the Miracle on Ice.  "Miracle" was directed by Gavin O'Connor and written by Eric Guggenheim and Mike Rich.  It was released on February 6, 2004.

1991: The Year Punk Broke: 1991: The Year Punk Broke , released theatrically in 1992, is a documentary directed by Dave Markey featuring American alternative rock band Sonic Youth on tour in Europe in 1991.  While Sonic Youth is the focus of the documentary, the film also gives attention to Nirvana, Dinosaur Jr., Babes in Toyland, Gumball and The Ramones.  Also featured in the film are Mark Arm, Dan Peters and Matt Lukin of Mudhoney and roadie Joe Cole, who was murdered in a robbery three months after the tour ended.  The film is dedicated to him.

Roboreptile: The Roboreptile toy robot manufactured by WowWee Ltd.  The Roboreptile has infrared and sound sensors, and is able to autonomously explore its environment while avoiding obstacles.  It can also operate in different modes where it simulates behaviors of real animals.  It is able to rear up on its hind legs and attack.  Roboreptile was released in China on the 28 April 2006 and to the rest of the world later that year.  It is superficially similar to a theropod or prosauropod dinosaur but being quadrupedal it's better equated to a monitor lizard.

Question: Were Miracle and Dinosaur released in the same year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "comparison_result": {
      "type": "boolean",
      "description": "True if the entities were released in the same year, false otherwise."
    },
    "entity_1": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the first entity being compared."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the first entity."
        }
      },
      "required": [
        "name",
        "release_year"
      ],
      "additionalProperties": false
    },
    "entity_2": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the second entity being compared."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the second entity."
        }
      },
      "required": [
        "name",
        "release_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "comparison_result",
    "entity_1",
    "entity_2"
  ],
  "additionalProperties": false
}

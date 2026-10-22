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
Kiske/Somerville: Kiske/Somerville is a melodic heavy metal duet project, put together in late 2009 by Frontiers Records.  The project features vocalist Michael Kiske (ex-Helloween, Unisonic, Place Vendome) collaborating with American singer Amanda Somerville (Aina, HDK, Trillium, Epica).

Keeper of the Seven Keys: Part I: Keeper of the Seven Keys: Part I is the second studio album by German power metal band Helloween, released in 1987.  It marks the first appearance of vocalist Michael Kiske, and is considered the album that created the genre of European-style power metal.  Kai Hansen stepped away from doing vocal duties as he had difficulties singing and playing the guitar at the same time during the previous tour.  It was an album dominated by Hansen, due to an injury to co-guitarist Michael Weikath which prevented him from performing on much of the album. " Future World" was released as a single and a music video was made for "Halloween" but with 8 minutes omitted from the song.  The band originally planned to release "Keeper of the Seven Keys: Part I" and "" as a double album, but their record label refused, insisting that the albums be released separately.  Much later in 2010, both albums were released together with bonus tracks.

Yuju (singer): Choi Yu-na (born October 4, 1997), better known by her stage name Yuju, is a South Korean singer.  She is best known as the main vocalist of the South Korean girl group GFriend.

Kiske/Somerville (album): Kiske/Somerville is the debut album of the melodic rock / heavy metal duet project Kiske/Somerville.  The album features the collaboration of vocalist Michael Kiske (ex-Helloween, Unisonic, Place Vendome) with American singer Amanda Somerville (Aina, HDK, Trillium).  The album was released on 24 September 2010 with cover art credited to Stanis W. Decker.

Michael Kiske: Michael Kiske (born January 24, 1968) is a German singer best known as the lead vocalist for the German power metal band Helloween.  After his departure from the band, Kiske recorded four solo albums, participated on various metal and rock related projects, such as Avantasia, Place Vendome and Kiske/Somerville, while he also performed with numerous bands as a guest vocalist.  In late 2009, he formed the hard rock / heavy metal band Unisonic and began touring again after 17 years of absence.  On November 14, 2016 it was officially announced that Kiske will tour again with Helloween and Kai Hansen in 2017 and 2018.

City of Heroes (album): City of Heroes is the second studio album by the melodic rock / heavy metal duet project Kiske/Somerville.  The album features the collaboration between vocalist Michael Kiske (ex-Helloween, Unisonic, Place Vendome) and American singer Amanda Somerville (Aina, HDK, Trillium).  It was released on 17 April 2015 in Europe and on 21 April 2015 in North America.

Past in Different Ways: Past in Different Ways is the fourth solo album of vocalist Michael Kiske.  It features acoustic renditions of songs written by Kiske during his time in Helloween and one new track.  This came as a surprise to fans, considering Kiske's desire to leave the world of Helloween and heavy metal behind him.

Helloween: Helloween is a German power metal band founded in 1984 in Hamburg, Northern Germany by members of bands Iron Fist and Gentry.  Its first line-up consisted of singer and guitarist Kai Hansen, bass guitarist Markus Grosskopf, guitarist Michael Weikath, and drummer Ingo Schwichtenberg.  After the release of a self-titled EP and their debut album "Walls of Jericho" in 1985, it expanded into a quintet with the addition of singer Michael Kiske, Hansen choosing to focus on guitar instead.  Under this line-up, they released the "Keeper of the Seven Keys" albums (1987 and 1988), which established Helloween as a notable heavy metal band and led to the creation of the power metal subgenre.  However, Hansen left the band quickly after the release of "Part II" and was replaced by Roland Grapow.  He then created the band Gamma Ray.

Mr. Ego (Take Me Down): "Mr Ego (Take Me Down)" is a song and an EP made by the German power metal band Helloween taken from the album "Master of the Rings".  It is "dedicated" to former Helloween's singer, Michael Kiske.

New Era (Revolution Renaissance album): New Era is the debut album of Finnish power metal pioneer Timo Tolkki's band, Revolution Renaissance.  After Tolkki's split from Stratovarius in 2008 he used what fan's knew the album to be titled "R.. .  R.. ."  as the namesake for his new project.  Using material he had written for Stratovarius's upcoming album, Tolkki's "New Era" features the talents of German power metal vocalist Tobias Sammet and German singer Michael Kiske among others.

Question: Are both Michael Kiske and Yuju singers?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question": {
      "type": "string",
      "description": "The original question asked."
    },
    "entities_checked": {
      "type": "array",
      "description": "Details about each entity mentioned in the question and whether they are a singer.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the person."
          },
          "is_singer": {
            "type": "boolean",
            "description": "True if the person is identified as a singer in the context, false otherwise."
          },
          "role_description": {
            "type": "string",
            "description": "A description of their role as a singer from the context."
          }
        },
        "required": [
          "name",
          "is_singer",
          "role_description"
        ],
        "additionalProperties": false
      }
    },
    "all_entities_are_singers": {
      "type": "boolean",
      "description": "The final answer to whether all specified entities are singers."
    }
  },
  "required": [
    "question",
    "entities_checked",
    "all_entities_are_singers"
  ],
  "additionalProperties": false
}

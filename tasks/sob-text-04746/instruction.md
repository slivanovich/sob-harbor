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
Milli Vanilli: Milli Vanilli was a German R&B duo from Munich.  The group was founded by Frank Farian in 1988 and consisted of Fab Morvan and Rob Pilatus.  The group's debut album "Girl You Know It's True" achieved international success and earned them a Grammy Award for Best New Artist on 21 February 1990.  Milli Vanilli became one of the most popular pop acts in the late 1980s and early 1990s, with millions of records sold.

My Little Red Book: "My Little Red Book" is a song composed by Burt Bacharach with lyrics by Hal David.  In the wake of the British Invasion, Bacharach, a former bandleader for Marlene Dietrich, began working hands-on with beat groups of the era such as Manfred Mann.  Manfred Mann recorded the song for the 1965 film "What's New Pussycat? ", filmed between October 1964 to June 1965; the entire catalogue of music for the film was written by Bacharach and David.

Blur (Blur album): Blur is the fifth studio album by the English rock band Blur, released on 10 February 1997 by Food Records.  Blur had previously been broadly critical of American popular culture and their previous albums had become associated with the Britpop movement, particularly "Parklife" (1994), which had helped them become one of Britain's leading pop acts.  After their previous album, "The Great Escape", the band faced media backlash and relationships between the members became strained.

Area Festival: The Area Festival was a music festival founded by popular electronic musician Moby, who asserted that he was "in large part, inspired by the ethos of Lollapalooza", and wished to create a similarly "genuinely eclectic, interesting, alternative music festival".  Moby organized the first such festival, called Area:One in 2001, and the sequel tour Area2, in 2002.  The festival is currently on indefinite hiatus.  The festival featured diverse genres of music.  Besides headliner Moby, the main stage mostly featured rock and pop acts.  The second stage was an air-conditioned tent where electronic, dance and smaller bands performed.

Vitamin String Quartet: Vitamin String Quartet (VSQ) is a musical group from Los Angeles, California, that is widely known for its series of tribute albums to rock and pop acts.  Their albums are released through Vitamin Records and primarily performed by a string quartet, though other instruments have been used.  "Vitamin String Quartet is about applying rock n' roll attitude to classical technique," says Tom Tally, a violist and arranger who has performed on and produced over fifty Vitamin String Quartet albums.

Venetta Fields: Venetta Lee Fields (born 1941) is an American-Australian singer, musical theater actress and vocal coach.  She was a backing vocalist for American and British rock and pop acts of the 1960s and 1970s including Ike & Tina Turner, Pink Floyd, Barbra Streisand, Elkie Brooks, Neil Diamond, Steely Dan, and the Rolling Stones.  Since 1982 she has lived and worked in Australia, and holds dual Australian-American citizenship.  She recorded or toured as a backing singer for Australian artists, Richard Clapton, Australian Crawl, Cold Chisel, Jimmy Barnes, James Morrison and John Farnham.

Fascination Records: Fascination Records is a United Kingdom-based record label, owned by Universal Music Group, and operated as an imprint of Polydor Records.  The label was launched in spring of 2006, and is managed by former TOTP Magazine editor Peter Loraine.  It concentrates on a relatively small number of pop acts and will complement the re-activated Fiction rock imprint.

Sunshine pop: Sunshine pop (originally called soft pop ) is a lightly-produced subgenre of pop music originating in Southern California in the mid 1960s.  Rooted in easy-listening, advertising jingles, and the growing drug culture, sunshine pop acts combined nostalgic or anxious moods with "an appreciation for the beauty of the world".  It largely consisted of lesser-known artists who imitated more popular groups like the Beach Boys, the Mamas & the Papas, and the 5th Dimension.  While the Beach Boys are noted as prominent influences, they rarely worked in the genre.

Operation Hurricane: Operation Hurricane was the test of the first UK atomic device, on 3 October 1952.  A plutonium implosion device was detonated in the lagoon in the Monte Bello Islands in Western Australia.  With the success of Operation Hurricane, Britain became the third nuclear power after the United States and the Soviet Union.

British Invasion: The British Invasion was a cultural phenomenon of the mid-1960s, when rock and pop music acts from the United Kingdom, as well as other aspects of British culture, became popular in the United States, and significant to rising "counterculture" on both sides of the Atlantic.  Pop and rock groups such as the Beatles, the Dave Clark Five, the Kinks, the Rolling Stones, Herman's Hermits, and the Animals were at the forefront of the invasion.

Question: What's the name of the group that  Bacharach worked hands-on with, when rock and pop acts from Britain became popular in the United States

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "composer_name": {
      "type": "string",
      "description": "The name of the composer who worked with the group."
    },
    "group_name": {
      "type": "string",
      "description": "The name of the group that the composer worked with."
    },
    "group_origin_country": {
      "type": "string",
      "description": "The country of origin for the group."
    },
    "historical_event_context": {
      "type": "string",
      "description": "The historical event during which the collaboration occurred."
    }
  },
  "required": [
    "composer_name",
    "group_name",
    "group_origin_country",
    "historical_event_context"
  ],
  "additionalProperties": false
}

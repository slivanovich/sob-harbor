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
Social guidance film: Social guidance films constitute a genre of educational films attempting to guide children and adults to behave in certain ways.  Originally produced by the U.S. government as "attitude-building films" during World War II, the genre grew to be a common source of instruction in elementary and high school classrooms in the United States from the late 1940s to the early 1970s.  The films covered topics including courtesy, grammar, social etiquette and dating, personal hygiene and grooming, health and fitness, civic and moral responsibility, sexuality, child safety, national loyalty, racial and social prejudice, juvenile delinquency, drug use, and driver safety; the genre also includes films for adults, covering topics such as marriage, business etiquette, general safety, home economics, career counseling and how to balance budgets.

Northern (genre): The Northern or Northwestern is a genre in various arts which tell stories set primarily in the later half of the 19th century in the north of North America, primarily in Canada but also in Alaska.  It is similar to the Western genre but many elements are different, as appropriate to its setting.  It is common for central character to be a Mountie instead of, for example, a cowboy or sheriff.  Other common characters include fur trappers and traders, lumberjacks, prospectors, First Nations people, settlers and townsfolk.

Well-made play: The well-made play (French: "la pièce bien faite" , pronounced ] ) is a dramatic genre from nineteenth-century theatre first codified by French dramatist Eugène Scribe.  Dramatists Victorien Sardou, Alexandre Dumas, fils, and Emile Augier wrote within the genre, each putting a distinct spin on the style.  The well-made play was a popular form of entertainment.  By the mid-19th century, however, it had already entered into common use as a derogatory term.  Henrik Ibsen and the other realistic dramatists of the later 19th century (August Strindberg, Gerhart Hauptmann, Émile Zola, Anton Chekhov) built upon its technique of careful construction and preparation of effects in the genre problem play.  "Through their example", Marvin Carlson explains, "the well-made play became and still remains the traditional model of play construction."

Noori: Noori (Urdu:نوری, literal English translation: "light") is a rock band from Lahore, Punjab, Pakistan, formed in 1996.  The group was formed by songwriter, lead vocalist and guitarist, Ali Noor, along with his younger brother Ali Hamza, who were soon joined by bassist Muhammad Ali Jafri and drummer Salman Albert.  Since the inception of the band, there had been many changes in the line-up; the only consistent members being, brothers, Ali Noor and Ali Hamza.

First-person shooter: First-person shooter (FPS) is a video game genre centered around gun and other weapon-based combat in a first-person perspective; that is, the player experiences the action through the eyes of the protagonist.  The genre shares common traits with other shooter games, which in turn makes it fall under the heading action game.  Since the genre's inception, advanced 3D and pseudo-3D graphics have challenged hardware development, and multiplayer gaming has been integral.

Return to the Field: Return to the Field (歸田賦) is a literary work written in the Chinese style known as a rhapsody, or "fu" style: it is by Zhang Heng (AD 78–139), an official, inventor, mathematician, and astronomer of the Han Dynasty of China (202 BC–220 AD).  Zhang's "Return to the Field" is a seminal work in the Fields and Gardens poetry genre which helped to sparked centuries of poetic enthusiasm for poems of various forms which share a common theme of nature foremost with human beings and human thought seemingly not in main focus, somewhat similar to the Landscape poetry genre; however, in the case of the Fields and Gardens genre, nature was focused upon in its more domestic manifestation, paying homage to the appearance of nature in gardens, as found in backyards, and cultivated in the countryside.  "Return to the Field" also invokes traditional themes of Classical Chinese poetry involving nature versus society.

Biblical genre: A Biblical genre is a classification of Bible literature according to literary genre.  The genre of a particular Bible passage is ordinarily identified by analysis of its general writing style, tone, form, structure, literary technique, content, design, and related linguistic factors; texts that exhibit a common set of literary features (very often in keeping with the writing styles of the times in which they were written) are together considered to be belonging to a genre.  In Biblical studies, genres are usually associated with whole books of the Bible, because each of its books comprises a complete textual unit; however, a book may be internally composed of a variety of styles, forms, and so forth, and thus bear the characteristics of more than one genre (for example, chapter 1 of the Book of Revelation is prophetic/visionary; chapters 2 and 3 are similar to the epistle genre; etc.).

Augustana (band): Augustana is an American rock band from San Diego, California that has released five albums and an EP while being signed to Epic Records and Razor & Tie.  They are best known for their song "Boston" and the album "All the Stars and Boulevards", both entering the Billboard charts.  They are fronted by Dan Layus who currently is the only remaining member of the band.

Genre painting: Genre painting, also called genre scene or petit genre, depicts aspects of everyday life by portraying ordinary people engaged in common activities.  One common definition of a genre scene is that it shows figures to whom no identity can be attached either individually or collectively—thus distinguishing "petit genre" from history paintings (also called "grand genre") and portraits.  A work would often be considered as a genre work even if it could be shown that the artist had used a known person—a member of his family, say—as a model.  In this case it would depend on whether the work was likely to have been intended by the artist to be perceived as a portrait—sometimes a subjective question.  The depictions can be realistic, imagined, or romanticized by the artist.  Because of their familiar and frequently sentimental subject matter, genre paintings have often proven popular with the bourgeoisie, or middle class.

Jenny Lind Chapel: The Jenny Lind Chapel is a historic church located at the southwest corner of 6th and Oak Streets in Andover, Illinois.  Completed in 1851 for a congregation founded the previous year, the church was the first built by the Augustana Synod, the main Swedish Lutheran church in America.  Pastor Lars Paul Ebsjorn founded the church for local Swedes who still wished to worship with the Church of Sweden; many were former members of the nearby Bishop Hill Colony who had lost faith in Eric Jansson's teachings, while the others were Swedes who had immigrated to the area due to the colony's fame.  The church was named in honor of Swedish opera singer Jenny Lind, who donated $1,500 for its construction.  The building has a simple design with Greek Revival features, a common form for small rural churches of the era.

Question: Augustana and Noori, have which genre in common?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "band_names": {
      "type": "array",
      "description": "The names of the bands being compared.",
      "items": {
        "type": "string"
      }
    },
    "common_genre": {
      "type": "string",
      "description": "The genre that both bands have in common."
    },
    "genre_category": {
      "type": "string",
      "description": "The broader category of the common genre (e.g., 'music', 'film')."
    }
  },
  "required": [
    "band_names",
    "common_genre",
    "genre_category"
  ],
  "additionalProperties": false
}

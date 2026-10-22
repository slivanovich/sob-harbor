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
Birthday (short story collection): Birthday (バースデイ , Bāsudei ) is an anthology by Japanese writer Koji Suzuki first published on February 5, 1999 in Japan.  It is the fourth installment of Suzuki's "Ring" series.

Reiko Asakawa: Reiko Asakawa (浅川 玲子 , Asakawa Reiko ) is a character in the 1998 film adaptation of Koji Suzuki's novel "Ring", published in 1991, portrayed by Nanako Matsushima.  She also plays important roles in "Ring 2" and "Rasen".  She was adapted from Suzuki's original protagonist, Kazuyuki Asakawa, who was originally male.  Producers changed the character's gender because they felt that a woman would be more appealing to the box office audience.

Ring: Kanzenban: Ring: Kanzenban (Japanese: リング 完全版 , Hepburn: Ringu: Kanzenban , lit. " "Ring: The Complete Edition"") is a 1995 Japanese horror film based on the book "Ring" by Koji Suzuki.  Unlike that of the later film series the characters remain largely unchanged and in comparison other films made of this novel it is the most accurate in relation to the original text.

The Ring: Terror's Realm: The Ring: Terror's Realm (known simply as Ring (リング "Ringu") in Japan) is a survival horror video game developed and published by Asmik Ace Entertainment in Japan and published by Infogrames in North America.  It was released for Dreamcast on February 24, 2000 in Japan and August 22, 2000 in North America.  It is based on the "Ring" series of novels by Japanese author Koji Suzuki, which also inspired the Japanese film "Ring" (1998) and its American remake, "The Ring" (2002).

Ring (Suzuki novel): Ring (リング , Ringu ) is a Japanese mystery horror novel by Koji Suzuki first published in 1991, and set in modern-day Japan.  It was the basis for a 1995 film (""), a television series (""), a film of the same name (1998's "Ring"), and two remakes of the 1998 film: a South Korean version ("The Ring Virus"), an American version ("The Ring"), and The Ring's sequel, Rings.

The Ring (2002 film): The Ring is a 2002 American supernatural psychological horror film directed by Gore Verbinski and starring Naomi Watts, Martin Henderson, and David Dorfman.  It is a remake of the 1998 Japanese horror film "Ringu", which was based on the novel of the same name, written by Koji Suzuki.

Koji Suzuki: Koji Suzuki (鈴木 光司 , Suzuki Kōji , born 13 May 1957) is a Japanese writer, who was born in Hamamatsu and currently lives in Tokyo.  Suzuki is the author of the "Ring" novels, which have been adapted into other formats, including films, manga, TV series and video games.  He has written several books on the subject of fatherhood.  His hobbies include traveling and motorcycling.

Spiral (Suzuki novel): Spiral (らせん , Rasen ) is a 1995 Japanese novel, a part of author Koji Suzuki's "Ring" series.  It is the second in the "Ring series", and a film based on the book, "Rasen" was released in 1998.  The English translation of the book was published by Vertical Press in the United States and by Harper Collins in Britain.

The Ring Virus: The Ring Virus () is a South Korean horror film adapted from the Japanese novel "Ring" by Koji Suzuki.  A joint project between Japan and Korea, this version has Park Eun-Suh as the creator of the cursed videotape.  Although the filmmakers claimed that the film was adapted from the novel, there are various scenes in the film that match the 1998 film "Ring", such as the sex of the lead character, some of the scenes on the videotape as well as copying other film scenes directly from the original film, including the film's climax.

List of Ring characters: This article lists the characters who have appeared in the Japanese Ring films, based on a series of novels written by Koji Suzuki.  The series is made up of "Ring", "Rasen", "Ring 2", "" and "Sadako 3D".  The films have also been adapted into the Korean film "The Ring Virus", and the American series "The Ring", "Rings" (2005), "The Ring Two" and "Rings" (2017).  In television the first novel has been adapted into the television film as well as a 12 episode series.  A follow up series, Rasen was also made.

Question: What is the South Korean horror film adapted from the Japanese novel "Ring" by Koji Suzuki which was first published in 1991, and set in modern-day Japan?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the South Korean horror film."
    },
    "film_country_of_origin": {
      "type": "string",
      "description": "The country of origin for the film."
    },
    "source_novel_title": {
      "type": "string",
      "description": "The title of the Japanese novel the film was adapted from."
    },
    "source_novel_author": {
      "type": "string",
      "description": "The author of the source novel."
    },
    "source_novel_publication_year": {
      "type": "integer",
      "description": "The year the source novel was first published."
    },
    "source_novel_setting": {
      "type": "string",
      "description": "The setting of the source novel."
    }
  },
  "required": [
    "film_title",
    "film_country_of_origin",
    "source_novel_title",
    "source_novel_author",
    "source_novel_publication_year",
    "source_novel_setting"
  ],
  "additionalProperties": false
}

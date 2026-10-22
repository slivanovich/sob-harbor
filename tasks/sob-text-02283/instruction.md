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
Christine Feehan: Christine Feehan (b. Christine King in California) is an American romance-paranormal writer.  She has published more than 40 novels, including five series, and numerous novellas since 1999.

Unleashed (Sara Humphreys book): Unleashed is a paranormal/suspense novel written by American author Sara Humphreys.  Published in 2011, it is the first book in her The Amoveo Legend Series, which to date has 7 titles.

Dark Guardian (novel): Dark Guardian is a paranormal/suspense novel written by American author Christine Feehan.  Published in 2002, it is the 9th book in the Dark Series, and focuses on Jaxon and Lucian.

Lair of the Lion: Lair of the Lion is a paranormal/romance written by American author Christine Feehan.  Unlike most for her other works, this novel is not part of an ongoing series and isn’t set in the present day.  "Lair of the Lion" is set in Italy.

Lisa Mason (writer): Lisa Mason is an American writer of science fiction, fantasy, and urban fantasy.  She lives in Piedmont, California with her husband, the artist and jeweler Tom Robinson.  She is a Phi Beta Kappa scholar and graduate of the University of Michigan, the College of Literature, Sciences, and the Arts, and the University of Michigan Law School.  She practiced law in Washington D.C. and San Francisco.  To have more time to write, she transitioned to Matthew Bender and Company, a national law book publisher, where she started as a legal writer and rose to an executive editor.  Many of her novels take place in the vicinity of San Francisco, California, either in the future or in the past through time travel.  Her early works are recognized as cyberpunk.  She has also written paranormal romance, historical romantic suspense, comedy, and a screenplay.

P. N. Elrod: Patricia Nead Elrod is an American novelist specializing in urban fantasy.  She has written in the mystery, romance, paranormal, and historical genres with at least one foray into comedic fantasy.  Elrod is also an editor, having worked on several collections for Ace Science Fiction, DAW, Benbella Books, and St. Martin's Griffin.  She self-published a signed, limited edition novel under her own imprint, Vampwriter Books.

The Bozz Chronicles: The Bozz Chronicles , now a graphic novel, was originally a six-issue comic book series written by David Michelinie, with artwork by Bret Blevins and John Ridgway.  The original series was published by Epic Comics from December 1985 - December 1986.  The series was set primarily in Victorian era England and centered on the crime-solving adventures of "Bozz", an alien with a long tail and an unpronounceable name who crash-landed on Earth.  Bozz partners with prostitute Amanda Flynn and American Salem Hawkshaw to solve crimes as a means of stimulating his mind and avoiding suicidal thoughts brought on by ennui.  Most mysteries presented in the series were paranormal or speculative in nature, for example, resurrection, death rays, and portals to hell.  In 2014, it was announced that the six issue series would finally be collected into one publication by Dover Publications in 2015.

Rosemary Ellen Guiley: Rosemary Ellen Guiley (born 8 July 1950) is an American writer on topics related to spirituality, the occult, and the paranormal.  She is also a radio show host, a certified hypnotist, a board director of the "National Museum of Mysteries and Research" and the "Foundation for Research into Extraterrestrial Encounters", and a "Lifetime Achievement Award" winner from the Upper Peninsula Paranormal Research Society, Michigan.  She has written more than 49 books, including ten encyclopedias.

Michele Bardsley: Michele Bardsley is the pen name of Michele Freeman (born Michele Renee Vail on January 21, 1970 in Tulsa, Oklahoma) who is an award-winning American writer of paranormal and contemporary romantic fiction.  Bardsley is a New York Times and USA Today bestselling author and has published more than 40 novels, novellas, short stories, and articles since the publication of her first book in 1999.  She's written young adult paranormal fiction under Michele Vail.  She lives in Texas with her husband, four dogs, and two cats.

Warm Bodies (film): Warm Bodies is a 2013 American paranormal romantic zombie comedy film based on Isaac Marion's novel of the same name.  Directed and written by Jonathan Levine, the film stars Nicholas Hoult, Teresa Palmer, Analeigh Tipton and John Malkovich.

Question: which paranormal novel was written by an american romance-paranormal writer?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "novel_title": {
      "type": "string",
      "description": "The title of the paranormal novel."
    },
    "novel_genres": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of genres associated with the novel."
    },
    "author_info": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the author."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the author."
        },
        "author_primary_genres": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of primary genres the author is known for, including romance and paranormal."
        }
      },
      "required": [
        "name",
        "nationality",
        "author_primary_genres"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "novel_title",
    "novel_genres",
    "author_info"
  ],
  "additionalProperties": false
}

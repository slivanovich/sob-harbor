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
Spark (1998 film): Spark is a 1998 film starring Terrence Howard and Nicole Ari Parker.  Garret Williams made his directorial debut with this tale of an urban black couple trapped in a desert town of rednecks after their car breaks down after hitting a dog.  Byron (Terrence Howard) and Nina (Nicole Ari Parker) are driving a BMW from Chicago to L.A. to take Nina to school when they experience a back-road breakdown.  Teen Mooney (Brendan Sexton III) tows them to a white-trailer-trash town where they're charged $500 for repairs.  When the BMW dies again, they stay overnight in a motel, and the situation soon gets grim as Byron starts spending more time with Mooney and his true colors start to show revealing a disturbing town story.  The characters in this low-budgeter were first introduced in a 1996 short.  "Spark" was shown at 1998 film festivals (Sundance, Berlin).

Jeans (soundtrack): Jeans is the soundtrack from the 1998 film of the same name, released by West Top in March 1998.  The soundtrack features artists such as Hariharan, Harini and Unnikrishnan.  A. R. Rahman composed the music for this movie.  The original soundtrack featured lyrics by Vairamuthu in Tamil.  Following the success of the soundtrack, it was dubbed to Hindi with lyrics by Javed Akhtar and was released by T-Series.  The Telugu version lyrics were written by A. M. Rathnam and Sivaganesh which was released by Aditya Music.  The album consists of eight songs, but the last two songs were featured in the cassettes only.  Audio disks of both versions featured six songs.

Zilla (TriStar Godzilla): Zilla (ジラ , Jira ) is a film monster that first appeared as the title character in TriStar Pictures' 1998 film "Godzilla".  It was initially created as a reimagining of Godzilla; however after 2004, Toho (the Godzilla IP owners) began trademarking future incarnations of TriStar's Godzilla as "Zilla", with only the incarnations from the 1998 film and "" retaining the Godzilla copyright and trademark.

Faith of the Heart: "Faith of the Heart" is a song written by Diane Warren and performed by Rod Stewart for the soundtrack to the 1998 film "Patch Adams".  Stewart's version charted at number 3 on the US Hot Adult Contemporary Tracks and at number 60 on the UK Singles Chart.  It was warmly received by critics.  The song was later covered in 1999 by Susan Ashton for her album "Closer" and released as her first single in the country music genre.  Although it was expected to do well, it was outperformed by her subsequent single.

Mulan Jr.: Mulan Jr. is a one-act stage musical based on the 1998 Disney animated film "Mulan", which in turn was based on the Chinese legend of Hua Mulan) and the story "Fa Mulan" by Robert D. San Souci.  The adaptation mixes songs featured in the 1998 film as well as deleted songs from the film, including the revival of songs written by Stephen Schwartz, who was the original composer for the 1998 film before leaving to work on "The Prince of Egypt".  The musical is G-rated, any mature content from the sources it is based on having been deleted in the adaptation.  The cast includes 26 roles plus an ensemble.

Haunting Me (song): "Haunting Me" is a song by American industrial rock band Stabbing Westward.  The song was released as the third and final single from the album "Darkest Days".  The song was featured in the film "The Faculty".

Alice Hoffman: Alice Hoffman (born March 16, 1952) is an American novelist and young-adult and children's writer, best known for her 1995 novel "Practical Magic", which was adapted for a 1998 film of the same name.  Many of her works fall into the genre of magic realism and contain elements of magic, irony, and non-standard romances and relationships.

The Faculty: The Faculty is a 1998 American science fiction teen horror film written by Kevin Williamson, directed by Robert Rodriguez, and starring Elijah Wood, Josh Hartnett, Shawn Hatosy, Jordana Brewster, Clea DuVall, Laura Harris, Robert Patrick, Bebe Neuwirth, Piper Laurie, Famke Janssen, Usher Raymond, Salma Hayek, and Jon Stewart.

Blade (soundtrack): Blade is the soundtrack to the 1998 film, "Blade".  It was released on August 25, 1998 through TVT Records and Epic Records and featured a wide range of musical genres including hip hop, techno, electronic and alternative rock.  The soundtrack managed to make it to #36 on the "Billboard" 200 and #28 on the Top R&B/Hip-Hop Albums and featured one charting single "Wrek Tha Discotek" which peaked at #42 on the Hot Dance Music/Club Play chart.

Singh Kaur: Laura Drew, a.k.a. Singh Kaur or Lorellei (1955–1998) was a new-age music composer, vocalist and instrumentalist, who had a prolific career that lasted from the early 1970s to the late 1990s, releasing 23 albums.  With her angelic voice and haunting melodies, Singh Kaur was a pioneer in the growing genre of Western interpretations of Indian chanting music.

Question: What is the genre of the 1998 film that Haunting Me was featured in?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "film_year": {
      "type": "integer",
      "description": "The release year of the film."
    },
    "film_genre": {
      "type": "string",
      "description": "The genre of the film."
    }
  },
  "required": [
    "film_title",
    "film_year",
    "film_genre"
  ],
  "additionalProperties": false
}

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
Jørgen Jørgensen: Jørgen Jørgensen (name of birth: Jürgensen, and changed to Jorgenson from 1817) (29 March 1780 – 20 January 1841) was a Danish adventurer during the Age of Revolution.  During the Action of 2 March 1808 his ship was captured by the British.  In 1809 he sailed to Iceland, declared the country independent from Denmark and pronounced himself its ruler.  He intended to found a new republic following the United States and the French First Republic.  He was also a prolific writer of letters, papers, pamphlets and newspaper articles covering a wide variety of subjects, and was an associate of the famous botanists Joseph Banks and William Jackson Hooker for a period.  He left over hundred written autographs and drawings, most of them are collected in the British Library.  Marcus Clarke referred to Jørgensen as "a singularly accomplished fortune wooer—one of the most interesting human comets recorded in history".

For the Term of His Natural Life (1908 film): For the Term of His Natural Life is a 1908 Australian silent film based on the 1874 novel by the same name by Marcus Clarke.  The film is an adaptation of MacMahon's stage adaptation of the novel.

Marcus Clarke: Marcus Andrew Hislop Clarke FRSA (24 April 1846 – 2 August 1881), known simply as and published as Marcus Clarke' was an English-born Australian novelist, journalist, poet, editor, librarian., playwright and magazine owner/ editor, he was best known for his 1874 novel "For the Term of His Natural Life".

Patricia Payne: Patricia Payne is an Australian screenwriter and film producer.  Her best-known work is "For the Term of His Natural Life", based on the book by Marcus Clarke.

Little Shop of Horrors (film): Little Shop of Horrors is a 1986 American rock musical horror comedy film directed by Frank Oz.  It is a film adaptation of the off-Broadway musical comedy of the same name by composer Alan Menken and writer Howard Ashman about a nerdy florist shop worker who finds out his venus fly trap can speak.  Menken and Ashman's Off-Broadway musical was based on the low-budget 1960 film "The Little Shop of Horrors", directed by Roger Corman.  The 1986 film stars Rick Moranis, Ellen Greene, Vincent Gardenia, Steve Martin, and Levi Stubbs as the voice of Audrey II.  The film also featured special appearances by James Belushi, John Candy, Christopher Guest, and Bill Murray.  It was produced by David Geffen through The Geffen Company and released by Warner Bros. on December 19, 1986.

Debbie Does Dallas: The Musical: Debbie Does Dallas: The Musical is an Off-Broadway musical with a book by Susan L. Schwartz, composed by Andrew Sherman, with Tom Kitt and Jonathan Callicutt providing additional music and lyrics.  It is based on the 1978 pornographic film "Debbie Does Dallas".  The musical, like the movie, centers on high schooler Debbie and her friends' attempts to become Dallas Cowboys cheerleaders; however, the musical contains far less sexual content than the movie.  The original Off-Broadway choreography was by Jennifer Cody.

Marcus Clarke (puppeteer): Marcus Clarke is a puppeteer and voice actor from Nottinghamshire.  He is best known as the puppeteer and voice actor behind the BAFTA-winning ITV Kids series Bookaboo and the principal puppeteer of Audrey II in the 1986 version of Little Shop of Horrors.  Clarke has worked as a puppeteer in over 60 television series and has created a similar number of puppets.  He was also a puppeteer and voice actor in two Muppet feature films and Who Framed Roger Rabbit.

For the Term of His Natural Life (disambiguation): For the Term of His Natural Life is a novelisation of life as a convict by Marcus Clarke.

For the Term of His Natural Life (1927 film): For the Term of His Natural Life is a 1927 Australian film, based on the novel by Marcus Clarke, directed, produced and co-wriiten by Norman Dawn.  It was the most expensive Australian silent film ever made and remains one of the most famous Australian films of the silent era.

Donald Molosi: Donald Leungo Gosego Molosi, (born 11 December, 1985) is an actor, writer and playwright.  Molosi debuted off-Broadway in 2010 as Philly Lutaaya in "Today It’s Me" making him the first Motswana to perform off-Broadway.  In 2011, Molosi won the Best Short Solo Award at United Solo Theatre Festival for his performance as Seretse Khama in "Blue, Black and White".  In 2013, Molosi returned off-Broadway to perform "Motswana: Africa, Dream Again".  He played supporting roles in the following historic films; "A United Kingdom" 2016 and "Given" 2009.  As a playwright, Molosi has published a collection of his original off-Broadway plays, which include "We Are All Blue", "Blue, Black and White" and "Motswana: Africa, Dream Again" in 2016.

Question: Who composed the original off-Broadway score for a film where Marcus Clarke was a puppetteer?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "composer_name": {
      "type": "string",
      "description": "The name of the composer of the original off-Broadway score."
    },
    "musical_title": {
      "type": "string",
      "description": "The title of the off-Broadway musical."
    },
    "film_adaptation_title": {
      "type": "string",
      "description": "The title of the film adaptation of the musical."
    },
    "puppeteer_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the puppeteer."
        },
        "role_in_film": {
          "type": "string",
          "description": "The specific role the puppeteer had in the film."
        }
      },
      "required": [
        "name",
        "role_in_film"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "composer_name",
    "musical_title",
    "film_adaptation_title",
    "puppeteer_details"
  ],
  "additionalProperties": false
}

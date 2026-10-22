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
Five Are Together Again: Five Are Together Again (published 1963) is a children's novel in The Famous Five series by Enid Blyton.  It was first published by Hodder and Stoughton and in its first edition illustrated by Eileen Soper.

Pinocchio: The Series: Pinocchio: The Series, also known as Saban's The Adventures of Pinocchio and known in Japan as Mock of the Oak Tree (樫の木モック , Kashi no Ki Mokku ) in Japan, is a 52-episode anime series by Tatsunoko Productions first aired on Fuji Television in 1972, which was edited by Saban in 1990.  The story is based on the novel "The Adventures of Pinocchio" by Italian author Carlo Collodi.

Enrico Mazzanti: Enrico Mazzanti (5 April 1850, in Florence - 3 September 1910) was an Italian engineer and cartoonist, who illustrated the first edition of "Pinocchio".

The Adventures of Pinocchio (1972 film): The Adventures of Pinocchio (Italian: "Le avventure di Pinocchio" ) is a 1972 Italian miniseries directed by Luigi Comencini.  Based on the Carlo Collodi's novel with the same name, the miniseries got a large critical success, and had an average of twenty-one and a half million viewers during its first airing on Rai 1.  A 135-minute edit of the miniseries was released to theatrical film markets in Europe the same year.

The Adventures of Pinocchio (unfinished film): The Adventures of Pinocchio (Italian: "Le avventure di Pinocchio" ) was an Italian animated film directed by Raoul Verdini and Umberto Spano.  Created and produced by Cartoni Animati Italiani Roma (CAIR) and distributed by De Vecchi, this cartoon was based on the famous children's book "The Adventures of Pinocchio" by Carlo Collodi.  The film was intended to be the first animated feature film from Italy, but was never completed; if the film was finished, it also would have been the first cel animated feature film ever, beating "Snow White and the Seven Dwarfs", and the first animated film adaptation based on the novel of the same name, It is now considered lost: only the original script and a couple of still frames are all that survived of the film.

Piccolino no Bōken: Piccolino no Bōken (ピコリーノの冒険 , Pikorīno no Bōken , lit.  "Adventures of Pinocchio") is a 52 episode anime series by Nippon Animation first aired in 1976.  The story is based on the novel "Pinocchio" by Italian author Carlo Collodi.

Buratino: Buratino (Russian: Буратино ) is the main character of the book "The Golden Key, or the Adventures of Buratino" (1936) by Aleksey Nikolayevich Tolstoy.  Based on the 1883 novel "The Adventures of Pinocchio" by Carlo Collodi, Buratino originated as a character in the commedia dell'arte.  The name Buratino is derived from the Italian "burattino", which means wooden puppet or doll.  The book was published in 1936, and Buratino quickly became hugely popular among children in the Soviet Union, and remains so to this day.  The story has been made into several films, including in 1959 and in 1975.

Jiminy Cricket: Jiminy Cricket is the Walt Disney version of The Talking Cricket (Italian: "Il Grillo Parlante" ), a fictional character created by Carlo Collodi for his children's book "The Adventures of Pinocchio", which Disney adapted into the animated film "Pinocchio" in 1940.  Originally an unnamed, minor character in Collodi's novel, he was transformed in the Disney version into a comical and wise partner who accompanies Pinocchio on his adventures, having been appointed by the Blue Fairy (known in the book as The Fairy with Turquoise Hair) to serve as Pinocchio's official conscience.  His design is different from real crickets, which are black or dark brown, with very long antennae.  Since his debut in "Pinocchio", he has become a recurring iconic Disney character and has made numerous other appearances.

The Adventures of Pinocchio: The Adventures of Pinocchio ( ; Italian: "Le avventure di Pinocchio" ] ) is a novel for children by Italian author Carlo Collodi, written in Pescia.  The first half was originally a serial in 1881 and 1882, published as "La storia di un burattino" (literally ""The tale of a puppet""), and then later completed as a book for children in February 1883.  It is about the mischievous adventures of an animated marionette named Pinocchio and his father, a poor woodcarver named Geppetto.

Carlo Collodi: Carlo Lorenzini, better known by the pen name Carlo Collodi (] ; 24 November 1826 – 26 October 1890), was a children's writer born in the Grand Duchy of Tuscany and writer of the world-renowned fairy tale novel "The Adventures of Pinocchio".

Question: What novel by Carlo Collodi had its first edition illustrated by Enrico Mazzanti?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "novel_title": {
      "type": "string",
      "description": "The title of the novel."
    },
    "author": {
      "type": "string",
      "description": "The author of the novel."
    },
    "illustrator": {
      "type": "string",
      "description": "The person who illustrated the first edition of the novel."
    },
    "edition_type": {
      "type": "string",
      "description": "The specific edition that was illustrated."
    }
  },
  "required": [
    "novel_title",
    "author",
    "illustrator",
    "edition_type"
  ],
  "additionalProperties": false
}

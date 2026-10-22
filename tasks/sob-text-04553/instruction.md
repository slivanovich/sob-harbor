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
Saad Z Hossain: Saad Z Hossain is a Bangladeshi author writing in English.  His war satire, "Escape from Baghdad!" , was published in 2015 by Unnamed Press in the US, and Aleph in India.  It is currently being translated into French.

Accent kernel: Accent was an operating system kernel developed at Carnegie Mellon University (CMU).  Accent was developed as a follow-on to the Aleph kernel developed at the University of Rochester, fixing several of its problems and re-targeting its hardware support for networks of workstation machines (specifically, the Three Rivers PERQ) instead of minicomputers. Accent was part of the SPICE Project at CMU which ran from 1981 to 1985.  Development of Accent led directly to the famous Mach kernel.

The Aleph (short story): "The Aleph" is a short story by the Argentine writer and poet Jorge Luis Borges.  First published in September 1945, it was reprinted in the short story collection, "The Aleph and Other Stories", in 1949, and revised by the author in 1974.

Hamza: Hamza (Arabic: همزة‎ ‎ , "hamzah ") (ء ) is a letter in the Arabic alphabet, representing the glottal stop ʔ] .  Hamza is not one of the 28 "full" letters, and owes its existence to historical inconsistencies in the standard writing system.  It is derived from the Arabic letter "‘ayn ".  In the Phoenician and Aramaic alphabets, from which the Arabic alphabet is descended, the glottal stop was expressed by "aleph" (), continued by "alif" (  ) in the Arabic alphabet.  However, alif was used to express both a glottal stop and a long vowel /aː/ .  To indicate that a glottal stop, and not a mere vowel, was intended, hamza was added diacritically to alif.  In modern orthography, under certain circumstances, hamza may also appear on the line, as if it were a full letter, independent of an alif.

Paulo Coelho: Paulo Coelho de Souza ( , , , ] ; born August 24, 1947) is a Brazilian lyricist and novelist and the recipient of numerous international awards.  He is best known for his widely translated novel "The Alchemist".  He is the writer with the highest number of social media followers reaching over 29.5 million fans through his Facebook page and 12.2 million followers on Twitter .  A keen user of electronic media, in 2014 he uploaded his personal papers online to create a virtual Paulo Coelho Foundation.

Harto The Borges: Harto The Borges is a documentary film by Eduardo Montes-Bradley.  "Harto The Borges" explores the narcissistic side of Jorge Luis Borges, the author of El Aleph, his frequent and often criticized comments to the press, his distinctive and gentle ironies.  Harto The Borges had a theatrical release in Buenos Aires in September 2000, and was well received by the critics.  Since then has been frequently exhibited at forums, campuses, and film festivals.  On October 4, 2011, Harto The Borges was made available to the general audience in Argentina through the On Line version of Revista Cultura Ñ, (Diario Clarin) in Buenos Aires.  The film was released alongside an article in which the director views the film ten years after its premier at the Cine Cosmos.  The film is currently available in Vimeo .

Aleph (novel): Aleph is a 2011 novel by the Brazilian writer Paulo Coelho.  It is the fourteenth major book by Coelho, and touches on the theme of spirituality.  "Aleph" was written in Coelho's native language, Portuguese.  Under the sentence "Some books are read.  "Aleph" is lived", the book is an autobiographical account written in a novel format.  Upon release it became a bestselling novel in Brazil.

David Davidar: David Davidar (born 27 September 1958) is an Indian novelist and publisher.  He is the author of three published novels, "The House of Blue Mangoes" (2002), "The Solitude of Emperors" (2007) and "Ithaca" (2011).  In parallel to his writing career, Davidar has been a publisher for a quarter century.  He is the co-founder of Aleph Book Company, a literary publishing firm based in New Delhi.

The Writing of the God: "The Writing of the God" (original Spanish title: "La escritura del dios") is a short story by Argentinian writer Jorge Luis Borges.  It was published in "Sur" in February 1949, and later reprinted in the collection "The Aleph".

Jorge Luis Borges and mathematics: Jorge Luis Borges and mathematics concerns several modern mathematical concepts found in certain essays and short stories of Argentinian author Jorge Luis Borges (1899-1986), including concepts such as set theory, recursion, chaos theory, and infinite sequences, although Borges' strongest links to mathematics are through Georg Cantor's theory of infinite sets, outlined in "The Doctrine of Cycles" ("La doctrina de los ciclos").  Some of Borges' most popular works such as "The Library of Babel" ("La Biblioteca de Babel"), "The Garden of Forking Paths" ("El Jardín de Senderos que se Bifurcan"), "The Aleph" ("El Aleph"), an allusion to Cantor's use of the Hebrew letter aleph (formula_1) to denote cardinality of transfinite sets.  and "The Approach to Al-Mu'tasim" ("El acercamiento a Almotásim") illustrate his use of mathematics.

Question: What is the author of Aleph most famous for writing?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "author_name": {
      "type": "string",
      "description": "The name of the author of the book mentioned in the question."
    },
    "book_in_question": {
      "type": "string",
      "description": "The title of the book from the question."
    },
    "most_famous_work": {
      "type": "string",
      "description": "The title of the author's most famous work."
    },
    "author_nationality": {
      "type": "string",
      "description": "The nationality of the author."
    }
  },
  "required": [
    "author_name",
    "book_in_question",
    "most_famous_work",
    "author_nationality"
  ],
  "additionalProperties": false
}

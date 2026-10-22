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
Morten Tyldum: Morten Tyldum (born 19 May 1967) is a Norwegian film director.  He is best known for directing internationally successful films such as "Headhunters" (2011), a thriller based on a novel by Jo Nesbø, and "The Imitation Game" (2014), a historical drama for which he was nominated for the Academy Award for Best Director.

The Leopard (Nesbø novel): The Leopard is a crime novel by Norwegian novelist, Jo Nesbø.  Its Norwegian title is "Panserhjerte", which does not directly translate to The Leopard; it rather means something along the lines of "armoured heart".  Moreover, "leopard" refers to the stealthy tread of the killer in the book, while "armoured heart" is what Harry Hole himself gains by his experiences.  "Panserhjerte" is also a Norwegian term for Constrictive pericarditis.  "The Leopard" is the eighth novel featuring Nesbø's crime detective, Inspector Harry Hole.

Phantom (Nesbø novel): Phantom is a crime novel by Norwegian novelist Jo Nesbø, published jn 2012.  Its Norwegian title is "Gjenferd", which does not directly translate to "Phantom"; rather it translates to a word similar to "ghosts".  "Phantom" is the ninth novel featuring crime detective Inspector Harry Hole.

The Son (Nesbø novel): The Son (Norwegian: "Sønnen" , 2014) is a crime novel by Norwegian novelist Jo Nesbø.  It is the second stand-alone crime novel by Nesbø, following "Headhunters" (2008).

Harry Hole: Harry Hole (pronounced "Harry HOO-LEH") is the main character in a series of crime novels written by Norwegian author Jo Nesbø.  Hole is a brilliant and driven detective with unorthodox methods, a classic loose cannon in the police force.  Critics liken the personality of Harry Hole to those of the famous literary detectives: Sherlock Holmes, Hercule Poirot, Jules Maigret, and Nero Wolfe.

Bokvennen litterært magasin: Bokvennen litterært magasin is a Norwegian literary magazine, established in 1989 by Jan M. Claussen.  The magazine publishes articles, essays, poetry and short fiction from both Norwegian and international writers.  Four paper editions are issued annually.  "Bokvennen" was in 2011 awarded the Magazine of the Year Award in Norway and also honored as the best cultural magazine in the Nordic countries at the Copenhagen book fair Bogforum.  The Norwegian Broadcasting Corporation named "Bokvennen" Norway´s best literary magazine in 2010.  Many contemporary authors have been interviewed or presented in Bokvennen, among others Elfriede Jelinek, Dave Eggers, Mircea Cărtărescu, Benjamin Kunkel, Péter Nádas, Jean Echenoz, Michael Cera, Junot Díaz, J. M. Coetzee, Joyce Carol Oates, Miranda July, Nam Le, Alberto Manguel, Nadine Gordimer, Gary Snyder, Michael Chabon, Uwe Tellkamp, Sara Stridsberg, Linn Ullmann, Jon Fosse, Jo Nesbø, Johan Harstad and Karl Ove Knausgård.  The editor-in-chief from 2010 to 2014 was literary critic Gabriel Vosgraff Moro.  The editor-in-chief from 2015 is journalist and writer Alberte Bremberg.  Editorial board: Lene Ask, Mari Nymoen Nilsen, Thea Marie Dolva, Tina Åmodt.  "Bokvennen" is supported by the Cultural Council of Norway and the foundation Fritt Ord.

Yellow Bird (company): Yellow Bird is a Swedish film and television production company.  In 2003 Danish producer Ole Søndberg and Swedish author Henning Mankell started a collaboration on a series of television films based on Mankell’s famous fictional detective Kurt Wallander and Yellow Bird was born.  The success of the initial Wallander films was followed by Stieg Larsson’s worldwide phenomena, the Millennium trilogy, Jo Nesbø’s Headhunters, Liza Marklund’s Annika Bengtzon series as well as the British version of Wallander starring Kenneth Branagh.

Police (Nesbø novel): Police (Norwegian: "Politi" , 2013) is a crime novel by Norwegian novelist Jo Nesbø.  It is the tenth novel in Nesbø's Harry Hole series.

Jo Nesbø: Jo Nesbø (] ; born 29 March 1960) is a Norwegian writer, musician, former economist and reporter.  As of March 2014 more than 3 million copies of his novels have been sold in Norway, and his work has been translated into over 40 languages, selling 30 million copies worldwide.  Nesbø is primarily known for his crime novels about Inspector Harry Hole, but he is also the main vocalist and songwriter for the Norwegian rock band Di Derre.  In 2007 Nesbø also released his first children's book, "Doktor Proktors Prompepulver" (English translation: "Doctor Proctor's Fart Powder").  The 2011 film "Headhunters" is based on Nesbø's novel "Hodejegerne (The Headhunters)".

Restaurant Schrøder: Restaurant Schrøder is a restaurant in Waldemar Thranes gate 8 at St. Hanshaugen in Oslo, Norway.  This restaurant appeared in several fictional works including Jo Nesbø's books about Harry Hole and several books by Bjørg Vik.

Question: Jo Nesbø primary known for writing about a particular detective, who is it critic liken his personality to? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "author_name": {
      "type": "string",
      "description": "The name of the author."
    },
    "primary_detective": {
      "type": "string",
      "description": "The name of the detective the author is primarily known for."
    },
    "critic_comparisons": {
      "type": "array",
      "description": "A list of famous literary detectives whose personalities critics liken to the primary detective.",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "author_name",
    "primary_detective",
    "critic_comparisons"
  ],
  "additionalProperties": false
}

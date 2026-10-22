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
Manifesto of the Sixteen: The Manifesto of the Sixteen (French: "Manifeste des seize" ), or Proclamation of the Sixteen, was a document drafted in 1916 by eminent anarchists Peter Kropotkin and Jean Grave which advocated an Allied victory over Germany and the Central Powers during the First World War.  At the outbreak of the war, Kropotkin and other anarchist supporters of the Allied cause advocated their position in the pages of the "Freedom" newspaper, provoking sharply critical responses.  As the war continued, anarchists across Europe campaigned in anti-war movements and wrote denunciations of the war in pamphlets and statements, including one February 1916 statement signed by prominent anarchists such as Emma Goldman and Rudolf Rocker.

Oulipo: Oulipo (] , short for French: "Ouvroir de littérature potentielle" ; roughly translated: ""workshop of potential literature"") is a loose gathering of (mainly) French-speaking writers and mathematicians who seek to create works using constrained writing techniques.  It was founded in 1960 by Raymond Queneau and François Le Lionnais.  Other notable members have included novelists Georges Perec and Italo Calvino, poets Oskar Pastior, Jean Lescure and poet/mathematician Jacques Roubaud.

François Le Vau: François Le Vau was a French Late Baroque and Neoclassical architect.

François Le Levé: François Le Levé (1882-1945), was born in Locmiquélic, Morbihan.  Militant anarcho-syndicalist.  Le Levé was one of fifteen anarchists who signed The "Manifesto of the Sixteen", along with Peter Kropotkin, Jean Grave and others, favoring the Allies during World War I.  (Overwhelmingly, anarchists refused to take sides, opposing the killing in favor of class war; see, for example, Errico Malatesta.)

Klaas's cuckoo: The Klaas's cuckoo ("Chrysococcyx klaas") is a species of cuckoo in the family Cuculidae which is native to the wooded regions of sub-Saharan Africa.  The species was named by French explorer François Le Vaillant after his Khoikhoi servant.  Le Vaillant was the only colonial biologist to name some bird species after local people.

François Le Roux: François Le Roux (born 30 October 1955) is a French baritone.  Le Roux began vocal studies at 19 with François Loup, winning prizes in Barcelona and Rio de Janeiro.  He was a member of the Lyon Opera Company from 1980 to 1985, before appearing in many international houses, making his Paris Opéra debut in 1988 as Valentin in Gounod's "Faust".  He is most renowned for his portrayal of Pelléas in Debussy's opera, first singing the role in 1985 and being hailed by critics as "the greatest Pelléas of his generation".  Since 1998 he has also sung Golaud in the same opera to similar acclaim.  It was as Golaud he sang in the centenary performance at the Opéra-Comique, and also in the Russian national premiere.  He voiced Gaston, the villainous hunter in the European French dub of Disney's "Beauty and the Beast (1991 film).

Cape Town French School: The Cape Town French School or the François Le Vaillant French School (French: École française du Cap "François Le Vaillant" ) is a French international school in Cape Town, South Africa.

François Lemoyne: François Lemoyne or François Le Moine (1688 – 4 June 1737) was a French rococo painter, born in Paris.  In 1701, when he was 13 years old, he entered the Académie de peinture et de sculpture.  He studied under Louis Galloche and stayed until 1713.  In 1711, Lemoyne won the Prix de Rome.  He was accepted as a member of the Académie in 1718 and was elected as a professor in 1733.

François Le Diascorn: François Le Diascorn (Born January 10, 1947 at La Flèche, near Mans, Sarthe "département") is a French photographer, close to the humanist school, who has developed a poetic vision of the world through his unusual images in which a dream-like world seems to superimpose itself upon reality.

André le Breton: André François le Breton (2 September 1708 – 5 October 1779) was a French publisher.  He was one of the four publishers of the "Encyclopédie" of Diderot and d'Alembert, along with Michel-Antoine David, Laurent Durand, and Antoine-Claude Briasson.  Le Breton contributed some articles to the "Encyclopédie" (see External links, below), but acted primarily as publisher and editor, often against Diderot's will.

Question: Which document did François Le Levé sign in 1916?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "document_name": {
      "type": "string",
      "description": "The name of the document signed."
    },
    "signer_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the person who signed the document."
        },
        "role": {
          "type": "string",
          "description": "The role or affiliation of the signer."
        }
      },
      "required": [
        "name",
        "role"
      ],
      "additionalProperties": false
    },
    "year_signed": {
      "type": "integer",
      "description": "The year the document was signed or drafted."
    },
    "document_purpose": {
      "type": "string",
      "description": "The main purpose or advocacy of the document."
    },
    "other_notable_signers": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Other prominent individuals who signed the document."
    }
  },
  "required": [
    "document_name",
    "signer_details",
    "year_signed",
    "document_purpose"
  ],
  "additionalProperties": false
}

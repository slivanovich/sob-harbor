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
Peking Man: Peking Man (), "Homo erectus pekinensis" (formerly known by the junior synonym "Sinanthropus pekinensis"), is an example of "Homo erectus".  Discovered in 1923–27 during excavations at Zhoukoudian (Chou K'ou-tien) near Beijing (written "Peking" before the adoption of the Pinyin romanization system), China, in 2009 this group of fossil specimens dated from roughly 750,000 years ago, and a new Al/Be dating suggests they are in the range of 680,000–780,000 years old.

Mauer 1: The Mauer 1 mandible is the oldest known specimen of the genus "Homo" in Germany.  It was found in 1907 in a sand mine in the community Mauer, around 10 km south-east of Heidelberg.  The Mauer 1 mandible is the type specimen of the species "Homo heidelbergensis".  Some European researchers have classified the find as "Homo erectus heidelbergensis", regarding it as a subspecies of "Homo erectus".  In 2010 the mandible's age was for the first time exactly determined to be 609,000 ± 40,000 years.  Previously, specialist literature had referred to an age of either 600,000 or 500,000 years on the basis of less accurate dating methods.

Nanjing Man: Nanjing Man (Homo erectus nankinensis) is a subspecies of "Homo erectus" found in China.  Large fragments of one male and one female skull and a molar tooth of "H. e. nankinensis "were discovered in 1993 in the Hulu cave on the Tangshan hills near Nanjing, the former capital city of China.  The term Nanjing man is used to describe the subspecies of "Homo erectus" but is also used when referring to the three fossils.  The specimens were found in the Hulu limestone cave at a depth of 60-97 cm by Liu Luhong, a local worker.  Dating the fossils yielded an estimated age of 580,000 to 620,000 years old.

Homo ergaster: Homo ergaster (meaning "working man") or African "Homo erectus" is an extinct chronospecies of the genus "Homo" that lived in eastern and southern Africa during the early Pleistocene, that is, between 1.9 million and 1.4 million years ago.  It is one of the earliest hominins, which are those hominids that comprise the original members and species of the human clade after splitting from the line of the chimpanzees.  "Homo ergaster" is variously thought to be ancestral to, or as sharing a common ancestor with, or as being the same species as, "Homo erectus".

Solo Man: Solo Man ("Homo erectus soloensis") was formerly classified as "Homo sapiens soloensis" and is now regarded as a subspecies of the extinct hominin, "Homo erectus".  Discovered between 1931 and 1933 by Gustav Heinrich Ralph von Koenigswald, the only known specimens of this anomalous hominid were retrieved from sites along the Solo River, on the Indonesian island of Java.  The remains are also commonly referred to as Ngandong (now at Kradenan district, Blora Regency), after the village near where they were first recovered.

Atapuerca Mountains: The Atapuerca Mountains (Spanish: "Sierra de Atapuerca" ) is a karstic hill formation near the village of Atapuerca in Castile and León, northern Spain.  In a still ongoing excavation campaign rich fossil deposits and stone tool assemblages were discovered in the complex of local caves that are attributed to the earliest known hominin residents in Western Europe.  This "exceptional reserve of data" has been deposited during extensive Lower Paleolithic presence as the Atapuerca Mountains served as the preferred occupation site of "Homo erectus", "Homo antecessor" (or "Homo erectus antecessor") and "Homo heidelbergensis" communities.  The earliest specimen yet unearthed and reliably dated confirm an age between 1.2 Million and 600,000 years.  The site was designated a UNESCO World Heritage Site, under the name, "Archaeological Site of Atapuerca".

Tautavel Man: Tautavel Man ("Homo erectus tautavelensis") is a proposed subspecies of the hominid "Homo erectus", the 450,000-year-old fossil remains of whom were discovered in the Arago Cave in Tautavel, France.  Excavations began in 1964, with the first notable discovery occurring in 1969.

Homo Erectus (film): Homo Erectus (released on DVD in the United States as National Lampoon's Stoned Age) is a 2007 comedy film written and directed by Adam Rifkin, and starring Giuseppe Andrews, Gary Busey, David Carradine, Ron Jeremy, Ali Larter, Hayes MacArthur, Adam Rifkin, and Talia Shire.  The film premiered at the 2007 Slamdance Film Festival in January 2007.

Samu (Homo erectus): Samu is the nickname given to a prehistoric man (described as "Homo erectus seu sapiens palaeohungaricus", i. e., "ancient Hungarian Homo erectus or sapiens") whose remains were found in 1964 near Vértesszőlős, Hungary.  He was a late "Homo erectus", somewhere between "Homo erectus" and "Homo neanderthalensis".  Only a part of the occipital bone was found.  He lived about 350,000 years ago.

Giuseppe Andrews: Giuseppe Andrews (born Joey Murcia; April 25, 1979) is an American film actor, writer, and director known for his roles as Lex in the 1999 film "Detroit Rock City", a bizarre sheriff's deputy in "Cabin Fever" (2002), a small role in "Never Been Kissed" (1999), as well as appearances in The Smashing Pumpkins videos "1979" and "Perfect".

Question: Before the film Homo Erectus, Giuseppe Andrews played a deputy in what film

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor."
    },
    "film_before_homo_erectus": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film where the actor played a deputy."
        },
        "role": {
          "type": "string",
          "description": "The specific role played by the actor in the film."
        },
        "release_year": {
          "type": "integer",
          "description": "The release year of the film."
        }
      },
      "required": [
        "title",
        "role",
        "release_year"
      ],
      "additionalProperties": false
    },
    "homo_erectus_film_release_year": {
      "type": "integer",
      "description": "The release year of the 'Homo Erectus' film for chronological context."
    }
  },
  "required": [
    "actor_name",
    "film_before_homo_erectus",
    "homo_erectus_film_release_year"
  ],
  "additionalProperties": false
}

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
Dinosaur: Dinosaurs are a diverse group of reptiles of the clade Dinosauria that first appeared during the Triassic period.  Although the exact origin and timing of the evolution of dinosaurs is the subject of active research, the current scientific consensus places their origin between 231 and 243 million years ago.  They became the dominant terrestrial vertebrates after the Triassic–Jurassic extinction event 201 million years ago.  Their dominance continued through the Jurassic and Cretaceous periods and ended when the Cretaceous–Paleogene extinction event led to the extinction of most dinosaur groups 66 million years ago.

Bayan Shireh Formation: The Bayan Shireh Formation (also known as Bayanshiree Svita or the Baynshirenskaya Formation) is a geological formation in Burkhant, Mongolia, that dates to the late Cretaceous period.  The exact age is uncertain, with two competing hypotheses; based on comparisons with other formations, the Bayan Shireh fauna seems to correspond best with the Turonian through early Campanian stages of the Late Cretaceous, about 93 to 80 million years ago.  However, examination of the magnetostratigraphy of the formation seems to confirm that the entire Bayan Shireh lies within the Cretaceous Long Normal, which lasted only until the end of the Santonian stage, giving a possible Cenomanian through Santonian age, or between 98 and 83 million years ago.  The fauna of this formation is similar to the nearby Iren Dabasu Formation.

Judith River Formation: The Judith River Formation is a fossil-bearing geologic formation in Montana, and is part of the Judith River Group.  It dates to the upper Cretaceous, between 80 and 75 million years ago, corresponding to the "Judithian" land vertebrate age.  It was laid down during the same time period as portions of the Two Medicine Formation of Montana and the Oldman Formation of Alberta.

Palintropus: Palintropus is a prehistoric bird genus from the Late Cretaceous.  A single species has been named (Palintropus retusus) based on a proximal coracoid from the Lance Formation of Wyoming, dated to the latest Maastrichtian, round 5 million years ago.  Coracoids and a proximal scapula of two unnamed species from the upper Campanian Dinosaur Park Formation of Alberta, dating to between 76.5 and 75 million years ago, are also known.

Chaotian (geology): In the geologic record the Chaotian eon or era is unofficially proposed to denote the time preceding the solidification of the Earth's crust and the formation of Earth's moon, it is the earliest era within the eon of Hadean.  It lasted 196 million years, at   million years ago to the beginning of the Zirconian era,   million years ago .  It is named after Chaos, the primeval void in Greek mythology.  The Chaotian sets in with the emergence of Earth at 4.6 billion years ago.  Its upper limit and thus the transition to the Zirconian era is defined by the occurrence of the first conservation capable mineral.  These are zircon, the oldest mineral in the Jack Hills of Narryer Gneiss Terrane in Western Australia (Yilgarn craton) found and were dated 4,404 ± 8 million years ago

Paranthodon: Paranthodon ( ) is a genus of extinct stegosaurian dinosaur that lived in South Africa during the Early Cretaceous, between 145.5 and 136.4 million years ago.  Discovered in 1845, it was one of the first stegosaurians found.  Its only remains, a partial skull and isolated teeth, were found in the Kirkwood Formation.  British paleontologist Richard Owen initially identified the fragments as those of the pareiasaur "Anthodon".  After remaining untouched for years in the British Museum of Natural History, the partial skull was identified by South African paleontologist Robert Broom as belonging to a different genus; he named the specimen "Palaeoscincus africanus".  Several years later, Hungarian paleontologist Franz Nopcsa, unaware of Broom's new name, similarly concluded that it represented a new taxon, and named it "Paranthodon owenii".  Since Nopcsa's species name was assigned after Broom's, and Broom did not assign a new genus, both names are now synonyms of the current binomial, "Paranthodon africanus".  The genus name combines the Ancient Greek "para" (near) with the genus name "Anthodon", to represent the initial referral of the remains.

Sinornithosaurus: Sinornithosaurus (derived from a combination of Latin and Greek, meaning 'Chinese bird-lizard') is a genus of feathered dromaeosaurid dinosaur from the early Cretaceous Period (early Aptian) of the Yixian Formation in what is now China.  It was the fifth non–avian feathered dinosaur genus discovered by 1999.  The original specimen was collected from the Sihetun locality of western Liaoning.  It was found in the Jianshangou beds of the Yixian Formation, dated to 124.5 million years ago.  Additional specimens have been found in the younger Dawangzhangzi bed, dating to around 122 million years ago.

Evolution of insects: The most recent understanding of the evolution of insects is based on studies of the following branches of science: molecular biology, insect morphology, paleontology, insect taxonomy, evolution, embryology, bioinformatics and scientific computing.  It is estimated that the class of insects originated on Earth about 480 million years ago, in the Ordovician, at about the same time terrestrial plants appeared.  Insects evolved from a group of crustaceans.  The first insects were land bound, but about 400 million years ago in the Devonian period one lineage of insects evolved flight, the first animals to do so.  The oldest definitive insect fossil, "Rhyniognatha hirsti", is estimated to be  396 .  Global climate conditions changed several times during the history of Earth, and along with it the diversity of insects.  The Pterygotes (winged insects) underwent a major radiation in the Carboniferous (356 to 299 million years ago) while the Endopterygota (insects that go through different life stages with metamorphosis) underwent another major radiation in the Permian (299 to 252 million years ago).

Cimolopterygidae: Cimolopterygidae is a group of extinct birds known from the late Cretaceous Period.  Remains attributed to cimolopterygids have been found in the Frenchman Formation of Saskatchewan, the Lance Formation of Wyoming, the Fox Hills Formation of Colorado, the Hell Creek Formation of Montana, and the Allen Formation of Rio Negro, Argentina.  Most date to the end of the Maastrichtian age, about round 5 million years ago, though a much earlier species has also been identified from the Campanian-aged Dinosaur Park Formation of Alberta, about 75 million years ago.

Palaeoscincus: Palaeoscincus (meaning "ancient skink" from the Greek παλαιός and σκίγγος) is a dubious genus of ankylosaurian dinosaur based on teeth from the mid-late Campanian-age Upper Cretaceous Judith River Formation of Montana.  Like several other dinosaur genera named by Joseph Leidy ("Deinodon", "Thespesius", and "Trachodon"), it is an historically important genus with a convoluted taxonomy that has been all but abandoned by modern dinosaur paleontologists. Because of its wide use in the early 20th century, it was somewhat well-known to the general public, often through illustrations of an animal with the armor of "Edmontonia" and the tail club of an ankylosaurid.

Question: Palaeoscincus is a genus of dinosaur based on what upper Cetaceous Formation from 80 - 75 million years ago?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "dinosaur_genus": {
      "type": "string",
      "description": "The name of the dinosaur genus."
    },
    "geological_formation": {
      "type": "string",
      "description": "The name of the geological formation where the dinosaur remains were found."
    },
    "formation_location": {
      "type": "string",
      "description": "The geographical location of the formation."
    },
    "formation_period": {
      "type": "string",
      "description": "The geological period to which the formation dates."
    },
    "formation_age_range_mya": {
      "type": "object",
      "properties": {
        "start_mya": {
          "type": "integer",
          "description": "The start age of the formation in million years ago."
        },
        "end_mya": {
          "type": "integer",
          "description": "The end age of the formation in million years ago."
        }
      },
      "required": [
        "start_mya",
        "end_mya"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "dinosaur_genus",
    "geological_formation",
    "formation_location",
    "formation_period",
    "formation_age_range_mya"
  ],
  "additionalProperties": false
}

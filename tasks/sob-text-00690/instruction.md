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
List of placental mammals: List of placental mammals contains the placental mammals.  The class Mammalia (mammals) is divided into two subclasses based on reproductive techniques: Monotremes, which lay eggs, and therians, mammals which give live birth, which has two infraclasses: Marsupials, pouched mammals and placental mammals.  See List of monotremes and marsupials, and for the clades and families, see mammal classification.  Classification updated from Wilson and Reeder's using the "Planet' Mammifères website.

Apatemyidae: Apatemyidae is an extinct family of placental mammals that took part in the first placental evolutionary radiation together with other early mammals such as the leptictids.

List of monotremes and marsupials: The class Mammalia (mammals) is divided into two subclasses based on reproductive techniques: egg-laying mammals (yinotherians or monotremes - see also Australosphenida), and mammals which give live birth (therians).  The latter subclass is divided into two infraclasses: pouched mammals (therians or marsupials), and placental mammals (eutherians, for which see List of placental mammals).  Classification updated from Wilson and Reeder's "Mammal Species of the World: A Taxonomic and Geographic Reference" using the "Planet Mammifères" website.

X-inactivation: X-inactivation (also called lyonization) is a process by which one of the copies of the X chromosome present in female mammals is inactivated.  The inactive X chromosome is silenced by its being packaged in such a way that it has a transcriptionally inactive structure called heterochromatin.  As nearly all female mammals have two X chromosomes, X-inactivation prevents them from having twice as many X chromosome gene products as males, who only possess a single copy of the X chromosome (see dosage compensation).  The choice of which X chromosome will be inactivated is random in placental mammals such as humans, but once an X chromosome is inactivated it will remain inactive throughout the lifetime of the cell and its descendants in the organism.  Unlike the random X-inactivation in placental mammals, inactivation in marsupials applies exclusively to the paternally derived X chromosome.

Mesozoic mammals of Madagascar: Several mammals are known from the Mesozoic of Madagascar.  The Bathonian (middle Jurassic) "Ambondro", known from a piece of jaw with three teeth, is the earliest known mammal with molars showing the modern, tribosphenic pattern that is characteristic of marsupial and placental mammals.  Interpretations of its affinities have differed; one proposal places it in a group known as Australosphenida with other Mesozoic tribosphenic mammals from the southern continents (Gondwana) as well as the monotremes, while others favor closer affinities with northern (Laurasian) tribosphenic mammals or specifically with placentals.  At least five species are known from the Maastrichtian (late Cretaceous), including a yet undescribed species known from a nearly complete skeleton that may represent a completely new group of mammals.  The gondwanathere "Lavanify", known from two teeth, is most closely related to other gondwanatheres found in India and Argentina.  Two other teeth may represent another gondwanathere or a different kind of mammal.  One molar fragment is one of the few known remains of a multituberculate mammal from Gondwana and another (UA 8699) has been interpreted as either a marsupial or a placental.

List of mammals of Tasmania: Tasmanian mammals are divided into three major groups based on reproductive techniques: egg laying mammals (the monotremes), pouched mammals (the marsupials), and placental mammals.  This is a list of mammals of Tasmania:

Evolution of sirenians: Sirenia is the order of placental mammals which comprises modern "sea cows" (manatees and the Dugong) and their extinct relatives.  They are the only extant herbivorous marine mammals and the only group of herbivorous mammals to have become completely aquatic.  Sirenians are thought to have a 50-million-year-old fossil record (early Eocene-recent).  They attained modest diversity during the Oligocene and Miocene, but have since declined as a result of climatic cooling, oceanographic changes, and human interference.  Two genera and four species are extant: "Trichechus", which includes the three species of manatee that live along the Atlantic coasts and in rivers and coastlines of the Americas and western Africa, and "Dugong", which is found in the Indian and Pacific oceans.

Dugong: The dugong ( , ; "Dugong dugon") is a medium-sized marine mammal.  It is one of four living species of the order Sirenia, which also includes three species of manatees.  It is the only living representative of the once-diverse family Dugongidae; its closest modern relative, Steller's sea cow ("Hydrodamalis gigas"), was hunted to extinction in the 18th century.  The dugong is the only strictly marine herbivorous mammal.

Leptictida: Leptictida ("leptos iktis" "small/slender weasel") is a possibly invalid extinct order of placental mammals.  Their classification is contentious: according to cladistic studies, they may be (distantly) related to Euarchontoglires (rodents, primates and their relatives), although they are more recently regarded as the first branch to split from basal eutherians.  One recent large-scale cladistic analysis of eutherian mammals favored lepictidans as close to the placental crown-clade; and several other recent analyses that included data from Cretaceous non-eutherian mammals found "Leptictis" to belong to the superorder Afrotheria

Fauna of Australia: The fauna of Australia consists of a huge variety of animals; some 83% of mammals, 89% of reptiles, 24% of fish and insects and 93% of amphibians that inhabit the continent are endemic to Australia.  This high level of endemism can be attributed to the continent's long geographic isolation, tectonic stability, and the effects of an unusual pattern of climate change on the soil and flora over geological time.  A unique feature of Australia's fauna is the relative scarcity of native placental mammals.  Consequently, the marsupials — a group of mammals that raise their young in a pouch, including the macropods, possums and dasyuromorphs — occupy many of the ecological niches placental animals occupy elsewhere in the world.  Australia is home to two of the five known extant species of monotremes and has numerous venomous species, which include the platypus, spiders, scorpions, octopus, jellyfish, molluscs, stonefish, and stingrays. Uniquely, Australia has more venomous than non-venomous species of snakes.

Question: What is the medium sized marine animal that is part of the order of placental mammals?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "animal_name": {
      "type": "string",
      "description": "The common name of the marine animal."
    },
    "mammal_type": {
      "type": "string",
      "description": "The classification of the mammal (e.g., placental, marsupial, monotreme)."
    },
    "order": {
      "type": "string",
      "description": "The taxonomic order to which the animal belongs."
    },
    "size_description": {
      "type": "string",
      "description": "A description of the animal's size."
    },
    "habitat": {
      "type": "string",
      "description": "The primary habitat of the animal."
    }
  },
  "required": [
    "animal_name",
    "mammal_type",
    "order",
    "size_description",
    "habitat"
  ],
  "additionalProperties": false
}

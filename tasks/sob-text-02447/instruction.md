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
Epibiont: An epibiont (from the Ancient Greek meaning "living on top of") is an organism that lives on the surface of another living organism.  An epibiont is, by definition, harmless to its host and in this sense, the relationship between the two organisms can be considered neutralistic or commensalistic (as opposed to, for example, parasitic, in which case one organism benefits at the expense of the other, or mutualistic, in which both organisms obtain some explicit benefit from their coexistence).  Although there is no direct effect of the epibiont to the host, there are often indirect effects resulting from this interaction and change in the surface of the host.  This has been found to be especially important to marine organisms and aquatic ecosystems as surface qualities do impact necessary ecological functions such as drag, radiation absorption, nutrient uptake etc.  Examples of common epibionts are barnacles, remoras and algae, many of which live on the surfaces of larger marine organisms such as whales, sharks, sea turtles and mangrove trees.  The host of the epibiont is typically referred to as the basibiont ("living underneath").

Anagallis: Anagallis is a genus of about 20–25 species of flowering plants in the family Primulaceae, commonly called pimpernel and perhaps best known for the scarlet pimpernel referred to in literature.  The botanical name is from the Greek, "ana", "again", and "agallein", "to delight in", and refers to the opening and closing of the flowers in response to environmental conditions.

Environmental DNA: Environmental DNA or eDNA is DNA that is collected from a variety of environmental samples such as soil, seawater, or even air rather than directly sampled from an individual organism.  As various organisms interact with the environment, DNA is expelled and accumulates in their surroundings.  Example sources of eDNA include, but are not limited to, feces, mucus, gametes, shed skin, carcasses and hair.  Such samples can be analyzed by high-throughput DNA sequencing methods, known as metagenomics, for rapid measurement and monitoring of biodiversity.  In order to better differentiate between organisms within a sample, DNA metabarcoding is used in which the sample is analyzed and uses previously studied DNA libraries to determine what organisms are present (e.g. BLAST).  The analysis of eDNA has great potential, not only for monitoring common species, but to genetically detect and identify other extant species that could influence conservation efforts.  This method allows for biomonitoring without requiring collection of the living organism, creating the ability to study organisms that are invasive, elusive, or endangered without introducing anthropogenic stress on the organism.  Access to this genetic information makes a critical contribution to the understanding of population size, species distribution, and population dynamics for species not well documented.  The integrity of eDNA samples is dependent upon its preservation within the environment.  Soil, permafrost, freshwater and seawater are well-studied macro environments from which eDNA samples have been extracted, each of which include many more conditioned subenvironments.  Because of its versatility, eDNA is applied in many subenvironments such as freshwater sampling, seawater sampling, terrestrial soil sampling (tundra permafrost), aquatic soil sampling (river, lake, pond, and ocean sediment), or other environments where normal sampling procedures can become problematic.

Sternbergia: Sternbergia is a genus of Eurasian and North African plants in the Amaryllis family, subfamily Amaryllidoideae.

Pharmacokinetics: Pharmacokinetics (from Ancient Greek "pharmakon" "drug" and "kinetikos" "moving, putting in motion"; see chemical kinetics), sometimes abbreviated as PK, is a branch of pharmacology dedicated to determining the fate of substances administered to a living organism.  The substances of interest include any chemical xenobiotic such as: pharmaceutical drugs, pesticides, food additives, cosmetic ingredients, etc.  It attempts to analyze chemical metabolism and to discover the fate of a chemical from the moment that it is administered up to the point at which it is completely eliminated from the body.  Pharmacokinetics is the study of how an organism affects a drug, whereas pharmacodynamics is the study of how the drug affects the organism.  Both together influence dosing, benefit, and adverse effects, as seen in PK/PD models.

Genetically modified organism: A genetically modified organism (GMO) is any organism whose genetic material has been altered using genetic engineering techniques (i.e., a genetically "engineered" organism).  GMOs are used to produce many medications and genetically modified foods and are widely used in scientific research and the production of other goods.  The term GMO is very close to the technical legal term, 'living modified organism', defined in the Cartagena Protocol on Biosafety, which regulates international trade in living GMOs (specifically, "any living organism that possesses a novel combination of genetic material obtained through the use of modern biotechnology").

Fish acute toxicity syndrome: Fish acute toxicity syndrome (FATS) is a set of common chemical and functional responses in fish resulting from a short-term, acute exposure to a lethal concentration of a toxicant, a chemical or material that can produce an unfavorable effect in a living organism.  By definition, modes of action are characterized by FATS because the combination of common responses that represent each fish acute toxicity syndrome characterize an adverse biological effect.  Therefore, toxicants that have the same mode of action elicit similar sets of responses in the organism and can be classified by the same fish acute toxicity syndrome.

Wigglesworthia glossinidia: Wigglesworthia glossinidia is a species of gram-negative bacteria which was isolated from the gut of the tsetse fly.  "W. glossinidia" is a bacterial endosymbiont of the tsetse fly.  Because of this relationship, "Wigglesworthia" has lost a large part of its genome and has one of the smallest known genomes of any living organism, consisting of a single chromosome of 700,000 bp and a plasmid of 5,200.  Together with "Buchnera aphidicola", "Wigglesworthia" has been the subject of genetic research into the minimal genome necessary for any living organism.  "Wigglesworthia" also synthesizes key B-complex vitamins which the tsetse fly does not get from its diet of blood.  Without the vitamins "Wigglesworthia" produces, the tsetse fly has greatly reduced growth and reproduction.  Since the tsetse fly is the primary vector of "Trypanosoma brucei", the pathogen that causes African trypanosomiasis, it has been suggested that "W. glossinidia" may one day be used to help control the spread of this disease.

Xenoestrogen: Xenoestrogens are a type of xenohormone that imitates estrogen.  They can be either synthetic or natural chemical compounds. Synthetic xenoestrogens are widely used industrial compounds, such as PCBs, BPA, and phthalates, which have estrogenic effects on a living organism even though they differ chemically from the estrogenic substances produced internally by the endocrine system of any organism.  Natural xenoestrogens include phytoestrogens which are plant-derived xenoestrogens.  Because the primary route of exposure to these compounds is by consumption of phytoestrogenic plants, they are sometimes called "dietary estrogens".  Mycoestrogens, estrogenic substances from fungi, are another type of xenoestrogen that are also considered mycotoxins.

Social organism: In sociology, the social organism is an ideological concept in which a society or social structure is viewed as a "living organism".  From this perspective, typically, the relation of social features, e.g. law, family, crime, etc., are examined as they interact with other features of society to meet social needs.  All elements of a society or social organism have a function that maintains the stability and cohesiveness of the organism.

Question: What type of living organism does Sternbergia and Anagallis have in common?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "organism_type": {
      "type": "string",
      "description": "The common type of living organism shared by the mentioned entities."
    },
    "organisms_mentioned": {
      "type": "array",
      "description": "A list of the specific organisms from the question.",
      "items": {
        "type": "string"
      }
    },
    "common_classification_source": {
      "type": "string",
      "description": "A brief explanation of where the common classification was found in the text."
    }
  },
  "required": [
    "organism_type",
    "organisms_mentioned",
    "common_classification_source"
  ],
  "additionalProperties": false
}

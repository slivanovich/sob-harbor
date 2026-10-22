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
Manxmouse: Manxmouse: The Mouse Who Knew No Fear is a 1968 children's novel by Paul Gallico.  The plot is an epic narrative of the adventures of a creature called a Manx Mouse as he meets and interacts with other people, climaxing in a meeting with a Manx cat who characters say is destined to eat him.

American Bobtail: The American Bobtail is an uncommon breed of domestic cat which was developed in the late 1960s.  It is most notable for its stubby "bobbed" tail about one-third to one-half the length of a normal cat's tail.  This is the result of a cat body type genetic mutation affecting the tail development, similar to that of a Manx cat.  The breed is not related to the Japanese Bobtail despite the similar name and physical type—the breeding programs are entirely unrelated, and the genetic mutation causing the bobbed tail are known to be different because the mutation causing the American Bobtail's tail is dominant, whereas the Japanese Bobtail tail mutation is recessive.

Peta (cat): Manninagh KateDhu, commonly known as Peta, was the Chief Mouser to the Cabinet Office of the United Kingdom government between 1964 and sometime between 1969 and 1976, and was the first female cat in that role.  She became the replacement to Peter III, who had died at the age of 16 in 1964.  After Peter III's death, the Lieutenant Governor of the Isle of Man, Sir Ronald Garvey, suggested that a Manx cat be his replacement, and sent Peta to the Cabinet.  She was noted to be lazy and loud, and by 1969, some civil servants tried to remove her from Cabinet, but this did not happen, because of the suspected bad publicity that this action would incur.  She was not heard of again, until a reply to a member of the public in 1976 revealed that she had retired to the home of a civil servant.  Her successor was Wilberforce, who became the next Chief Mouser in the 1970s.

Meyers Manx: The Meyers Manx dune buggy is a small recreationally-oriented automobile, designed initially for desert racing by Californian engineer, artist, boat builder and surfer Bruce F. Meyers.  It was produced by his Fountain Valley, California company, B. F. Meyers & Co. from 1964 to 1971, in the form of car kits applied to shortened chassis of Volkswagen Beetles.  The car line dominated dune racing in its time, breaking records immediately, and was eventually also released in street-oriented models, until the company's demise due to tax problems after Meyers's departure.  New vehicles inspired by the original Manx buggy have been produced by Meyers's re-founded operation, Meyers Manx, Inc., since 2000.  The name and cat logo of the brand derives from the Manx cat, by virtue of the tailless breed's and the shortened vehicle's truncated "stubbiness".

Cat body-type mutation: Cats, like all living organisms, occasionally have mutations that affect their body type.  Sometimes, these cat body-type mutations are striking enough that humans select for and perpetuate them.  This is not always in the best interests of the cat, as many of these mutations are harmful; some are even lethal in their homozygous form.

Extinct animals from the Isle of Man: Some animal species and breeds once existed on the Isle of Man but are now extinct.  Some plant species have also been included at the end of this article.  There are no known specimens of the following breeds of dog, cattle, pig, horse and sheep.  Today only the Manx cat, Manx Loaghtan, Manx robber fly, Isle of Man cabbage and Manx marvel tomato exist as native breeds / types of the Isle of Man.

Geodakyan's evolutionary theory of sex: Geodakyan Evolutionary Theory of Sex theory (ETS) (ETS) was proposed by Vigen Geodakyan in 1960-80s.  This theory has many components related to systemic effects in sex ratios, shapes of phenotypic distributions in male and female phenotypes, sex dimorphism, mutation rates in genotypes, sex differences in birth ratios, mortality rates, and in susceptibility to new diseases.  Geodakyan started working on the theory in 1965.  Two main hypotheses of this theory that complement each other are: the principle of conjugated subsystems and the theory of asynchronous evolution.  These hypotheses relate to the paradox of sexual reproduction and suggest an explanation of why sexual reproduction became the most common way of reproduction among three types of reproduction known in biology: asexual, hermaphrodite reproduction and sexual reproduction.  The paradox of sexual reproduction (discussed more on the page evolution of sexual reproduction) notes that Hermaphrodite reproduction gives the highest diversity of configurations and an easier mating process than bi-sexual reproduction (such as in humans, when half of the members (males) can’t reproduce and can only diversify the genes).  Since in bi-sexual reproduction members of species can mate only with the opposite sex, there are fewer opportunities for mating and a lower diversity of outcome of their gene recombinations, in comparison to hermaphrodites.  Meanwhile bisexual species still have to share food and other resources with members who don’t reproduce (males).  In spite of these disadvantages of bi-sexual reproduction, paradoxically, most plants and animals shifted from hermaphroditism and gonochorism to sexual dimorphism.  Why?  (Figure 1).  (for comparison of types of reproduction see the review: In 2001, Vladimir Iskrin began refining and expanding on Geodakyan's theory.

Manx cat: The Manx cat ( , in earlier times often spelled Manks), is a breed of domestic cat ("Felis catus") originating on the Isle of Man, with a naturally occurring mutation that shortens the tail.  Many Manx have a small stub of a tail, but Manx cats are best known as being entirely tailless; this is the most distinguishing characteristic of the breed, along with elongated hind legs and a rounded head.  Manx cats come in all coat colours and patterns, though all-white specimens are rare, and the coat range of the original stock was more limited.  Long-haired variants are sometimes considered a separate breed, the Cymric.  Manx are prized as skilled hunters, and thus have often been sought by farmers with rodent problems, and been a preferred ship's cat breed.  They are said to be social, tame and active.  An old local term for the cats on their home island is stubbin.  Manx have been exhibited in cat shows since the 1800s, with the first known breed standard published in 1903.

Shooting (association football): Shooting is easily the most common way for goals to be scored.  It is done using the feet; using the head, i.e. heading the ball, is the second most common way in which goals are scored.

BRCA mutation: A "BRCA" mutation is a mutation in either of the "BRCA1" and "BRCA2" genes, which are tumour suppressor genes.  Hundreds of different types of mutations in these genes have been identified, some of which have been determined to be harmful, while others have no proven impact.  Harmful mutations in these genes may produce a hereditary breast-ovarian cancer syndrome in affected persons.  Only 5-10% of breast cancer cases in women are attributed to "BRCA1" and "BRCA2" mutations (with "BRCA1" mutations being slightly more common than "BRCA2" mutations), but the impact on women with the gene mutation is more profound.  Women with harmful mutations in either "BRCA1" or "BRCA2" have a risk of breast cancer that is about five times the normal risk, and a risk of ovarian cancer that is about ten to thirty times normal.  The risk of breast and ovarian cancer is higher for women with a high-risk "BRCA1" mutation than with a "BRCA2" mutation.  Having a high-risk mutation does not guarantee that the woman will develop any type of cancer, or imply that any cancer that appears was actually caused by the mutation, rather than some other factor.

Question: What is the common way to distinguish the Manx cat because of the cat body-type mutation?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "cat_breed": {
      "type": "string",
      "description": "The name of the cat breed."
    },
    "mutation_type": {
      "type": "string",
      "description": "The type of genetic mutation affecting the cat."
    },
    "distinguishing_characteristic": {
      "type": "string",
      "description": "The primary physical characteristic that distinguishes the breed due to the mutation."
    },
    "is_most_distinguishing": {
      "type": "boolean",
      "description": "Indicates if this characteristic is considered the most distinguishing feature of the breed."
    }
  },
  "required": [
    "cat_breed",
    "mutation_type",
    "distinguishing_characteristic",
    "is_most_distinguishing"
  ],
  "additionalProperties": false
}

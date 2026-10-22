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
Welsh Springer Spaniel: The Welsh Springer Spaniel is a breed of dog and a member of the spaniel family.  Thought to be comparable to the old Land Spaniel, they are similar to the English Springer Spaniel and historically have been referred to as both the Welsh Spaniel and the Welsh Cocker Spaniel.  They were relatively unknown until a succession of victories in dog trials by the breed increased its popularity.  Following recognition by The Kennel Club in 1902, the breed gained the modern name of Welsh Springer Spaniel.  The breed's coat only comes in a single colour combination of white with red markings, usually in a piebald pattern.  Loyal and affectionate, they can become very attached to family members and are wary of strangers.  Health conditions are limited to those common among many breeds of dog, although they are affected more than average by hip dysplasia and some eye conditions.  They are a working dog, bred for hunting, and while not as rare as some varieties of spaniel, they are rarer than the more widely known English Springer Spaniel with which they are sometimes confused.

Scienter: The scienter action is a category within [tort] law in some[common law] jurisdictions which deals with the damage done by an animal directly to a human.  It had a long history in English law, although it was abolished by the [Animals Act 1971].  An action in those common law jurisdictions where it has not been extinguished by statute, is in addition to the torts of negligence and nuisance, or more bespoke torts like cattle trespass.  Where an animal is known to behave in a certain way, and that is expressed on a person causing injury, an action can be taken in this tort.  This tort is not available in New South Wales, The Australian Capital Territory, South Australia or New Zealand.  In these jurisdictions the actions involving animals need to be in nuisance or negligence.  To be successful the plaintiff needs to take action against the person in control of the animal, and it is strict liability, requiring no more than proof of injury, that the animal had a problematic trait, and the person in control knew about the trait in the animal.  Being strict liability, there is no need to argue fault in the form of wilful intent or negligence on the part of the animal or its controller.  The only defence is if it can be proved the plaintiff voluntarily assumed the risk of injury by their actions, or if the plaintiff was the cause of the injury.  It is common to distinguish between harmless animals and wild animals.  No scienter is needed for wild animals.  Animals are classed as wild or harmless on the basis of species or kind, not on the basis of being a tame individual.  An elephant is considered wild irrespective of its use.  The scienter action is referred to in Rylands v. Fletcher in that one who keeps a wild thing “must keep it at his peril” to make reference to part of Justice Colin Blackburn’s comment.

Sussex Spaniel: The Sussex Spaniel is a breed of dog developed in Sussex in southern England.  It is a low, compact spaniel and is similar in appearance to the Clumber Spaniel.  They can be slow-paced, but can have a clownish and energetic temperament.  They suffer from health conditions common to spaniels and some large dogs, as well as a specific range of heart conditions and spinal disc herniation.

There Was an Old Lady Who Swallowed a Fly: The phrase and title There Was an Old Lady Who Swallowed a Fly—alternatively, "I Know an Old Lady Who Swallowed a Fly," or "There Was an Old Woman Who Swallowed a Fly," or "I Know an Old Woman Who Swallowed a Fly"—is a children's rhyme and song of a kind known as cumulative.  The song tells the story of an old woman who swallowed increasingly large animals, each to catch the previously swallowed animal.  There are many variations of phrasing in the lyrics, especially for the description of swallowing each animal.  The spider and fly are described in each verse, but the other animals are only described when they are introduced starting with the bird.  The absurdity stems from the increasingly improbable solutions that only worsen the initial problem and are more likely to cause the woman's death: the logic of swallowing of even more animals of preposterous sizes without dying, contrasted with the expected, matter-of-fact recounting of her death from swallowing an animal larger than herself, when in fact the swallowing of any animal as a solution was absurd.

Pont-Audemer Spaniel: The Pont-Audemer Spaniel or Epagneul Pont-Audemer is a rare breed of French gundog.  It originated in the nineteenth century from different breeds of water spaniels, and took more of a setter role in hunting than that of a traditional spaniel.  Following the Second World War, the breed's numbers dropped so low that the breed club decided to allow cross breeding with other breeds because of fears of the existing stock becoming overly inbred.  In 1980, the breed club was merged with that of the Picardy Spaniel.

Cuddly Dudley: Cuddly Dudley is a "lifesize" (at 28.5 inch tall) shiny plush stuffed animal nostalgic cocker spaniel doll that was used as a subscription sales promotional item by the "Chicago Tribune" in the mid-1960s.  In addition, the animal took on a life of its own as a recurring character on Chicago children's TV for many years.

Canine Chiari-like malformation: Chiari-like malformation (CM) is the most common cause of foramen magnum obstruction and syringomyelia in dogs.  Syringomyelia (SM) is a disease of the spinal cord typified by fluid filled cavities, or syrinxes, within the spinal cord substance.  The disease is caused by the obstruction of cerebrospinal fluid (CSF), in the nervous system.  A situation of high pressure in the spinal cord compared to low pressure outside, leads to fluid accumulation, which eventually forms cavities.  CM is a condition characterized by the mismatch of size between the brain and the skull.  The skull is too small causing part of the brain to descend out of the skull through the opening at its base, crowding the spinal cord.  The cause of CM is not yet fully understood.  CM is rare in most breeds but reportedly has become very widespread in the Cavalier King Charles Spaniel and the Griffon Bruxellois (Brussels Griffon).  Some researchers estimate that as many as 95% of CKCSs may have CM.  It is worldwide in scope and not limited to any country, breeding line, or kennel, and experts report that it is believed to be inherited in the Cavalier King Charles Spaniel.  CM is so widespread in the Cavalier that it may be an inherent part of the CKCS's breed standard.  This disease not only affects thousands of dogs, but a similar condition affects over three hundred thousand children yearly.  Therefore, canines are an appropriate model for the treatment of the human condition.

Paraveterinary workers in Japan: Veterinary support personnel in Japan do not currently hold any official state recognition and are known under a variety of equivalent names.  Credentialing is carried out by various private organizations.  These organizations are the Japan Animal Health Technicians Association (JAHTA), the Japanese Animal Hospital Association (JAHA), the Japan Small Animal Veterinary Association (JSAVA), the All Japan Veterinary Co-operative (JVC), and the Japanese Society of Animal Nursing.  The Japanese Veterinary Nurses & Technicians Association (JVNTA), a non-certifying body which closed its doors in 2007, was one of the original member organizations of the IVNTA.  In 2009 the Japanese Veterinary Nursing Association (JVNA) was organized as an effort to unify and standardize the profession in Japan and to seek state recognition.  The JVNA, which has the support of the Japanese Veterinary Medical Association (JVMA—the national organization for veterinarians), may serve only as a temporary vehicle towards a single permanent national certifying body.  All of the organizations have been collaborating since 2010 as the Council for Veterinary Nursing Examination and have reached an agreement to share a common examination in February 2012.  In the meantime, a new organization, supported by the Ministry of Agriculture, Forestry, and Fisheries; the JVMA; and the JVNA has been tasked with developing a nationally sanctioned unified exam, the first of which was scheduled to be given in February 2013.  Education lacks uniformity but in most cases consists of two- to three-year programs.  A council of universities for animal nursing was also established and tasked with building a core curriculum for veterinary nursing.  The council is made up of: Yamazaki Gakuen University, Nippon Veterinary and Life Science University, Kurashiki University of Science and the Arts, Teikyo University of Science, and Rakuno Gakuen University.

Jämthund: The Jämthund, also called the Swedish Elkhound/Moosehound, is a breed of dog of the Spitz type that are found in Northern Europe.  The Jämthund is eponymous to Jämtland, a province in the middle of Sweden.  The dog is described as having a wolf-like appearance.

List of English animal nouns: The following is a list of English animal nouns, (the common names of kinds of animals).  This list includes the common names used for the animal in general; names for the male animal and the female animal where such names exist; the name used for the young or juveniles of the animal; the common name given for the sound the animal makes, if any; the group noun where applicable; and the name of both the natural shelter and (if applicable) an artificial shelter for the animals.

Question: What kind of animal does Pont-Audemer Spaniel and Jämthund have in common?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "animal_breeds_in_question": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "The names of the animal breeds mentioned in the question."
    },
    "common_animal_type": {
      "type": "string",
      "description": "The animal type that both breeds belong to."
    },
    "type_confirmation": {
      "type": "string",
      "description": "A statement confirming that both breeds are of the identified common animal type."
    },
    "is_common_type_identified": {
      "type": "boolean",
      "description": "Indicates whether a common animal type was successfully identified for both breeds."
    }
  },
  "required": [
    "animal_breeds_in_question",
    "common_animal_type",
    "type_confirmation",
    "is_common_type_identified"
  ],
  "additionalProperties": false
}

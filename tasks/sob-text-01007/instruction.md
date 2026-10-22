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
Bull Terrier: The Bull Terrier is a breed of dog in the terrier family.  There is also a miniature version of this breed which is officially known as the Miniature Bull Terrier.

Brazilian Terrier: The Brazilian Terrier, is a breed of dog developed in Brazil.  It is one of several terriers probably descended from the combining of the Fox Terrier with other small breeds.

Pit bull: Pit bull is the common name for a type of dog.  Formal breeds often considered in North America to be of the pit bull type include the American Pit Bull Terrier, American Staffordshire Terrier, American Bully, and Staffordshire Bull Terrier.  The American Bulldog is also sometimes included.  Many of these breeds were originally developed as fighting dogs from cross breeding bull-baiting dogs (used to hold the faces and heads of larger animals such as bulls) and terriers.  After the use of dogs in blood sports was banned, such dogs were used as catch dogs in the United States for semi-wild cattle and hogs, to hunt and drive livestock, and as family companions.  Despite dog fighting now being illegal in the United States, it still exists as an underground activity, and pit bulls are a common breed of choice.

Teddy Roosevelt Terrier: The Teddy Roosevelt Terrier is a small to medium-sized American hunting terrier.  Lower-set with shorter legs, more muscular, and heavier bone density than its cousin the American Rat Terrier.  There is much diversity in the history of the Teddy Roosevelt Terrier breed and it shares a common early history with the American Rat Terrier, Fox Paulistinha and Tenterfield Terrier.  It is said the Rat Terrier background stems from the terriers or other dogs that were brought over by early English and other working class immigrants.  Since the breed was a farm, hunting and utility dog there was little to no planned breeding other than breeding dogs with agreeable traits to each other in order to produce the desired work ethic in the dog.  It is assumed that the Feist (dog), Bull Terrier, Smooth Fox Terrier, Manchester Terrier, Whippet, Italian Greyhound, the now extinct English White Terrier, Turnspit dog and or Wry Legged Terrier all share in the Teddy Roosevelt Terrier's ancestry.  These early Ratting Terriers were then most likely bred to the Beagle or Beagle cross bred dogs (for increased scenting ability) and other dogs.  Maximizing the influences from these various breeds provides the modern Teddy Roosevelt Terrier with a keen sense of awareness and prey drive, an acute sense of smell and a very high intellect.  Although they tend to be aloof with strangers they are devoted companion dogs with a strong desire to please and be near their owners side at all times.

American Russell Terrier Club: The American Russell Terrier Club (formerly named the English Jack Russell Terrier Club), founded by JoAnn Stoll in 1995, was the first registry in the United States to maintain the Russell Terrier as a separate breed from the Parson Russell Terrier.  The American Jack Russell Terrier Club is affiliated with both the United Kennel Club and the American Kennel Club.  The purpose of the early founders was to establish a registry for the perpetuation and development of the Russell Terrier as a pure strain of working Jack Russell Terrier keeping their blood and type pure within the registry to works towards Kennel Club recognition as an official breed in the US.  On January 1, 2001, the United Kennel Club recognized the Russell Terrier as an official breed, designating only the stock from the American Russell Terrier Club as Foundation stock for the UKC Russell Terrier.  In 2004 the American Russell Terrier Club submitted an official request to include the American Russell Terrier Club stock into the AKC FSS Program to work towards becoming an official breed under the perimeters.  On December 8, 2004, the AKC officially accepted the Russell Terrier.

Airedale Terrier: The Airedale Terrier (often shortened to "Airedale"), also called Bingley Terrier and Waterside Terrier, is a dog breed of the terrier type that originated in the valley ("dale") of the River Aire, in the West Riding of Yorkshire, England.  It is traditionally called the "King of Terriers" because it is the largest of the terrier breeds.  The Airedale was bred from the Old English Black and Tan Terrier (now extinct), the Bull Terrier, the Otterhound and probably some other Terrier breeds, originally to serve as an all around working farm dog.  In Britain this breed has also been used as a war dog, guide dog and police dog.  In the United States, this breed has been used to hunt big game, upland birds, and water fowl, and serve in many other working capacities.

Chamuco: The Chamuco (a Mexican word which means "devil") or Mexican Pitbull is a dog breed not recognized by any Canofile association.  It originated in the center of Mexico, it was developed in this country in the 1970s, product of the accidental or intentional crosses of the American Pit Bull Terrier with the now extinct Mexican Bulldog, street dogs, American Bully, Pitbull Blue, Staffordshire bull terrier, American Staffordshire Terrier, and probably with the Boxer.  Its name comes from the Mexican slang "Chamuco", which means devil because of its temperament and tenacity.  Also it called Mexican pitbull or miniature pitbull, but actually is Dogo of Mexican origin.

Bull and Terrier: The Bull and Terrier is a breed of dog that was the progenitor of the American Pit Bull Terrier, American Staffordshire Terrier, English Bull Terrier and the Staffordshire Bull Terrier.

American Pit Bull Terrier: The American Pit Bull Terrier (APBT) is a dog breed.  It is a medium-sized, solidly-built, intelligent, short-haired dog whose early ancestors came from the British Isles.  When compared with the English Staffordshire Bull Terrier (another breed within the type commonly called pit bulls), the American Pit Bull Terrier is larger by margins of 6 - in height and 25 - in weight.  The American Pit Bull Terrier varies in size.  Males normally are about 18-21 inches (45–53 cm) in height and around 35-60 pounds (15–27 kg) in weight.  Females are normally around 17-20 inches (43–50 cm) in height and 30-50 pounds (13–22 kg) in weight.

Rocky Top's Sundance Kid: Ch.  Rocky Top's Sundance Kid ("aka: "Rufus"") (April 8, 2000 – August 9, 2012), is a Bull Terrier who is best known for being the 2006 Best In Show winner at the Westminster Dog Show.  He is the first Colored Bull Terrier to win Best in Show at Westminster, with the only other victory for his breed going to a White Bull Terrier in 1918.  He also won Best in Show at the National Dog Show in 2005, and on retirement trained as a therapy dog.  He is the most successful Colored Bull Terrier Show Dog of all time.

Question: Brazilian Terrier and Bull Terrier, are a breed of what?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "breeds": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "is_terrier_family": {
            "type": "boolean"
          }
        },
        "required": [
          "name",
          "is_terrier_family"
        ],
        "additionalProperties": false
      }
    },
    "common_type": {
      "type": "string"
    },
    "number_of_breeds_identified": {
      "type": "integer"
    }
  },
  "required": [
    "breeds",
    "common_type",
    "number_of_breeds_identified"
  ],
  "additionalProperties": false
}
